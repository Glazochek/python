import re

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'

ra = re.compile(r'(?:\d{2,3}[.]){2,3}\d{2,3}')
rd = re.compile(r'\[([^]]+)\]')
rt = re.compile(r'[ ]\D\S{3,4}[ ]')
rr = re.compile(r'[/]\D{18}\d')
rc = re.compile(r'[ ]\d{3}[ ]')
rs = re.compile(r'\d[ ]\d{1,3}[ ]')

response_code = rc.findall(raw)
requested_resource = rr.findall(raw)
remote_addr = ra.findall(raw)
response_size = rs.findall(raw)
request_type = rt.findall(raw)
request_datetime = rd.findall(raw)
# <remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>
parsed_raw = ((''.join(remote_addr)), (''.join(request_datetime)), str(request_type)[4:-3], (''.join(requested_resource)), str(response_code)[3:-3], str(response_size)[4:-3])
print(parsed_raw)