from tkinter import *

from tkinter import ttk

from simplegist import Simplegist

GHgist = Simplegist(username='Leon-96', api_token='2feb211d0c9dfe066a25559ac746a88ab7f7ef04')

root = Tk()
root.title("EasyTextShare")
root['bg'] = "darkslategrey"
ico = PhotoImage(file="C:\\Users\\GoodBoy69\\Downloads\\files.png")
filename1 = PhotoImage(file="C:\\Users\\GoodBoy69\\Downloads\\back.gif")
background_label = Label(root, image=filename1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.iconphoto(False, ico)
root.resizable(width=False, height=False)
root.geometry("800x800")


def create_window():
    createWindow = Toplevel(root)
    createWindow.title("Create A List")
    createWindow['bg'] = 'darkslategrey'
    createWindow.geometry("800x650")

    createWindow.resizable(height=False, width=False)

    desc_entered = StringVar()
    desc_entered.set("")

    description = Label(createWindow, text="Enter the Name          : ", bg="darkslategrey", fg="white",
                        highlightcolor="khaki",
                        font=("Tahoma", 15, "bold"), justify=CENTER)
    description.place(x=0, y=52)

    description_entry = Entry(createWindow, textvariable=desc_entered, bg="white", fg="black", highlightcolor="khaki",
                              font=("Bitter", 15, "bold"), justify=LEFT, width=42)
    description_entry.place(x=233, y=53)

    contents = Label(createWindow, text="Enter the Contents     : ", bg="darkslategrey", fg="white",
                     highlightcolor="khaki",
                     font=("Tahoma", 15, "bold"), justify=CENTER)
    contents.place(x=0, y=100)

    contents_entry = Text(createWindow, height=20, width=50, bg="white", fg="black",
                          font=("cambria", 14,))
    contents_entry.place(x=233, y=100)

    label_var = StringVar()
    label_var.set("")

    label = Label(createWindow, textvariable=label_var, bg='darkslategrey', fg='white', font=("cambria", 14, 'bold'))
    label.pack_forget()

    def make():

        try:
            GHgist.create(name=description_entry.get(), public=False, content=contents_entry.get("1.0", END))

            label_var.set("Your List Has Been Made")

        except:

            label_var.set("Error : Name or Content is empty")

    make_list = Button(createWindow, text="Make List", bg="orchid", bd=8, width=20, height=1, relief=RAISED,
                       fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER,
                       command=make)
    make_list.place(x=233, y=550)
    label.place(x=230, y=620)


def view_window():
    viewWindow = Toplevel(root)
    viewWindow.title("View Lists")
    viewWindow['bg'] = 'darkslategrey'
    viewWindow.geometry("800x650")
    viewWindow.resizable(height=False, width=False)

    a = Label(viewWindow, text="Select From Your Lists : ", font=("Tahoma", 15, "bold"), justify=CENTER,
              bg="darkslategrey",
              fg="white")
    a.place(x=0, y=0)

    viewcombo = ttk.Combobox(viewWindow, width=20, font=("Helvetica", 18,))
    viewcombo.place(x=260, y=0)
    viewcombo['values'] = (GHgist.profile().listall())
    viewcombo['state'] = 'readonly'

    scrollbar = Scrollbar(viewWindow)

    view_desc = Text(viewWindow, height=20, width=65, bg="darkslategrey", fg="white",
                     font=("cambria", 14,), relief=FLAT, yscrollcommand=scrollbar.set)

    view_desc.pack_forget()

    scrollbar.config(command=view_desc.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    def get_content():

        try:
            GHgist.profile().content(name=viewcombo.get())
            view_desc.delete(1.0, "end")
            view_desc.insert(1.0, GHgist.profile().content(name=str(viewcombo.get())))
            view_desc.place(x=40, y=150)


        except:
            view_desc.insert(1.0, "Error : You Have No Lists")
            view_desc.place(x=40, y=150)

    see_list = Button(viewWindow, text="View Contents", bg="orchid", bd=8, width=20, height=1, relief=RAISED,
                      fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER, command=get_content)
    see_list.place(x=260, y=75)


def delete_window():
    deleteWindow = Toplevel(root)
    deleteWindow.title("Delete Lists")
    deleteWindow['bg'] = 'darkslategrey'
    deleteWindow.geometry("800x400")
    deleteWindow.resizable(height=False, width=False)

    label3 = Label(deleteWindow, text="Select the list to be deleted : ", bg='darkslategrey', fg='white',
                   font=("cambria", 15, 'bold'))
    label3.place(x=0, y=5)

    delcombo = ttk.Combobox(deleteWindow, width=20, font=("Helvetica", 18,))
    delcombo.place(x=260, y=0)
    delcombo['values'] = (GHgist.profile().listall())
    delcombo['state'] = 'readonly'

    delvar = StringVar()
    delvar.set("")

    label1 = Label(deleteWindow, textvariable=delvar, bg='darkslategrey', fg='white', font=("cambria", 20, 'bold'))
    label1.pack_forget()

    def delete():

        try:
            GHgist.profile().delete(name=str(delcombo.get()))
            delvar.set("Your List Has Been Deleted!")
            label1.place(x=240, y=180)

        except:
            delvar.set("Error : You Have No Lists")
            label1.place(x=240, y=180)

    delete_list = Button(deleteWindow, text="Delete list", bg="orchid", bd=8, width=20, height=1, relief=RAISED,
                         fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER,
                         command=delete)
    delete_list.place(x=266, y=60)


def edit_window():
    editWindow = Toplevel(root)
    editWindow.title("Edit Existing Lists")
    editWindow['bg'] = 'darkslategrey'
    editWindow.geometry("800x800")
    editWindow.resizable(height=False, width=False)

    label2 = Label(editWindow, text="Select the list to be edited : ", bg='darkslategrey', fg='white',
                   font=("cambria", 15, 'bold'))
    label2.place(x=0, y=10)

    editcombo = ttk.Combobox(editWindow, width=20, font=("Helvetica", 18,))
    editcombo.place(x=260, y=10)
    editcombo['values'] = (GHgist.profile().listall())
    editcombo['state'] = 'readonly'

    scrollbar = Scrollbar(editWindow)

    view_desc = Text(editWindow, height=20, width=65, bg="darkslategrey", fg="white",
                     font=("cambria", 14,), relief=FLAT, yscrollcommand=scrollbar.set)

    view_desc.pack_forget()

    scrollbar.config(command=view_desc.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    b = StringVar()
    b.set("")

    label4 = Label(editWindow, textvariable=b, bg='darkslategrey', fg='white',
                   font=("cambria", 16, 'bold'))
    label4.pack_forget()

    def get_content():

        try:

            view_desc.delete(1.0, "end")
            view_desc.insert(1.0, GHgist.profile().content(name=str(editcombo.get())))
            view_desc.place(x=40, y=150)
            b.set("Here is your List, you can now make changes to it .")
            label4.place(x=150, y=750)

        except:
            view_desc.insert(1.0, "Error : You Have No List")
            view_desc.place(x=40, y=150)

    def update_list():

        try:

            GHgist.profile().edit(name=editcombo.get(), content=view_desc.get(1.0, "end"))
            b.set("Your list has been edited and updated")
            label4.place(x=150, y=750)

        except:
            b.set("Error : You have No List")
            label4.place(x=150, y=750)

    see_list = Button(editWindow, text="View Contents", bg="orchid", bd=8, width=20, height=1, relief=RAISED,
                      fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER, command=get_content)
    see_list.place(x=75, y=75)

    change_list = Button(editWindow, text="Edit Contents", bg="orchid", bd=8, width=20, height=1, relief=RAISED,
                         fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER,
                         command=update_list)
    change_list.place(x=375, y=75)


create_list = Button(root, text="Create A New List", bg="orchid", bd=8, width=20, height=10, relief=RAISED,
                     fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER,
                     command=create_window)
create_list.place(x=80, y=50)

view_list = Button(root, text="View Your Lists", bg="orchid", bd=8, width=20, height=10, relief=RAISED,
                   fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER,
                   command=view_window)
view_list.place(x=450, y=50)

delete_list = Button(root, text="Delete Your Lists", bg="orchid", bd=8, width=20, height=10, relief=RAISED,
                     fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER,
                     command=delete_window)
delete_list.place(x=450, y=400)

edit_list = Button(root, text="Edit Existing Lists", bg="orchid", bd=8, width=20, height=10, relief=RAISED,
                   fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER,
                   command=edit_window)
edit_list.place(x=80, y=400)

# MAKE NEW FEATURE WHERE PEOPLE CAN UPLOAD & SEE THEIR SHIT

root.mainloop()
