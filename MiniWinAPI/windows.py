import ctypes
from ctypes.wintypes import (
    BOOL as C_BOOL,
    HWND as C_HWND,
    LPARAM,
    RECT
)

from typing import (
    Optional
)

from .common import (
    HWND,
    Rect,
    Pack,
    WinAPIError,
    _get_last_err,
    _reset_last_err
)


user32 = ctypes.windll.user32


def get_hwnd_by_title(title: str) -> Optional[HWND]:
    """
    Returns first window hwnd with the given title
    """
    pack = Pack(None)

    @ctypes.WINFUNCTYPE(C_BOOL, C_HWND, LPARAM)
    def callback(hwnd: int, lparam: int) -> bool:
        c_hwnd = ctypes.c_int(hwnd)

        if user32.IsWindowVisible(c_hwnd) and user32.IsWindow(c_hwnd):
            title_len = user32.GetWindowTextLengthW(c_hwnd)
            buffer = ctypes.create_unicode_buffer(title_len + 1)
            user32.GetWindowTextW(
                c_hwnd,
                buffer,
                title_len + 1
            )
            if title == buffer.value:
                pack.value = hwnd
                return False

        return True

    user32.EnumWindows(callback, LPARAM(0))
    return pack.value

def get_window_title(hwnd: HWND) -> str:
    """
    Returns a window title as a str
    """
    _reset_last_err()

    title_len = user32.GetWindowTextLengthW(hwnd)
    if not title_len:
        last_err = _get_last_err()
        if last_err:
            raise WinAPIError("failed to get title length", last_err)

    buffer = ctypes.create_unicode_buffer(title_len + 1)
    result = user32.GetWindowTextW(
        hwnd,
        buffer,
        title_len + 1
    )
    if result != title_len:
        last_err = _get_last_err()
        if last_err:
            raise WinAPIError("failed to get title", last_err)

    return buffer.value

def get_window_rect(hwnd: HWND) -> Rect:
    """
    Returns a window rect
    """
    c_rect = RECT()
    result = user32.GetWindowRect(hwnd, ctypes.byref(c_rect))
    if not result:
        raise WinAPIError("failed to get window rect", _get_last_err())

    return Rect.from_coords(c_rect.top, c_rect.left, c_rect.bottom, c_rect.right)


def get_active_window_hwnd() -> Optional[HWND]:
    """
    Returns active window title hwnd (id)
    """
    active_win_hwnd = user32.GetForegroundWindow()
    if not active_win_hwnd or not user32.IsWindowVisible(active_win_hwnd):
        return None

    return active_win_hwnd

def get_active_window_title() -> Optional[str]:
    """
    Returns active window title as a str
    """
    hwnd = get_active_window_hwnd()
    if hwnd is None:
        return None

    return get_window_title(hwnd)

def get_active_window_rect() -> Optional[Rect]:
    """
    Returns active window rect
    """
    hwnd = get_active_window_hwnd()
    if hwnd is None:
        return None

    return get_window_rect(hwnd)
