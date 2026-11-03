-- S02 [Basic] GROUP BY · Week 0 · 03-Nov-2026
-- Question: Total revenue and order count per store for COMPLETED orders.
-- Tables: syw_de.orders
-- Result: 25 rows (one per store)

SELECT
  store_id,
  SUM(amount) AS revenue,
  COUNT(member_id) AS order_count
FROM `shc-syw-tech-release-planning.syw_de.orders`
WHERE status = 'COMPLETED'
GROUP BY 1;
