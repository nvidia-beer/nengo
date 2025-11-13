import nengo

# Create a simple Nengo model
model = nengo.Network()

with model:
    # Create an ensemble of 100 neurons, one-dimensional
    a = nengo.Ensemble(100, dimensions=1)
    
    # Node that provides input (you can control with a slider in GUI)
    stimulus = nengo.Node(0)
    
    # Connect the stimulus node to the ensemble
    nengo.Connection(stimulus, a)

