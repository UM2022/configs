from netmiko import ConnectHandler

isr_os = {
    'device_type': 'cisco_ios',
    'ip': '85.118.10.108',
    'username': 'rtradmin',
    'password': 'Aq1Sw2De3Fr4Gt5$$$',
}

net_connect = ConnectHandler(**isr_os)
#output = net_connect.send_command('show ip int brief')
output = net_connect.send_command('show run')
print(output)