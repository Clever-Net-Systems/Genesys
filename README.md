# Genesys
Virtual machine first start configuration assistant.
![alt text](https://lh3.googleusercontent.com/NL8rWNusOAnFuHHyvFnstbDnsGxiUN7ss0xJz3-E5PHS8FiCLKA6bx_vVFhRiBLLgqS53xLyPG-72sTodkuL4tUsQaKbGM-l_K5on9LlOfTRu6dpzLAc4ucTIhhfAbTB5-k2BgM-wOTW91qxGrRjrmtue66OLfxciEVVMvWpXLTwhoO537KkQOOmRXNbIXhFKkBxLtYLZ58pOo1IdwCUJKHoWu5kKkdMS8D3-E0MhNri4Tl80hYz4nn-U7dtKaWptVWWlXNtosW2xhw9dJHeM-xWDHVI96XHCkdWgPq4A1kwlCMgsbCfRxjco6PTgGN8XZCscQXqAMN3rCb8Uh85k-CaoiCsjxocxmR57YvC-U7MBzakqlNTo_C5LFZTs586IgF5iugPGTZl5s3_OG0xgNOL_p8I9AL4rc9Dyy1Ir7dxHd6_TH5X1zh8CKTXBQL5O_bc2cqq4Y127zndb-8HzRtONvYdUdTj9j0P2dxpx4AysiwDJXF83qdnvSbOefYwHQukUf0EFl68rJmkEgHMPqRUEmnPsuSRH_xRtz8xuxA-FGDVHhxDffs3KRdul9HME5G02igpqIRGJO_DRjfrnCqBOdiptWE=w946-h526-no "Genesys Welcome screen")

![alt text](https://lh3.googleusercontent.com/zjLNeG8bet0ljZEzDTd-RT33UlgRHgAsL0J6AeJ8dE9vi2Gaf6Ugd7YDaWe6PWmJlQT8yzfbLd9m5ZAfn2EFqPeKsHBlrmthxkLAtYFX7C4RafjJPmKdTUYabYw_4_lM2eA-JL92seTlRerxYx_JkeJJfSXYSFUZZTB_oY6xEZsM_8d_oa0m9i84Indf7EskLYua0kaLaauBdaF_8_wN-dCYj8Q1JyPpJFtG458cQx4ES0Ct1LOQpNUZ7R38YBUD3LYr6Bws1I0EZnM31pEsOqA4GUVn2z13kicy2szkPc3DGHbH0oItdHF7l0QXiTvQSXcSFqAIrrR_EhT3AuzbBkeoBMw7DEOKeP-o_6yZUcH86_9JiXByYZfnU9NscdW-A8Wxva2Vm6h7fiPtb1TnAMHdS_WFkP_bFzYflvizWjJBT56HVJ0QzNqbHrIkiU1kxr_czEBT63KZN8ZMyo0qBCj58HAt-dEpiQcI5zLkrCfyB2FZiAEaVyieK6bpNnRqt2Hz7JOC2b3-IDdp1KPcOeenmrGqmos8kuZQaS89zyVQ-6HdRI0E_T2LC3f9noSUlAWd0pYlLxxbeSYOru9aPutkpoiQwyU=w945-h526-no "Genesys menu")


## Prerequisites
Here are some prerequisites needed by Genesys

 - [dialog](http://linuxgazette.net/101/sunil.html)
 - [python-dnspython](http://www.dnspython.org/)
 - [python2-pythondialog](http://pythondialog.sourceforge.net/)
 - [debinterface](https://github.com/dggreenbaum/debinterface)

## Installation

### prerequisites:
```
apt-get install python-dnspython dialog python-pip
pip install python2-pythondialog debinterface
```
### genesys:

download Genesys .deb file [here](https://github.com/clevernet/Genesys/releases)
```
dpkg -i genesys.deb
```
Done :)
