import os
import time
import threading

def execute_bash_command(command):
    return os.system(command)

def animate():
    spin_chars = ["|", "/", "-", "\\"]
    for _ in range(20):
        for char in spin_chars:
            print(f"\rBypassing Tutul King... {char}", end="")
            time.sleep(0.1)

def main():
    # Clear terminal and print logo/banner
    os.system('clear')  # Use 'cls' instead of 'clear' for Windows
    logo = ("""
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\033[0;91m██████╗  █████╗ ██╗  ██╗██╗   ██╗██╗     
║\033[0;91m██╔══██╗██╔══██╗██║  ██║██║   ██║██║     
║\033[0;91m██████╔╝███████║███████║██║   ██║██║     
║\033[0;91m██╔══██╗██╔══██║██╔══██║██║   ██║██║     
║\033[0;91m██║  ██║██║  ██║██║  ██║╚██████╔╝███████╗
║\033[0;91m╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               \033[0;92m
 ┌─────────────────────────────────────────┐
 │ [✓] AUTHOR   : RAHULISLAM               │
 │ [✓] TOOL     : RAHUL              │
 │ [✓] STATUS   : PAID                 │
 │ [✓] GITHUB   : Rahulislam          │
 │ [✓] FACEBOOK : RAHULISLAM        │
 └─────────────────────────────────────────┘""")
    print(logo)

while True:
        print("\nMenu:")
        print("1) Bypass Rahul-Kids")
        print("2) Follow Us")
        print("0) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter the key: ")
            print("\nStarted bypass...")
            animation_thread = threading.Thread(target=animate)
            animation_thread.start()
            execute_bash_command(f"./bypass.sh {key}")
            animation_thread.join()
            print("\nBypass successfully!")
        elif choice == "2":
            os.system(f'xdg-open https://github.com/Rahullslam)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()






