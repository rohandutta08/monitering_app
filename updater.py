import requests
import os
import sys

def check_for_update(server_url, current_version):
    try:
        r = requests.get(server_url + "version.json")
        if r.status_code == 200:
            version_info = r.json()
            if version_info["version"] != current_version:
                print("[Update] New version available:", version_info["version"])
                download_url = server_url + version_info["exe_name"]
                new_exe = requests.get(download_url, stream=True)
                with open("update.exe", "wb") as f:
                    for chunk in new_exe.iter_content(chunk_size=8192):
                        f.write(chunk)
                os.startfile("update.exe")
                sys.exit(0)
    except Exception as e:
        print("[Update Error]", e)
