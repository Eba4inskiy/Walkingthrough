import random
import tkinter as tk

# Функція, яка генерує псевдовипадкове число з використанням введених параметрів
def generate_random_number(length, digits):
    # Перевірка вхідних даних
    if not length.isdigit() or not digits.isdigit():
        return "Помилка: Введіть числові значення для довжини та цифр"
    length = int(length)
    digits = int(digits)
    if length <= 0 or digits <= 0 or digits > 10:
        return "Помилка: Неприпустимі значення довжини та цифр"

    # Генерування псевдовипадкового числа
    number = ""
    for i in range(length):
        number += str(random.randint(0, digits-1))
    return number

# Функція, яка викликається при натисканні кнопки "Згенерувати"
def generate_button_clicked():
    length = length_entry.get()
    digits = digits_entry.get()
    result = generate_random_number(length, digits)
    result_label.config(text=result)
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)
    result_text.config(state=tk.DISABLED)
    scrollbar.config(command=result_text.yview)

# Створення головного вікна програми
root = tk.Tk()
root.title("Генератор псевдовипадкового числа")

# Додавання елементів на головне вікно
length_label = tk.Label(root, text="Довжина числа:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

digits_label = tk.Label(root, text="Цифри (від 2 до 10):")
digits_label.pack()
digits_entry = tk.Entry(root)
digits_entry.pack()

generate_button = tk.Button(root, text="Згенерувати", command=generate_button_clicked)
generate_button.pack()

result_label = tk.Label(root, text="Результат:")

result_text = tk.Text(root, height=1, state=tk.DISABLED)
result_text.pack(side=tk.LEFT, fill=tk.Y)
scrollbar = tk.Scrollbar(root, command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()
