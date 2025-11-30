class ModelBasedReflexAgent:
    Action_on = "Turn ON Heater"
    Action_off = "Turn OFF Heater"

    def __init__(self, temp):
        self.fixed_temp = temp
        self.last_action = None
        self.history = {}

    def sensor(self, temp):
        self.current_temp = temp

    def performance(self):
        if self.current_temp in self.history:
            return f"From history: {self.history[self.current_temp]}"
        if self.current_temp < self.fixed_temp:
            action = self.Action_on
        else:
            action = self.Action_off

        self.history[self.current_temp] = action
        return action

    def actuator(self, room_name):
        action = self.performance()
        print(room_name, "temperature is", self.current_temp, "°C =>", action)


rooms = {
    "Living_Room": 20,
    "Drawing_Room": 29,
    "kitchen": 20,
    "Bed_Rooms": 18,
    "study_Room": 25,
    "Dinning_Room": 18,
    "Guest_Room": 35,
    "Garage": 30,
}

print("Model-Based Reflex Agent Detection")
agent = ModelBasedReflexAgent(22)

for room, temp in rooms.items():
    agent.sensor(temp)
    agent.actuator(room)