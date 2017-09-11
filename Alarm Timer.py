import time

def countdown(input_time):
    while input_time > 0:
        print (input_time)
        input_time -= 1
        time.sleep(1)
        if input_time == 0:
            print ("ALARM TURNING OFF")
            break

countdown(20)
