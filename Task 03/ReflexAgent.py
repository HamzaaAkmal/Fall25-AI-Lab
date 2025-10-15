class SmartClimateAgent:

    def __init__(self, set_temp=25):   # default temperature target
        self.set_temp = set_temp
        self.heater_state = "OFF"
        self.fan_state = "OFF"
        self.records = []

    def operate(self, current_temp):

        if current_temp < 15:
            status = "System Jam Giyya hai - Extremely Cold"
            self.heater_state = "OFF"
            self.fan_state = "OFF"

        elif current_temp < self.set_temp - 1 and self.heater_state != "ON":
            self.heater_state = "ON"
            status = "Heater Turned ON"

        elif current_temp > self.set_temp + 1 and self.heater_state != "OFF":
            self.heater_state = "OFF"
            status = "Heater Turned OFF"

        else:
            status = f"No Adjustment Needed (Heater: {self.heater_state})"

        # Fan operation

        
        if current_temp > 30:
            self.fan_state = "ON"
            status += " | Cooling Fan Activated"
        else:
            self.fan_state = "OFF"

        self.records.append((current_temp, status))
        return status

    def show_log(self):
        print("\nSystem Operation Log:")
        for temp, status in self.records:
            print(f"Temperature {temp}°C → {status}")



climate_agent = SmartClimateAgent()
temp_values = [12, 22, 24, 25, 28, 32, 27, 15, 31]


for temp in temp_values:
    print(f"Current Temperature: {temp} => {climate_agent.operate(temp)}")

climate_agent.show_log()
