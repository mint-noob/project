import tkinter as tk
from tkinter import messagebox,ttk
import pickle as pk
import csv
# Code for Homescreen
EntryWindow = tk.Tk()




found_forcreate = False
found_forload = False

def info():
    messagebox.showinfo("Info","Made By Ojas Class 12th")

def add_placeholder(entry, text):

        
        entry.insert(0, f"{text}")
    
        def select(event):
            if entry.get() == f"{text}":
                entry.delete(0, tk.END)
                entry.config(fg="Black")
    
        def deselect(event):
            if entry.get().strip()=="":
                entry.insert(0, f"{text}")
                entry.config(fg="gray")
            elif entry.get() == f"{text}":
                entry.insert(0, f"{text}")
                entry.config(fg="gray")

            else:
                None

        entry.bind("<FocusIn>", select)
        entry.bind("<FocusOut>", deselect)
        entry.pack(pady=10)

def main():
    global EntryWindow
    
    EntryWindow.title("Home Screen")
    # EntryWindow.geometry("500x400")

  
    welcome = tk.Label(EntryWindow, text="Welcome To Database", font=("Times New Roman",24, "bold"), fg="red")
    welcome.pack(pady=10, padx=10)

    #Enter Password Prompt
    DataBasePassword = tk.Entry(EntryWindow, fg="Gray")
    add_placeholder(DataBasePassword, "Enter Password")

    #Login Button
    login_button = tk.Button(EntryWindow, text="Log In", command=lambda:login(DataBasePassword.get()))
    login_button.pack(pady=10)
    # def show_xy(event):
    #     print(f"Cursor: x={event.x}, y={event.y}")

    # EntryWindow.bind("<Motion>", show_xy)
    start_text = tk.Label(EntryWindow, text="Press The Button To Log In", font=("Times New Roman",15))
    start_text.pack(pady=10)

    #Implementation Of Menu

    main_menu = tk.Menu(EntryWindow)
    EntryWindow.config(menu=main_menu)
    
    help_menu = tk.Menu(main_menu,tearoff=0)
    main_menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="Exit", command=EntryWindow.quit)
    help_menu.add_command(label="Info", command=info)#Add your name and class


    
    EntryWindow.mainloop()

