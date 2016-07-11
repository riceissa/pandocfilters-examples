#!/usr/bin/python

# This is a Python (using pandocfilters) implementation of behead.hs
# from http://pandoc.org/scripting.html#a-simple-example

from __future__ import print_function
import sys

from pandocfilters import toJSONFilter, Para, Emph

def behead(key, value, format_, meta):
    '''
    "[R]eplace all level 2+ headers in a markdown document with regular
    paragraphs, with text in italics."
    ( http://pandoc.org/scripting.html#a-simple-example )
    '''
    if key == "Header":
        # Here n is an int giving the level of the header, and xs is a list
        # with the actual header data. The discarded middle value contains the
        # slug data.
        n, _, xs = value
        if n >= 2:
            # Emph takes a list, so we can just pass it xs; however, Para also
            # takes a list, so we must envelop the Emph in a list first.
            return Para([Emph(xs)])

if __name__ == '__main__':
    toJSONFilter(behead)
