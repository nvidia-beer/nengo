import nengo

# Example showing how to change the value range using radius
model = nengo.Network()

with model:
    # Ensemble with radius=2 can represent values between -2 and 2
    # (default is -1 to 1)
    a = nengo.Ensemble(100, dimensions=1, radius=2)
    
    # Input node - try values between -2 and 2
    stimulus = nengo.Node(0)
    nengo.Connection(stimulus, a)

