import ctypes
from ctypes.wintypes import POINT

from .common import Point, WinAPIError, _get_last_err


user32 = ctypes.windll.user32


def get_screen_mouse_pos() -> Point:
    """
    Returns mouse position in screen coords
    """
    c_point = POINT()
    result = user32.GetCursorPos(ctypes.byref(c_point))
    if not result:
        raise WinAPIError("failed to get mouse position", _get_last_err())

    return Point(c_point.x, c_point.y)
