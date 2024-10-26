import subprocess
import optparse
import re

def getMacAddress():
    parseOption = optparse.OptionParser()
    parseOption.add_option("-i","--interface",dest="interface",help="which change interface ?")
    parseOption.add_option("-m","--mac",dest="macAddress",help="set mac address.")
    return parseOption.parse_args()

def changeMacAddress(Interface,MacAddress):
    subprocess.call(["ifconfig",Interface,"down"])
    subprocess.call(["ifconfig",Interface,"hw","ether",MacAddress])
    subprocess.call(["ifconfig",Interface,"up"])

def checkMacAddress(Interface,MacAddress):
    interface = subprocess.check_output(["ifconfig",Interface])
    newMacAddress = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(interface))
    if newMacAddress.group(0) == MacAddress:
        return [True , newMacAddress.group(0)]
    else:
        return False
def run():
    print("Changing mac address...")
    (userInterface,argument) = getMacAddress()
    changeMacAddress(userInterface.interface,userInterface.macAddress)
    result = checkMacAddress(userInterface.interface,userInterface.macAddress)
    if result == False:
        print("Error. Not changed mac address.")
    else:
        print(f"Success. Changed mac address: {result[1]}")
run()