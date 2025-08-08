import subprocess
from datetime import datetime as dt

def internet_health_check(host="", count=3):
    print(f"Pinging {host} {count} times...\n")

    try:
        # raise RuntimeError("Simulated error")
        proc = subprocess.Popen(
            ["ping", "-c", str(count), host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
    except FileNotFoundError:
        with open("Day-5/log.txt", "a") as file:
            file.write(f"\n[{dt.now()}]\nERROR: ping command not found\n")
        return
    except Exception as e:
        with open("Day-5/log.txt", "a") as file:
            file.write(f"\n[{dt.now()}] \nERROR: unexpected error when starting ping: {e}\n")
        return

    try:
        stdout, stderr = proc.communicate(timeout=10) 
    except subprocess.TimeoutExpired:
        proc.kill()
        stdout, stderr = proc.communicate()
        with open("Day-5/log.txt", "a") as file:
            file.write(f"\n[{dt.now()}] \nERROR: ping command timed out\n")
        return
 

    with open("Day-5/log.txt", "a") as file:
        file.write(f"\n[{dt.now()}]\n")
        if proc.returncode == 0:
            file.write(f"SUCCESS: ping successful: {stdout}")
        else:
            file.write(f"ERROR: ping failed with error: {stderr}")

internet_health_check(host="google.com")
