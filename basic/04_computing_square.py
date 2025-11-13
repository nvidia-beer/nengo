import nengo

# Example showing function computation: y = x^2
model = nengo.Network()

with model:
    # First ensemble receives input
    a = nengo.Ensemble(100, dimensions=1)
    stimulus = nengo.Node(0)
    nengo.Connection(stimulus, a)
    
    # Second ensemble computes and represents the square
    b = nengo.Ensemble(100, dimensions=1)
    
    # Connection computes the square function
    nengo.Connection(a, b, function=lambda x: x**2)

