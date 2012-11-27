# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:30:11 2012

group of functions for reading text data and producing a clean array

@author: dhanson
"""
import json, re, sys


def jsonLines(loc):
    content = None
    with open(loc) as f:
        content = f.readlines()
    
    r =[]
    e = re.compile('[^ a-z]', re.I)
#    e = re.compile(' [0-9]{4} ')
    d = json.JSONDecoder()
    if content is not None:
        for line in content:
            c = d.decode(line)
            if 'text' in c:
                r.append( e.sub('', c['text']) )
    
    return r
            
            
    
    
    