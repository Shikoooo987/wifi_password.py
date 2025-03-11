import subprocess
import re

def get_wifi_passwords():
    # Get list of saved WiFi profiles
    profiles_data = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True).stdout
    profiles = re.findall(r"All User Profile\s*:\s*(.*)", profiles_data)

    if not profiles:
        print("No saved WiFi profiles found.")
        return

    for profile in profiles:
        profile = profile.strip()
        print(f"\n[+] WiFi Name: {profile}")

        # Get password for each WiFi profile
        password_data = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True, text=True).stdout
        password = re.search(r"Key Content\s*:\s*(.*)", password_data)

        if password:
            print(f"[*] Password: {password.group(1)}")
        else:
            print("[-] No password found or profile is open.")

if __name__ == "__main__":
    get_wifi_passwords()