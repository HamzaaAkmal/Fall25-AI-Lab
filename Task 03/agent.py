class Modelbasedagent:

    def __init__(self, desired_temp=25):   # by default i sets to 25
        self.desired_temp = desired_temp
        self.last_action = "OFF"
        self.fan_status = "OFF"
        self.history = []

    def act(self, current_temp):
        if current_temp < 15:
            action = "System Shutdown Too Cold "
            self.last_action = "OFF"
            self.fan_status = "OFF"
        elif current_temp < self.desired_temp - 1 and self.last_action != "ON":
            self.last_action = "ON"
            action = "Heater ON"
        elif current_temp > self.desired_temp + 1 and self.last_action != "OFF":
            self.last_action = "OFF"
            action = "Heater OFF"
        else:
            action = f"No Change, Heater is {self.last_action}"

        if current_temp > 30:
            self.fan_status = "ON"
            action += " + Fan ON"
        else:
            self.fan_status = "OFF"

        self.history.append((current_temp, action))
        return action

    def show_history(self):
        print("Action History")
        for temp, action in self.history:
            print(f"Temp {temp} => {action}")



agent = Modelbasedagent()
temperatures = [12, 22, 24, 25, 28, 32, 27, 15, 31]

print("Advanced ModelBased Reflex Agent")
for temp in temperatures:
    print(f"Current Temp: {temp} : {agent.act(temp)}")

agent.show_history()
