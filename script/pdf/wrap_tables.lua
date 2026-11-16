-- Ensure ordinary Org tables wrap within the PDF text area.
--
-- Pandoc emits l/c/r LaTeX columns for Org tables without width hints.
-- Those columns cannot wrap long prose and can overrun the page boundary.
-- Adding explicit relative widths makes Pandoc emit paragraph (p{}) columns;
-- longtable can then also break between multi-line rows across pages.
--
-- Respect widths already specified with Org <N> hints. For mixed tables,
-- use the existing proportions as weights and apportion unspecified columns
-- equally, normalized to one available line width.
function Table(tbl)
  local count = #tbl.colspecs
  if count == 0 then return nil end

  local weights = {}
  local needs_widths = false
  local total = 0
  for i, col in ipairs(tbl.colspecs) do
    local width = col[2]
    if type(width) ~= "number" or width <= 0 then
      width = 1 / count
      needs_widths = true
    end
    weights[i] = width
    total = total + width
  end

  -- Leave fully specified tables untouched, including their exact proportions.
  if not needs_widths then return nil end

  for i, col in ipairs(tbl.colspecs) do
    tbl.colspecs[i] = {col[1], weights[i] / total}
  end
  return tbl
end
