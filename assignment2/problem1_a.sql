# σdocid=10398_txt_earn(frequency)
SELECT count(*) FROM (
    SELECT *
    FROM frequency f
    WHERE f.docid == "10398_txt_earn"
);

