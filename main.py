import json
import time
import requests
import os
from tracker import get_running_apps, get_active_window_info
from updater import check_for_update
from utils import get_device_id, ensure_folder

# Load config
with open("config.json") as f:
    config = json.load(f)

server_url = config["server_url"]
device_id = get_device_id() if config["device_id"] == "auto" else config["device_id"]
log_folder = os.path.join("logs", device_id)
ensure_folder(log_folder)

def save_and_upload(data, filename):
    filepath = os.path.join(log_folder, filename)
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(json.dumps(data) + "\n")
    try:
        requests.post(
            server_url + f"upload/{device_id}",
            files={"file": open(filepath, "rb")},
            timeout=10
        )
    except Exception as e:
        print("[Upload Error]", e)

def main():
    counter = 0
    while True:
        save_and_upload(get_running_apps(), "app_usage.json")
        save_and_upload(get_active_window_info(), "active_window.json")

        counter += 1
        if counter % (config["check_update_interval"] // 5) == 0:
            check_for_update(server_url, config["current_version"])

        time.sleep(5)

if __name__ == "__main__":
    main()
