# Imported Libraries

from tkinter import *

from tkinter import ttk

from PIL import ImageTk, Image

from simplegist import Simplegist

import os

from tkinter.filedialog import askopenfilename

import webbrowser

import pyperclip

GHgist = Simplegist(username='Leon-96', api_token='ddca1e9a1e2e7cd38ec5823061aaf587d05a4cd1')

# root basic stuff

root = Tk()
root.title("GistMaker")
root['bg'] = "darkslategrey"
ico = PhotoImage(file="C:\\Users\\GoodBoy69\\Downloads\\files.png")
filename1 = PhotoImage(file="C:\\Users\\GoodBoy69\\Downloads\\back.gif")
background_label = Label(root, image=filename1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.iconphoto(False, ico)
root.resizable(width=False, height=False)
root.geometry("800x800")


# Widgets

def create_window():
    global background_image

    createWindow = Toplevel(root)
    createWindow.title("Create A Gist")
    createWindow['bg'] = 'darkslategrey'
    createWindow.geometry("800x650")

    image2 = Image.open('C:\\Users\\GoodBoy69\\Downloads\\back-1.gif')
    background_image = ImageTk.PhotoImage(image2)
    background_label1 = Label(createWindow, image=background_image)
    background_label1.place(x=0, y=0, relwidth=1, relheight=1)

    createWindow.resizable(height=False, width=False)

    desc_entered = StringVar()
    desc_entered.set("")

    description = Label(createWindow, text="Enter the Name          : ", bg="darkslategrey", fg="white",
                        highlightcolor="khaki",
                        font=("Tahoma", 15, "bold"), justify=CENTER)
    description.place(x=0, y=52)

    description_entry = Entry(createWindow, textvariable=desc_entered, bg="white", fg="black",
                              highlightcolor="khaki",
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

            label_var.set("Your Gist Has Been Made")

        except:

            label_var.set("Error : Name or Content is empty")

    make_Gist = Button(createWindow, text="Make Gist", bg="orchid", bd=8, width=20, height=1, relief=RAISED,
                       fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER,
                       command=make)
    make_Gist.place(x=233, y=550)
    label.place(x=230, y=620)


def view_window():
    global background_image1

    viewWindow = Toplevel(root)
    viewWindow.title("View Gists")
    viewWindow['bg'] = 'darkslategrey'
    viewWindow.geometry("800x650")
    viewWindow.resizable(height=False, width=False)

    image2 = Image.open('C:\\Users\\GoodBoy69\\Downloads\\back-1.gif')
    background_image1 = ImageTk.PhotoImage(image2)
    background_label2 = Label(viewWindow, image=background_image1)
    background_label2.place(x=0, y=0, relwidth=1, relheight=1)

    a = Label(viewWindow, text="Select From Your Gists : ", font=("Tahoma", 15, "bold"), justify=CENTER,
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
            view_desc.insert(1.0, "Error : You Have No Gists")
            view_desc.place(x=40, y=150)

    see_Gist = Button(viewWindow, text="View Contents", bg="orchid", bd=8, width=20, height=1, relief=RAISED,
                      fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER, command=get_content)
    see_Gist.place(x=260, y=75)

    def beautifycode():

        pyperclip.copy(str(view_desc.get(1.0, "end")))
        pyperclip.paste()

        new = 1
        url = "https://codebeautify.org"
        webbrowser.open(url, new=new)

    beautify = Button(viewWindow, text="Beautify Code", bg="orchid", bd=8, width=15, height=1,
                      relief=RAISED,
                      fg="Black", font=("Unispace", 13, "bold"), anchor="center", justify=CENTER, command=beautifycode)
    beautify.place(x=40, y=600)


def delete_window():
    deleteWindow = Toplevel(root)
    deleteWindow.title("Delete Gists")
    deleteWindow['bg'] = 'darkslategrey'
    deleteWindow.geometry("800x400")
    deleteWindow.resizable(height=False, width=False)

    global background_image2

    image2 = Image.open('C:\\Users\\GoodBoy69\\Downloads\\back-1.gif')
    background_image2 = ImageTk.PhotoImage(image2)
    background_label3 = Label(deleteWindow, image=background_image2)
    background_label3.place(x=0, y=0, relwidth=1, relheight=1)

    label3 = Label(deleteWindow, text="Select the Gist to be deleted : ", bg='darkslategrey', fg='white',
                   font=("cambria", 15, 'bold'))
    label3.place(x=0, y=5)

    delcombo = ttk.Combobox(deleteWindow, width=20, font=("Helvetica", 18,))
    delcombo.place(x=270, y=3)
    delcombo['values'] = (GHgist.profile().listall())
    delcombo['state'] = 'readonly'

    delvar = StringVar()
    delvar.set("")

    label1 = Label(deleteWindow, textvariable=delvar, bg='darkslategrey', fg='white', font=("cambria", 20, 'bold'))
    label1.pack_forget()

    def delete():

        try:
            GHgist.profile().delete(name=str(delcombo.get()))
            delvar.set("Your Gist Has Been Deleted!")
            label1.place(x=240, y=180)

        except:
            delvar.set("Error : You Have No Gists")
            label1.place(x=240, y=180)

    delete_Gist = Button(deleteWindow, text="Delete Gist", bg="orchid", bd=8, width=20, height=1, relief=RAISED,
                         fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER,
                         command=delete)
    delete_Gist.place(x=266, y=60)


def edit_window():
    editWindow = Toplevel(root)
    editWindow.title("Edit Existing Gists")
    editWindow['bg'] = 'darkslategrey'
    editWindow.geometry("800x800")
    editWindow.resizable(height=False, width=False)

    global background_image3

    image2 = Image.open('C:\\Users\\GoodBoy69\\Downloads\\back.gif')
    background_image3 = ImageTk.PhotoImage(image2)
    background_label4 = Label(editWindow, image=background_image3)
    background_label4.place(x=0, y=0, relwidth=1, relheight=1)

    label2 = Label(editWindow, text="Select the Gist to be edited : ", bg='darkslategrey', fg='white',
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
            b.set("Here is your Gist, you can now make changes to it .")
            label4.place(x=150, y=750)

        except:
            view_desc.insert(1.0, "Error : You Have No Gist")
            view_desc.place(x=40, y=150)

    def update_Gist():

        try:

            GHgist.profile().edit(name=editcombo.get(), content=view_desc.get(1.0, "end"))
            b.set("Your Gist has been edited and updated")
            label4.place(x=150, y=750)

        except:
            b.set("Error : You have No Gist")
            label4.place(x=150, y=750)

    see_Gist = Button(editWindow, text="View Contents", bg="orchid", bd=8, width=20, height=1, relief=RAISED,
                      fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER, command=get_content)
    see_Gist.place(x=75, y=75)

    change_Gist = Button(editWindow, text="Update Contents", bg="orchid", bd=8, width=20, height=1, relief=RAISED,
                         fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER,
                         command=update_Gist)
    change_Gist.place(x=375, y=75)


def upload_window():
    global background_image4

    uploadWindow = Toplevel(root)
    uploadWindow.title("Edit Existing Gists")
    uploadWindow['bg'] = 'darkslategrey'
    uploadWindow.geometry("800x400")
    uploadWindow.resizable(height=False, width=False)

    file_name = StringVar()

    image2 = Image.open('C:\\Users\\GoodBoy69\\Downloads\\back.gif')
    background_image4 = ImageTk.PhotoImage(image2)
    background_label5 = Label(uploadWindow, image=background_image4)
    background_label5.place(x=0, y=0, relwidth=1, relheight=1)

    label2 = Label(uploadWindow, text="The File Selected is : ", bg='darkslategrey', fg='white',
                   font=("cambria", 15, 'bold'))
    label2.place(x=0, y=10)

    filename = askopenfilename(parent=uploadWindow)
    f = open(filename)
    x = f.read()
    file_name.set(os.path.basename(filename))

    upload_entry = Label(uploadWindow, textvariable=file_name, bg="darkslategrey", fg="white",
                         font=("cambria", 17, "bold"), justify=LEFT, bd=0)
    upload_entry.place(x=192, y=10)

    label_var = StringVar()
    label_var.set("")

    label = Label(uploadWindow, textvariable=label_var, bg='darkslategrey', fg='white', font=("cambria", 20, 'bold'))
    label.pack_forget()

    try:
        GHgist.create(name=os.path.basename(filename), public=False, content=x)

        label_var.set("Your File Has Been Uploaded &\n Gist Has Been Made")
        label.place(x=220, y=150)
    except:

        label_var.set("Error : File Not Uploaded")
        label.place(x=220, y=150)


# root buttons

create_Gist = Button(root, text="Create A New Gist", bg="orchid", bd=8, width=20, height=10, relief=RAISED,
                     fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER,
                     command=create_window)
create_Gist.place(x=80, y=50)

view_Gist = Button(root, text="View Your Gists", bg="orchid", bd=8, width=20, height=10, relief=RAISED,
                   fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER,
                   command=view_window)
view_Gist.place(x=450, y=50)

delete_Gist = Button(root, text="Delete Your Gists", bg="orchid", bd=8, width=20, height=10, relief=RAISED,
                     fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER,
                     command=delete_window)
delete_Gist.place(x=450, y=400)

edit_Gist = Button(root, text="Edit Existing Gists", bg="orchid", bd=8, width=20, height=10, relief=RAISED,
                   fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER,
                   command=edit_window)
edit_Gist.place(x=80, y=400)

upload_Gist = Button(root, text="Upload File to \n Create Gist", bg="orchid", bd=8, width=20, height=10, relief=RAISED,
                     fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER,
                     command=upload_window)
upload_Gist.place(x=260, y=230)

root.mainloop()
