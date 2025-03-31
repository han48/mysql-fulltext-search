import mysql.connector
from faker import Faker
from tqdm import tqdm

fake = Faker()

db = mysql.connector.connect(
    host="127.0.0.1",
    user="sabitech",
    password="Sbt12345",
    database="sample_1m_record"
)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    FULLTEXT(full_name)
)
""")

insert_query = "INSERT INTO users (full_name, address) VALUES (%s, %s)"
for _ in tqdm(range(10000000), desc="Generating fake data"):
    cursor.execute(insert_query, (fake.name(), fake.address()))
    db.commit()

cursor.close()
db.close()

print("1 triệu tên đầy đủ và địa chỉ ngẫu nhiên đã được insert vào database.")