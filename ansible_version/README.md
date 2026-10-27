# Automated Cisco IS-IS Deployment using Ansible 🚀

This repository contains an Infrastructure as Code (IaC) project for automating the deployment of the IS-IS routing protocol across a Cisco IOSv network topology in GNS3. It features High Availability (HA) routing and automated Day-2 operations.

## 🎯 Project Objectives
- **Zero-Touch Provisioning:** Automate the configuration of physical interfaces, Loopbacks, and IS-IS routing protocols simultaneously across multiple nodes.
- **High Availability & Traffic Engineering:** Implement redundant links (Fiber Optic & Microwave) between core routers, utilizing IS-IS metric manipulation to ensure seamless automatic failover.
- **Configuration Management:** Ensure idempotent execution and automate the backup of `running-config` from RAM to local storage.

## 🏗️ Network Topology
*Please insert your GNS3 topology screenshot here*
`![Network Topology](topology.png)`

**Infrastructure Details:**
- **Nodes:** 4x Cisco IOSv Routers (R1, R2, R3, R4)
- **Environment:** GNS3 hosted on Pop!_OS (Linux)
- **OOB Management:** DHCP NAT via GNS3 (`192.168.122.0/24`)
- **Redundancy (R3 ↔ R4):**
  - **Main Link (Fiber Optic):** Metric 10
  - **Backup Link (Microwave):** Metric 50

## 🛠️ Prerequisites
- Ansible installed on the control node.
- GNS3 with Cisco IOSv appliances.
- Reachability to the Out-of-Band (OOB) management network.

## 📂 Repository Structure
- `inventory/hosts.ini`: Ansible inventory defining the routers and SSH credentials.
- `playbooks/deploy_isis_topology.yml`: Main playbook for interface IP provisioning, IS-IS global/interface routing, and `write memory`.
- `playbooks/backup_config.yml`: Playbook to fetch and save `show running-config` to local `.txt` files.
- `backups/`: Directory where the automated configuration backups are stored.
- `ansible.cfg`: Ansible configuration file for optimal SSH and connection settings.

## 🚀 How to Usage

**1. Deploy the Network (Provisioning & IS-IS)**
Run the deployment playbook to configure all routers idempotently:
```bash
ansible-playbook playbooks/deploy_isis_topology.yml
