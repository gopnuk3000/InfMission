import tkinter as tk

# функция отображения фреймов
text_show = False


def show_frame(frame):
    global text_show
    if str(frame) == '.!frame2':
        if not text_show:
            typewriter_effect(frame2, animtext, labelanimtext)
            text_show = True
    frame.tkraise()


# функция отображения фото (название фрейма, название фото с расширением, координаты вставки)
def placephoto(page, imgfile, xx, yy):
    img = tk.PhotoImage(file=imgfile)
    lbl = tk.Label(page, image=img, borderwidth=0)
    lbl.image = img
    lbl.place(x=xx, y=yy)


def typewriter_effect(frame, text, label, delay=12, index=0):
    if index < len(text):
        label.config(text=label.cget('text') + text[index])
        frame.after(delay, typewriter_effect, frame, text, label, delay, index + 1)

    return index


try:
    root = tk.Tk()
    icon = tk.PhotoImage(file="icon.png")
    root.iconphoto(True, icon)
    root.title("IT-тринашка")
    root.geometry("1300x800")

    # Создаем фреймы
    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root)
    frame3 = tk.Frame(root)
    frame4 = tk.Frame(root)

    for frame in (frame1, frame2, frame3, frame4):
        frame.grid(row=0, column=0, sticky="nsew")

    # Фрейм 1 (Меню)
    label_menu = tk.Label(frame1, text="Меню", fg='#191970', font=("Arial", 30), width=56)
    label_menu.pack(fill=tk.X, pady=10)

    button_to_frame2 = tk.Button(frame1, text="О нас", bg='#0000CD', fg='#FFFFFF', activebackground='#FFFFFF',
                                 activeforeground='#0000CD', font=("Arial", 16),
                                 command=lambda: show_frame(frame2), width=30)
    button_to_frame2.pack(pady=40)

    button_to_frame3 = tk.Button(frame1, text="Галерея", bg='#0000CD', fg='#FFFFFF', activebackground='#FFFFFF',
                                 activeforeground='#0000CD', font=("Arial", 16),
                                 command=lambda: show_frame(frame3), width=30)
    button_to_frame3.pack(pady=40)

    button_to_frame4 = tk.Button(frame1, text="Участники", bg='#0000CD', fg='#FFFFFF', activebackground='#FFFFFF',
                                 activeforeground='#0000CD', font=("Arial", 16),
                                 command=lambda: show_frame(frame4), width=30)
    button_to_frame4.pack(pady=40)

    # Фрейм 2
    label_frame2 = tk.Label(frame2, text="О нас", fg='#191970', font=("Arial", 20))
    label_frame2.pack(pady=20)

    button_back_frame2 = tk.Button(frame2, text="Назад", bg='#0000CD', fg='#FFFFFF', activebackground='#FFFFFF',
                                   activeforeground='#0000CD', font=("Arial", 12),
                                   command=lambda: show_frame(frame1), width=20)
    button_back_frame2.place(relx=0.9, rely=0.1, anchor="ne")
    labelanimtext = tk.Label(frame2, text='', font=("Arial", 16), width=100, anchor="nw", fg='#191970',
                             justify="left")
    labelanimtext.pack(pady=20, anchor="nw", padx=50)
    f = open('text.txt', mode='r', encoding='utf-8')
    animtext = f.read()

    # Фрейм 3
    label_frame3 = tk.Label(frame3, text="Галерея", fg='#191970', font=("Arial", 20))
    label_frame3.pack(pady=20)

    button_back_frame3 = tk.Button(frame3, text="Назад", bg='#0000CD', fg='#FFFFFF', activebackground='#FFFFFF',
                                   activeforeground='#0000CD', font=("Arial", 12),
                                   command=lambda: show_frame(frame1), width=20)
    button_back_frame3.place(relx=0.9, rely=0.1, anchor="ne")

    # Фрейм 4
    label_frame4 = tk.Label(frame4, text="Участники", fg='#191970', font=("Arial", 20))
    label_frame4.pack(pady=20)

    button_back_frame4 = tk.Button(frame4, text="Назад", bg='#0000CD', fg='#FFFFFF', activebackground='#FFFFFF',
                                   activeforeground='#0000CD', font=("Arial", 12),
                                   command=lambda: show_frame(frame1), width=20)
    button_back_frame4.place(relx=0.9, rely=0.1, anchor="ne")

    # Показываем первый фрейм при запуске

    show_frame(frame1)
    root.mainloop()
except Exception as error:
    print(error.__class__.__name__)
