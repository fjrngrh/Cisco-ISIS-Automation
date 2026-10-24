import csv
from netmiko import ConnectHandler

# 1. Baca IP dari file CSV
ip_list = []
with open('hosts1.csv', mode='r') as f:
    reader = csv.reader(f)
    for row in reader:
        ip_list.append(row[1])

print(f"Daftar IP router Cisco yang ditemukan: {ip_list}\n")

# 2. Looping ke setiap router Cisco
for ip in ip_list:
    print("="*50)
    print(f"   MENGHUBUNGKAN KE ROUTER CISCO: {ip}")
    print("="*50)
    
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'cisco',
        'password': 'cisco',
        'port': 22,
        'global_delay_factor': 2
    }

    try:
        # Membuka koneksi SSH
        net_connect = ConnectHandler(**cisco_device)
        
        # Mengirim perintah Cisco IOS
        output_ver = net_connect.send_command('show version | include Software')
        output_int = net_connect.send_command('show ip interface brief')
        
        print("\n--- OUTPUT SHOW VERSION ---")
        print(output_ver)
        
        print("\n--- OUTPUT SHOW IP INT BRIEF ---")
        print(output_int)
        
        # Menutup koneksi
        net_connect.disconnect()
        print(f"\n[OK] Koneksi ke {ip} selesai.\n")
        
    except Exception as e:
        print(f"\n[GAGAL] Tidak dapat terhubung ke {ip}. Error: {e}\n")