#!/usr/bin/env python3

import os
import subprocess

script_dir = os.path.dirname(__file__)
build_dir = os.path.dirname(__file__) + "/build"

if not os.path.exists(build_dir):
    os.makedirs(build_dir)
    if os.name == 'nt':
        subprocess.call(["cmake", "-G", "Ninja", script_dir], cwd=build_dir)
    else:
        subprocess.call(["cmake", script_dir], cwd=build_dir)

subprocess.call(["cmake", "--build", "."], cwd=build_dir)
