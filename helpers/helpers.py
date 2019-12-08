#!/usr/bin/env python

def endwith(string: str, end: str):
    if not string.endswith(end):
        return string + end
    return string