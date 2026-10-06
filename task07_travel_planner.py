destination = input("Destination: ")
distance = float(input("Distance in km: "))
speed = float(input("Average speed in km/h: "))

travel_time_hours = distance / speed

hours = int(travel_time_hours)
minutes = int((travel_time_hours - hours) * 60)

print(f"Destination: {destination}")
print(f"Distance: {distance:.1f} km")
print(f"Average Speed: {speed:.1f} km/h")
print(f"Estimated Travel Time: {hours} hours and {minutes} minutes ({travel_time_hours:.2f} hours)")