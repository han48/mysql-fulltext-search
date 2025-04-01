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

## Create table with FULLTEXT
```sql
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    FULLTEXT(full_name)
)
```

## Alter table with FULLTEXT
```sql
ALTER TABLE users ADD FULLTEXT(full_name)
```

## Sample SQL
```sql
SELECT SQL_NO_CACHE * FROM users WHERE full_name LIKE '%Lawson%'; -- Có chứa Lawson
SELECT SQL_NO_CACHE * FROM users WHERE full_name LIKE '%Law%'; -- Có chứa Law
SELECT SQL_NO_CACHE * FROM users WHERE MATCH(full_name) AGAINST('Lawson' IN NATURAL LANGUAGE MODE); -- Có chứa từ Lawson
SELECT SQL_NO_CACHE * FROM users WHERE MATCH(full_name) AGAINST('Law' IN NATURAL LANGUAGE MODE); -- Có chứa từ Law
SELECT SQL_NO_CACHE *, MATCH(full_name) AGAINST('Lawson' IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION) AS RATE FROM users WHERE MATCH(full_name) AGAINST('Lawson' IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION); -- Có chứa từ Lawson hoặc từ tương tự
SELECT SQL_NO_CACHE *, MATCH(full_name) AGAINST('Law' IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION) AS RATE FROM users WHERE MATCH(full_name) AGAINST('Law' IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION); -- Có chứa từ Law hoặc từ tương tự
SELECT SQL_NO_CACHE * FROM users WHERE MATCH(full_name) AGAINST('Law' IN BOOLEAN MODE); -- Có chứa từ Law
SELECT SQL_NO_CACHE * FROM users WHERE MATCH(full_name) AGAINST('Lawson' IN BOOLEAN MODE); -- Có chứa từ Lawson
SELECT SQL_NO_CACHE * FROM users WHERE MATCH(full_name) AGAINST('Paul AND Lawson' IN BOOLEAN MODE); -- Có chứa từ Paul và từ Lawson
SELECT SQL_NO_CACHE * FROM users WHERE MATCH(full_name) AGAINST('Jones OR Lawson' IN BOOLEAN MODE); -- Có chứa từ Jones hoặc từ Lawson
SELECT SQL_NO_CACHE * FROM users WHERE MATCH(full_name) AGAINST('+Paul +Lawson' IN BOOLEAN MODE); -- Có chứa cả 2 từ Paul và từ Lawson
SELECT SQL_NO_CACHE * FROM users WHERE MATCH(full_name) AGAINST('-Paul +Lawson' IN BOOLEAN MODE); -- Có chứa từ Lawson và không chứa từ Paul
SELECT SQL_NO_CACHE * FROM users WHERE MATCH(full_name) AGAINST('Law*' IN BOOLEAN MODE); -- Có chứa từ bắt đầu bằng Law
```

# Fulltext

MySQL Fulltext là một loại chỉ mục đặc biệt được sử dụng để thực hiện tìm kiếm toàn văn (full-text search) trong các cột văn bản. Nó cho phép bạn tìm kiếm các từ hoặc cụm từ trong các cột văn bản một cách hiệu quả và nhanh chóng.
Một số điểm nổi bật của MySQL Fulltext:
1. **Tìm kiếm toàn văn**: Cho phép tìm kiếm các từ hoặc cụm từ trong các cột văn bản.
2. **Hiệu quả**: Tìm kiếm nhanh chóng và hiệu quả hơn so với việc sử dụng các phương pháp tìm kiếm thông thường.
3. **Hỗ trợ các loại dữ liệu**: Có thể được sử dụng với các cột có kiểu dữ liệu CHAR, VARCHAR, hoặc TEXT.
4. **Các chế độ tìm kiếm**: Hỗ trợ các chế độ tìm kiếm như boolean mode, natural language mode, và query expansion.

Mặc dù MySQL Fulltext có nhiều ưu điểm, nhưng nó cũng có một số nhược điểm cần lưu ý:

1. **Hiệu suất khi chèn dữ liệu lớn**: Việc chèn hoặc cập nhật dữ liệu lớn vào bảng có chỉ mục FULLTEXT có thể làm giảm hiệu suất. Điều này là do MySQL phải cập nhật chỉ mục mỗi khi có thay đổi dữ liệu.
2. **Hạn chế về loại bảng**: Trước đây, chỉ mục FULLTEXT chỉ hỗ trợ trên bảng MyISAM, nhưng hiện nay đã hỗ trợ trên bảng InnoDB. Tuy nhiên, vẫn có một số hạn chế về hiệu suất khi sử dụng với InnoDB.
3. **Tìm kiếm tiếng Việt có dấu và không dấu**: MySQL Fulltext gặp khó khăn trong việc tìm kiếm tiếng Việt có dấu và không dấu. Để giải quyết vấn đề này, bạn có thể cần sử dụng các công cụ tìm kiếm ngoài như Solr hoặc Sphinx.
4. **Không hỗ trợ tất cả các loại dữ liệu**: Chỉ mục FULLTEXT chỉ hỗ trợ các cột có kiểu dữ liệu CHAR, VARCHAR, hoặc TEXT. Điều này có thể hạn chế khi bạn cần tìm kiếm toàn văn trên các loại dữ liệu khác.
5. **Cấu hình phức tạp**: Việc cấu hình và tối ưu hóa chỉ mục FULLTEXT có thể phức tạp, đặc biệt khi làm việc với các bảng dữ liệu lớn và yêu cầu hiệu suất cao.

