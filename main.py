from mouse.mouse_se import MouseSE
import mouse.mouse_client as mse
import wordHuntTool
import time


def goto_spot(val, debug=False):
    x = val % 4
    y = val // 4
    my_mouse.goto(130 + x * 100, 480 + y * 100)


if __name__ == "__main__":
    global my_mouse
    my_mouse = MouseSE()
    words = wordHuntTool.collect_info()
    for i in words:
        my_mouse.press(False)
        for spot in i:
            time.sleep(1)
            goto_spot(spot)
            my_mouse.press(True)
        my_mouse.press(False)
    print("done")
