## SQL Statements 유형
|유형|역할|SQL 키워드|
|------|------|------|
|DDL(Data Definition Language)|데이터의 기본 구조 및 형식 변경|CREATE DROP ALTER|
|DQL(Data Query Language)|데이터 검색|SELECT|
|DML(Data Manipulation Language)|데이터 조작(추가, 수정, 삭제)|INSERT UPDATE DELETE|
|DCL(Data Control Language)|데이터 및 작업에 대한 사용자 권한 제어|COMMIT ROLLBACK GRANT REVOKE|

# DDL(Data Definition Language)
## CREATE TABLE Syntax
```SQL
CREATE TABLE table_name (
    column_1 data_type,
    column_2 data_type,
    ...,
    constraints
);
-- 각 필드에 적용할 데이터 타입 및 테이블과 필드에 대한 제약조건 작성
-- 제약 조건은 데이터 무결성을 지키기 위해 데이터를 입력받을 때 실행하는 검사 규칙
```

## CREATE TABLE examples 
```SQL
CREATE TABLE examples (
    examID INT AUTO_INCREMENT,
    lastname VARCHAR(50) NOT NULL,
    firstname VARCHAR(50) NOT NULL,
    PRIMARY KEY (examID)
-- PK, FK는 주로 하단에 작성
-- AUTO_INCREMENT attribute는 테이블의 기본 키에 대한 번호 자동 생성
);
```
```SQL
-- Table 구조 확인
SHOW COLUMNS FROM examples;
```
## AUTO_INCREMENT 특징
- 기본 키 필드에 사용 (고유한 숫자를 부여)
- 시작 값은 1이며, 데이터 입력 시 값을 생략하면 자동으로 1씩 증가 
- 이미 사용한 값을 재사용하지 않음
- 기본적으로 NOT NULL 제약 조건을 포함

## DROP TABLE statement
```SQL
-- 테이블 examples를 삭제
DROP TABLE examples;
```

## ALTER TABLE statement
```SQL
-- 테이블 필드 조작(생성, 수정, 삭제)
ALTER TABLE ADD             -- 필드 추가
ALTER TABLE MODIFY          -- 필드 속성 변경
ALTER TABLE CHANGE COLUMN   -- 필드 이름 변경
ALTER TABLE DROP COLUMN     -- 필드 삭제
```
## ALTER TABLE ADD Syntax
```SQL
ALTER TABLE
    table_name
ADD
    new_column_name column_definition;
-- ADD 키워드 이후 추가하고자 하는 새 필드 이름과 데이터 타입 및 제약 조건 작성
```
## ALTER TABLE ADD practice #1
- examples 테이블에 country 필드 추가
(단, country 필드는 가변길이 문자열 최대 100자이며 NULL값을 허용하지 않음)

|Field|Type|Null|Key|Default|Extra|
|---|---|---|---|---|---|
|examID|int|NO|PRI|NULL|auto_increment
|lastName|varchar(50)|NO||NULL|
|firstName|varchar(50)|NO||NULL|
|country|varchar(100)|NO||NULL|

```SQL
ALTER TABLE
    examples
ADD
    country VARCHAR(100) NOT NULL;
```

## ALTER TABLE ADD practice #2
- examples 테이블에 age와 address 필드 추가
(단, age 필드는 정수 타입이 저장되며 NULL값을 허용하지 않음
 address 필드는 가변길이 문자열 최대 100자이며 NULL값을 허용하지 않음)

|Field|Type|Null|Key|Default|Extra|
|---|---|---|---|---|---|
|examID|int|NO|PRI|NULL|auto_increment
|lastName|varchar(50)|NO||NULL|
|firstName|varchar(50)|NO||NULL|
|country|varchar(100)|NO||NULL|
|age|int|NO||NULL|
|address|varchar(100)|NO||NULL|

```SQL
ALTER TABLE
    examples
ADD
    age INT NOT NULL
    address VARCHAR(100) NOT NULL;
```
## ALTER TABLE MODIFY Syntax
```SQL
ALTER TABLE
    table_name
MODIFY
    column_name column_definition;
-- MODIFY 키워드 이후 변경하고자 하는 필드 이름 그리고 데이터 타입 및 제약 조건 작성
```
## ALTER TABLE MODIFY practice #1
- examples 테이블의 address 필드를 가변길이 문자열 최대 50자까지 그리고 NULL값을 허용하지 않도록 변경

