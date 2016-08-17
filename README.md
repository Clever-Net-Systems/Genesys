# Genesys
Virtual machine first start configuration assistant    

## Prerequisites
Here are some prerequisites needed by Genesys

 - [dialog](http://linuxgazette.net/101/sunil.html)
 - [python-dnspython](http://www.dnspython.org/)
 - [python2-pythondialog](http://pythondialog.sourceforge.net/)
 - [debinterface](https://github.com/dggreenbaum/debinterface)

## Installation

prerequisites:
```
apt-get install python-dnspython dialog python-pip
pip install python2-pythondialog debinterface
```
genesys
```
dpkg -i genesys.deb
```
Done :)
