-- License: CC0

-- This Pandoc Lua filter expands MediaWiki cite web templates, which
-- are ordinarily untouched (they are passed through as MediaWiki
-- RawInlines).

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
   io.stderr:write(dump(t))
   io.stderr:write("DATE: " .. t["date"])
   local result = ""
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
   return result
end

function RawInline(elem)
   if elem.format == "mediawiki" then
      return pandoc.Str(printCiteWeb(parseTemplate(elem.text)))
   end
   return elem
end

