import tkinter as tk
from tkinter import messagebox
from not_sistemi import NotSistemi

sistem = NotSistemi()

window = tk.Tk()
window.title("Öğrenci Not Takip Sistemi")
window.geometry("500x500")
window.resizable(False, False)


def ogrenci_ekle():
    ad = entry_ad.get()
    soyad = entry_soyad.get()
    numara = entry_numara.get()

    if ad == "" or soyad == "" or numara == "":
        messagebox.showerror("Hata", "Tüm alanları doldurunuz.")
        return

    sistem.ogrenci_ekle(ad, soyad, numara)
    messagebox.showinfo("Başarılı", "Öğrenci eklendi.")

    entry_ad.delete(0, tk.END)
    entry_soyad.delete(0, tk.END)
    entry_numara.delete(0, tk.END)


def not_gir():
    numara = entry_not_numara.get()

    try:
        vize = float(entry_vize.get())
        final = float(entry_final.get())

        if vize < 0 or vize > 100 or final < 0 or final > 100:
            messagebox.showerror("Hata", "Notlar 0-100 arasında olmalıdır.")
            return

        sonuc = sistem.not_gir(numara, vize, final)

        if sonuc:
            messagebox.showinfo("Başarılı", "Notlar kaydedildi.")
        else:
            messagebox.showerror("Hata", "Öğrenci bulunamadı.")

        entry_not_numara.delete(0, tk.END)
        entry_vize.delete(0, tk.END)
        entry_final.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Hata", "Sayısal değer giriniz.")


def listele():
    text_alani.delete(1.0, tk.END)

    ogrenciler = sistem.ogrencileri_getir()

    if len(ogrenciler) == 0:
        text_alani.insert(tk.END, "Kayıtlı öğrenci bulunmuyor.\n")
        return

    for ogrenci in ogrenciler:
        text_alani.insert(tk.END, f"Ad Soyad: {ogrenci.ad} {ogrenci.soyad}\n")
        text_alani.insert(tk.END, f"Numara: {ogrenci.numara}\n")

        if ogrenci.vize is not None:
            text_alani.insert(tk.END, f"Vize: {ogrenci.vize}\n")
            text_alani.insert(tk.END, f"Final: {ogrenci.final}\n")
            text_alani.insert(tk.END, f"Ortalama: {ogrenci.ortalama_hesapla()}\n")
            text_alani.insert(tk.END, f"Durum: {ogrenci.durum_hesapla()}\n")
        else:
            text_alani.insert(tk.END, "Not girilmedi.\n")

        text_alani.insert(tk.END, "-----------------------------\n")


baslik = tk.Label(
    window,
    text="ÖĞRENCİ NOT TAKİP SİSTEMİ",
    font=("Arial", 16, "bold")
)
baslik.pack(pady=10)

frame1 = tk.Frame(window)
frame1.pack(pady=10)

tk.Label(frame1, text="Ad:").grid(row=0, column=0)
entry_ad = tk.Entry(frame1)
entry_ad.grid(row=0, column=1)

tk.Label(frame1, text="Soyad:").grid(row=1, column=0)
entry_soyad = tk.Entry(frame1)
entry_soyad.grid(row=1, column=1)

tk.Label(frame1, text="Numara:").grid(row=2, column=0)
entry_numara = tk.Entry(frame1)
entry_numara.grid(row=2, column=1)

tk.Button(frame1, text="Öğrenci Ekle", command=ogrenci_ekle).grid(
    row=3,
    column=0,
    columnspan=2,
    pady=5
)

frame2 = tk.Frame(window)
frame2.pack(pady=10)

tk.Label(frame2, text="Numara:").grid(row=0, column=0)
entry_not_numara = tk.Entry(frame2)
entry_not_numara.grid(row=0, column=1)

tk.Label(frame2, text="Vize:").grid(row=1, column=0)
entry_vize = tk.Entry(frame2)
entry_vize.grid(row=1, column=1)

tk.Label(frame2, text="Final:").grid(row=2, column=0)
entry_final = tk.Entry(frame2)
entry_final.grid(row=2, column=1)

tk.Button(frame2, text="Not Gir", command=not_gir).grid(
    row=3,
    column=0,
    columnspan=2,
    pady=5
)

tk.Button(window, text="Öğrencileri Listele", command=listele).pack(pady=10)

text_alani = tk.Text(window, width=55, height=12)
text_alani.pack(pady=10)

window.mainloop()
