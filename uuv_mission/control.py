# Code for the controller

class PDController:
    def __init__(self, Kp, Kd):
     
        self.Kp = Kp
        self.Kd = Kd
        self.previous_error = 0.0

    def compute_control(self, reference, measured_value, dt):
       
        error = reference - measured_value
        
        derivative = (error - self.previous_error) / dt
        
        control_action = self.Kp * error + self.Kd * derivative
        
        self.previous_error = error
        
        return control_action