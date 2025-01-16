import tkinter as tk
from tkinter import messagebox
import subprocess
import os
def run_spider(spider_name, output_file):
    try:
        scrapy_project_path = "C:/Users/Axel/Desktop/ScraperPrueba/scrapers"
        output_path = f"C:/Users/Axel/Desktop/ScraperPrueba/output/{spider_name}.csv"
        os.chdir(scrapy_project_path)
        command = ['py', '-m', 'scrapy', 'crawl', spider_name, '-o', output_path]
        try:
            subprocess.run(command, check=True)
            print(f"Spider {spider_name} ejecutado correctamente y guardado en {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el spider: {e}")
        os.chdir('..')

    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el spider: {e}")

def create_app():
    root = tk.Tk()
    root.title("Interfaz de Scrapers")
    root.geometry("400x300")

    label = tk.Label(root, text="Selecciona un scraper para ejecutar:", font=("Arial", 14))
    label.pack(pady=20)

    button1 = tk.Button(root, text="Ejecutar Prueba 1 (Libros)", width=30, command=lambda: run_spider('books', 'output/books.csv'))
    button1.pack(pady=5)

    button2 = tk.Button(root, text="Ejecutar Prueba 2 (Clima)", width=30, command=lambda: run_spider('weather', 'output/weather.csv'))
    button2.pack(pady=5)

    button3 = tk.Button(root, text="Ejecutar Prueba 3 (Tags)", width=30, command=lambda: run_spider('quotes_by_tag', 'output/quotes_by_tag.csv'))
    button3.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_app()
