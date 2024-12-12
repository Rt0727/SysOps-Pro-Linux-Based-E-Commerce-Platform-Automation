import os
import subprocess

class ServerManager:
    @staticmethod
    def start_service(service_name):
        try:
            subprocess.run(["sudo", "systemctl", "start", service_name], check=True)
            return f"{service_name} started successfully."
        except subprocess.CalledProcessError as e:
            return f"Error starting {service_name}: {e}"

    @staticmethod
    def stop_service(service_name):
        try:
            subprocess.run(["sudo", "systemctl", "stop", service_name], check=True)
            return f"{service_name} stopped successfully."
        except subprocess.CalledProcessError as e:
            return f"Error stopping {service_name}: {e}"

    @staticmethod
    def check_disk_space():
        result = subprocess.run(["df", "-h"], capture_output=True, text=True)
        return result.stdout