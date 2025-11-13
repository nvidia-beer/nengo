"""
Simplified Adaptive Model Predictive Control Network using Nengo
Based on: "Continuous adaptive nonlinear model predictive control using 
          spiking neural networks and real-time learning"
Published in: Neuromorphic Computing and Engineering (IOPScience), 2024
By: Raz Halaly, Elishai Ezra Tsur

This example demonstrates a hybrid MPC system combining:
1. Static predictor (model-based component)
2. Adaptive predictor (learns model errors online)
The system was tested for autonomous driving with up to 96% error reduction.
"""

import nengo
import numpy as np

# Create the Nengo network
model = nengo.Network(label="Adaptive MPC Predictor")

with model:
    # Inputs to the predictor
    # State: vehicle state [px, py, yaw_cos, yaw_sin, vx, vy]
    # Yaw is represented as cos/sin to avoid discontinuities
    vehicle_state = nengo.Node([0, 0, 1.0, 0, 1.0, 0])  # [px, py, yaw_cos, yaw_sin, vx, vy]
    
    # Action: control inputs (steering, throttle)
    control_action = nengo.Node([0, 0])
    
    # --- Static Predictor (Model-Based) ---
    # Uses known bicycle model dynamics
    static_predictor = nengo.Ensemble(
        n_neurons=200,
        dimensions=8,  # state (6) + action (2)
        radius=np.sqrt(8),
        label="Static Model-Based Predictor"
    )
    
    # Connect inputs to static predictor
    nengo.Connection(control_action, static_predictor[:2], synapse=None)
    nengo.Connection(vehicle_state, static_predictor[2:], synapse=None)
    
    # --- Adaptive Predictor (Learning-Based) ---
    # Learns to correct model errors in real-time
    adaptive_predictor = nengo.Ensemble(
        n_neurons=1000,  # Paper uses 5 to 5000 neurons
        dimensions=8,  # state (6) + action (2)
        radius=np.sqrt(8),
        label="Adaptive Error Predictor"
    )
    
    # Connect inputs to adaptive predictor
    nengo.Connection(control_action, adaptive_predictor[:2], synapse=None)
    nengo.Connection(vehicle_state, adaptive_predictor[2:], synapse=None)
    
    # --- Predicted Dynamics Output ---
    # Combines both predictors: [px, py, yaw_cos, yaw_sin, vx, vy]
    predicted_dynamics = nengo.Node(size_in=6, label="Next State Prediction")
    
    # Static predictor connection (uses bicycle model)
    def bicycle_model(x):
        """Simplified bicycle model for vehicle dynamics"""
        steering = x[0]
        throttle = x[1]
        px, py, yaw_cos, yaw_sin, vx, vy = x[2], x[3], x[4], x[5], x[6], x[7]
        
        # Simplified next state prediction
        dt = 0.1
        yaw = np.arctan2(yaw_sin, yaw_cos)  # Reconstruct yaw angle
        
        # Bicycle model dynamics
        next_px = px + vx * np.cos(yaw) * dt - vy * np.sin(yaw) * dt
        next_py = py + vx * np.sin(yaw) * dt + vy * np.cos(yaw) * dt
        next_yaw = yaw + steering * vx * dt  # Simplified steering dynamics
        next_vx = vx + throttle * dt
        next_vy = vy
        
        return [next_px, next_py, np.cos(next_yaw), np.sin(next_yaw), next_vx, next_vy]
    
    nengo.Connection(
        static_predictor,
        predicted_dynamics,
        function=bicycle_model,
        synapse=0.05
    )
    
    # Adaptive predictor connection with PES learning
    adaptive_connection = nengo.Connection(
        adaptive_predictor,
        predicted_dynamics,
        function=lambda x: [0, 0, 0, 0, 0, 0],  # Initially zero (6D output)
        learning_rule_type=nengo.PES(learning_rate=1e-4),
        synapse=0.05
    )
    
    # Dynamics error signal for training
    # In practice: actual_next_state - predicted_dynamics
    dynamics_error = nengo.Node([0, 0, 0, 0, 0, 0])
    
    # Connect error to learning rule
    nengo.Connection(
        dynamics_error,
        adaptive_connection.learning_rule,
        synapse=None
    )
    
    # Probes for monitoring
    state_probe = nengo.Probe(vehicle_state)
    prediction_probe = nengo.Probe(predicted_dynamics, synapse=0.01)

print("Network created successfully!")
print("This hybrid MPC predictor combines model-based and learning-based approaches.")
print("The static predictor uses known dynamics (bicycle model),")
print("while the adaptive predictor learns to correct model errors online.")
print("In the paper, this achieved up to 96.08% median prediction error reduction")
print("in autonomous driving scenarios with vehicle malfunctions.")

