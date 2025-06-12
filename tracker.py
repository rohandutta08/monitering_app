import psutil
import win32gui
import win32process
from datetime import datetime

def get_active_window_info():
    try:
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)
        return {
            "timestamp": datetime.now().isoformat(),
            "application": process.name(),
            "window_title": win32gui.GetWindowText(hwnd)
        }
    except:
        return {"timestamp": datetime.now().isoformat(), "application": None, "window_title": None}

def get_running_apps():
    data = {
        "timestamp": datetime.now().isoformat(),
        "applications": []
    }
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            data["applications"].append({
                "pid": proc.info['pid'],
                "name": proc.info['name']
            })
        except:
            continue
    return data