|Field|Type|Null|Key|Default|Extra|
|---|---|---|---|---|---|
|examID|int|NO|PRI|NULL|auto_increment
|lastName|varchar(50)|NO||NULL|
|firstName|varchar(50)|NO||NULL|
|country|varchar(100)|NO||NULL|
|age|int|NO||NULL|
|address|varchar(50)|NO||NULL|

```SQL
ALTER TABLE
    examples
MODIFY
    adresss VARCHAR(50) NOT NULL;
```
## ALTER TABLE MODIFY practice #2
- examples 테이블의 lastName, firstName 필드를 가변길이 문자열 최대 10자까지 그리고 NULL값을 허용하지 않도록 변경

|Field|Type|Null|Key|Default|Extra|
|---|---|---|---|---|---|
|examID|int|NO|PRI|NULL|auto_increment
|lastName|varchar(10)|NO||NULL|
|firstName|varchar(10)|NO||NULL|
|country|varchar(100)|NO||NULL|
|age|int|NO||NULL|
|address|varchar(50)|NO||NULL|
```SQL
ALTER TABLE
    examples
MODIFY
    lastName VARCHAR(10) NOT NULL,
    firstName VARCHAR(10) NOT NULL;
```
## ALTER TABLE CHANGE COLUMN Syntax
```SQL
ALTER TABLE
    table_name
CHANGE COLUMN
    original_name new_name column_definition;
-- CHANGE COLUMN 키워드 이후 기존 필드 이름, 새 이름, 데이터 타입 및, 제약조건 작성
```
## ALTER TABLE CHANGE COLUMN practice #1
- examples 테이블의 country 필드 이름을 state로 변경 (단, 데이터 타입 및 제약 조건은 이전과 동일)

|Field|Type|Null|Key|Default|Extra|
|---|---|---|---|---|---|
|examID|int|NO|PRI|NULL|auto_increment
|lastName|varchar(10)|NO||NULL|
|firstName|varchar(10)|NO||NULL|
|state|varchar(100)|NO||NULL|
|age|int|NO||NULL|
|address|varchar(50)|NO||NULL|
```SQL
ALTER TABLE
    examples
CHANGE COLUMN
    country state VARCHAR(100) NOT NULL;
```
## ALTER TABLE DROP COLUMN syntax
```SQL
ALTER TABLE
    table_name
DROP COLUMN
    column_name;
-- DROP COLUMN 키워드 이후 삭제하고자 하는 필드 이름 작성
```
## ALTER TABLE DROP COLUMN practice #1
- examples 테이블의 address 필드 삭제

|Field|Type|Null|Key|Default|Extra|
|---|---|---|---|---|---|
|examID|int|NO|PRI|NULL|auto_increment
|lastName|varchar(10)|NO||NULL|
|firstName|varchar(10)|NO||NULL|
|state|varchar(100)|NO||NULL|
|age|int|NO||NULL|
```SQL
ALTER TABLE
    examples
DROP COLUMN
    address;
```

## ALTER TABLE DROP COLUMN practice #2
- examples 테이블의 state와 age 필드 삭제

|Field|Type|Null|Key|Default|Extra|
|---|---|---|---|---|---|
|examID|int|NO|PRI|NULL|auto_increment
|lastName|varchar(10)|NO||NULL|
|firstName|varchar(10)|NO||NULL|
```SQL
ALTER TABLE
    examples
DROP COLUMN
    state,
DROP COLUMN
    age;
```
## 반드시 NOT NULL 제약을 사용해야 할까
- "NO"
- 데이터베이스를 사용하는 프로그램에 따라 NULL을 저장할 필요가 없는 경우가 많으므로 되도록 NOT NULL로 정의
- "값이 없다."라는 표현을 테이블에 기록하는 것은 0이나 빈 문자열 등을 사용하는 것으로 대체하는 것을 권장

# DML(Data Manipulation Language)
## INSERT syntax
```SQL
INSERT INTO table_name (c1,c2, ...)
VALUES (v1, v2, ...);
```
- INSERT INTO 절 다음에 테이블 이름과 괄호 안에 필드 목록을 작성
- VALUES 키워드 다음 괄호 안에 해당 필드에 삽입할 값 목록을 작성

## 예제 테이블 생성
```SQL
CREATE TABLE articles (
    id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    content VARCHAR(200) NOT NULL,
    createdAt DATE NOT NULL,
    PRIMARY KEY (id)
);

SHOW COLUMNS FROM articles;
```
|Field|Type|Null|Key|Default|Extra|
|---|---|---|---|---|---|
|id|int|NO|PRI|NULL|auto_increment
|title|varchar(100)|NO||NULL|
|content|varchar(200)|NO||NULL|
|createdAt|date|NO||NULL|

