import nengo

# Example showing subtraction: result = a - b
model = nengo.Network()

with model:
    # Two input ensembles
    a = nengo.Ensemble(100, dimensions=1)
    b = nengo.Ensemble(100, dimensions=1)
    
    # Input nodes
    stimulus_a = nengo.Node(0)
    stimulus_b = nengo.Node(0)
    nengo.Connection(stimulus_a, a)
    nengo.Connection(stimulus_b, b)
    
    # Result ensemble
    result = nengo.Ensemble(100, dimensions=1)
    
    # Connect: a adds, b subtracts (using transform=-1)
    nengo.Connection(a, result)
    nengo.Connection(b, result, transform=-1)

