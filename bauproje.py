import pyodbc

# Veritabanı bağlantısı oluştur
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\umtlh\Documents\BauProje\sdpbau.accdb;')

# Veritabanı bağlantısı üzerinde bir cursor oluştur
cursor = conn.cursor()

# Kullanıcıdan dosya kodunu al
dosya_kodu = input("Dosya Kodu: ")

# SQL sorgusu ile verileri seç
query = "SELECT [Konu Adı], [Saklama Suresi], [Saklama Kodu], [Saklama Kodu] FROM sdp WHERE [Dosya Kodu] = ?"
cursor.execute(query, dosya_kodu)

# Sonuçları al
results = cursor.fetchall()

# Sonuçları yazdır
if results:
    for row in results:
        print("Konu Adı:", row[0])
        print("Saklama Suresi:", row[1])
        print("Saklama Kodu :", row[2])
        print("Nihai Sonuc:", row[3])
else:
    print("Belirtilen dosya koduna sahip bir giriş bulunamadı.")

# Bağlantıyı kapat
cursor.close()
conn.close()