from tkinter import *
from tkinter import ttk, messagebox as mb, filedialog as fd
import json
from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        query = city
        results = geocoder.geocode(query)
        if results:
            return results[0]['geometry']['lat'], results[0]['geometry']['lng']
        else:
            return "Город не найден"
    except Exception as exc:
        mb.showerror("Ошибка!", f"Произошла ошибка: {exc}!")


key = '6686f5227c304d129ab326a8ffd9a887'
city = "Москва"
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")
