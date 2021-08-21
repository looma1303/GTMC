import pyautogui as pag
import pyautogui as click
from PIL import ImageGrab
import keyboard
import time



play_online = [955, 642]
connect = [1217, 846]
cancel = [678, 851]
event_x_botten = [1401, 201]
showing_random_world = [698, 463]
your_world = [851, 481]
world_1kty1 = [1001, 461]
start_icon = [127, 128]
detecter_addr = [466, 277]
start_screen_rgb = (6,23,30)


def login():
    click(x = start_icon[0], y = start_icon[1])
    time.sleep(0.2)
    click(x = start_icon[0], y = start_icon[1])
    time.sleep(5)
    #turn on game
    
    click(x = play_online[0], y = play_online[1])
    #click play online
    time.sleep(2)
    
    click(x = connect[0], y = connect[1])
    
    login_detecter()
    
    time.sleep(2)
    click(x = event_x_botten[0], y = event_x_botten[1])
    
    

    
    

def login_detecter():
    while 1:
        screen = ImageGrab.grab()
        rgb = screen.getpixel((466, 277))
        if rgb == start_screen_rgb:
            print("login successfull")
            break
        else:
            pass
            
    
    
    
    
    
    
    
    
    