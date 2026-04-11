seconds = int(input("Enter number of seconds: "))

hours = seconds // 3600
remaining_seconds = seconds % 3600

minutes = remaining_seconds // 60
remaining_seconds = remaining_seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", remaining_seconds)
