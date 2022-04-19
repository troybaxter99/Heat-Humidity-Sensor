# This program is the main program used to check temperature and humidity in the rover

import sht30
import sys
import time

sys.path.insert(1, "/home/pi/Audio-Alert-System/Code")
import audio

# Create AUDIO and SHT30 Sensor objects
sensor = sht30.SHT30()
sound = audio.AUDIO()
sound.set_espeak_gap(1000) # Set gap between each word to be 1 second (1000 ms)

# Instantiate humidity and temperature
global humidity
global temp


# This function serves to get the sensor measurements
def getMeasurements():
    global humidity
    global temp
    
    sensor.measure() # measures values
    
    # Get humidity and temperature values from measurement
    humidity = sensor.get_Humidity()
    temp = sensor.get_Temp_C()


# OVERHEATING Alert System!!!
def overheating():
    # Play Overheating Alert 3 Times
    for i in range(0,3):
        sound.play_audio("Overheating-Alert.wav")
        sound.play_message("Danger! Danger! Danger!")
        sound.play_message("Over Heating! Over Heating! Over Heating!")
    
# HUMIDITY Alert System!!!
def tooHumid():
    # Play Humidity Alert 3 Times
   for i in range(0,3):
        sound.play_audio("Humidity-Alert.wav")
        
        # Play message 3 teams
        for j in range(0,3):
            sound.play_message("Danger! Too Humid!")
            
def main():
    while True:
        getMeasurements()
        print("Humidity: %.2f%%" %humidity)
        print("Temperature: %.2f C" %temp)
        
        
        # If humidity is greater than 90% Alert Danger
        if (humidity > 90):
            tooHumid()
        
        # Of temperature is greater than 50 C Alert Danger
        if (temp > 50):
            overheating()
        
        # Sleep for 5 seconds before taking an other reading
        time.sleep(5)
    
if __name__ == "__main__":
    main()