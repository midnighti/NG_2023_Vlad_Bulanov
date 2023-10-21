import platform
import getpass

def getSystemInfo():
    system_info = platform.uname()
    print(f"system: {system_info.system}")
    print(f"node: {system_info.node}")
    print(f"release: {system_info.release}")
    print(f"version: {system_info.version}")
    print(f"machine: {system_info.machine}")

def getUsername():
    username = getpass.getuser()
    print(f"username: {username}")

def main():
    getSystemInfo()
    getUsername()

if __name__ == "__main__":
    main()