def login(Password):
    
    flag = False
    with open("school-project-main/password.dat","rb") as f:
        
        if Password==list(pk.load(f))[0]:
            flag = True
        else:
            flag = False

    if flag:
        global EntryWindow
        Data_Management_Window = tk.Tk()
        EntryWindow.destroy()
        Data_Management_Window.title("Database")
        Data_Management_Window.geometry("450x400")

        #Menu Config
        main_menu = tk.Menu(Data_Management_Window)
        Data_Management_Window.config(menu=main_menu)

        def refresh_table():
            table.delete(*table.get_children())
            with open(f"school-project-main/data.csv", "r") as file:
                reader = csv.reader(file)
                rows = list(reader)
                for row in rows[1:]:
                    table.insert("", "end", values=row)

        help_menu = tk.Menu(main_menu,tearoff=0)
        main_menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Exit", command=Data_Management_Window.quit)
        help_menu.add_command(label="Refresh Table", command=refresh_table)
        help_menu.add_command(label="Info", command=info)#Add your name and class
        # more_menu.add_command(label="Delete Databases", command=messagebox.showerror("Sorry", "Feature Not Available"))
        
        with open(f"school-project-main/data.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
    
        
        
        
        
        #Treeview widget (table)
        table = ttk.Treeview(Data_Management_Window)
        table.pack(fill="both", expand=True)

        table["columns"] = rows[0]
        table["show"] = "headings"

        for header in rows[0]:
            table.heading(header, text=header)
            table.column(header, width=100, anchor="center")
        
        for row in rows[1:]:
            table.insert("", "end", values=row)
        #scrollbar
        scrollbar = ttk.Scrollbar(Data_Management_Window, orient="vertical", command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        

        button_close = tk.Button(Data_Management_Window, text="Add", command=add_csv)
        button_close.pack(pady=5)

        button_close = tk.Button(Data_Management_Window, text="Delete", command=delete_csv)
        button_close.pack()

        button_edit_data_table = tk.Button(Data_Management_Window, text="Edit", command=edit_csv)
        button_edit_data_table.pack(pady=5)


        Data_Management_Window.mainloop()
        
    
    else:
        messagebox.showwarning("Invalid Password","The password entered is Invalid")

def add_csv():
    
    add_window = tk.Tk()
    add_window.title("Add New Items")
    
    
    # Item ID Entry
    Item_id = tk.Entry(add_window, fg="Gray")
    add_placeholder(Item_id, "Enter Item ID")
    
    
    #Item Name Entry
    Item_name = tk.Entry(add_window, fg="Gray")
    add_placeholder(Item_name, "Enter Item Name")

    #Item Price Entry
    Item_Price = tk.Entry(add_window, fg="Gray")
    add_placeholder(Item_Price, "Enter Item Price")
    

    #Item Quantity Entry
    Item_Quantity = tk.Entry(add_window, fg="Gray")
    add_placeholder(Item_Quantity, "Enter Item Quantity")

    def add_item_to_csv():
        
        
        with open(f"school-project-main/data.csv", "a") as file:
            if Item_id.get() in ["", "Enter Item ID"] or Item_name.get() in ["", "Enter Item Name"] or Item_Price.get() in ["", "Enter Item Price"] or Item_Quantity.get() in ["", "Enter Item Quantity"]:
                messagebox.showerror("Error", "Please fill all fields correctly.")
                return
            
            elif not Item_Price.get().isdigit() or not Item_Quantity.get().isdigit():
                messagebox.showerror("Error", "Price and Quantity must be numeric.")
                return
            
            elif float(Item_Price.get()) < 0 or int(Item_Quantity.get()) < 0:
                messagebox.showerror("Error", "Price and Quantity must be non-negative.")
                return
            
            

            else:           
                with open(f"school-project-main/data.csv", "r") as file1:
                    reader = csv.reader(file1)
                    for row in reader:
                        if row and row[0] == Item_id.get():
                            messagebox.showerror("Error", "Item ID already exists.")
                            return
                
                writer = csv.writer(file)
                writer.writerow((Item_id.get(), Item_name.get(), Item_Price.get(), Item_Quantity.get()))
                messagebox.showinfo("Success", "Item Added Successfully!") 
                add_window.destroy()
    
    
    add_button = tk.Button(add_window, text="Add Item", command=add_item_to_csv)#Fill Command
    add_button.pack(pady=10)

    

    add_window.mainloop()

def delete_csv():
   
    
    delete_window = tk.Tk()
    delete_window.title("Delete Item")
    
    def delete_item_csv_function(database, item_to_edit):
        delete_window.destroy()
        temp_reader = []
        with open(f"school-project-main/data.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        for row in rows:
            if row[0] == item_to_edit:
                pass
            else:
                temp_reader.append(row)
        
        with open(f"school-project-main/data.csv", "w") as updated:
            writer = csv.writer(updated)
            for rows in temp_reader:
                writer.writerow(rows)
        messagebox.showinfo("Success", f"Item '{item_to_edit}' Deleted Successfully")
        delete_window.mainloop()


    to_delete_entry = tk.Entry(delete_window, fg="Gray")
    to_delete_entry.insert(0, "Enter Item ID To Delete")
    #For Placeholder
    def select(event):
        if to_delete_entry.get() == "Enter Item ID To Delete":
            to_delete_entry.delete(0, tk.END)
            to_delete_entry.config(fg="Black")
    
    def deselect(event):
        if to_delete_entry.get().strip()=="":
            to_delete_entry.insert(0, "Enter Item ID To Delete")
            to_delete_entry.config(fg="gray")
        else:
            None
    
    to_delete_entry.bind("<FocusIn>", select)
    to_delete_entry.bind("<FocusOut>", deselect)
    
    def delete_item_csv():
        delete_item_csv_function(f"school-project-main/data.csv", to_delete_entry.get())

    
    to_delete_entry.pack(pady=5)
    delete_item_button = tk.Button(delete_window, text="Delete Item", command=delete_item_csv)
    delete_item_button.pack(pady=5)

    
    

    delete_window.mainloop()

def edit_csv():

    edit_window = tk.Tk()
    edit_window.title("Edit Item")


    # ---------- Item ID ----------
    Item_id = tk.Entry(edit_window)
    add_placeholder(Item_id, "Enter Item ID")

    # ---------- Checkboxes ----------
    name_var = tk.IntVar()
    price_var = tk.IntVar()
    qty_var = tk.IntVar()

    # ---------- Entry Fields ----------
    Item_name = tk.Entry(edit_window, state="disabled")
    add_placeholder(Item_name, "New Item Name")

    Item_price = tk.Entry(edit_window, state="disabled")
    add_placeholder(Item_price, "New Item Price")

    Item_qty = tk.Entry(edit_window, state="disabled")
    add_placeholder(Item_qty, "New Item Quantity")

    # ---------- Toggle Functions ----------
    def toggle(entry, var):
        entry.config(state="normal" if var.get() else "disabled")

    tk.Checkbutton(edit_window, text="Edit Name",
                   variable=name_var,
                   command=lambda: toggle(Item_name, name_var)).pack(anchor="w")

    Item_name.pack(pady=5)

    tk.Checkbutton(edit_window, text="Edit Price",
                   variable=price_var,
                   command=lambda: toggle(Item_price, price_var)).pack(anchor="w")

    Item_price.pack(pady=5)

    tk.Checkbutton(edit_window, text="Edit Quantity",
                   variable=qty_var,
                   command=lambda: toggle(Item_qty, qty_var)).pack(anchor="w")

    Item_qty.pack(pady=5)

    # ---------- Edit Logic ----------
    def edit_item():

        item_id = Item_id.get().strip()

        if item_id == "" or "Enter" in item_id:
            messagebox.showerror("Error", "Please enter a valid Item ID")
            return

        if not (name_var.get() or price_var.get() or qty_var.get()):
            messagebox.showerror("Error", "Select at least one field to edit")
            return

        updated_rows = []
        found = False

        with open("school-project-main/data.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        for row in rows:
            if row[0] == item_id:
                found = True

                if name_var.get():
                    row[1] = Item_name.get()

                if price_var.get():
                    row[2] = Item_price.get()

                if qty_var.get():
                    row[3] = Item_qty.get()

            updated_rows.append(row)

        if not found:
            messagebox.showerror("Error", "Item ID not found")
            return

        with open("school-project-main/data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)

        messagebox.showinfo("Success", "Item updated successfully")
        edit_window.destroy()

    tk.Button(edit_window, text="Edit Item", command=edit_item).pack(pady=15)
    
main()
