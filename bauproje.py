import pyodbc

# Veritabanı bağlantısı oluştur
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\umtlh\Documents\BauProje\sdpbau.accdb;')

# Veritabanı bağlantısı üzerinde bir cursor oluştur
cursor = conn.cursor()

# Kullanıcıdan dosya kodunu al
dosya_kodu = input("Dosya Kodu: ")

# SQL sorgusu ile verileri seç
query = "SELECT [Konu Adı] FROM sdp WHERE [Dosya Kodu] = ?"
cursor.execute(query, dosya_kodu)

# Sonucu al
result = cursor.fetchone()

# Sonucu yazdır
if result:
    print("Konu Adı: ", result[0])
else:
    print("Belirtilen dosya koduna sahip bir giriş bulunamadı.")

# Bağlantıyı kapat
cursor.close()
conn.close()
