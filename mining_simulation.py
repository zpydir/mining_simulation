import subprocess
import psutil
import logging
import time
import os
import signal


logging.basicConfig(filename="crypto_jacking_simulation.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


mining_pool = "stratum+tcp://eth-eu1.nanopool.org:9999"
wallet_address = "your_wallet_address"
miner_name = "red_team_miner_001"


mining_command = [
    "ethminer",  
    "-P", f"{mining_pool}/{wallet_address}/{miner_name}"
]


def start_mining():
    try:
        
        process = subprocess.Popen(mining_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info("Mining simulation started on authorized machine.")
        return process
    except Exception as e:
        logging.error(f"Error while starting mining: {e}")
        return None


def stop_mining(process):
    try:
        
        process.terminate()  
        process.wait(timeout=5)  
        logging.info("Mining simulation stopped.")
    except Exception as e:
        logging.error(f"Error while stopping mining: {e}")


def monitor_cpu():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        logging.info(f"Current CPU Usage: {cpu_usage}%")
        time.sleep(5)


def run_simulation(duration_minutes=30):
    process = start_mining()
    if process:
        logging.info(f"Simulating mining for {duration_minutes} minutes...")
        
        monitor_process = subprocess.Popen(['python', 'monitor_cpu.py'])
        time.sleep(duration_minutes * 60)
        stop_mining(process)
        logging.info("Simulation complete.")

if __name__ == "__main__":
    try:
        run_simulation(30) 
    except KeyboardInterrupt:
        logging.info("Mining simulation interrupted by user.")
        exit()
