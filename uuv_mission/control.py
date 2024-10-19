# Code for the controller

class PDController:
    def __init__(self, Kp, Kd):
        """
        Initialize the PD controller with given gains.
        
        Parameters:
        Kp (float): Proportional gain
        Kd (float): Derivative gain
        """
        self.Kp = Kp
        self.Kd = Kd
        self.previous_error = 0.0

    def compute_control(self, setpoint, measured_value, dt):
        """
        Compute the control action using PD control logic.
        
        Parameters:
        setpoint (float): Desired setpoint value
        measured_value (float): Current measured value
        dt (float): Time step
        
        Returns:
        float: Control action
        """
        # Calculate error
        error = setpoint - measured_value
        
        # Calculate derivative of error
        derivative = (error - self.previous_error) / dt
        
        # Compute control action
        control_action = self.Kp * error + self.Kd * derivative
        
        # Update previous error
        self.previous_error = error
        
        return control_action