import nengo

# Model that multiplies two inputs
model = nengo.Network()

with model:
    # Two input ensembles
    a = nengo.Ensemble(100, dimensions=1)
    b = nengo.Ensemble(100, dimensions=1)
    
    # Input nodes (control these with sliders in GUI)
    stimulus_a = nengo.Node(0)
    stimulus_b = nengo.Node(0)
    nengo.Connection(stimulus_a, a)
    nengo.Connection(stimulus_b, b)
    
    # Combine both in a 2D ensemble
    c = nengo.Ensemble(200, dimensions=2)
    nengo.Connection(a, c[0])
    nengo.Connection(b, c[1])
    
    # Decode the product in a final ensemble
    product = nengo.Ensemble(100, dimensions=1)
    nengo.Connection(c, product, function=lambda x: x[0] * x[1])

