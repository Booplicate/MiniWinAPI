## winnie32api - Minimalistic wrapper around Win32 API using ctypes

### Requirements:
 - `Python 3.9.6`

### Examples:
```python
import winnie32api

## Windows utils
# Print title of the active window
title = winnie32api.get_active_window_title()
print(title)

# Get a rect of a window with the given title
hwnd = winnie32api.get_hwnd_by_title(r"This:\must\exist.txt - Notepad++")
rect = winnie32api.get_window_rect(hwnd)
print(rect)

## Mouse utils
# Get mouse position
mouse = winnie32api.get_screen_mouse_pos()
print(mouse)

## Notifications utils
# Make a manager for our notifications
manager = winnie32api.NotifManager("Test App", "./some_icon.ico")
# Manager can take a moment to "build" your windows app
# A way to check if it's ready
manager.is_ready()

# Let's send some notifs
manager.send("News!", "Cows can fly!")
manager.send("News!", "They lie to you!")

# Clear notifs
manager.clear()
# Here we didn't shutdown the manager
# GC will shutdown it for us, but it's better to call shutdown manually

# An example with callbacks
manager = winnie32api.NotifManager(
    "Test App",
    "./some_icon.ico",
    on_show=lambda: print("show"),
    on_hide=lambda: print("hide"),
    on_dismiss=lambda: print("dismiss"),
    on_hover=lambda: print("hover"),
    on_lmb_click=lambda: print("left click"),
    on_lmb_dclick=lambda: print("left double click"),
    on_mmb_click=lambda: print("middle click"),
    on_rmb_click=lambda: print("right click"),
    on_rmb_dclick=lambda: print("right double click")
)

manager.send("News!", "Birds are government spies!")
# Explicitly shutdown the app
manager.shutdown()

# And more...
```
