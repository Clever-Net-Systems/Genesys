#!/usr/bin/python
# coding: utf-8
#########################################################################################
#   Clever Net Systems [~]                                                              #
#   Clément Hampaï <clement.hampai@clevernetsystems.com>                                #
#   Genesys VM first start configuration assistant                                      #
#                                                                                       #
#	This program is free software: you can redistribute it and/or modify                  #
#	    it under the terms of the GNU General Public License as published by              #
#	    the Free Software Foundation, either version 3 of the License, or                 #
#	    (at your option) any later version.                                               #
#                                                                                       #
#	    This program is distributed in the hope that it will be useful,                   #
#	    but WITHOUT ANY WARRANTY; without even the implied warranty of                    #
#	    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                     #
#	    GNU General Public License for more details.                                      #
#                                                                                       #
#	    You should have received a copy of the GNU General Public License                 #
#	    along with this program.  If not, see <http://www.gnu.org/licenses/>.             #
#########################################################################################

import locale, sys, os, subprocess, re, time, dns.resolver
from debinterface.interfaces import Interfaces
from dialog import Dialog

class GlobalVars:
  DHCP = 'dhcp'
  STATIC = 'static'
  BACKGROUND_TITLE = "Genesys VM configuration"
  WELCOME_TXT = """Welcome to the Genesys VM first start configuration assistant
  \n\nWould you like to start the configuration ?"""
  HOME_MENU_TXT = """Choose what to configure:"""
  SET_HOSTNAME_TXT = "Choose a hostname:"
  SUCCESS_HOSTNAME = "New hostname configured !\n\nNew hostname: "
  FAILED_HOSTNAME = "Failed to configure the new hostname."
  SUCCESS_DNS = "New DNS configured !\n\nNew DNS: "
  FAILED_DNS = "Failed to configure the new DNS."
  DNS_TITLE = "Enter some DNS \n(example: 8.8.8.8,8.8.4.4)"
  TXT_CONFIG_STATIC_TITLE = "Provide the values for static IP configuration"
  TXT_MESSAGE_DHCP = 'Configuring for DHCP provided address...'
  TXT_MESSAGE_STATIC = 'Configuring for static IP address...'
  stored_interfaces = ""
  selected_interface = ""

## Interface and window systems ------------------------------------------------
def ini_interface(bg_title):
    locale.setlocale(locale.LC_ALL, '')
    dial = Dialog(dialog='dialog', autowidgetsize=True)
    dial.set_background_title(str(bg_title))
    return dial

def display_yes_no_question(question, yes_label, no_label, dial, height="15", width="65"):
    code = dial.yesno(str(question), height, width, yes_label=str(yes_label), no_label=str(no_label))
    return code

def display_menu(data, choices, dial, ok_label, cancel_label):
    available_adapters = []
    available_iface_list = choices
    code, tag = dial.menu(GlobalVars.HOME_MENU_TXT, choices=choices, ok_label=str(ok_label), cancel_label=str(cancel_label))
    result = {}
    result[code] = tag
    return result

def display_input_text(text, ok_label, cancel_label, dial):
    code, tag = dial.inputbox(text, ok_label=ok_label, cancel_label=cancel_label)
    result = {}
    result[code] = tag
    return result

def display_infobox(text, height="15", width="65"):
    dial = ini_interface(GlobalVars.BACKGROUND_TITLE)
    dial.infobox(text, height=height, width=width)

def display_msgbox(text, dial, height="15", width="65"):
    code, tag = dial.msgbox(text, height=height, width=width)
    result = {}
    result[code] = tag
    return result

def welcome():
    dial = ini_interface(GlobalVars.BACKGROUND_TITLE)
    return display_yes_no_question(GlobalVars.WELCOME_TXT, "Start", "Cancel", dial, 10)

def home_menu():
    dial = ini_interface(GlobalVars.BACKGROUND_TITLE)
    choices = []
    choices.append(("hostname", "set this machine's hostname"))
    choices.append(("ipv4", "configure an IPv4 inet"))
    choices.append(("DNS", "configure some domain name servers"))
    return display_menu(GlobalVars.HOME_MENU_TXT, choices, dial, "Configure", "Quit")

