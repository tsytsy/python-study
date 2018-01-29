#!/usr/bin/env python
# _*_ coding:utf8 _*_

import json
import struct
import socket

import os
from os.path import join, getsize


def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size