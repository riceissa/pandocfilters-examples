#!/usr/bin/python

# This is a Python (using pandocfilters) implementation of
# extracturls.hs from
# http://pandoc.org/scripting.html#queries-listing-urls

from pandocfilters import walk, Para, Emph
import sys, json

def extracturls(key, value, format_, meta):
    '''
    "[E]xtract all the URLs linked to in a markdown document" (
    http://pandoc.org/scripting.html#queries-listing-urls )
    '''
    if key == "Link" or key == "Image":
        _, _, (url, _) = value
        print(url)

if __name__ == "__main__":
    doc = json.loads(sys.stdin.read())
    if len(sys.argv) > 1:
        format_ = sys.argv[1]
    else:
        format_ = ""
    walk(doc, extracturls, format_, doc[0]['unMeta'])
