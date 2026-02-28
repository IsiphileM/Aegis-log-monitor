import time

def simulate_attack(log_path):
    print("--- [STARTING BRUTE-FORCE SIMULATION] ---")
    with open(log_path, "a") as f:
        for i in range(5):
            print(f"Injecting failed attempt {i+1}...")
            f.write(f"Feb 28 18:10:0{i} server-01 sshd[999]: Failed password for root from 172.16.0.5 port 1234 ssh2\n")
            f.flush() 
            time.sleep(2)
    print("--- [SIMULATION COMPLETE] ---")

if __name__ == "__main__":
    simulate_attack("logs/auth.log")