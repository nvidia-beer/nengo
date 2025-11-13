import nengo

# Example showing communication between two ensembles
model = nengo.Network()

with model:
    # First ensemble receives input
    a = nengo.Ensemble(100, dimensions=1)
    stimulus = nengo.Node(0)
    nengo.Connection(stimulus, a)
    
    # Second ensemble receives the same information
    b = nengo.Ensemble(100, dimensions=1)
    
    # Identity connection: b represents the same value as a
    nengo.Connection(a, b)
    
    # Compare the "value" plots of both ensembles - they should match!

