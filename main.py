from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # replace from random randint
    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(8, 10))
    # nr_numbers = random.randint(8, 10)

    #password_lis =[]
    # list comprehension
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    # replace below password_letters
    password_letters = [choice(letters) for _ in range(randint(8, 10))]


    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    # replace below password_symbols
    password_symbols = [choice(symbols) for _ in range(randint(2, 5))]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    # replace below password_numbers
    password_numbers = [choice(numbers) for _ in range(randint(2, 5))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    # replace with password below

    password = "".join(password_list)
    # print(f"Your password is: {password}")
    pass_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email = user_name_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="PLease make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving update data
                json.dump(data, data_file, indent=4)

        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)




        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email} "
        #                                               f"\nPassword: {password} \nIs it ok to save?")
        #
        # if is_ok :
        #     with open("data.txt", "a") as data_file:
        #         # data_file.write(f"{website} | {email} | {password}\n")
        #         web_input.delete(0, END)
        #         pass_input.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = web_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No detail for {website} exist.")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
passw_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=passw_img)
canvas.grid(column=1, row=0)

# label
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username: ")
username_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# Entry
web_input = Entry(width=21)
web_input.grid(column=1, row=1, sticky="ew")
web_input.focus()

user_name_input = Entry(width=35)
user_name_input.grid(column=1, row =2, columnspan=2, sticky="ew")
user_name_input.insert(0, "suhendra.eli@gmail.com")

pass_input = Entry(width=21)
pass_input.grid(column=1, row=3, sticky="ew")

# Button
generated_pass_button = Button(text="Generate Password", command=generate_password)
generated_pass_button.grid(column=2, row=3, sticky="ew")


add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1, sticky="ew")




window.mainloop()