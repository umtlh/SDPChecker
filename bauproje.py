import pyodbc

# Veritabanı bağlantısı oluştur
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\umtlh\Documents\BauProje\sdpbau.accdb;')

# Veritabanı bağlantısı üzerinde bir cursor oluştur
cursor = conn.cursor()

# Kullanıcıdan sdp kodunu al
sdp_kod = input("SDP Kodu: ")

# SQL sorgusu ile verileri seç
query = "SELECT Kanunlar FROM YourTableName WHERE SDP_Kod = ?"
cursor.execute(query, sdp_kod)

# Sonucu al
result = cursor.fetchone()

# Sonucu yazdır
if result:
    print("Kanunlar: ", result[0])
else:
    print("Belirtilen SDP koduna sahip bir giriş bulunamadı.")

# Bağlantıyı kapat
cursor.close()
conn.close()
