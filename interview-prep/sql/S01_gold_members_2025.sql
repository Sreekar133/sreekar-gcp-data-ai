-- S01 [Basic] Filtering · Week 0 · 03-Nov-2026
-- Question: List Gold-tier members who joined in 2025, newest first.
-- Tables: syw_de.members
-- Result: 356 rows

SELECT *
FROM `shc-syw-tech-release-planning.syw_de.members`
WHERE tier = "Gold"
  AND join_date BETWEEN "2025-01-01" AND "2025-12-31"
ORDER BY join_date ASC;
