# This program is the main program used to check temperature and humidity in the rover

import sht30
import sys
import time
import board

sys.path.insert(1, "/home/pi/Audio-Alert-System/Code")
import audio

# Create AUDIO and SHT30 Sensor objects
i2c = board.I2C()
sensor = sht30.SHT31D(i2c)
sound = audio.AUDIO("/home/pi/Audio-Alert-System/Audio-Files/Alert-Audio/")
sound.set_espeak_gap(1000) # Set gap between each word to be 1 second (1000 ms)

# Instantiate humidity and temperature
global humidity
global temp


# This function serves to get the sensor measurements
def getMeasurements():
    global humidity
    global temp
    
    # Get humidity and temperature values from measurement
    humidity = sensor.relative_humidity
    temp = sensor.temperature


# OVERHEATING Alert System!!!
def overheating():
    # SEt Volume to Max Level:
    sound.set_volume(100)
    # Play Overheating Alert 3 Times
    for i in range(0,3):
        sound.play_audio("Overheating-Alert.wav")
        time.sleep(1)
        sound.play_message("Danger! Danger! Danger! Over Heating! Over Heating! Over Heating!")
    
# HUMIDITY Alert System!!!
def tooHumid():
    # Set Volume to Max Level:
    sound.set_volume(100)
    # Play Humidity Alert 3 Times
    for i in range(0,3):
        sound.play_audio("Humidity-Alert.wav")
        time.sleep(2)
        
        sound.play_message("Danger! Too Humid! Danger! Too Humid! Danger! Too Humid!")
            
def main():
    while True:
        getMeasurements()
        print("Humidity: %.2f%%" %humidity)
        print("Temperature: %.2f C" %temp)
        
        
        # If humidity is greater than 90% Alert Danger
        if (humidity > 90):
            tooHumid()
        
        # If temperature is greater than 50 C Alert Danger
        if (temp > 50):
            overheating()
        
        # Sleep for 5 seconds before taking an other reading
        time.sleep(5)
    
if __name__ == "__main__":
    main()