from datetime import datetime

# Get current time
current_time = datetime.now()

# Display the current time in different formats
print("Current Time:")
print(f"Time: {current_time.strftime('%H:%M:%S')}")
print(f"Date: {current_time.strftime('%Y-%m-%d')}")
print(f"Full: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Alternative way to display
print(f"\nCurrent datetime object: {current_time}")
