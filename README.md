# Genesys
Virtual machine first start configuration assistant.
![alt text](https://lh3.googleusercontent.com/liJEc8ihefh9rLXog2Eof6htG1he1lHDr5bRIbOUeen6OCHm2zdtjj0n4r5KnNgCYkTWS28NSIP5O7-wkl9We-d5M9mFXaqiHKn5ynhXKkm2lossoUxLyjNBzAbM-T_QDDTp8Rr3SjUGTbbSKVnrISsRVWrruyqZuCeJuCEiXeDLOFkVSE2srOQEtXTvmLr0rs9_pS6hw7IHyrAD_QogU22dZH8Rc-XeuZFxBLm2kFXVeAYYxOwF84lCg3UGxx0ukSc1C32iR5Sk2EE7g728fkMBQvo_Lcsb9Q125ozuCzUwuc-KtlOYVaDB4GiuvTxN28IW34UqTkqLTQfePpwOYmFLmDkTPlGXz2bnS7KOgiL4dd-l1oUtmc6yS9yQFkThglxXa8vTqKFZPa6UaGLCJjrX5Lk3Y5tkBjTPAI31U0FDgxhF8BGz_N2t9yzmkoBEQunMfZIZzNECPmMb6QMoBpJebrbOVlo0DKt5OEML4FFIqROeQTSEhen3ZBo-g04rxLlhZPdfCo5xu1J_Xfcd6XdOAXOJf29fkztDO_4RV-ndWpV4BAB3mYSK8ZHKAiFpQ_zIZkBaJg36g8L2L26_9vboUuY2kKo=w946-h526-no "Genesys Welcome screen")

![alt text](https://lh3.googleusercontent.com/VneqAO2rDJtNMgtiVFwswk2A90BVbuHt32krk5QVQ-G5MX58OBvix5P7ofLEm_-ZLlBfOtsuWPqFWK_7sQxokehpjOwWEkx-ueQgsZ9MS_byepMoNR1i1veVHXPo6zjAtI2zUvGrZ8-ZbhzlunDOgSms8QNMLSAOGJs5ZAVT8rSVM6BqdMn0gYrpMdgqhQF46hAIdkYW8h7_YePDGRo3odxdoobecu2s1P4dHmGH75SB8ECfTZCHnjAxYsEvCGIZRPBuFLSb59uRjyEUAkQfiba6CsSyxXtXgzJv2rXMQxdBHd1A4dip2I3E1hYVwrUXCTd_e5U2ftM9PbRXINqhYsohJG2rWRQMqrfhnNo5biJrYi0lgJ23XZzdOaOpcDGugmsgGr9OhjqwySNgjxcBEVr_DVZK5ARx2uejLXZOK1Mpn5PRx1vWx0SvEXGS6aAJU1W8BZTiBdtTkX0rBwdiJCTVD3oV1JZz-6hF-fJvGxvgsOhu_f9E2vxuDTilC_c5I0C--Q2htcNJf_1rguBccsbbYyAfqbvDDuuvZN5lcZ2IPmL7n1CHZGxAcO_OfFnQHhGFfLrb2v-iSPnDGBFQG30188oJsqM=w945-h526-no "Genesys menu")


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

## Usage
Genesys is based on systemd. You can easily turn on or down the genesys service like this:

### Enable Genesys for the next boot
```
systemctl enable genesys.service
```

### Disable Genesys
```
systemctl disable genesys.service
```
! When leaving the Genesys assistant, by default, the Genesys wizard is disabled !
