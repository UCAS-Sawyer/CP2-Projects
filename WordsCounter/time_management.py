#Sawyer Wood, getting the date and time for the other files
import time

def current_time():
    # Convert the current time to a readable format
    current_time = time.time()
    local_time = time.localtime(current_time)
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    return formatted_time