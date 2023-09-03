import requests
import cv2, os, numpy as np
import tkinter as tk
from PIL import ImageTk, Image
from datetime import datetime
import pymongo

# Inisialisasi koneksi MongoDB
client = pymongo.MongoClient("mongodb://<username>:<password>@<host>:<port>/")
db = client["nama_database"]
collection = db["nama_koleksi"]

def send_file(chat_id, file_path):
    # Fungsi pengiriman file Telegram (sama seperti sebelumnya)
    # ...

def selesai1():
    intructions.config(text="Rekam Data Telah Selesai!")

# ... (fungsi selesai2() dan selesai3() tetap sama)

def rekamDataWajah():
    # ... (kode fungsi rekamDataWajah() tetap sama)
    selesai1()
    cam.release()
    cv2.destroyAllWindows()

def trainingWajah():
    # ... (kode fungsi trainingWajah() tetap sama)
    selesai2()

def markAttendance(name):
    # ... (kode fungsi markAttendance() tetap sama)

def absensiWajah():
    # ... (kode fungsi absensiWajah() tetap sama)
    markAttendance(id)
    selesai3()
    cam.release()
    cv2.destroyAllWindows()

def kirim_kehadiran_ke_telegram():
    # ... (kode fungsi kirim_kehadiran_ke_telegram() tetap sama)

# ... (kode GUI tetap sama)

# Fungsi untuk mengirim data ke MongoDB
def kirim_data_ke_mongodb(nama, nis, kelas, waktu):
    data_to_insert = {
        "nama": nama,
        "nis": nis,
        "kelas": kelas,
        "waktu": waktu
    }
    collection.insert_one(data_to_insert)

# Fungsi saat GUI ditutup
def on_closing():
    # Panggil fungsi untuk mengirim data kehadiran ke MongoDB
    for data in attendance_data:
        kirim_data_ke_mongodb(data["nama"], data["nis"], data["kelas"], data["waktu"])
    
    # Panggil fungsi untuk mengirim kehadiran ke Telegram
    kirim_kehadiran_ke_telegram()
    
    # Tutup koneksi MongoDB
    client.close()
    
    # Tutup GUI
    root.destroy()

# ... (kode GUI tetap sama)

attendance_data = []  # List untuk menyimpan data kehadiran

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
