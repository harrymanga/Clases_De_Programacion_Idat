""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

for ch in "abc123XYX":
    
    if ch.isupper():
        
        print(ch.lower(), end="")
    
    elif ch.islower():
        
        print(ch.upper(), end="")
        
    else:
        
        print(ch, end="")