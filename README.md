# MAC Changer

`macchanger.py` is a program designed for Linux-based systems to change the MAC address of network interfaces. This tool allows you to temporarily or permanently change the MAC address using specified parameters.

## Usage

```bash
python3 macchanger.py -m <mac_address> -i <interface_name>
```

**or**
```bash
python3 macchanger.py --mac <mac_address> --interface <interface_name>
```

**arameters**
-m or --mac (Required): Specifies the new MAC address to be set.
-i or --interface (Required): Specifies the network interface whose MAC address will be changed (e.g., wlan0, eth0).

**Example Usage:**
python3 macchanger.py -m 00:11:22:33:44:55 -i wlan0

**Legal Notice and Disclaimer**
This program is intended for authorized and ethical use only. Changing a MAC address can have legal implications; therefore, users are solely responsible for ensuring their usage complies with applicable laws. The developers of this tool do not assume any responsibility for misuse or unauthorized actions carried out using this program.

>**Note:** macchanger.py is designed to work on Linux systems only.


This README provides instructions for using the program and includes a legal disclaimer to limit liability.
