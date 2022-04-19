import smbus
import time

# sht30 class
class SHT30():
    
    # Initialize SHT30 sensor
    def __init__(self):
        # Get I2C bus
        self.bus = smbus.SMBus(1)

        # SHT30 address: 0x44
        # Send measurement command, 0x2C
        #    0x06 - High Repeatability Measurement
        self.bus.write_i2c_block_data(0x44, 0x2C, [0x06])

        time.sleep(0.5)
    
    # Measure Temperature and Humidity
    def measure(self):
        # SHT30 address: 0x44
        # Read data back from 0x00 (6 bytes)
        # cTemp MSB, cTemp LSB, cTemp CRC, Humidity MSB, Humidity LSB, Humidity CRC
        self.data = self.bus.read_i2c_block_data(0x44, 0x00, 6)
        
    
    # Returns measured temperature value in Celsius
    def get_Temp_C(self):
        # Convert cTemp MSB and cTemp LSB to Temperature Value in Celsius
        self.cTemp = ((((self.data[0] * 256.0) + self.data[1]) * 175) / 65535.0) - 45
        return self.cTemp
    
    
    # Returns measured temperature value in Fahrenheit
    def get_Temp_F(self):
        cTemp = self.get_Temp_C()
        self.fTemp = cTemp * 1.8 + 32
        return self.fTemp
    
    # Returns measured humidity value
    def get_Humidity(self):
        # Convert Humidity MSB and Humidity LSB to humidity percentage
        self.humidity = 100 * (self.data[3] * 256 + self.data[4]) / 65535.0
        return self.humidity