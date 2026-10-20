'''Lobashevsky Gleb R3140 559599'''
from pygame import mixer

click_sound = None


def init_music():
    mixer.init()
    mixer.music.load('undertale_068. Death by Glamour.mp3')
    mixer.music.set_volume(0.1)
    mixer.music.play(-1)


def init_sound():
    global click_sound
    click_sound = mixer.Sound('enemy-encounter-undertale.wav')
    click_sound.set_volume(0.1)


def play_click():
    click_sound.play()


def stop_music():
    mixer.music.stop()
    mixer.quit()
