import nengo
import numpy as np
# Instructions:
# 1. Run this file in Nengo GUI
# 2. Right-click on `spring_strength` node and select "slider" (range 0.1 to 5.0)
# 3. Right-click on `state` node and select "value" to see actual dynamics
# 4. Right-click on `prediction` node to see what the SNN learns
# 5. Right-click on `error` node to see learning error (should decrease over time)
# 6. For a trajectory plot, right-click on `state` and select "XY-value"
#    - X axis: dimension 0 (x_pos)
#    - Y axis: dimension 2 (y_pos)
# 7. Press play and watch the ensemble LEARN the spring dynamics via PES!
#    - The prediction should converge to match the actual state
#    - Adjust spring_strength slider to see if it can adapt to changes
# 
# The state represents: [x_position, x_velocity, y_position, y_velocity]
# Initial conditions: x=1.0, vx=0.0, y=-1.0, vy=0.5
# Learning: PES rule with learning_rate=1e-4

# Spring parameters
m = 1.0  # Mass
dt = 0.001  # Time step

class Spring2DProcess(nengo.Process):
    """Process that integrates 2D spring dynamics with variable spring constant"""
    def __init__(self, m, dt):
        self.m = m
        self.dt = dt
        self.state = np.array([1.0, 0.0, -1.0, 0.5])  # [x, vx, y, vy]
        super().__init__(default_size_in=1, default_size_out=4)  # Input is k (spring constant)
    
    def make_step(self, shape_in, shape_out, dt, rng, state=None):
        m = self.m
        current_state = self.state.copy()
        
        def step(t, k_input):
            # Get spring constant from input (default to 1.0 if not provided)
            k = k_input[0] if len(k_input) > 0 else 1.0
            
            # Spring dynamics: derivatives
            # x = [x_pos, x_vel, y_pos, y_vel]
            # dx/dt = [vx, -k/m*x, vy, -k/m*y]
            derivatives = np.array([
                current_state[1],           # dx/dt = vx
                -k/m * current_state[0],    # dvx/dt = -k/m*x
                current_state[3],           # dy/dt = vy
                -k/m * current_state[2]     # dvy/dt = -k/m*y
            ])
            
            # Euler integration
            current_state[:] = current_state + derivatives * dt
            return current_state.copy()
        
        return step

# Network
model = nengo.Network(label="Interactive 2D Spring System")
with model:
    # Slider for spring constant (k)
    spring_strength = nengo.Node(output=lambda t: 1.0, label="spring_strength")
    
    # Physics node - implements the spring dynamics
    state = nengo.Node(Spring2DProcess(m, dt))
    
    # Connect spring strength slider to physics
    nengo.Connection(spring_strength, state, synapse=None)
    
    # Ensemble for learning prediction
    ensemble = nengo.Ensemble(100, dimensions=4, radius=2)
    nengo.Connection(state, ensemble, synapse=0.01)
    
    # Prediction node - what the ensemble predicts
    prediction = nengo.Node(size_in=4, label="prediction")
    
    # Learning connection with PES rule
    learn_conn = nengo.Connection(
        ensemble, 
        prediction,
        learning_rule_type=nengo.PES(learning_rate=1e-4),
        function=lambda x: np.zeros(4)  # Start with zero prediction
    )
    
    # Error calculation: actual state - prediction
    error = nengo.Node(size_in=4, label="error")
    nengo.Connection(state, error, synapse=0.01, transform=1)
    nengo.Connection(prediction, error, synapse=0.01, transform=-1)
    
    # Feed error back to learning rule
    nengo.Connection(error, learn_conn.learning_rule)
    
    # Visualization probes
    state_probe = nengo.Probe(state, synapse=0.01)
    prediction_probe = nengo.Probe(prediction, synapse=0.01)
    error_probe = nengo.Probe(error, synapse=0.01)


