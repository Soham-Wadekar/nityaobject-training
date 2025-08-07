from threading import Thread
import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"⏳ Time remaining: {mins:02d}:{secs:02d}", end='\r')  
        time.sleep(1)
        seconds -= 1
    print("\n⏰ Timer finished!")

t1 = Thread(target=countdown, args=(10,))
t1.start()

user = input("💬 Type anything while the timer runs: ")
print(f"📨 You said: {user}")

t1.join()
print("🎉 Done!")
