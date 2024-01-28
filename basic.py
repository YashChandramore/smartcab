initial_radius = 100  # Setting an initial radius value
time_interval = 1
current_radius = initial_radius
timer = 0
max_wait_time = 5

def identify_available_cabs(current_radius):
    pass

def display_cabs_to_user(available_cabs):
    
    pass

def send_request_to_drivers(available_cabs):
    pass

def driver_accepts_request():
    
    pass

def allocate_cab_to_user():
   
    pass

def reset_time_interval():
    
    pass

def notify_user_cab_unavailability():
   
    pass

# setting time interval for radius expansion to 1 minute
time_interval = 1
current_radius = initial_radius
timer = 0

while timer < max_wait_time:
    available_cabs = identify_available_cabs(current_radius)
    display_cabs_to_user(available_cabs)
    send_request_to_drivers(available_cabs)

    if driver_accepts_request():
        allocate_cab_to_user()
        break

    if timer % time_interval == 0:
        current_radius *= 2
        reset_time_interval()

    timer += 1

if timer == max_wait_time:
    notify_user_cab_unavailability()
