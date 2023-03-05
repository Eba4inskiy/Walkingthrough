from tkinter import *
import random
import tkinter.messagebox as messagebox

class RandomNumberGenerator:

    def __init__(self, master):
        self.master = master
        master.title("Random Number Generator")

        self.num_digits_label = Label(master, text="Enter the number of digits:")
        self.num_digits_label.pack()

        self.num_digits_entry = Entry(master)
        self.num_digits_entry.pack()

        self.digits_label = Label(master, text="Select the digits to use:")
        self.digits_label.pack()

        self.digits_frame = Frame(master)
        self.digits_frame.pack()

        self.digits = {}
        for i in range(10):
            self.digits[i] = IntVar()
            checkbutton = Checkbutton(self.digits_frame, text=str(i), variable=self.digits[i])
            checkbutton.pack(side=LEFT)

        self.generate_button = Button(master, text="Generate", command=self.generate_number)
        self.generate_button.pack()

        self.clear_button = Button(master, text="Clear", command=self.clear_data)
        self.clear_button.pack()

    def generate_number(self):
        num_digits = self.num_digits_entry.get()

        # Check if the input is a valid number
        if not num_digits.isnumeric():
            error_message = "Invalid input: Please enter a number"
            messagebox.showerror("Error", error_message)
            return

        num_digits = int(num_digits)

        selected_digits = [str(i) for i in self.digits if self.digits[i].get()]

        if not selected_digits:
            error_message = "Please select at least one digit"
            messagebox.showerror("Error", error_message)
            return

        number = "".join(random.choices(selected_digits, k=num_digits))

        result_window = Toplevel(self.master)
        result_window.title("Result")

        result_label = Label(result_window, text="Generated number: " + number)
        result_label.pack()

        copy_button = Button(result_window, text="Copy", command=lambda: self.copy_to_clipboard(number))
        copy_button.pack()

    def copy_to_clipboard(self, text):
        self.master.clipboard_clear()
        self.master.clipboard_append(text)
        self.master.update()

    def clear_data(self):
        self.num_digits_entry.delete(0, END)
        for i in self.digits:
            self.digits[i].set(0)

    def exit(self):
        self.master.destroy()

root = Tk()
random_number_generator = RandomNumberGenerator(root)
root.mainloop()
