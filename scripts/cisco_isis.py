from netmiko import ConnectHandler

# 1. Definisi Perintah Konfigurasi untuk Masing-Masing Router
# R1 Config
r1_config = [
    'router isis', 'net 49.0001.1720.1600.0001.00', 'is-type level-2-only', 'metric-style wide',
    'interface Loopback0', 'ip address 172.16.0.1 255.255.255.255', 'ip router isis',
    'interface GigabitEthernet0/1', 'ip address 10.12.12.1 255.255.255.252', 'no shutdown', 'ip router isis',
    'interface GigabitEthernet0/2', 'ip address 10.13.13.1 255.255.255.252', 'no shutdown', 'ip router isis'
]

# R2 Config
r2_config = [
    'router isis', 'net 49.0001.1720.1600.0002.00', 'is-type level-2-only', 'metric-style wide',
    'interface Loopback0', 'ip address 172.16.0.2 255.255.255.255', 'ip router isis',
    'interface GigabitEthernet0/1', 'ip address 10.12.12.2 255.255.255.252', 'no shutdown', 'ip router isis',
    'interface GigabitEthernet0/2', 'ip address 10.23.23.1 255.255.255.252', 'no shutdown', 'ip router isis'
]

# R3 Config (Termasuk Skenario Fiber & Microwave)
r3_config = [
    'router isis', 'net 49.0001.1720.1600.0003.00', 'is-type level-2-only', 'metric-style wide',
    'interface Loopback0', 'ip address 172.16.0.3 255.255.255.255', 'ip router isis',
    'interface GigabitEthernet0/1', 'ip address 10.23.23.2 255.255.255.252', 'no shutdown', 'ip router isis',
    'interface GigabitEthernet0/2', 'ip address 10.13.13.2 255.255.255.252', 'no shutdown', 'ip router isis',
    'interface GigabitEthernet0/3', 'description LINK-FIBER-TO-R4', 'ip address 10.34.34.1 255.255.255.252', 'no shutdown', 'ip router isis', 'isis metric 10',
    'interface GigabitEthernet0/4', 'description LINK-MICROWAVE-TO-R4', 'ip address 10.43.43.1 255.255.255.252', 'no shutdown', 'ip router isis', 'isis metric 100'
]

# R4 Config (Termasuk Skenario Fiber & Microwave)
r4_config = [
    'router isis', 'net 49.0001.1720.1600.0004.00', 'is-type level-2-only', 'metric-style wide',
    'interface Loopback0', 'ip address 172.16.0.4 255.255.255.255', 'ip router isis',
    'interface GigabitEthernet0/1', 'description LINK-FIBER-TO-R3', 'ip address 10.34.34.2 255.255.255.252', 'no shutdown', 'ip router isis', 'isis metric 10',
    'interface GigabitEthernet0/2', 'description LINK-MICROWAVE-TO-R3', 'ip address 10.43.43.2 255.255.255.252', 'no shutdown', 'ip router isis', 'isis metric 100'
]

# 2. Pemetaan IP Management ke Konfigurasi
router_map = {
    '192.168.61.11': r1_config,
    '192.168.61.12': r2_config,
    '192.168.61.13': r3_config,
    '192.168.61.14': r4_config
}

# 3. Looping Eksekusi
for ip, commands in router_map.items():
    print("="*60)
    print(f" MENGIRIM KONFIGURASI KE ROUTER : {ip}")
    print("="*60)
    
    device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'cisco',
        'password': 'cisco',
        'port': 22,
        'global_delay_factor': 2
    }

    try:
        # Buka Koneksi
        net_connect = ConnectHandler(**device)
        
        # send_config_set otomatis masuk ke mode 'configure terminal'
        output = net_connect.send_config_set(commands)
        print(output)
        
        # Simpan konfigurasi dengan timeout yang diperpanjang (30 detik)
        print("\nMenyimpan konfigurasi (mohon tunggu, GNS3 butuh waktu)...")
        save_out = net_connect.send_command('write memory', read_timeout=30)
        print(save_out)
        
        net_connect.disconnect()
        print(f"[SUKSES] Konfigurasi {ip} selesai.\n")
        
    except Exception as e:
        print(f"[GAGAL] Error pada {ip}: {e}\n")