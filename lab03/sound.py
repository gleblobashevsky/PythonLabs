'''Lobashevsky Gleb R3140 559599'''
from pygame import mixer

click_sound = None


def init_music():
    '''Функция создания музыки на заднем фоне'''
    mixer.init()
    mixer.music.load('undertale_068. Death by Glamour.mp3')
    mixer.music.set_volume(0.1)
    mixer.music.play(-1)


def init_sound():
    '''Функция для создания звука нажатия на кнопку'''
    global click_sound
    click_sound = mixer.Sound('enemy-encounter-undertale.wav')
    click_sound.set_volume(0.1)


def play_click():
    '''Воспроизведение звука нахатия на кнопку'''
    click_sound.play()


def stop_music():
    '''Остановка воспроизведения мелодии на заднем фоне'''
    mixer.music.stop()
    mixer.quit()
