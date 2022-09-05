# winnie32api - Minimalistic wrapper around Wind32 API using ctypes

### Requirements:
 - `Python 3.9.6`

### Examples:
```python
import winnie32api

# Print title of the active window
title = winnie32api.get_active_window_title()
print(title)

# Get a rect of a window with the given title
hwnd = winnie32api.get_hwnd_by_title(r"This:\must\exist.txt - Notepad++")
rect = winnie32api.get_window_rect(hwnd)
print(rect)

# Get mouse position
mouse = winnie32api.get_screen_mouse_pos()
print(mouse)

# Send notifications
manager = winnie32api.NotifManager("Test Manager", "./some_icon.ico")
manager.send("News!", "Cows can fly!")
manager.send("News!", "They lie to you!")

# Clear notifs
manager.clear()

manager.send("News!", "Birds are government spies!")
# Shutdown the app
manager.shutdown()
```
