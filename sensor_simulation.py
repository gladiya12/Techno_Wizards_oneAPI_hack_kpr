from machine import Pin, ADC
import time

current_sensor = ADC(26)  
alarm = Pin(15, Pin.OUT)  
led = Pin(14, Pin.OUT)    


current_threshold = 10.0  # Modify according to your need

# Conversion factor for ACS712 current sensor (change as per your sensor version)
conversion_factor = 0.066  # For ACS712-30A

def read_current():
    raw_value = current_sensor.read_u16()  # Read the analog value (0-65535)
    voltage = (raw_value / 65535.0) * 3.3  # Convert raw value to voltage (3.3V reference)
    current = (voltage - 1.65) / conversion_factor  # Calculate current in Amps
    return current

while True:
    current_value = read_current()
    print("Current Value: ", current_value, "A")
    
    # Check if the current exceeds the threshold
    if current_value >= current_threshold:
        alarm.high()  # Turn on alarm
        led.high()    # Turn on LED
    else:
        alarm.low()   # Turn off alarm
        led.low()     # Turn off LED
    
    time.sleep(1)  # Delay of 1 second
