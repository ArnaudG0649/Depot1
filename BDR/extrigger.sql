CREATE TABLE employee (
    emp_id serial primary key,
    name varchar(30),
    email varchar(50));

INSERT INTO employee(name,email) VALUES('John Doe','jdoe@wanadoo.fr'),('Jane Doe','janedoe@gmail.com');


CREATE FUNCTION check_repeated_email()
    RETURNS TRIGGER
    LANGUAGE PLPGSQL AS
$$
BEGIN
    -- mon code pl/pgSQL
    IF EXISTS (SELECT * FROM employee WHERE email LIKE NEW.email)
    THEN 
        RETURN null;
    END IF;
    RETURN NEW;
END
$$;

CREATE TRIGGER check_email_insert
    BEFORE INSERT ON employee
    FOR EACH ROW
    EXECUTE FUNCTION check_repeated_email();

ALTER TABLE employee ADD COLUMN age int;

UPDATE employee SET age=1;

ALTER TABLE employee
ALTER COLUMN age SET NOT NULL;
