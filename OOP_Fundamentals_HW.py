# OOP Fundamentals HW
# Task 1: Vehicle Registration System

# # Basic structure of Vehicle class
# class Vehicle:
#     def __init__(self, reg_num, vehicle_type, owner):
#         self.reg_num = reg_num
#         self.type = vehicle_type
#         self.owner = owner



# Basic structure of Vehicle class with update_owner method
class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.reg_num = reg_num
        self.vehicle_type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

    def display_info(self):
        print(f"Registration Number: {self.reg_num}")
        print(f"Type: {self.vehicle_type}")
        print(f"Owner: {self.owner}")

# Instance of Vehicle class: #1
vehicle_1 = Vehicle("123123", "pickup truck", "Bob")
print("vehicle_1")
print(f" Registration number: ", vehicle_1.reg_num)
print(f" vehicle type: ", vehicle_1.vehicle_type)
print(f" owner: ", vehicle_1.owner)

# Instance of Vehicle class: #2
vehicle_2 = Vehicle("234234", "car", "Synthia")
print("vehicle_2")
print(f" Registration number: ", vehicle_2.reg_num)
print(f" vehicle type: ", vehicle_2.vehicle_type)
print(f" owner: ", vehicle_2.owner)

# Instance of Vehicle class: #3
vehicle_3 = Vehicle("456456", "reefer", "Trucker John")
print("vehicle_3")
print(f" Registration number: ", vehicle_3.reg_num)
print(f" vehicle type: ", vehicle_3.vehicle_type)
print(f" owner: ", vehicle_3.owner)

    


new_owner_pickup_truck = input("Enter the new owner of the pickup truck: ")
vehicle_1.update_owner(new_owner_pickup_truck)

new_owner_car = input("Enter the new owner of the car: ")
vehicle_2.update_owner(new_owner_car)
vehicle_2.display_info()


vehicle_1.display_info()
vehicle_2.display_info()





# Task 2: Event Management System Enhancement

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = []
        self.participants_count = 0

    def add_participant(self, participant_name):
        self.participants.append(participant_name)
        self.participants_count += 1

    def remove_participant(self, participant_name):
        if participant_name in self.participants:
            self.participants.remove(participant_name)
            self.participants_count -= 1

    def get_participant_count(self):
        return self.participants_count

    def display_info(self):
        print(f"Event Name: {self.name}")
        print(f"Event Date: {self.date}")
        print(f"Number of participants: {self.participants_count}")
        print("Participants: ")
        for participant in self.participants:
            print(f" - {participant}")

def add_participants_via_input(event):
    while True:
        participant_name = input("Enter participant name (or 'done' to finish): ")
        if participant_name.lower() == 'done':
            break
        event.add_participant(participant_name)
        print(f"Added participant: {participant_name}")
        print(f"Current participant count: {event.get_participant_count()}")

# Example usage
event = Event("Music Concert", "2024-06-15")
event.display_info()

# Add participants using user input
add_participants_via_input(event)

# Display updated information
event.display_info()
