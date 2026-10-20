'''Lobashevsky Gleb R3140 559599'''
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # строка нужна чтобы при запуске в консоль не выводилась информация про один из используемых модулей
import tkinter as tk
from keygen import main_func
from sound import init_music, stop_music, init_sound, play_click


def generate_key(plc):
    '''Функция для обработки нажания на кнопку btn_key'''
    play_click()
    plc['text'] = main_func()


def my_exit(window):
    '''Функция для завершения работы программы'''
    stop_music()
    window.destroy()


def create_components(window, w, h):
    '''Функция для создания интерфейса с возможностью взаимодействия пользователя'''
    label = tk.Label(window,
                     text='',
                     fg="white",
                     bg='black',
                     justify='left',
                     font=('Helvetica 12 bold', 14)
                     )

    label.place(x=(w - 550),
                y=(h - 125))

    self_btn_width = 60
    self_btn_height = 20

    btn_exit = tk.Button(window,
                         text='Exit',
                         fg="white",
                         bg='black',
                         command=lambda: my_exit(window),
                         relief='flat',
                         activebackground='black'
                         )
    btn_exit.place(x=(w - self_btn_width - 150),
                   y=(h - self_btn_height - 35),
                   width=self_btn_width,
                   height=self_btn_height
                   )

    btn_key = tk.Button(window,
                        text='Key',
                        fg="white",
                        bg='black',
                        command=lambda: generate_key(label),
                        relief='flat',
                        activebackground='black'
                        )
    btn_key.place(x=(w - self_btn_width - 150),
                  y=(h - 6 * self_btn_height - 15),
                  width=self_btn_width,
                  height=self_btn_height
                  )


def init_window():
    '''Функция инициализации основного окна и его параметров'''
    window = tk.Tk()
    window.overrideredirect(True)
    window.resizable(False, False)
    window.image = tk.PhotoImage(file='undertail_mettaton.png')

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    image_width = window.image.width()
    image_height = window.image.height()

    window.geometry(
        f'{image_width}x{image_height}+{width // 2 - (image_width // 2)}+{height // 2 - (image_height // 2)}')

    bg_logo = tk.Label(window, image=window.image)
    bg_logo.grid(row=0, column=0)

    create_components(window, image_width, image_height)

    init_music()
    init_sound()

    return window


if __name__ == '__main__':
    init_window().mainloop()
