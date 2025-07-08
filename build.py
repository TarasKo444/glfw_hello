#!/usr/bin/env python3

import os
import subprocess

build_dir = os.path.dirname(__file__) + "/build"

if not os.path.exists(build_dir):
    os.makedirs(build_dir)
    subprocess.call(["cmake", ".."], cwd=build_dir)

subprocess.call(["cmake", "--build", "."], cwd=build_dir)