# Fulltext vs LIKE

## MySQL Fulltext
1. **Hiệu suất**: Tìm kiếm toàn văn (full-text search) nhanh hơn và hiệu quả hơn khi làm việc với các văn bản lớn.
2. **Chức năng**: Hỗ trợ tìm kiếm các từ hoặc cụm từ trong các cột văn bản, bao gồm các chế độ tìm kiếm như boolean mode và natural language mode.
3. **Chỉ mục**: Yêu cầu tạo chỉ mục FULLTEXT trên các cột cần tìm kiếm.
4. **Độ chính xác**: Cung cấp các kết quả tìm kiếm có độ chính xác cao hơn, đặc biệt khi tìm kiếm các từ khóa trong văn bản dài.

## Điều kiện `WHERE LIKE`
1. **Hiệu suất**: Tìm kiếm chậm hơn khi làm việc với các văn bản lớn, đặc biệt là khi không có chỉ mục.
2. **Chức năng**: Tìm kiếm các mẫu ký tự trong các cột văn bản, sử dụng ký tự đại diện như `%` và `_`.
3. **Chỉ mục**: Không yêu cầu chỉ mục đặc biệt, nhưng có thể sử dụng chỉ mục thông thường để cải thiện hiệu suất.
4. **Độ chính xác**: Tìm kiếm đơn giản và ít chính xác hơn, phù hợp với các truy vấn tìm kiếm mẫu ký tự ngắn.

### Khi nào nên sử dụng?
- **MySQL Fulltext**: Khi bạn cần tìm kiếm toàn văn trong các cột văn bản lớn và yêu cầu hiệu suất cao.
- **Điều kiện `WHERE LIKE`**: Khi bạn cần tìm kiếm các mẫu ký tự đơn giản hoặc khi làm việc với các văn bản ngắn.



## So sánh tốc độ thực thi
Tổng số bản ghi: 2.000.000

### Thực hiện tìm kiếm bằng SQL LIKE
```SQL
SELECT SQL_NO_CACHE COUNT(id) FROM users WHERE full_name LIKE '%Law%'; -- Có chứa Law
```
Execute time: 1.438 ~ 2.672
Result: 5956 records

### Thực hiện tìm kiếm bằng MATCH AGAINST
```SQL
SELECT SQL_NO_CACHE COUNT(id) FROM users WHERE MATCH(full_name) AGAINST('Law*' IN BOOLEAN MODE); -- Có chứa Law
```
Execute time: 0.0 ~ 0.016
Result: 5956 records

Có thể thấy, dù kết quả trả về là như nhau: đều là 5956 bản ghi, nhưng thời gian thực hiện của SQL LIKE lâu hơn gấp hơn 90 lần so với sử dụng MATCH AGAINST.
Trong trường hợp dữ liệu lớn hơn nữa, thì thời gian thực thi này càng xa hơn.

Ngoài khả năng tăng performance thì Fulltext còn hỗ trợ query expansion giúp tăng tính hiệu quả của việc tìm kiếm thay vì phải chứa các ký tự cố định.

**WITH QUERY EXPANSION** trong MySQL Fulltext là một phương pháp mở rộng tìm kiếm để cải thiện kết quả tìm kiếm khi từ khóa quá ngắn hoặc không đủ cụ thể. Đây là cách hoạt động của nó:

1. **Tìm kiếm lần đầu**: MySQL thực hiện tìm kiếm ban đầu với từ khóa bạn cung cấp.
2. **Phân tích kết quả**: MySQL phân tích các kết quả tìm kiếm ban đầu để tìm các từ khóa liên quan.
3. **Tìm kiếm lần hai**: MySQL thực hiện tìm kiếm lần hai, sử dụng từ khóa ban đầu kết hợp với các từ khóa liên quan từ kết quả tìm kiếm lần đầu.

Ví dụ, nếu bạn tìm kiếm từ "database" với `WITH QUERY EXPANSION`, MySQL sẽ tìm kiếm các tài liệu chứa từ "database" và sau đó mở rộng tìm kiếm để bao gồm các tài liệu chứa các từ liên quan như "MySQL", "Oracle", "DB2", v.v.

### Lợi ích của Query Expansion
- **Cải thiện độ chính xác**: Giúp tìm kiếm các tài liệu liên quan hơn bằng cách mở rộng từ khóa.
- **Tìm kiếm thông minh hơn**: Tìm kiếm các từ khóa liên quan mà người dùng có thể không nghĩ đến.
- **Hiệu quả hơn**: Giảm thiểu việc bỏ sót các tài liệu quan trọng chỉ vì từ khóa ban đầu quá ngắn hoặc không đủ cụ thể.

Lưu ý rằng kết quả trả về của việc mở rộng tìm kiếm đôi khi có thể không như người dùng mong đợi, nhưng cũng nên khuyến khích sử dụng bởi đó là giải pháp giúp giữ chân khách hàng.