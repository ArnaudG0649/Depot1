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
