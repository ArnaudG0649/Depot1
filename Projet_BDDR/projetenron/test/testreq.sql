SELECT t.emailadress_id_id, m.path
FROM app1_mail m
INNER JOIN app1_to t
    ON m.mail_id=t.mail_id_id
;

SELECT COUNT(*) FROM app1_mail
    WHERE subject LIKE 'RE: %'
;



SELECT e.emailadress_id, e.interne, m.path
    FROM app1_mail m
    INNER JOIN app1_emailadress e
        ON m.emailadress_id_id = e.emailadress_id
    WHERE e.interne=False,
    e.emailadress_id LIKE '%@enron.com'
;