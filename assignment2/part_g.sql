SELECT a.row_num, b.col_num, sum(a.value * b.value) AS value
FROM A a, B b
WHERE a.col_num = b.row_num
GROUP BY a.row_num, b.col_num
