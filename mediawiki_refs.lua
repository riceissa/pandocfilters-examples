-- License: CC0

-- This Pandoc Lua filter expands MediaWiki cite web templates, which
-- are ordinarily untouched (they are passed through as MediaWiki
-- RawInlines).

-- Unfortunately, as of March 2018 it seems like Pandoc's MediaWiki
-- reader does not parse the "name" attribute of <ref> tags. This
-- means there is no way to associate repeated ref citations with the
-- same content. In fact, all of the repeated instances (like <ref
-- name="citename" />) appear as blank footnotes.

-- This is trim3 from http://lua-users.org/wiki/StringTrim
function trim(s)
   return s:gsub("^%s+", ""):gsub("%s+$", "")
end

function parseTemplate(refstring)
   local result = {}
   local argcount = 0
   for arg in string.gmatch(refstring, "[^|]+") do
      local count = 0
      local value = ""
      local key = ""
      for k in arg:gmatch("[^={}]+") do
         -- There are two types of template arguments: those that are
         -- like {{key=value}}, and those that are just {{value}}.
         if count == 0 then
            value = k
         elseif count == 1 then
            key = value
            value = k
         end
         count = count + 1
      end
      if count == 1 then
         result[argcount] = trim(value)
      else
         result[trim(key)] = trim(value)
      end
      count = 0
      argcount = argcount + 1
   end
   return result
end

function printCiteWeb(t)
   local result = ""
   if t["last"] ~= nil then
      result = result .. t["last"] .. ", "
   end
   if t["first"] ~= nil then
      result = result .. t["first"] .. ". "
   end
   if t["author"] ~= nil then
      result = result .. t["author"] .. ". "
   end
   if t["title"] ~= nil then
      result = result .. "“" .. t["title"] .. "”. "
   end
   if t["publisher"] ~= nil then
      result = result .. t["publisher"] .. ". "
   end
   if t["date"] ~= nil then
      result = result .. t["date"] .. ". "
   end
   return trim(result)
end

function RawInline(elem)
   if elem.format == "mediawiki" then
      return pandoc.Str(printCiteWeb(parseTemplate(elem.text)))
   end
   return elem
end

