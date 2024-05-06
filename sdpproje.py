import pypyodbc

def dosya_bilgisi_al(dosya_kodu):
    try:
        # Veritabanına bağlanma
        conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\umtlh\Belgeler\SDPChecker\sdpbau.accdb;')
        cursor = conn.cursor()

        # SQL sorgusu ile dosya bilgisini al
        cursor.execute("SELECT Konu_Adı, Saklama_Suresi, Saklama_Kodu, Nihai_Sonuc FROM sdp WHERE Dosya_Kodu = ?", (dosya_kodu,))
        row = cursor.fetchone()

        if row:
            # Bilgileri ekrana yazdır
            print("Konu:", row[0])
            print("Saklama Süresi:", row[1])
            print("Saklama Kodu:", row[2])
            print("Nihai Sonuc:", row[3])
        else:
            print("Dosya kodu bulunamadı.")

    except Exception as e:
        print("Hata:", e)

    finally:
        # Bağlantıyı ve imleci kapat
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

# Kullanıcıdan dosya kodunu al
dosya_kodu = input("Dosya Kodu: ")

# Dosya bilgisini al ve yazdır
dosya_bilgisi_al(dosya_kodu)