## INSERT practice #1
- articles 테이블에 각 필드에 적합한 데이터 입력 (단, CreatedAt 필드 값은 2000년 1월 1일이며 title과 content 필드 값은 자율)

|id|title|content|createdAt
|---|---|---|---
|1|hello|world|2000-01-01
```SQL
INSERT TO articles (title, content, createdAt)
VALUES ('hello', 'world', '2000-01-01');
```
## INSERT practice #2
- articles 테이블에 각 필드에 적합한 데이터를 3개 입력(단, 모든 필드 값은 자율)

|id|title|content|createdAt
|---|---|---|---
|1|hello|world|2000-01-01
|2|title1|content1|1900-01-01
|3|title2|content2|1800-01-01
|4|title3|content3|1700-01-01
```SQL
INSERT INTO articles (title, content, createdAt)
VALUES ('title1','content1','1900-01-01'),
       ('title2','content2','1800-01-01'),
       ('title3','content3','1700-01-01');
```
## INSERT practice #3
- articles 테이블에 각 필드에 적합한 데이터 입력 (단, createdAt 필드에는 현재 작성하는 날짜가 자동으로 입력 나머지 필드 자율)
```SQL
INSERT INTO
    articles (title, content, createdAt)
VALUES
    ('mytitle', 'mycontent', CURDATE());
-- 현재 날짜를 반환, MySQL이 제공하는 Date Functions 중 하나
```
## UPDATE Syntax
```SQL
UPDATE table_name
SET column_name = expression,
[WHERE
    condition];
-- SET절 다음에 수정 할 필드와 새 값을 지정
-- WHERE 절에서 수정 할 레코드를 지정하는 조건 작성
-- WHERE 절을 작성하지 않으면 모든 레코드를 수정
```
## UPDATE practice #1
- articles 테이블 1번 레코드의 title 필드 값을 'newTitle'로 변경

|id|title|content|createdAt
|---|---|---|---
|1|newTitle|world|2000-01-01
|2|title1|content1|1900-01-01
|3|title2|content2|1800-01-01
|4|title3|content3|1700-01-01
|5|title4|mycontent|현재 날짜
```SQL
UPDATE
    articles
SET
    title = 'newTitle'
WHERE
    id = 1;
```
## UPDATE practice #2
- articles 테이블 2번 레코드의 title, content 필드 값을 자유롭개 변경

|id|title|content|createdAt
|---|---|---|---
|1|newTitle|world|2000-01-01
|2|newTitle2|newContent2|1900-01-01
|3|title2|content2|1800-01-01
|4|title3|content3|1700-01-01
|5|title4|mycontent|현재 날짜
```SQL
UPDATE
    articles
SET
    title = 'newTitle2'
    content = 'newContent2'
WHERE
    id = 2;
```
## UPDATE practice #3
- articles 테이블 모든 레코드의 content 필드 값 중 문자열 'contest'를 'TEST'로 변경

|id|title|content|createdAt
|---|---|---|---
|1|newTitle|world|2000-01-01
|2|newTitle2|newContent2|1900-01-01
|3|title2|content2|1800-01-01
|4|title3|content3|1700-01-01
|5|title4|mycontent|현재 날짜
```SQL
UPDATE
    articles
SET
    content = REPLACE(content, 'content', 'TEST');
```
## DELETE syntax
```SQL
DELETE FROM table_name
[WHERE
    condition];
-- DELETE FROM 절 다음에 테이블 이름 작성
-- WHERE 절에서 삭제할 레코드를 지정하는 조건 작성
    -- WHERE 절을 작성하지 않으면 모든 레코드를 삭제
```
## DELETE practice #1
- articles 테이블의 1번 레코드 삭제

|id|title|content|createdAt
|---|---|---|---
|2|newTitle2|newContent2|1900-01-01
|3|title2|TEST2|1800-01-01
|4|title3|TEST3|1700-01-01
|5|myTitle|myTest|현재 날짜
```SQL
DELETE FROM
    articles
WHERE
    id = 1;
```
## DELETE practice #2
- articles 테이블에서 가장 최근에 작성된 레코드 2개를 삭제

|id|title|content|createdAt
|---|---|---|---
|3|title2|TEST2|1800-01-01
|4|title3|TEST3|1700-01-01
```SQL
SELECT * FROM articles
ORDER BY createdAt DESC;

DELETE FROM
    articles
ORDER BY
    createdAt DESC
LIMIT 2;
```