import nengo
import numpy as np

# Example with time-varying input (sine wave)
model = nengo.Network()

with model:
    # Create an ensemble
    a = nengo.Ensemble(100, dimensions=1)
    
    # Create a time-varying input (sine wave)
    stimulus = nengo.Node(lambda t: np.sin(2 * np.pi * t))
    nengo.Connection(stimulus, a)
    
    # You can visualize how neurons track the sine wave over time

