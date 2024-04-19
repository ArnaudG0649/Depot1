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


(SELECT m.employee_id as id_destinataire, SUM(m.nbmail) as nbmail, ea.employee_id as id_expediteur FROM 
(SELECT ea.emailadress_id, emp.employee_id FROM app1_emailadress ea
    INNER JOIN app1_employee emp ON emp.employee_id=ea.employee_id_id
) ea
INNER JOIN
(SELECT t.employee_id, COUNT(m.mail_id) AS nbmail, m.emailadress_id_id FROM app1_mail m 
RIGHT JOIN
    (SELECT ea2.employee_id, t.mail_id_id FROM app1_to t 
    RIGHT JOIN
        (SELECT ea2.emailadress_id, emp2.employee_id FROM app1_emailadress ea2
            INNER JOIN app1_employee emp2 ON emp2.employee_id=ea2.employee_id_id) ea2 
            ON ea2.emailadress_id=t.emailadress_id_id /*les adresses mails des destinataires*/
    ) t ON t.mail_id_id=m.mail_id
GROUP BY t.employee_id, m.emailadress_id_id
) m ON ea.emailadress_id=m.emailadress_id_id
GROUP BY m.employee_id,ea.employee_id
UNION
SELECT c.aid, c.aid*0, c.bid FROM 
    (SELECT a.employee_id as aid, b.employee_id as bid
    FROM app1_employee a CROSS JOIN app1_employee b
    EXCEPT (SELECT mid, eid FROM
        (SELECT m.employee_id as mid, SUM(m.nbmail), ea.employee_id as eid FROM 
        (SELECT ea.emailadress_id, emp.employee_id FROM app1_emailadress ea
            INNER JOIN app1_employee emp ON emp.employee_id=ea.employee_id_id
        ) ea
        INNER JOIN
        (SELECT t.employee_id, COUNT(m.mail_id) AS nbmail, m.emailadress_id_id FROM app1_mail m 
        RIGHT JOIN
            (SELECT ea2.employee_id, t.mail_id_id FROM app1_to t 
            RIGHT JOIN
                (SELECT ea2.emailadress_id, emp2.employee_id FROM app1_emailadress ea2
                    INNER JOIN app1_employee emp2 ON emp2.employee_id=ea2.employee_id_id) ea2 
                    ON ea2.emailadress_id=t.emailadress_id_id /*les adresses mails des destinataires*/
            ) t ON t.mail_id_id=m.mail_id
        GROUP BY t.employee_id, m.emailadress_id_id
        ) m ON ea.emailadress_id=m.emailadress_id_id
        GROUP BY m.employee_id, ea.employee_id ) ea
    ) ) c )Tdp
;




SELECT t.employee_id as id_expediteur, SUM(t.nbmail) as nbmail, ea.employee_id as id_destinataire FROM 
(SELECT ea.emailadress_id, emp.employee_id FROM app1_emailadress ea
    INNER JOIN app1_employee emp ON emp.employee_id=ea.employee_id_id
) ea
INNER JOIN
(SELECT m.employee_id, COUNT(m.mail_id) AS nbmail, t.emailadress_id_id FROM app1_to t 
RIGHT JOIN
    (SELECT ea2.employee_id, m.mail_id FROM app1_mail m 
    RIGHT JOIN
        (SELECT ea2.emailadress_id, emp2.employee_id FROM app1_emailadress ea2
            INNER JOIN app1_employee emp2 ON emp2.employee_id=ea2.employee_id_id) ea2 
            ON ea2.emailadress_id=m.emailadress_id_id /*les adresses mails des expediteurs*/
    ) m ON t.mail_id_id=m.mail_id
GROUP BY m.employee_id, t.emailadress_id_id
) t ON ea.emailadress_id=t.emailadress_id_id
GROUP BY t.employee_id,ea.employee_id
ORDER BY nbmail DESC



SELECT ea2.employee_id FROM app1_mail m 
    RIGHT JOIN
        (SELECT ea2.emailadress_id, emp2.employee_id FROM app1_emailadress ea2
            INNER JOIN app1_employee emp2 ON emp2.employee_id=ea2.employee_id_id) ea2 
            ON ea2.emailadress_id=m.emailadress_id_id 
GROUP BY ea2.employee_id


----Requête n°5----

SELECT m.path, m.timedate, m.mail_id, m.subject, m.emailadress_id_id, t.dest_interne, aut.interne as exp_interne FROM app1_mail m 
    INNER JOIN 
    (SELECT t.mail_id_id, bool_and(ea.interne) as dest_interne FROM app1_to t
    INNER JOIN app1_emailadress ea ON ea.emailadress_id=t.emailadress_id_id 
    GROUP BY t.mail_id_id
    ) t ON t.mail_id_id=m.mail_id
    INNER JOIN app1_emailadress aut ON aut.emailadress_id=m.emailadress_id_id
    WHERE (m.Timedate BETWEEN '2001-10-01 00:00:00' AND '2001-11-02 00:00:00') 
;


SELECT path, timedate, mail_id, subject, emailadress_id_id FROM app1_mail 
    WHERE mail_id='10923348.1075862085338.JavaMail.evans@thyme' AND timedate - interval '9 hours' BETWEEN '2001-10-23' AND '2001-10-24'
;