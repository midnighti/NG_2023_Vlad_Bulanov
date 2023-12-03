import platform
import psutil

def get_system_info():
    system_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "CPU Usage (%)": psutil.cpu_percent(),
        "RAM Total (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "RAM Used (GB)": round(psutil.virtual_memory().used / (1024 ** 3), 2),
        "RAM Free (GB)": round(psutil.virtual_memory().free / (1024 ** 3), 2),
    }
    return system_info

def main():
    system_info = get_system_info()

    print("\nSystem Information:")
    for key, value in system_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
