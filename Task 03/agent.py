class SmartTempController:

    def __init__(self, target_temp=25):   # default target temperature
        self.target_temp = target_temp
        self.heater_mode = "OFF"
        self.cooler_mode = "OFF"
        self.log = []

    def control(self, room_temp):
        if room_temp < 15:
            action = "System Halted - Too Cold!"
            self.heater_mode = "OFF"
            self.cooler_mode = "OFF"
        elif room_temp < self.target_temp - 1 and self.heater_mode != "ON":
            action = "Heater Activated"
            self.heater_mode = "ON"
        elif room_temp > self.target_temp + 1 and self.heater_mode != "OFF":
            action = "Heater Deactivated"
            self.heater_mode = "OFF"
        else:
            action = f"Stable Condition - Heater: {self.heater_mode}"

        # Fan logic
        if room_temp > 30:
            self.cooler_mode = "ON"
            action += "  Fan Running"
        else:
            self.cooler_mode = "OFF"

        self.log.append((room_temp, action))
        return action

    def display_log(self):
        print("Action Record:")
        for temp, action in self.log:
            print(f"At {temp} => {action}")


# running the controller
controller = SmartTempController()
temperature_readings = [12, 22, 24, 25, 28, 32, 27, 15, 31]

print("Down Temperature Management System")
for t in temperature_readings:
    print(f"Room Temp: {t} => {controller.control(t)}")

controller.display_log()
