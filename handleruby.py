#!/usr/bin/python

# This is a Python (using pandocfilters) implementation of handleruby.hs
# from
# http://johnmacfarlane.net/pandoc/scripting.html#a-filter-for-ruby-text

from pandocfilters import toJSONFilter, Para, Emph, RawInline, stringify

def handleruby(key, value, format_, meta):
    '''
    "[R]eplace all level 2+ headers in a [...] document with regular
    paragraphs, with text in italics"
    ( http://johnmacfarlane.net/pandoc/scripting.html#a-simple-example )
    '''
    if key == 'Link':
        [txt, [url, attr]] = value
        if url.startswith('-'):
            kanji = url[1:].encode('utf-8')
            ruby = stringify(txt).encode('utf-8')
            if format_ == 'html':
                result = "<ruby>{kanji}<rp>(</rp><rt>{ruby}</rt><rp>)</rp></ruby>".format(kanji=kanji, ruby=ruby)
                return RawInline(format_, result)
            if format_ == 'latex':
                result = "\\ruby{{{kanji}}}{{{ruby}}}".format(kanji=kanji, ruby=ruby)
                return RawInline(format_, result)

if __name__ == '__main__':
    toJSONFilter(handleruby)
