from tkinter import *
from tkinter import ttk, messagebox as mb, filedialog as fd
import json
from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language="ru")
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            return f"Широта: {lat}, Долгота {lng}"
        else:
            return "Город не найден"
    except Exception as exc:
        mb.showerror("Ошибка!", f"Произошла ошибка: {exc}!")


def show_coordinates():
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}:\n{coordinates}")


key = '6686f5227c304d129ab326a8ffd9a887'


window = Tk()
window.title("Координаты городов")
window.geometry("300x150")

entry = ttk.Entry(window)
entry.pack(pady=10)

button = ttk.Button(window, text="Поиск координат", command=show_coordinates)
button.pack(pady=(0, 10))

label = ttk.Label(text="Введите город и нажмите кнопку")
label.pack(pady=(0, 10))

window.mainloop()
