import time
import re
import os

IP_PATTERN = r"from ([\d\.]+) port"

def monitor_logs(log_path):
    print(f"--- [AEGIS SYSTEM ACTIVE: MONITORING {log_path}] ---")
    if not os.path.exists(log_path):
        print(f"Error: {log_path} not found.")
        return

    with open(log_path, "r") as f:
        f.seek(0, 2) 
        while True:
            line = f.readline()
            if not line:
                time.sleep(1) 
                continue
            if "Failed password" in line:
                match = re.search(IP_PATTERN, line)
                if match:
                    ip = match.group(1)
                    print(f"[⚠️ SECURITY ALERT] Failed Login Attempt | Source IP: {ip}")
            elif "Accepted password" in line:
                print(f"[✓] Successful Login Detected.")

if __name__ == "__main__":
    monitor_logs("logs/auth.log")