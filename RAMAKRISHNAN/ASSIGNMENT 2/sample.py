import time
import random

i=0

while(i==0): # Creates infinity number of Loops
    
    temperature = random.randint(10,50) # Temperature value generated randomly
    
    humidity = random.randint(10,100) # Humidity value generated randomly
    
    if temperature<=25:
        print(temperature,": Temperature is Low")
    elif temperature>=25 and temperature<=36:
        print(temperature,": Temperature is Normal")
    else:
        print(temperature,": Temperature is High")

    time.sleep(1)
    
    if humidity<=15:
        print(humidity,": Humidity is Low")
    elif humidity<=80:
        print(humidity,": Humidity is Normal")
    else:
        print(humidity,": Humidity is High")

    time.sleep(1)
