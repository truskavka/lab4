import tkinter as tk
from tkinter import messagebox


# Налаштування вікна
root = tk.Tk()
root.title("Калькулятор")

# Поля для вводу
entry1 = tk.Entry(root, width=10)
entry2 = tk.Entry(root, width=10)
entry1.grid(row=0, column=1, padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Текст для полів
tk.Label(root, text="Перше число:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Друге число:").grid(row=1, column=0, padx=5, pady=5)

# Кнопки для операцій
tk.Button(root, text="+", width=5, command=add).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="-", width=5, command=subtract).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="*", width=5, command=multiply).grid(row=2, column=2, padx=5, pady=5)
tk.Button(root, text="/", width=5, command=divide).grid(row=2, column=3, padx=5, pady=5)

# Поле для відображення результату
result_label = tk.Label(root, text="Результат: ")
result_label.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

# Запуск інтерфейсу
root.mainloop()
