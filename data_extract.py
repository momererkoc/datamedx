import mysql.connector
import csv

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="datamedx"
)

if db_connection.is_connected():
    print("Veritabanına bağlantı başarılı!")

cursor = db_connection.cursor()

cursor.execute("SELECT all_medications FROM hasta_verileri")

rows = cursor.fetchall()

with open('medications.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)

    for row in rows:
        medications = row[0]
        texts = medications.split(",")
        first_words = [text.split()[0] for text in texts if text.strip()]

        csv_writer.writerow(first_words)

cursor.close()
db_connection.close()

print("CSV dosyası oluşturuldu: medications.csv")
