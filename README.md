# Genesys
Virtual machine first start configuration assistant.
![Genesys Welcome screen](https://lh3.googleusercontent.com/b1qZEpMxGFQ63yMHX-DTK7u5UaTlVtaUrqHYCr7idsC4C48mgKluO3LRRiHLT74qJq6WpmRhWILY4qm7ITRQB5eeMWpIkScu3_yw_YV4nXii9M0G01kk9xxHQ0_8mulgJOXGU70V_XgUCOsbRidksbdcuzuS05TyUC0hILN70__23iL0mPM4LoTrMYwSm1So4ngti-ikh4gOnkv6SIxa8-9KxSbaZdmKiMYvOb7xhSc5tEO0_ux0VZ9ZqQveB1Uwfn0QWbtpo9FOJORtfMej2A3mBa4rNR53fpX2k_1oSQS2nbis4EsJKNrdSZz_s-m1DnL-iTOhcoi4qSOAjKoOiOEx1ATi8nOtnvJsIuR0xSucSpXw5vZBT7rQ6jKjjpQRllviimd_Zc3w1kPyytM1bogV1oalaDflyyr0pSRVb-zsf0wnpNO3fgn28rfosi3CMmSel0EcE-_6NHcq2labKBFgwx4S6HKAInRr0N-UbzIpVsa5Ln71u94qD3LjzpF_PHRqQqgJch40POKoEwp_4dShcZ5NXwwWvrfolde6-2SGtwIMChU1AAlI5JWw67h5VKiMkNhnFi-nIVL2X2s9TY3zttIJjiA=w946-h526-no "Genesys Welcome screen")

![Genesys menu](https://lh3.googleusercontent.com/npQJyFoWSGghjqSlmNs3E1esrRZ3MNJ2BcEK7DvvXI396yiR-Lq8kjFCgE74FyOK-9ZPk8SHo5I1HMz6O55k0P2hBw_Nit-vrmbZ_SZMxeRoCAF0VzWAuvMGDwqEwWadNx1sftlGOYDqg56kZNJkKlR-VvC7uHFvvY7yg4jWJQogvtfeTWalOA_q_UNFz5yvvfWaLIfvSXevPFTBaLeavUjKF5VLfauBqamqp13AcEVxu4IoHy21piLrAF_l8gf5bu1CjeERMYtwT2RCxNlC-sVvCjuYYkjee5j_6xNSYoKy_wzyldGI8kHfhU-oK1tTX8YyhsKbb_H0elrzfYEuCtbpfXZk_2TgzuqwnpUWKYgi8q0XbdfdKLe-a2JfYivCKRHhKzweUKXwf0z0c9sFz_UcDbXiBbTAryaJ1x84gnkVgX0mbu-_1PvtnlONYfxRTz-DaKszgcP_I8QR2fBsjA_HRLZyz0VBlz5qubjCdnyr7KfBzBkfYq3eO7ITJ05f50hTKX8EWanIE8ppMK02bqGSZRPCqy_3mZWBGJfvVhtcz6hx2cZyx4PnQvgXYzkmWnMnGUi7DkGRql84oHBe7WmixvmYjaE=w945-h526-no "Genesys menu")


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
