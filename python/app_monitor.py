import time

def monitor_application(app_url, interval=60):
    import requests
    while True:
        try:
            response = requests.get(app_url)
            if response.status_code == 200:
                print(f"Application is running. Status code: {response.status_code}")
            else:
                print(f"Application returned status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error accessing application: {e}")
        time.sleep(interval)

if __name__ == "__main__":
    app_url = "http://localhost:5000"
    monitor_application(app_url)