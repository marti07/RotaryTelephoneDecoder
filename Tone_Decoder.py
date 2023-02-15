# Source: Electrocredible.com, Language: MicroPython
from machine import Pin
import time, _thread

pin = Pin(5, Pin.IN, Pin.PULL_UP)

interrupt_flag=0

current_time=time.ticks_us()
debounce_time=50

count=0
number=""

   
def rotary_pulses(p):        
    global interrupt_flag, debounce_time, count, current_time    
    if time.ticks_us() - current_time > debounce_time:
        interrupt_flag=1
        count+=1
        current_time=time.ticks_us()
        
pin.irq(trigger=Pin.IRQ_FALLING, handler=rotary_pulses)
print("Ready")

while True:
    if interrupt_flag is 1:        
        time.sleep(1)        
        number = number + str(count%10)
        print ("Number: ", number)
        count=0
        interrupt_flag=0
        
        