
SELECT * FROM
(
SELECT f1.docid AS f1docid, f2.docid AS f2docid, sum(f1.count*f2.count)
FROM frequency f1, frequency f2
WHERE f1.term = f2.term AND f1.docid < f2.docid
GROUP BY f1.docid, f2.docid
) as result
WHERE result.f1docid = '10080_txt_crude' AND result.f2docid = '17035_txt_earn'

