import nengo

# Example showing 2D representation (X and Y coordinates)
model = nengo.Network()

with model:
    # Create a 2D ensemble that can represent two values
    a = nengo.Ensemble(100, dimensions=2)
    
    # Provide two input values (you'll get two sliders in GUI)
    stimulus = nengo.Node([0, 0])
    
    nengo.Connection(stimulus, a)

