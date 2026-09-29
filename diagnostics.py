#!/usr/bin/env python3

import os
import platform
import shutil
import socket
import subprocess


def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            capture_output=True,
            timeout=10
        )
        return result.stdout.strip() or result.stderr.strip()
    except Exception as error:
        return f"Error: {error}"


def main():
    print("=" * 50)
    print("SRE Linux Diagnostics")
    print("=" * 50)

    print("\nHostname:")
    print(socket.gethostname())

    print("\nOperating System:")
    print(platform.platform())

    print("\nKernel:")
    print(platform.release())

    print("\nCPU Cores:")
    print(os.cpu_count())

    print("\nMemory:")
    print(run_command("free -h"))

    print("\nDisk Usage:")
    disk = shutil.disk_usage("/")
    print(f"Total: {disk.total // (1024**3)} GB")
    print(f"Used : {disk.used // (1024**3)} GB")
    print(f"Free : {disk.free // (1024**3)} GB")

    print("\nUptime:")
    print(run_command("uptime"))

    print("\nNetwork:")
    print(run_command("ip -brief address"))

    print("\nListening Ports:")
    print(run_command("ss -tuln"))

    print("\nTop CPU Processes:")
    print(run_command("ps aux --sort=-%cpu | head -n 6"))

    print("\nDiagnostics completed successfully.")


if __name__ == "__main__":
    main()
