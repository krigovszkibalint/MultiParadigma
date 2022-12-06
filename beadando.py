from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import mysql.connector
import csv
import os

data = []

def update(rows):
    global data
    data = rows
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i)

        print(i)

def search():
    searchQuery = searchValue.get()
    query = "SELECT id, vezeteknev, keresztnev, eletkor, varos FROM dolgozok WHERE vezeteknev LIKE '%"+searchQuery+"%' OR keresztnev LIKE '%"+searchQuery+"%' OR varos LIKE '%"+searchQuery+"%'  OR eletkor LIKE '%"+searchQuery+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)

def clear():
    query = "SELECT * FROM dolgozok"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)

def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    tvID.set(item['values'][0])
    tvVezeteknev.set(item['values'][1])
    tvKeresztnev.set(item['values'][2])
    tvEletkor.set(item['values'][3])
    tvVaros.set(item['values'][4])
    

def update_dolgozo():
    vezeteknev = tvVezeteknev.get()
    keresztnev = tvKeresztnev.get()
    eletkor = tvEletkor.get()
    varos = tvVaros.get()
    dolgozo_id = tvID.get()

    query = "UPDATE dolgozok SET vezeteknev = %s, keresztnev = %s, eletkor = %s, varos = %s WHERE id = %s"
    cursor.execute(query, (vezeteknev, keresztnev, eletkor, varos, dolgozo_id))
    db.commit()
    clear()

def add_dolgozo():
    vezeteknev = tvVezeteknev.get()
    keresztnev = tvKeresztnev.get()
    eletkor = tvEletkor.get()
    varos = tvVaros.get()
    query = "INSERT INTO dolgozok(id, vezeteknev, keresztnev, eletkor, varos) VALUES (NULL, %s, %s, %s, %s)"
    cursor.execute(query, (vezeteknev, keresztnev, eletkor, varos))
    clear()

def delete_dolgozo():
    dolgozo_id = tvID.get()
    if messagebox.askyesno("Dolgozó törlése", "Biztos törölni szeretnéd a dolgozót?"):
        query = "DELETe FROM dolgozok WHERE id = "+dolgozo_id
        cursor.execute(query)
        db.commit()
        query = "SELECT id, vezeteknev, keresztnev, eletkor, varos FROM dolgozok"
        cursor.execute(query)
        rows = cursor.fetchall()
        update(rows)
    else:
        return True

def exportCSV():
    if len(data) < 1:
        messagebox.showerror("Nincsenek adatok","Nincsenek exportálható adatok")
        return False

    fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="CSV mentése", filetypes=(("CSV File", "*.csv"), ("All files", "*.*")))
    with open(fln, mode='w', newline='') as myfile:
        export_writer = csv.writer(myfile, delimiter=';')
        for i in data:
            export_writer.writerow(i)

    messagebox.showinfo("Adatok exportálása", "Adatok exportálva ide: "+os.path.basename(fln))

def importCSV():
    data.clear()
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="CSV megnyitása", filetypes=(("CSV File", "*.csv"), ("All files", "*.*")))
    with open(fln, mode='r+', newline='') as myfile:
        csv_reader = csv.reader(myfile, delimiter=';')
        for i in csv_reader:
            data.append(i)
    
    messagebox.showinfo("Adatok importálása", "Adatok importálva innen: "+os.path.basename(fln))

    update(data)

def saveDB():
    for i in data:
        uid = i[0]
        vnev = i[1]
        knev = i[2]
        kor = i[3]
        varos = i[4]
 
        query = "INSERT INTO dolgozok(id, vezeteknev, keresztnev, eletkor, varos) VALUES (NULL, %s, %s, %s, %s)"
        cursor.execute(query, (vnev, knev, kor, varos))

db = mysql.connector.connect(host="localhost", user="root", password="", database="multiparadigma", auth_plugin="mysql_native_password");

cursor = db.cursor()

root = Tk()

searchValue = StringVar()
tvID = StringVar()
tvVezeteknev = StringVar()
tvKeresztnev = StringVar()
tvEletkor = StringVar()
tvVaros = StringVar()

# Dolgozók listázása

style = ttk.Style(root)
style.theme_use("winnative")
style.configure("Treeview.Heading", background="#eee", foreground="black")

