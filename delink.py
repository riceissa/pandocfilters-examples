#!/usr/bin/python

# This is a Python (using pandocfilters) implementation of delink.hs
# from http://johnmacfarlane.net/pandoc/scripting.html#removing-links

from pandocfilters import toJSONFilter

def delink(key, value, format_, meta):
    '''
    Remove links but retain their text.
    '''
    if key == 'Link':
        txt, link = value
        return txt

if __name__ == '__main__':
    toJSONFilter(delink)
