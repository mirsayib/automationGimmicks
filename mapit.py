import webbrowser, sys, pyperclip

sys.argv  # ['mapit.py', '870', 'Valencia', 'st.]

#Check if command line arguements were passed

if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'st.] -> join them into '870 Valencai St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
#https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)

