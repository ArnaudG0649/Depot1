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

----Req n°2 mail reçu version longue----
SELECT lastname,firstname,nbmail FROM
    (SELECT emp.lastname,emp.firstname, COUNT(*) as nbmail   
        FROM app1_emailadress ea
        INNER JOIN app1_employee emp
            ON emp.employee_id=ea.employee_id_id
        INNER JOIN (
            SELECT t.emailadress_id_id as ead
            FROM app1_to t
            INNER JOIN app1_mail m
                ON t.mail_id_id=m.mail_id 
        WHERE Timedate > '2000-01-01 00:00:00'
        ) t2
        ON t2.ead=ea.emailadress_id
        GROUP BY emp.employee_id
    ) T
    WHERE nbmail>100
; 


----version longue où l'on peut filtrer les expéditeurs internes ou externes---- 
SELECT lastname,firstname,nbmail FROM
    (SELECT emp.lastname,emp.firstname, COUNT(*) as nbmail  
        FROM app1_emailadress ea
        INNER JOIN app1_employee emp
            ON emp.employee_id=ea.employee_id_id
        INNER JOIN app1_to t
            ON t.emailadress_id_id=ea.emailadress_id
        LEFT JOIN 
            (SELECT m.mail_id , ea2.interne
            FROM app1_mail m 
            INNER JOIN app1_emailadress ea2
                ON m.emailadress_id_id=ea2.emailadress_id
            WHERE m.Timedate > '2000-01-01 00:00:00' /* AND ea2.interne=False */
            ) m
            ON m.mail_id=t.mail_id_id
        GROUP BY emp.employee_id
    ) T
     WHERE nbmail>100 
;

----Version avec Tableau qui marche pas----
SELECT Ti.lastname,Ti.firstname,(Ti.nbinterne + Te.nbexterne) as nbmail, Ti.nbinterne, Te.nbexterne FROM
    (SELECT emp.employee_id, emp.lastname,emp.firstname, COUNT(m.mail_id) as nbinterne   
        FROM app1_emailadress ea
        INNER JOIN app1_employee emp
            ON emp.employee_id=ea.employee_id_id
        INNER JOIN app1_to t
            ON t.emailadress_id_id=ea.emailadress_id
        LEFT JOIN app1_mail m 
            ON m.mail_id=t.mail_id_id
        INNER JOIN app1_emailadress ea2 
            ON m.emailadress_id_id=ea2.emailadress_id
        WHERE Timedate > '2000-01-01 00:00:00' AND ea2.interne=True
        GROUP BY emp.employee_id
    ) Ti
    LEFT OUTER JOIN 
    (SELECT emp.employee_id, emp.lastname,emp.firstname, COUNT(m.mail_id) as nbexterne   
        FROM app1_emailadress ea
        INNER JOIN app1_employee emp
            ON emp.employee_id=ea.employee_id_id
        INNER JOIN app1_to t
            ON t.emailadress_id_id=ea.emailadress_id
        LEFT JOIN app1_mail m 
            ON m.mail_id=t.mail_id_id
        INNER JOIN app1_emailadress ea2 
            ON m.emailadress_id_id=ea2.emailadress_id
        WHERE Timedate > '2000-01-01 00:00:00' AND ea2.interne=False
        GROUP BY emp.employee_id
    ) Te
        ON Ti.employee_id=Te.employee_id 
    WHERE Ti.nbinterne + Te.nbexterne>100
;


