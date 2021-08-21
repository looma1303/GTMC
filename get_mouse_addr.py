import pyautogui as pag
import keyboard
from PIL import ImageGrab


play_online = [955, 642]
connect = [1217, 846]
cancel = [678, 851]
event_x_botten = [1401, 201]
showing_random_world = [698, 463]
your_world = [851, 481]
world_1kty1 = [1001, 461]
start_icon = [127, 128]
detecter_addr = [466, 277]


def mouse_addr():
    x, y = pag.position()
    return x,y


if __name__ == "__main__":
    while 1:
        if keyboard.read_key() == "p":
            x, y = mouse_addr()
            screen = ImageGrab.grab()
            
            print("지금 마우스 위치: {x}, {y}".format(x = x, y = y))
            print("지금 마우스 위치 RGB 값: {rgb}".format(rgb = screen.getpixel((x, y))))
        elif keyboard.read_key() == "s":
            break
        else:
            pass
                
        


