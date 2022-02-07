import re
data = "https://www.facebook.com:1010"
hostname = re.findall('f[^:^/]*',data)
print("Hostname is :" , hostname)
protocol = re.findall('(\w+)://',data)
print("protocol is :" , protocol)
portno = re.findall(':([\w]+)',data)
print("portno is :" , portno)
