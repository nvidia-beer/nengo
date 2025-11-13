"""
Simplified Adaptive Arm Control Network using Nengo
Based on: "Adaptive Control of a Wheelchair Mounted Robotic Arm with 
          Neuromorphically Integrated Velocity Readings and Online-Learning"
Submitted to: Frontiers in Neuroscience (~2020)
By: Michael Ehrlich, Yuval Zaidel, Patrice L. Weiss, Arie Melamed Yekel,
    Naomi Gefen, Lazar Supic, Elishai Ezra Tsur

This example demonstrates adaptive control with online learning using
the Prescribed Error Sensitivity (PES) learning rule to adapt to
unmodeled forces and disturbances in real-time.
"""

import nengo
import numpy as np

# Create the Nengo network
model = nengo.Network(label="Adaptive Arm Control")

with model:
    # Input: joint state (positions and velocities)
    # For a 2-joint arm: [q1, q2, dq1, dq2]
    joint_state = nengo.Node([0, 0, 0, 0])
    
    # Adaptive ensemble: learns to compensate for unmodeled dynamics
    # Uses triangular intercept distribution for better coverage
    # In the paper, they use 1000 neurons per ensemble
    adaptive_ensemble = nengo.Ensemble(
        n_neurons=1000,
        dimensions=4,  # joint positions and velocities
        radius=np.sqrt(4),  # radius scales with dimensionality
        intercepts=nengo.dists.Uniform(0.35, 0.55),
        label="Adaptive Dynamics Compensation"
    )
    
    # Connect joint state to adaptive ensemble
    nengo.Connection(joint_state, adaptive_ensemble, synapse=0.012)
    
    # Output: learned compensation forces for each joint
    compensation_forces = nengo.Node(size_in=2)
    
    # Learning connection: adapts weights based on error signal
    # Uses PES (Prescribed Error Sensitivity) learning rule
    learning_connection = nengo.Connection(
        adaptive_ensemble.neurons,
        compensation_forces,
        transform=np.zeros((2, 1000)),  # Initially zero weights
        learning_rule_type=nengo.PES(learning_rate=1e-6),
        synapse=0.2
    )
    
    # Training signal: error between desired and actual forces
    # In practice, this comes from the difference between 
    # predicted and actual system behavior
    training_signal = nengo.Node([0, 0])
    
    # Connect training signal to learning rule (negative for error correction)
    nengo.Connection(
        training_signal,
        learning_connection.learning_rule,
        transform=-1,
        synapse=0.012
    )
    
    # Probes for monitoring
    state_probe = nengo.Probe(joint_state)
    compensation_probe = nengo.Probe(compensation_forces, synapse=0.01)

print("Network created successfully!")
print("This network adapts to external forces and payload changes online.")
print("The PES learning rule adjusts synaptic weights in real-time to")
print("compensate for unexpected disturbances and model inaccuracies.")
print("In the paper, this was deployed on Intel's Loihi neuromorphic chip.")

