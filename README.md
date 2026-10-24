# Cisco IOSv Network Automation & Traffic Engineering (IS-IS)

Project ini merupakan simulasi infrastruktur jaringan *Enterprise/Service Provider* menggunakan GNS3, yang dikonfigurasi sepenuhnya secara otomatis menggunakan **Python (Netmiko)**. Lab ini mendemonstrasikan implementasi protokol routing **IS-IS (Intermediate System to Intermediate System)** dan skenario **High Availability (Failover)** antara jalur Fiber Optic dan Microwave.

## 📌 Tujuan Proyek (Objectives)
*   Membangun automasi jaringan *Out-of-Band Management* menggunakan Python.
*   Melakukan *Bulk Configuration* (IP Address, Loopback, IS-IS Routing) pada banyak perangkat sekaligus.
*   Menerapkan *Traffic Engineering* menggunakan manipulasi Metrik IS-IS.
*   Menguji skenario *Failover* otomatis saat jalur utama terputus tanpa ada *downtime* yang signifikan.

## 🏗️ Topologi Jaringan
*   **Routing Protocol:** IS-IS (Level-2 Only).
*   **Management Network:** 192.168.61.0/24 (Out-of-Band via SSH).
*   **Core / Distribution:** R1, R2, R3 (Topologi Ring).
*   **Access / Edge:** R4 (Dual-Homing ke R3).
    *   **Jalur Utama (Fiber):** Interface Gi0/3 (Metric 10).
    *   **Jalur Backup (Microwave):** Interface Gi0/4 (Metric 100).

*(Opsional: Sisipkan screenshot topologi GNS3 Anda di sini)*

## 🛠️ Tech Stack & Tools
*   **Python 3.x**
*   **Library:** `netmiko`, `csv`, `warnings`
*   **Emulator:** GNS3 (Cisco IOSv)
*   **Protokol:** SSH (dengan penyesuaian algoritma `diffie-hellman-group14-sha1` dan `ssh-rsa` untuk *legacy support*).

## 🚀 Skrip Automasi (Python Scripts)
Proyek ini terdiri dari beberapa skrip Python modular:
1.  **`hosts.csv`**: Database *inventory* berisi daftar IP Management dan *hostname* router.
2.  **`cisco_audit.py`**: Skrip *Read-Only* untuk mengekstrak data dari router (Show Version, Interface Brief, CDP Neighbors).
3.  **`cisco_isis.py`**: Skrip *Push Configuration* untuk menyuntikkan IP Address, Loopback, dan menyalakan proses IS-IS beserta metriknya.
4.  **`cisco_verify.py`**: Skrip verifikasi pasca-konfigurasi untuk mengekstrak tabel *Routing* dan *Neighbors* guna memastikan konvergensi IS-IS.

## 📊 Hasil Pengujian Failover (Traffic Engineering)
Logika *failover* berhasil divalidasi. Saat jalur Fiber Optic R3-R4 diputus (melalui simulasi `shutdown` interface), protokol IS-IS secara instan melakukan konvergensi ulang (*re-convergence*) dan memindahkan seluruh tabel *routing* menuju **10.43.43.0/30 (Jalur Microwave)** dengan metrik 110.

---
*Didesain dan dikonfigurasi oleh: Ahmad Fajar Nugraha (NOC IP-Transport)*