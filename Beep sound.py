import winsound
frequency=745
duration=800
print('Enter 1 in terminal to play sound')
sound = int(input("Turn on sound?"))
if sound == 1:
    winsound.Beep(frequency,duration)
else: 
    print('wrong number to activate the sound signal')