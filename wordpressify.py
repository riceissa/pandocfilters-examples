#!/usr/bin/python

# This is a Python (using pandocfilters) implementation of wordpressify.hs
# from http://johnmacfarlane.net/pandoc/scripting.html#latex-for-wordpress

from pandocfilters import toJSONFilter, Math

def wordpressify(key, value, format_, meta):
    '''
    Convert math formulas so they work with WordPress.
    When writing to HTML, use -m in pandoc so the $s are preserved
    '''
    if key == 'Math':
        return Math(value[0], "LaTeX " + value[1])

if __name__ == '__main__':
    toJSONFilter(wordpressify)
