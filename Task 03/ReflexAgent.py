class ReflexAgent:
    def __init__(self, temp):
        self.temp = temp
        self.action = None

    def perceive(self, temperature):
        
        if temperature >= 22:
            if self.action != "Turn off Heater":
                self.action = 'Turn off Heater'
                return self.action
            else:
                return "Oops Already Exists"
        else:
            if temperature < 22 and self.action != "Turn on Heater":
                self.action = "Turn on Heater"
                return self.action
            else:
                return "Oops Already Exists"
    
rooms = {
    "Hamza Room": 21,
    'Parents Room' : 21,
    'Hamza Room' : 21,
    "Drawing Room": 21,
    "Gaming Room": 26,
    "Brother's Room": 24

}

ai_model = ReflexAgent(22)
for key , value in rooms.items():
    action = ai_model.perceive(value)
    print(f"{key} temperature is {value} => {action}")





