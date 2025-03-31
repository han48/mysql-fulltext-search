# SETUP
```shell
python -m venv env

# Windows
.\env\Scripts\Activate.ps1 

# Linux
source env/bin/active

pip install -r requirements.txt
```

# INSERT 100M RECORD
```shell
python create_database.py
```

# SQL
```sqlsql
SELECT * FROM users WHERE full_name LIKE '%Lawson%'; -- Có chứa Lawson
SELECT * FROM users WHERE full_name LIKE '%Law%'; -- Có chứa Law
SELECT * FROM users WHERE MATCH(full_name) AGAINST('Lawson' IN NATURAL LANGUAGE MODE); -- Có chứa từ Lawson
SELECT * FROM users WHERE MATCH(full_name) AGAINST('Law' IN NATURAL LANGUAGE MODE); -- Có chứa từ Law
SELECT *, MATCH(full_name) AGAINST('Lawson' IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION) AS RATE FROM users WHERE MATCH(full_name) AGAINST('Lawson' IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION); -- Có chứa từ Lawson hoặc từ tương tự
SELECT *, MATCH(full_name) AGAINST('Law' IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION) AS RATE FROM users WHERE MATCH(full_name) AGAINST('Law' IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION); -- Có chứa từ Law hoặc từ tương tự
SELECT * FROM users WHERE MATCH(full_name) AGAINST('Law' IN BOOLEAN MODE); -- Có chứa từ Law
SELECT * FROM users WHERE MATCH(full_name) AGAINST('Lawson' IN BOOLEAN MODE); -- Có chứa từ Lawson
SELECT * FROM users WHERE MATCH(full_name) AGAINST('Paul AND Lawson' IN BOOLEAN MODE); -- Có chứa từ Paul và từ Lawson
SELECT * FROM users WHERE MATCH(full_name) AGAINST('Jones OR Lawson' IN BOOLEAN MODE); -- Có chứa từ Jones hoặc từ Lawson
SELECT * FROM users WHERE MATCH(full_name) AGAINST('+Paul +Lawson' IN BOOLEAN MODE); -- Có chứa cả 2 từ Paul và từ Lawson
SELECT * FROM users WHERE MATCH(full_name) AGAINST('-Paul +Lawson' IN BOOLEAN MODE); -- Có chứa từ Lawson và không chứa từ Paul
SELECT * FROM users WHERE MATCH(full_name) AGAINST('Law*' IN BOOLEAN MODE); -- Có chứa từ bắt đầu bằng Law
```