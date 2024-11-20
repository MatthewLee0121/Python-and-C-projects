import os
import sys
import time

print("hello")

def hello_world():
 print("hello world")

hello_world()

def generate_trip_instructions(location):
  print(f"Looks like you are planning a trip to visit {location}")
  print(f"You can use the public subway system to get to {location}")

generate_trip_instructions("Central Park")

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate , trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  print(car_rental_total + hotel_total + plane_ticket_price)
calculate_expenses(200, 100, 100, 5)


def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
 print("Here is what your trip will look like!")
 print(f"First, we will stop in {first_destination}, then {second_destination}, and lastly {final_destination}")
trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination = "Iceland", final_destination = "Germany", second_destination = "India")
trip_planner("Brooklyn", "Queens")

def trip_planner_welcome(name):
  print(f"Welcome to tripplanner v1.0 {name}")

trip_planner_welcome("matty")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(4.56)

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
   print(
    f"Your trip starts off in {origin}"
    f" And you are traveling to {destination}"
    f" You will be traveling by {mode_of_transport}"
    f" It will take approximately {estimated_time} hours"
    )

destination_setup("Newcastle", "london", estimate)
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
 lengthLN = len(last_name)
 lengthFN = len(first_name)
 password = first_name[lengthFN-3:] + last_name[lengthLN-3:]
 return password

temp_password = password_generator(first_name, last_name)
print(temp_password)


current_directory = os.path.dirname(os.path.abspath(__file__))
print("Current directory:", current_directory)

def typing(new_print, delay = 0.07):
    for c in new_print:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    return ""
