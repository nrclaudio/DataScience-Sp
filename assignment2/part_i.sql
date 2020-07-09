CREATE TEMP VIEW new_freq(docid, term, count)
AS
    SELECT * FROM frequency
    UNION
    SELECT 'q' as docid, 'washington' as term, 1 as count
    UNION
    SELECT 'q' as docid, 'taxes' as term, 1 as count
    UNION
    SELECT 'q' as docid, 'treasury' as term, 1 as count;

CREATE TEMP VIEW  sim_matrix(docid1, docid2, similarity)
AS
    SELECT f1.docid, f2.docid, sum(f1.count*f2.count)
    FROM new_freq f1, new_freq f2
    WHERE f1.term = f2.term
    GROUP BY f1.docid, f2.docid;

SELECT *
FROM sim_matrix
WHERE sim_matrix.docid1 = 'q'
GROUP BY docid1
HAVING max(similarity)
