import pygetwindow, win32con, win32gui

download_page = pygetwindow.getWindowsWithTitle("Untitled")[0]
win32gui.PostMessage(download_page._hWnd, win32con.WM_CLOSE, 0, 0)