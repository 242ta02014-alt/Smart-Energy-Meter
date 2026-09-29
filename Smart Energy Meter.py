# Smart-Energy-Meter
# Simple Smart Energy Meter

voltage = float(input("Enter voltage (V): "))
current = float(input("Enter current (A): "))
time = float(input("Enter usage time (hours): "))

# Calculate power
power = voltage * current

# Calculate energy
energy = (power * time) / 1000

print("\n--- Smart Energy Meter ---")
print("Voltage :", voltage, "V")
print("Current :", current, "A")
print("Power   :", power, "W")
print("Energy  :", energy, "kWh")
