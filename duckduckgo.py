#!/usr/bin/python

from pandocfilters import toJSONFilter, stringify, Link

def duck(key, value, format_, meta):
    '''
    If a link is of the form "!STRING", use the !-expression to search
    DuckDuckGo.
    '''
    if key == 'Link':
        [txt, [url, attr]] = value
        if url.startswith("!"):
            url = "http://duckduckgo.com/?q=" + url + " " + stringify(txt)
            return Link(txt, [url, attr])

if __name__ == '__main__':
    toJSONFilter(duck)