wrapper1 = LabelFrame(root, text="Dolgozó lista")
wrapper2 = LabelFrame(root, text="Keresés")
wrapper3 = LabelFrame(root, text="Adatok")

wrapper1.pack(fill="both", expand="no", padx=20, pady=10)
wrapper2.pack(fill="both", expand="no", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5), show="headings", height="6")
trv.pack()

trv.heading(1,text="Dolgozó ID")
trv.column(1, minwidth=0, width=100, anchor=CENTER)

trv.heading(2,text="Vezetéknév")
trv.column(2, minwidth=0, width=154, anchor=CENTER)

trv.heading(3,text="Keresztnév")
trv.column(3, minwidth=0, width=150, anchor=CENTER)

trv.heading(4,text="Életkor")
trv.column(4, minwidth=0, width=100, anchor=CENTER)

trv.heading(5,text="Város")
trv.column(5, minwidth=0, width=150, anchor=CENTER)

trv.bind('<Double 1>', getrow)

exportButton = Button(wrapper1, text="Exportálás CSV-be", command=exportCSV)
exportButton.pack(side=tk.LEFT, padx=10, pady=10)

importButton = Button(wrapper1, text="Importálás CSV-ből", command=importCSV)
importButton.pack(side=tk.LEFT, padx=10, pady=10)

saveButton = Button(wrapper1, text="Adatok mentése", command=saveDB)
saveButton.pack(side=tk.LEFT, padx=10, pady=10)

exitButton = Button(wrapper1, text="Kilépés", command=lambda: exit())
exitButton.pack(side=tk.RIGHT, padx=10, pady=10)

query = "SELECT id, vezeteknev, keresztnev, eletkor, varos FROM dolgozok"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)
print(rows)

# Keresés

entry = Entry(wrapper2, textvariable=searchValue)
entry.pack(side=tk.LEFT, padx=20, pady=10)
searchButton = Button(wrapper2, text="Keresés", command=search)
searchButton.pack(side=tk.LEFT, padx=20, pady=10)
clearButton = Button(wrapper2, text="Törlés", command=clear)
clearButton.pack(side=tk.LEFT, padx=10, pady=10)

# Dolgozó adatok

labelID = Label(wrapper3, text="Dolgozó ID")
labelID.grid(row=0, column=0, padx=5, pady=3)
entryID = Entry(wrapper3, textvariable=tvID)
entryID.grid(row=0, column=1, padx=5, pady=3)

labelVezeteknev = Label(wrapper3, text="Vezetéknév")
labelVezeteknev.grid(row=1, column=0, padx=5, pady=3)
entryVezeteknev = Entry(wrapper3, textvariable=tvVezeteknev)
entryVezeteknev.grid(row=1, column=1, padx=5, pady=3)

labelKeresztnev = Label(wrapper3, text="Keresztnév")
labelKeresztnev.grid(row=2, column=0, padx=5, pady=3)
entryKeresztnev = Entry(wrapper3, textvariable=tvKeresztnev)
entryKeresztnev.grid(row=2, column=1, padx=5, pady=3)

labelEletkor = Label(wrapper3, text="Életkor")
labelEletkor.grid(row=3, column=0, padx=5, pady=3)
entryEletkor = Entry(wrapper3, textvariable=tvEletkor)
entryEletkor.grid(row=3, column=1, padx=5, pady=3)

labelVaros = Label(wrapper3, text="Város")
labelVaros.grid(row=4, column=0, padx=5, pady=3)
entryVaros = Entry(wrapper3, textvariable=tvVaros)
entryVaros.grid(row=4, column=1, padx=5, pady=3)

updateButton = Button(wrapper3, text="Módosítás", command=update_dolgozo)
addButton = Button(wrapper3, text="Új dolgozó", command=add_dolgozo)
deleteButton =Button(wrapper3, text="Dolgozó törlése", command=delete_dolgozo)

addButton.grid(row=5, column=1, padx=5, pady=3)
updateButton.grid(row=5, column=2, padx=5, pady=3)
deleteButton.grid(row=5, column=3, padx=5, pady=3)

root.title("Beadandó - KDPEQ8")
root.geometry("700x600")
root.mainloop()