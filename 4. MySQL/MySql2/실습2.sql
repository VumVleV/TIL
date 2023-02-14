-- 문제 1
CREATE TABLE users (
	userId INT AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    birthday DATE NOT NULL,
    city VARCHAR(100) NULL,
    country VARCHAR(100) NULL,
    email VARCHAR(100) NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (userId)
)

-- 문제 2
INSERT INTO
	users (first_name, last_name, birthday, city, country, email)
VALUES 
	('Beemo', 'Jeong', '1000-01-01','','','beemo@hphk.kr'),
    ('Jieun', 'Lee', '1993-05-16', 'Seoul', 'Korea',''),
    ('Dam', 'Kim', '1995-04-09', 'Seoul', 'Korea',''),
    ('Kwangsoo', 'Lee', '1985-07-14', 'Seoul', 'Korea','');

-- 문제 3
INSERT INTO
	users (first_name, last_name, birthday, city, country, email)
VALUES 
	('A', 'B', '1000-01-01','','','beemo@hphk.kr'),
    ('B', 'C', '1993-05-16', 'Seoul', 'Korea',''),
    ('C', 'D', '1995-04-09', 'Seoul', 'Korea',''),
    ('D', 'E', '1985-07-14', 'Seoul', 'Korea',''),
    ('E', 'F', '1985-07-14', 'Seoul', 'Korea','');

-- 문제 4
UPDATE
	users
SET
	first_name = 'Sihun',
    last_name = 'Kim',
    birthday = '1999-10-14'
WHERE
	userId = 2;

-- 문제 5
UPDATE
    users
SET  
    country = 'Korea'
WHERE
    country = ''

-- 문제 6
DELETE FROM
    users
WHERE
    first_name = 'Beemo';

-- 문제 7
DELETE FROM
    users
WHERE
    first_name = 'Kwangsoo'
    AND
    last_name = 'Lee';
    
-- 문제 8
DELETE FROM
    users
ORDER BY
    created_at DESC
LIMIT
    1;