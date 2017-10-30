# Examples of Pandoc filters

This repository contains various examples of Pandoc filters, using the [pandocfilters](https://github.com/jgm/pandocfilters) Python module.
So far, most of the filters are just Python implementations of the Haskell examples on the [scripting page](http://johnmacfarlane.net/pandoc/scripting.html).

When writing filters, printing out the abstract syntax tree using `-t native`
or `-t json` on Pandoc is helpful. All a filter does it manipulate that JSON
file to get another JSON file, which feeds back into Pandoc.

For [Lua filters](http://pandoc.org/lua-filters.html), the same trick works,
but there is no intermediate JSON step, so it takes more imagination to see
what's going on. Even more unfortunately, Lua lacks a native way to print
tables (its list/dictionary data structure), and since the Lua library is
embedded in the Pandoc executable, it doesn't seem easy to download a library
like [Penlight](https://stevedonovan.github.io/Penlight/api/libraries/pl.pretty.html#dump)
to dump tables for inspection. Lua filters *are* faster and don't require
GHC/Python though.
