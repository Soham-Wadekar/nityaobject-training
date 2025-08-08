import subprocess
from datetime import datetime as dt

def internet_health_check(host="google.com", count=3):

    print(f"Pinging {host} {count} times.../n")

    proc = subprocess.Popen(
        ["ping", "-c", str(count), host],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    with open("Day-5/log.txt", "a") as file:
        file.write(f"\n[{dt.now()}]\n")
        for line in proc.stdout:
            file.write(line)

        proc.wait()
        if proc.returncode != 0:
            file.write(f"{proc.stderr.read()}")

    file.close()

internet_health_check()