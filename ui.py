import tkinter as tk
from tkinter import ttk
import pypyodbc

def dosya_bilgisi_al():
    dosya_kodu = dosya_kodu_entry.get()
    try:
        conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\Program Files\JetBrains\PythonProjects\SDPChecker\yoksdp23.accdb')
        cursor = conn.cursor()
        cursor.execute("SELECT Konu_Adı, Saklama_Suresi, Saklama_Kodu, Nihai_Sonuc FROM sdp WHERE Dosya_Kodu = ?", (dosya_kodu,))
        row = cursor.fetchone()

        if row:
            konu_var.set("Konu: " + row[0])
            sure_var.set("Saklama Süresi: " + str(row[1]))
            kod_var.set("Saklama Kodu: " + row[2])
            sonuc_var.set("Nihai Sonuc: " + row[3])
        else:
            konu_var.set("")
            sure_var.set("")
            kod_var.set("")
            sonuc_var.set("Dosya kodu bulunamadı.")

    except Exception as e:
        print("Hata:", e)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

root = tk.Tk()
root.title("Dosya Bilgileri")
root.geometry("400x200")

dosya_kodu_label = ttk.Label(root, text="Dosya Kodu:")
dosya_kodu_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

dosya_kodu_entry = ttk.Entry(root)
dosya_kodu_entry.grid(row=0, column=1, padx=5, pady=5)
dosya_kodu_entry.focus()

gir_button = ttk.Button(root, text="Gir", command=dosya_bilgisi_al)
gir_button.grid(row=0, column=2, padx=5, pady=5)

konu_var = tk.StringVar()
sure_var = tk.StringVar()
kod_var = tk.StringVar()
sonuc_var = tk.StringVar()

konu_label = ttk.Label(root, textvariable=konu_var, wraplength=350)
konu_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="w")

sure_label = ttk.Label(root, textvariable=sure_var, wraplength=350)
sure_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="w")

kod_label = ttk.Label(root, textvariable=kod_var, wraplength=350)
kod_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="w")

sonuc_label = ttk.Label(root, textvariable=sonuc_var, wraplength=350)
sonuc_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky="w")

root.mainloop()
