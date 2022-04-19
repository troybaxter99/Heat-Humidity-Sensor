# This program is a test to check if the robot is in danger of overheating or if the internal humidity is too high
import sht30
import sys
import time

sys.path.insert(1, "/home/pi/Audio-Alert-System/Code")
import audio

sensor = sht30.SHT30()
sound = audio.AUDIO()
sound.set_espeak_gap(1000)

sensor.measure()

humidity = sensor.get_Humidity()
cTemp = sensor.get_Temp_C()
fTemp = sensor.get_Temp_F()

#Output data to screen
print("Relative Humidity : %.2f %%RH" %humidity)
print("Temperature in Celsius : %.2f C" %cTemp)
print("Temperature in Fahrenheit : %.2f F" %fTemp)

if (cTemp > 25):
    for i in range(1,4):
        sound.play_audio("Overheating-Alert.wav")
        sound.play_message("Danger! Danger! Danger!")
        sound.play_message("Over Heating! Over Heating! Over Heating!")
        
if (humidity>50):
    for i in range(1,4):
        sound.play_audio("Humidity-Alert.wav")
        
        for j in range(1,4):
            sound.play_message("Danger! Too Humid!")
