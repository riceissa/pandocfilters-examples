#!/usr/bin/python

# This is a Python (using pandocfilters) implementation of behead.hs
# from http://johnmacfarlane.net/pandoc/scripting.html#a-simple-example

from pandocfilters import toJSONFilter, Para, Emph

def behead(key, value, format_, meta):
    '''
    "[R]eplace all level 2+ headers in a [...] document with regular
    paragraphs, with text in italics"
    ( http://johnmacfarlane.net/pandoc/scripting.html#a-simple-example )
    '''
    if key == 'Header' and value[0] >= 2:
        # Here value is a list of length 3 where value[0] is an int
        # giving the level of the header; value[1] is a list containing
        # slug data (so one can reference the text like <a
        # href="#header-text">see header</a>); value[2] is a list with
        # the actual header data.
        print value
        # Emph takes a list, so we can just pass it value[2]; however,
        # Para also takes a list, so we must envelop the Emph in a list
        # first.
        return Para([Emph(value[2])])

if __name__ == '__main__':
    toJSONFilter(behead)
