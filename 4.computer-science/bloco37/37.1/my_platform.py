#!/usr/bin/env python

import platform


def system_info():
    info = {
        "computer_name": platform.node(),
        "architecture": platform.machine(),
        "operating_system": platform.system(),
        "os_version": platform.release(),
    }
    for key in info:
        print(f"{key}: {info[key]}")


system_info()
