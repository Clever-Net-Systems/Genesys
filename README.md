# Genesys
Virtual machine first start configuration assistant.
![Genesys Welcome screen](https://lh3.googleusercontent.com/2qy1oL9Hkh3Ztw3wwhyLknugI2kOv4jg9sefIoLz70ht9FPs_TGV-bSDYimO-pvvgRXft4zVfZmCC-OSxApeSV-Zm8H4t1bmPaQIFaQTRqhRhXMODvXKZ08lj3k58oa3xc3AWxXyCAZfr7gOM8jHfBx-txaIDzwFDBsBd2RHR7jv_htIkGzpsaWtzYWTmw4I5-jTYqIRU-6EPcpalwQnVVmHeelkvD4u8KlIvKshhpPOJvU9uWTdglHUyOv0bcJFmXjq18KZGXK2L_26Ha7jxO7R67UbJmJ5YtpMKs9Y0ZTvRG9hJOJjLdqvKhhI9esC9RLl4nj_86h5LoXukV_tnHNXCRWAK1OoIUHcl9yUfCPCJzb68LwKhGHpzwypardEIQ_Yzn0fSKw5EzFu-MHztZDWTXICTS0F41AHHJ9XCc0L1EfAvCwV3Eych-Jd9xqaVjnxs5TSnA4foLju8zsO8bY2JrjoGQF4LUt3mqqW5hAmH0wNNsVw4evEZ-fkAD67tFWDpieqUN1o3mnWAjefW2z9AjtsfbenjvSzafeU1EFIVqK_Y6NA6zkKl5Mo0TIAqy8FWA5N8jZL9A1R1hvXx_-seLpA8bA=w946-h526-no "Genesys Welcome screen")

![Genesys menu](https://lh3.googleusercontent.com/JfuRUVvtRtY7CTHko1kXWA2Cyw9rgj5Ga6lymDQVNuunjPI-VBrJUcx_s07QIUN7ZMP2HpALMhc-r7DM0SE7TeIDi3cxbnNZ6yYgESzdtHzn7dzozVS5_FPujJhOW2t7NdZUiQP8pA9iXBPTe8fdU53m6Xr5b3dUisoHtEnp6pdWEebneeWskPxQEFV93kjbcNnE4-hzeQoXZToXWSGnOcYXENd4Zxopws5S5py9-97tu2cGu9KrNVncib-ljlla8RkKW8LtW0poS3EjX0XLp6cLtrIR27I2SosaBm380_ZLsAPiiLkA38Xnmq4iCipz3LjYqBW0jSpwIHzfN5TKBpc9vzSYtDwNMRWv-02BxObYYis5tU6ivDin6XOlNy_duMUCKrv65fS8RfSO3OJV0xdnWbl8jRxFPiHc8iyMrmtM0zZzwl2PZWXkmwUElq5QRKxOhC_xlYe45yVDLvKyHJvzkuix9ELmcTZMD7ed98FzHW8ek-1ylsA-YC_mMkbCJhOjXmQytczUJoj7JxgnS4P0ZhkqiL3h0oLhyTbiY0fxRpIqI5imi3G3S9ITT_brwOxSkMFyoptBXszIBwPGjC0k0TSNIo0=w945-h526-no "Genesys menu")


## Prerequisites
Here are some prerequisites needed by Genesys

 - [dialog](http://linuxgazette.net/101/sunil.html)
 - [python2-pythondialog](http://pythondialog.sourceforge.net/)
 - [debinterface](https://github.com/dggreenbaum/debinterface)
 - [confparse](https://code.google.com/archive/p/confparse/)

## Installation

### prerequisites

#### Debian
```
apt-get install dialog python-pip
pip install python2-pythondialog debinterface confparse
```

#### CentOS/RHEL 7
```
yum install epel-release
yum install dialog python-pip
pip install python2-pythondialog debinterface confparse
```

### genesys

#### systemd:

##### Debian
```
wget https://github.com/Clever-Net-Systems/Genesys/releases/download/0.7/genesys-0.7.deb
dpkg -i genesys-0.7.deb
```
##### CentOs/RHEL
```
wget https://github.com/Clever-Net-Systems/Genesys/releases/download/0.7/genesys-0-7.el7.x86_64.rpm
yum localinstall genesys-0-7.el7.x86_64.rpm
```

#### SystemV:
```
Genesys does not support SystemV anymore.
```

More download options [here](https://github.com/clevernet/Genesys/releases)

Done :)

## Usage
Genesys is based on systemd. You can easily turn on or down the genesys service like this:

### Systemd

#### Enable Genesys for the next boot
After installing the genesys deb file, genesys is actived for the next reboot by defaut.
```
systemctl enable genesys.service
```

#### Disable Genesys
```
systemctl disable genesys.service
```
! When leaving the Genesys assistant, by default, the Genesys wizard is disabled !
