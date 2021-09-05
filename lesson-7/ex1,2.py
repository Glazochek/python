#1, 2
sl = [] #список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)
ip_addr = [] #все айпи адреса
ip_spam = [] #айпи адреса спамеров
ip_spam_sum = [] #айпи адреса спамеров и количество запросов
with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        remote_addr = line.split(' - - ', 1)[0]
        request_type = line.split(' "')[1].split(' /')[0]
        requested_resource = line.split(' /')[1].split(' H')[0].replace('down', '/down')
        r3 = (remote_addr, request_type, requested_resource)
        sl.append(r3)
        ip_addr.append(remote_addr)

for r in ip_addr:
    rc = ip_addr.count(r)
    if rc > 1:
        ip_spam.append(r)

for ips in ip_spam:
    ps = ips + f': [{ip_spam.count(ips)}]'
    ip_spam_sum.append(ps)

print('задание 1', sl)
print('задание 2*', list(set(ip_spam_sum)))