def hostname():
    dial = ini_interface(GlobalVars.BACKGROUND_TITLE)
    hostname = display_input_text(GlobalVars.SET_HOSTNAME_TXT, "OK", "Cancel", dial)
    check_continue(hostname)
    if "ok" in hostname:
        result = set_hostname(hostname["ok"])
    else:
        result = False
    if result:
        return display_msgbox(GlobalVars.SUCCESS_HOSTNAME+hostname["ok"], dial)
    else:
        return display_msgbox(GlobalVars.FAILED_HOSTNAME, dial)

def ask_dns():
    dial = ini_interface(GlobalVars.BACKGROUND_TITLE)
    dns = display_input_text(GlobalVars.DNS_TITLE, "OK", "Cancel", dial)
    check_continue(dns)
    if "ok" in dns:
        result = set_dns(dns["ok"])
    else:
        result = False
    if result:
        return display_msgbox(GlobalVars.SUCCESS_DNS+dns["ok"], dial)
    else:
        return display_msgbox(GlobalVars.FAILED_DNS, dial)

def select_eth():
    dial = ini_interface(GlobalVars.BACKGROUND_TITLE)
    choices = []
    for eth in str(list_eth()).splitlines():
        print str(eth)
        inet = eth.split(' ', 1)
        inet_name = inet[0].strip()
        inet_description = inet[1].strip()
        choices.append((inet_name, inet_description))
    selected_interface = display_menu(GlobalVars.HOME_MENU_TXT, choices, dial, "Configure", "Cancel")
    if "ok" in selected_interface:
        GlobalVars.selected_interface = selected_interface["ok"]
    return selected_interface

def config_eth():
    dial = ini_interface(GlobalVars.BACKGROUND_TITLE)
    choices = []
    choices.append((GlobalVars.DHCP, ""))
    choices.append((GlobalVars.STATIC, ""))
    return display_menu(GlobalVars.HOME_MENU_TXT, choices, dial, "OK", "Cancel")

def ask_static_config():
    dial = ini_interface(GlobalVars.BACKGROUND_TITLE)
    code, values = dial.form(GlobalVars.TXT_CONFIG_STATIC_TITLE, [
                          # title, row_1, column_1, field, row_1, column_20, field_length, input_length
                          ('IP Address', 1, 1, '192.168.0.10', 1, 20, 15, 15),
                          # title, row_2, column_1, field, row_2, column_20, field_length, input_length
                          ('Netmask', 2, 1, '255.255.255.0', 2, 20, 15, 15),
                          # title, row_3, column_1, field, row_3, column_20, field_length, input_length
                          ('Gateway', 3, 1, '192.168.0.1', 3, 20, 15, 15)
                          ], width=70, ok_label="Save", cancel_label="Cancel")
    result = {}
    result[code] = values
    return result

def clear_and_quit():
    os.system('clear')
    os.system('systemctl disable genesys.service')
    os.system('clear')
    sys.exit(0)

def clear():
    os.system('clear')

# ------------------------------------------------------------------------------

# Misc -------------------------------------------------------------------------
def check_continue(value_to_check, quit=False):
    if (Dialog.CANCEL in value_to_check or Dialog.ESC in value_to_check) and quit:
        run(-1)
    elif (Dialog.CANCEL in value_to_check or Dialog.ESC in value_to_check):
        clear()
        run(1)
    else:
        clear()

