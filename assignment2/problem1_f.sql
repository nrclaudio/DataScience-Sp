# Write a SQL statement to count the number of unique documents that contain
# both the word 'transactions' and the word 'world'. (Hint: Find the docs that
# contain one word and the docs that contain the other word separately, then find the intersection.)
SELECT count(*) FROM(
    SELECT *
    FROM frequency f1, frequency f2
    WHERE f1.docid = f2.docid AND f1.term = "transaction" AND f2.term = "world"
)

