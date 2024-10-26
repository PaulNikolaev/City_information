from tkinter import *
from tkinter import ttk, messagebox as mb, filedialog as fd
import json
from opencage.geocoder import OpenCageGeocode
import webbrowser

def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language="ru")
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']
            currency = results[0]['annotations']['currency']['name']
            osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lng}"

            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return {
                    "coordinates": f"Широта: {lat}, Долгота {lng},"
                                   f"\nСтрана: {country},\nВалюта: {currency},\nРегион: {region}",
                    "map_url": osm_url
                }
            else:
                return {
                    "coordinates": f"Широта: {lat}, Долгота {lng},\nСтрана: {country},\nВалюта: {currency}",
                    "map_url": osm_url
                }
        else:
            return "Город не найден"
    except Exception as exc:
        mb.showerror("Ошибка!", f"Произошла ошибка: {exc}!")


def show_coordinates(event=None):
    global map_url
    city = entry.get()
    result = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}:\n{result["coordinates"]}")
    map_url = result["map_url"]


def show_map():
    try:
        if map_url:
            webbrowser.open(map_url)
        else:
            mb.showerror("Ошибка!", "Сначала найдите координаты города!")
    except NameError:
        mb.showerror("Ошибка!", "Сначала найдите координаты города!")


def clear():
    label.config(text="Введите город и нажмите кнопку")
    entry.delete(0, END)


key = '6686f5227c304d129ab326a8ffd9a887'

window = Tk()
window.title("Координаты городов")
window.geometry("300x250")

entry = ttk.Entry(window)
entry.pack(pady=10)
entry.bind("<Return>", show_coordinates)

button = ttk.Button(window, text="Поиск координат", command=show_coordinates)
button.pack(pady=(0, 10))

label = ttk.Label(text="Введите город и нажмите кнопку", justify="center")
label.pack(pady=(0, 10))

map_button = ttk.Button(window, text="Показать на карте", command=show_map)
map_button.pack(pady=(0, 10))

clear_button = ttk.Button(window, text="Очистить", command=clear)
clear_button.pack(pady=(0, 10))

window.mainloop()
