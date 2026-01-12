import subprocess
import re

def get_wifi_mac_windows():
    try:
        result = subprocess.check_output(
            ["netsh", "wlan", "show", "interfaces"],
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        # Regex più robusta e corretta
        match = re.search(
            r"(address|indirizzo).*?([0-9A-Fa-f:-]{17})",
            result,
            re.IGNORECASE
        )

        if match:
            return match.group(2).upper()

        return None

    except Exception as e:
        print("Errore:", e)
        return None


def main():
    mac = get_wifi_mac_windows()
    print("MAC Wi-Fi:", mac)
    mac = mac.replace(":", "-")
    print(f"MAC Wi-Fi con trattino: {mac}")

if __name__ == "__main__":
    main()