def run(next_window_id):
    if next_window_id == -1:
        clear_and_quit()
    elif next_window_id == 0:
        # Welcome screen
        check_continue(welcome(), True)
        run(1)
    elif next_window_id == 1:
        # Home Menu
        menu_result = home_menu()
        check_continue(menu_result, True)
        if menu_result["ok"] == "hostname":
            run(2)
        elif menu_result["ok"] == "ipv4":
            run(3)
        elif menu_result["ok"] == "DNS":
            run(7)
    elif next_window_id == 2:
        # Hostname configuration screen
        check_continue(hostname())
        run(1)
    elif next_window_id == 3:
        # Interfaces list
        GlobalVars.stored_interfaces = Interfaces()
        menu_result = select_eth()
        check_continue(menu_result)
        run(4)
    elif next_window_id == 4:
        # Interface mode configuration screen
        menu_result = config_eth()
        check_continue(menu_result)
        if menu_result["ok"] == GlobalVars.DHCP:
            run(5)
        elif menu_result["ok"] == GlobalVars.STATIC:
            run(6)
    elif next_window_id == 5:
        # Interface mode dhcp configuration screen
        final = create_dhcp_eth_config(GlobalVars.selected_interface)
        display_infobox(GlobalVars.TXT_MESSAGE_DHCP)
        os.system('systemctl restart networking.service')
        display_infobox("Success !")
        time.sleep(3)
        run(1)
    elif next_window_id == 6:
        # Interface mode static configuration screen
        result = ask_static_config()
        check_continue(result)
        result_values = result["ok"]
        addr = result_values[0]
        mask = result_values[1]
        gateway = result_values[2]
        final = create_static_eth_config(GlobalVars.selected_interface, addr, mask, gateway)
        display_infobox(GlobalVars.TXT_MESSAGE_STATIC)
        os.system('systemctl restart networking.service')
        display_infobox("Success !")
        time.sleep(3)
        run(1)
    elif next_window_id == 7:
        # Dns configuration screen
        check_continue(ask_dns())
        run(1)
# ------------------------------------------------------------------------------

## Worker functions ------------------------------------------------------------
def run_process(command, stderr=False):
  p = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
  output = ""
  while(True):
    retcode = p.poll()
    if stderr:
      line = p.stderr.readline().decode('utf-8')
    else:
      line = p.stdout.readline().decode('utf-8')
    output = output + line
    if retcode is not None:
      break
    result = {}
    result["retcode"] = retcode
    result["output"] = output
    return result

def set_hostname(hostname):
    if validate_hostname(hostname):
        os.system('hostname '+str(hostname))
        new_hostname = {}
        new_hostname = run_process('hostname', stderr=False)
        new_hostname_value = new_hostname['output']
        new_hostname_value = re.sub('\n','', new_hostname_value)
        if new_hostname_value == hostname:
            return True
    return False

def validate_hostname(hostname):
    domain_regex = re.compile("(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$")
    if not domain_regex.match(hostname):
        return False
    return True

def validate_ip(ip):
    ip_regex = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    if not ip_regex.match(ip):
        return False
    return True

def create_dhcp_eth_config(selected_iface):
    try:
        interfaces = GlobalVars.stored_interfaces
        reset_eth_config(selected_iface)
        interfaces.addAdapter({
          'name': selected_iface,
          'auto': True,
          'addrFam': 'inet',
          'source': GlobalVars.DHCP}, 0)
        interfaces.writeInterfaces()
        return True
    except:
        return False

def create_static_eth_config(selected_iface, addr, netmask, gateway):
    if validate_ip(addr) and validate_ip(netmask) and validate_ip(gateway):
        try:
            interfaces = GlobalVars.stored_interfaces
            reset_eth_config(selected_iface)
            interfaces.addAdapter({
              'name': selected_iface,
              'auto': True,
              'addrFam': 'inet',
              'source': GlobalVars.STATIC,
              'address': addr,
              'netmask': netmask,
              'gateway': gateway}, 0)
            interfaces.writeInterfaces()
            return True
        except:
            return False
    else:
            return False

def set_dns(dns_array):
    dns_srv = dns.resolver.Resolver()
    for dns_ip in dns_array.split(','):
        if not validate_ip(dns_ip) and not validate_hostname(dns_ip):
            return False
    dns_srv.nameservers = dns_array
    return True

def reset_eth_config(selected_iface):
    # check if selected_iface is already listed or not in /etc/network/interfaces file using debinterfaces
    # remove from adapter list if it is already configured
    interfaces = GlobalVars.stored_interfaces
    configured_iface = None
    for adapter in interfaces.adapters:
      item = adapter.export()
      if item['name'] == selected_iface:
        configured_iface = item
        if configured_iface is not None:
            interfaces.removeAdapterByName(selected_iface)
            interfaces.writeInterfaces()

def list_eth():
    available_adapters = []
    available_iface_list = run_process("ifconfig -a | grep eth")
    return available_iface_list['output']
# ------------------------------------------------------------------------------

# MAIN -------------------------------------------------------------------------
run(0)
# ------------------------------------------------------------------------------
