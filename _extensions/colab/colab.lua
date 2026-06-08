-- {{< colab path/to/notebook.ipynb >}}
--
-- Renders an "Open in Colab" badge linking to the given notebook on GitHub.
-- The repo slug and branch are read from document/site metadata so they live in
-- one place (_quarto.yml), with sensible defaults.
--
--   colab-repo:   "owner/name"   (default: amhellmund/ai-engineering-in-100-days)
--   colab-branch: "branch"       (default: develop)

local BADGE = "https://colab.research.google.com/assets/colab-badge.svg"

local function meta_str(meta, key, default)
  local v = meta and meta[key]
  if v == nil then return default end
  return pandoc.utils.stringify(v)
end

return {
  ["colab"] = function(args, kwargs, meta)
    if #args == 0 then
      return pandoc.Null()
    end

    local path = pandoc.utils.stringify(args[1])
    local repo = meta_str(meta, "colab-repo", "amhellmund/ai-engineering-in-100-days")
    local branch = meta_str(meta, "colab-branch", "develop")

    local url = string.format(
      "https://colab.research.google.com/github/%s/blob/%s/%s",
      repo, branch, path
    )

    local html = string.format(
      '<a class="colab-badge" href="%s" target="_blank" rel="noopener">'
        .. '<img src="%s" alt="Open in Colab"></a>',
      url, BADGE
    )

    if quarto.doc.is_format("html") then
      return pandoc.RawInline("html", html)
    end
    -- Fallback for non-HTML output: a plain link.
    return pandoc.Link("Open in Colab", url)
  end
}
