#Write a SQL statement to find all documents that have more than 300 total terms,
# including duplicate terms. (Hint: You can use the HAVING clause, or you can use
# a nested query. Another hint: Remember that the count column contains the term
#frequencies, and you want to consider duplicates.) (docid, term_count)

# frequency(docid, term, count)
SELECT count(*) FROM(
    SELECT *
    FROM frequency f
    GROUP BY f.docid
    HAVING sum(f.count) > 300
)


