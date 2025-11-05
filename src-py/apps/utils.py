import os
import sys

def get_index_url():
    if hasattr(sys, "_MEIPASS"):
        # py-desk.exe
        base_path = sys._MEIPASS
        index_path = os.path.join(base_path, "gui/index.html")
        server_url = f"file://{index_path}"
    else:
        # pnpm dev
        # uv run main.py
        server_url = "http://localhost:5173"
        # server_url = "http://localhost:8097"
        # base_path = os.path.dirname(os.path.abspath(__file__))
        # index_path = os.path.join(base_path, "../dist/index.html")
        # server_url = f"file://{index_path}"
    return server_url
