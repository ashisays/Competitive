txt = """Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . : domain.name
   Link-local IPv6 Address . . . . . : fe80::c9b0:2a75:5aaf:64da%20
   IPv4 Address. . . . . . . . . . . : 192.168.1.6
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : fe80::bac1:acff:fe8c:cfdd%20
                                       192.168.1.1"""
import re

match = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',txt)
print (match)