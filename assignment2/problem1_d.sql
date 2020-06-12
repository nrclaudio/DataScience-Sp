#Write a SQL statement to count the number of unique documents
#containing the word "law" or containing the word "legal"
#(If a document contains both law and legal, it should only be counted once)

SELECT count(*) FROM(
    SELECT DISTINCT *
    FROM frequency f
    WHERE f.term = "law" OR f.term = "legal"
)
