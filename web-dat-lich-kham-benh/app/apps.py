from django.apps import AppConfig
import sqlite3

# Kết nối tới cơ sở dữ liệu (nếu không có sẽ tạo mới)
conn = sqlite3.connect('my_database.db')

# Tạo đối tượng cursor để thực thi các lệnh SQL
cursor = conn.cursor()

# Ví dụ tạo bảng
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')

# Đóng kết nối
conn.commit()
conn.close()

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