----Version avec Tableau qui marche----
SELECT Ti.lastname, Ti.firstname, (Ti.nbinterne + Te.nbexterne) as nbmail, Ti.nbinterne, Te.nbexterne FROM
    (SELECT emp.employee_id, emp.lastname, emp.firstname, COUNT(m.mail_id) as nbinterne  
        FROM app1_emailadress ea
        INNER JOIN app1_employee emp
            ON emp.employee_id=ea.employee_id_id
        LEFT JOIN app1_to t
            ON t.emailadress_id_id=ea.emailadress_id
        LEFT JOIN 
            (SELECT m.mail_id , ea2.interne
            FROM app1_mail m 
            INNER JOIN app1_emailadress ea2
                ON m.emailadress_id_id=ea2.emailadress_id
            WHERE m.Timedate > '2000-01-01 00:00:00' AND ea2.interne=True
            ) m
            ON m.mail_id=t.mail_id_id
        GROUP BY emp.employee_id 
    ) Ti
    LEFT OUTER JOIN 
    (SELECT emp.employee_id, emp.lastname,emp.firstname, COUNT(m.mail_id) as nbexterne  
        FROM app1_emailadress ea
        INNER JOIN app1_employee emp
            ON emp.employee_id=ea.employee_id_id
        LEFT JOIN app1_to t
            ON t.emailadress_id_id=ea.emailadress_id
        LEFT JOIN 
            (SELECT m.mail_id , ea2.interne
            FROM app1_mail m 
            INNER JOIN app1_emailadress ea2
                ON m.emailadress_id_id=ea2.emailadress_id
            WHERE m.Timedate > '2000-01-01 00:00:00' AND ea2.interne=False
            ) m
            ON m.mail_id=t.mail_id_id
        GROUP BY emp.employee_id
    ) Te
        ON Ti.employee_id=Te.employee_id 
    WHERE Ti.nbinterne + Te.nbexterne>100
;

----Requête 4----

SELECT emp.employee_id, emp2.employee_id, COUNT(m.mail_id) as nbmail /*Cette requête compte le nombre de mailS que l'employé de gauche à envoyé à l'employé de droite*/
    FROM app1_employee emp
    INNER JOIN app1_emailadress ea ON emp.employee_id=ea.employee_id_id
    LEFT JOIN app1_mail m ON m.emailadress_id_id=ea.emailadress_id
    INNER JOIN app1_to t ON t.mail_id_id=m.mail_id
    LEFT JOIN app1_emailadress ea2 ON ea2.emailadress_id=t.emailadress_id_id
    INNER JOIN app1_employee emp2 ON emp2.employee_id=ea2.employee_id_id
GROUP BY emp.employee_id, emp2.employee_id
ORDER BY emp.employee_id, emp2.employee_id
;



(SELECT t.employee_id, COUNT(m.mail_id), m.emailadress_id_id FROM app1_mail m 
RIGHT JOIN
    (SELECT ea2.employee_id, t.mail_id_id FROM app1_to t 
    RIGHT JOIN
        (SELECT ea2.emailadress_id, emp2.employee_id FROM app1_emailadress ea2
                    INNER JOIN app1_employee emp2 ON emp2.employee_id=ea2.employee_id_id) ea2 ON ea2.emailadress_id=t.emailadress_id_id /*les adresses mails des destinataires*/
    ) t ON t.mail_id_id=m.mail_id
GROUP BY t.employee_id, m.emailadress_id_id
) m 






SELECT m.employee_id, m.nbmail, m.emailadress_id_id, ea.employee_id FROM 
(SELECT ea.emailadress_id, emp.employee_id FROM app1_emailadress ea
                INNER JOIN app1_employee emp ON emp.employee_id=ea.employee_id_id
) ea
RIGHT JOIN
(SELECT t.employee_id, COUNT(m.mail_id) AS nbmail, m.emailadress_id_id FROM app1_mail m 
RIGHT JOIN
    (SELECT ea2.employee_id, t.mail_id_id FROM app1_to t 
    RIGHT JOIN
        (SELECT ea2.emailadress_id, emp2.employee_id FROM app1_emailadress ea2
                    INNER JOIN app1_employee emp2 ON emp2.employee_id=ea2.employee_id_id) ea2 ON ea2.emailadress_id=t.emailadress_id_id /*les adresses mails des destinataires*/
    ) t ON t.mail_id_id=m.mail_id
GROUP BY t.employee_id, m.emailadress_id_id
ORDER BY t.employee_id
) m ON ea.emailadress_id=m.emailadress_id_id
ORDER BY m.employee_id
;

