# Crypto-Jacking Simulation for Educational Purposes

## Introduction

This repository contains a Python-based simulation of cryptocurrency mining (also known as **cryptojacking**) to demonstrate how unauthorized mining can impact the performance of systems. The goal is to educate users on how such attacks work and the potential consequences they have on devices and networks. **This script is designed for use in controlled, authorized environments only**.

### What is Crypto-Jacking?

**Crypto-jacking** is a form of cyberattack where an attacker secretly uses a victim's computing resources to mine cryptocurrency without their consent. This can be done via malicious scripts or software running on a compromised system.

### Key Features

- **Simulate Cryptocurrency Mining**: This Python script uses `ethminer` to simulate a mining attack on your own machine.
- **Red Team Simulation**: Helps security professionals understand the tactics, techniques, and procedures (TTPs) used in real-world cryptojacking attacks.
- **Impact Demonstration**: Showcases the CPU/GPU load and network impact of running cryptojacking software.

---

## Ethical Usage Disclaimer

This repository is intended solely for **educational and ethical purposes**. It should **never** be used for unauthorized or malicious activities.

**Important**: Only run this simulation in environments where you have explicit permission, such as your own machine or a system set up for testing purposes. Running this code without permission is illegal and unethical.

### If you're a Red Team or Penetration Tester:
This repository can be used in a **test lab environment** to simulate the effects of cryptojacking and assess how well your organization’s defenses can detect unauthorized mining activities.

---

## Prerequisites

Before running this script, ensure that:

- You have **explicit authorization** to run the mining simulation on the target system.
- You are using it for **educational or testing purposes only**.
- You have Python 3.x installed and the following Python libraries:
  - `requests`
  - `psutil`
  - `subprocess`
  - `logging`

### How to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/zpydir/crypto-jacking-simulation.git
   cd crypto-jacking-simulation

2: Install the Requirements
```bash
psutil==5.9.4
requests==2.28.2
subprocess32==3.5.4
```
Usage
Running the Mining Simulation
Open the scripts/mining_simulation.py file and adjust the settings (e.g., your mining pool address and wallet address).
Start the mining simulation by running the following command in the terminal:
```bash
python scripts/mining_simulation.py
```
Stopping the Simulation
To stop the simulation, you can use:
```bash
pkill ethminer
```
Testing the Impact
- CPU/GPU Usage: Monitor the system's CPU and GPU usage via the system task manager or performance monitoring tools like htop or Task Manager to see the resource load.
- Network Traffic: Use tools like Wireshark to inspect network traffic for connections to mining pools.

