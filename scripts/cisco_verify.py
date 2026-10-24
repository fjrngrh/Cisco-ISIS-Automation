import warnings
warnings.filterwarnings("ignore")

import csv
from netmiko import ConnectHandler

ip_list = ['192.168.61.11', '192.168.61.12', '192.168.61.13', '192.168.61.14']

for ip in ip_list:
    print("\n" + "="*50)
    print(f" VERIFIKASI ROUTER : {ip}")
    print("="*50)
    
    device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'cisco',
        'password': 'cisco',
        'port': 22,
        'global_delay_factor': 2
    }

    try:
        net_connect = ConnectHandler(**device)
        
        print("\n--- STATUS TETANGGA IS-IS (NEIGHBORS) ---")
        print(net_connect.send_command('show isis neighbors'))
        
        print("\n--- TABEL ROUTING IS-IS ---")
        print(net_connect.send_command('show ip route isis'))
        
        net_connect.disconnect()
    except Exception as e:
        print(f"Error pada {ip}: {e}")