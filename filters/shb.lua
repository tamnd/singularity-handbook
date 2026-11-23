-- The filter of The Singularity Handbook. It is the filter of The Riemann Handbook (rhb.lua), and so of The
-- Handbook of Algorithms (hb.lua), with headings that carry their numbers. One Markdown source serves LaTeX and
-- EPUB.
--   Header level 1, attribute num   LaTeX: \hbchapter{num}{title}{id}; with no num, \hbintro{title}{id}
--   Header level 2, attribute num   LaTeX: \hbsection{num}{title}{id}
--   Header level 3                  LaTeX: \hbsubsection{title}{id}
--   class html-only                 the element is dropped from LaTeX
--   Div  latex-env=NAME             LaTeX: \begin{NAME}[{latex-arg}] ... \end{NAME}
--                                   (the Draft mark of a chapter is the Div .draft, latex-env=hbdraft)
--   Span latex-cmd=NAME             LaTeX: \NAME{...} (the Node line is the Span .node, latex-cmd=hblean)
--   Span .ref                       LaTeX: \hbref{...}, the number of a target after a link
-- In EPUB a heading with a number gets the number in front of its text.

local is_latex = FORMAT:match("latex") ~= nil

local function has(el, c)
  for _, x in ipairs(el.classes or {}) do if x == c then return true end end
  return false
end

local function texarg(s)
  return (s:gsub("([\\{}$&#^_%%~])", "\\%1"))
end

local function latex_inlines(inl)
  local doc = pandoc.Pandoc({ pandoc.Plain(inl) })
  local s = pandoc.write(doc, "latex")
  return (s:gsub("%s+$", ""))
end

function Header(el)
  if is_latex and has(el, "html-only") then return {} end
  local num = el.attributes["num"]
  if not is_latex then
    el.classes = el.classes:filter(function(c) return c ~= "html-only" end)
    if num then
      el.attributes["num"] = nil
      local inl = { pandoc.Str(num), pandoc.Space() }
      for _, x in ipairs(el.content) do table.insert(inl, x) end
      el.content = inl
    end
    return el
  end
  local title = latex_inlines(el.content)
  local function pdf_text(inl)
    local sym = { ell = "ℓ", infty = "∞", mathbb = "", mathrm = "", alpha = "α", beta = "β", gamma = "γ",
                  lambda = "λ", mu = "μ", pi = "π", sigma = "σ", chi = "χ", zeta = "ζ", Gamma = "Γ" }
    local t = pandoc.utils.stringify(inl)
    t = t:gsub("\\(%a+)", function(w) return sym[w] or w end):gsub("[{}_^\\]", "")
    return t
  end
  if title:find("\\%(") then
    -- math in a heading: give the bookmarks plain text
    title = "\\texorpdfstring{" .. title .. "}{" .. pdf_text(el.content) .. "}"
  end
  local id = el.identifier
  if el.level == 1 then
    if num then
      return pandoc.RawBlock("latex", "\\hbchapter{" .. num .. "}{" .. title .. "}{" .. id .. "}")
    end
    return pandoc.RawBlock("latex", "\\hbintro{" .. title .. "}{" .. id .. "}")
  elseif el.level == 2 then
    return pandoc.RawBlock("latex", "\\hbsection{" .. (num or "") .. "}{" .. title .. "}{" .. id .. "}")
  elseif el.level == 3 then
    return pandoc.RawBlock("latex", "\\hbsubsection{" .. title .. "}{" .. id .. "}")
  end
end

function Div(el)
  if is_latex and has(el, "html-only") then return {} end
  local env = el.attributes["latex-env"]
  if is_latex and env then
    local arg = el.attributes["latex-arg"]
    local open = "\\begin{" .. env .. "}" .. (arg and ("{" .. texarg(arg) .. "}") or "")
    local out = {}
    if el.identifier ~= "" then
      table.insert(out, pandoc.RawBlock("latex", "\\phantomsection\\label{" .. el.identifier .. "}"))
    end
    table.insert(out, pandoc.RawBlock("latex", open))
    for _, b in ipairs(el.content) do table.insert(out, b) end
    table.insert(out, pandoc.RawBlock("latex", "\\end{" .. env .. "}"))
    return out
  end
  if not is_latex then
    el.attributes["latex-env"] = nil
    el.attributes["latex-arg"] = nil
    return el
  end
end

function Span(el)
  if is_latex and has(el, "html-only") then return {} end
  local cmd = el.attributes["latex-cmd"]
  if is_latex and cmd then
    local out = { pandoc.RawInline("latex", "\\" .. cmd .. "{") }
    for _, x in ipairs(el.content) do table.insert(out, x) end
    table.insert(out, pandoc.RawInline("latex", "}"))
    return out
  end
  if is_latex and has(el, "ref") then
    return { pandoc.RawInline("latex", "\\hbref{" .. pandoc.utils.stringify(el.content) .. "}") }
  end
  if is_latex and #el.content == 0 and el.identifier ~= "" then
    return { pandoc.RawInline("latex", "\\phantomsection\\label{" .. el.identifier .. "}") }
  end
  if not is_latex then
    el.attributes["latex-cmd"] = nil
    if cmd == "hbsthead" then return pandoc.Strong(el.content) end
    if has(el, "ref") then
      return { pandoc.Str("\u{2009}"), pandoc.Span(el.content, { class = "ref" }) }
    end
    return el
  end
end

function CodeBlock(el)
  if is_latex and has(el, "plain") then
    local t = el.text:gsub("[\\{}]", { ["\\"] = "\\textbackslash{}", ["{"] = "\\{", ["}"] = "\\}" })
    return pandoc.RawBlock("latex", "\\begin{hbverbatim}\n" .. t .. "\n\\end{hbverbatim}")
  end
end
