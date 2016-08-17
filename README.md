# Genesys
Virtual machine first start configuration assistant    

## Prerequisites
Here are some prerequisites needed by Genesys

 - [dialog](ftp://ftp.traduc.org/pub/lgazette/html/2004/101/lg101-P.html)
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
