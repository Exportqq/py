import mysql.connector
import tkinter as tk
from tkinter import ttk

def get_db_connect():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='0p0p',
        database='restaurant_rent'
    )

def fetch_data():
        db_connect = get_db_connect()
        cursor = db_connect.cursor()
        cursor.execute("SELECT EstradaType, RentHours, TotalAmount FROM predsovlenie")
        return cursor.fetchall()

def create_gui():
    root = tk.Tk()
    root.title("Estrada View")

    columns = ("EstradaType", "RentHours", "TotalAmount")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    headings = ["EstradaType", "RentHours", "TotalAmount"]
    for col, heading in zip(columns, headings):
        tree.heading(col, text=heading)

    data = fetch_data()
    tree.tag_configure('even', background='#f0f0f0')
    for index, row in enumerate(data):
        tag = 'even' if index % 2 == 0 else ''
        tree.insert("", tk.END, values=row, tags=(tag,))

    tree.pack(expand=True, fill=tk.BOTH)
    root.mainloop()

if __name__ == '__main__':
    create_gui()




















CREATE OR REPLACE VIEW predsovlenie AS
SELECT 
    e.EstradaType,
    r.RentHours,
    r.TotalAmount,
    -- 1. Добавили новую колонку с расчетной суммой
    -- (Предполагаем, что в таблице Estrada есть колонка PricePerHour)
    (r.RentHours * e.PricePerHour) AS CalculatedAmount 
FROM
    Rent r
JOIN
    Estrada e ON e.EstradaID = r.EstradaID 
WHERE
    r.TotalAmount IS NULL
    -- 2. Добавили новое условие к существующему
    AND r.RentHours > 2;









