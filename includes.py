#!/usr/bin/python

# This is a Python (using pandocfilters) implementation of includes.hs
# from http://johnmacfarlane.net/pandoc/scripting.html#include-files

from pandocfilters import toJSONFilter, CodeBlock

def includes(key, value, format_, meta):
    '''
    '''
    if key == 'CodeBlock':
        [id_, classes, namevals], contents = value
        for i in namevals:
            key, val = i
            if key == "include":
                with open(val, 'r') as f:
                    data = f.read()
                    return CodeBlock([id_, classes, namevals], data)

if __name__ == '__main__':
    toJSONFilter(includes)
