#πterm(σdocid=10398_txt_earn and count=1(frequency))

SELECT count(*) FROM(
    SELECT f.term
    FROM frequency f
    WHERE f.docid = "10398_txt_earn" AND f.count = 1
)
