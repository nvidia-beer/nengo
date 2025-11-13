# Nengo Tutorial Examples

Interactive neural network examples based on the [Nengo Tutorial Video Series](https://www.youtube.com/watch?v=8TenlRW6TZg&list=PLX-XEf1yTMrnjFt30RQ7X6k-dfhL1fIGq).

## Installation

```bash
pip install nengo
pip install nengo_gui
```

## How to Run the Examples

### Start Nengo GUI

To run any example, use the command:

```bash
nengo <filename>.py
```

For example:
```bash
nengo 01_basic_ensemble.py
```

### For Remote/Container Environments

If you're running in a container, Codespace, or remote environment:

```bash
nengo <filename>.py -P 8081 -l '*' --unsecure -p "nengo" --no-browser
```

Then:
1. Forward port 8081 in your IDE
2. Open `http://localhost:8081` in your browser
3. Enter password: `nengo`

## Using the GUI

Once the GUI is open:

### 1. Add Input Controls
- **Right-click** on a **stimulus node** (small circle)
- Select **"slider"** to add an interactive slider

### 2. Visualize Neural Activity
- **Right-click** on an **ensemble** (larger circle)
- Choose visualization:
  - **"value"** - Decoded output (what neurons represent)
  - **"spikes"** - Individual neuron spike rasters
  - **"firing pattern"** - Neuron tuning curves
  - **"voltages"** - Membrane voltages

### 3. Run the Simulation
- Click the **▶ (play) button** at the bottom
- Move sliders to change inputs in real-time
- Watch how neurons respond!

## Examples Overview

### 01_basic_ensemble.py
**Concept:** Basic neural ensemble

A simple group of 100 neurons representing a single value.
- Add a slider to the stimulus node
- View the value plot to see what the neurons represent
- View spikes to see individual neuron firing

---

### 02_ensemble_with_radius.py
**Concept:** Controlling value ranges

Shows how to change the range of values neurons can represent using `radius`.
- Default radius is 1 (represents -1 to 1)
- This example uses radius=2 (represents -2 to 2)
- Try slider values outside the range to see degradation

---

### 03_two_dimensional.py
**Concept:** Multi-dimensional representation

Neurons can represent multiple values simultaneously.
- This ensemble represents 2D coordinates (X, Y)
- You'll get two sliders in the GUI
- View the "value" plot to see both dimensions

---

### 04_computing_square.py
**Concept:** Function computation (y = x²)

Neural networks can compute mathematical functions.
- Ensemble `a` receives input
- Ensemble `b` computes and represents x²
- Compare value plots: b should show the square of a

---

### 05_multiplication.py
**Concept:** Computing products (a × b)

Demonstrates how to multiply two numbers using neurons.
- Two input ensembles (a and b)
- Combined in a 2D ensemble (c)
- Product decoded in final ensemble
- This is a key nonlinear operation!

---

### 06_sine_wave.py
**Concept:** Time-varying inputs

Shows how neurons track dynamic signals over time.
- Stimulus generates a sine wave automatically
- No slider needed - just press play!
- Watch neurons encode the changing signal

---

### 07_communication_channel.py
**Concept:** Information passing

Demonstrates how ensembles can pass information between each other.
- Ensemble `a` receives input
- Ensemble `b` receives the same information from `a`
- Compare their "value" plots - they should match!

---

### 08_addition.py
**Concept:** Addition (a + b)

Shows how to add two numbers using neural networks.
- Two input ensembles with sliders
- Result ensemble shows the sum
- Multiple connections to the same ensemble add by default

---

### 09_subtraction.py
**Concept:** Subtraction (a - b)

Demonstrates subtraction using connection transforms.
- Similar to addition
- Uses `transform=-1` to negate the second input
- Result shows a - b

---

## Tips for Exploration

1. **Start with 01_basic_ensemble.py** to get familiar with the GUI
2. **Increase neuron count** in the code (e.g., change 100 to 200) for better accuracy
3. **Try different functions** in computation examples (e.g., `x**3`, `np.sin(x)`)
4. **Compare ensembles** by viewing the same plot type for multiple ensembles
5. **Pause and step** through simulations using GUI controls

## Key Concepts

- **Ensemble**: A group of neurons that represents values
- **Node**: Input or output to the network
- **Connection**: Links between components (can compute functions)
- **Dimensions**: Number of values an ensemble represents
- **Radius**: Range of values an ensemble can represent
- **Function**: Transformation applied in a connection
- **Transform**: Linear scaling applied to connections

## Troubleshooting

### Port Already in Use
If you see "Address already in use", either:
1. Kill the existing process: `pkill -f nengo`
2. Use a different port: `nengo file.py -P 8082`

### GUI Not Loading
- Make sure port is forwarded in your IDE
- Check the terminal for any error messages
- Try accessing `http://localhost:PORT` directly

### Password Required
If you started with `-p "nengo"`, use password: `nengo`

To disable password (local only):
```bash
nengo file.py -p ""
```

## Next Steps

After working through these examples:

1. **Modify the examples** - Change neuron counts, dimensions, functions
2. **Combine concepts** - Build more complex models
3. **Explore dynamics** - Add feedback connections for memory
4. **Try different neuron types** - Use `neuron_type` parameter
5. **Visit [nengo.ai](https://www.nengo.ai)** for advanced tutorials

## Resources

- **Official Documentation**: https://www.nengo.ai/nengo/
- **Tutorial Videos**: https://www.youtube.com/playlist?list=PLX-XEf1yTMrnjFt30RQ7X6k-dfhL1fIGq
- **Forum**: https://forum.nengo.ai/
- **Examples**: https://www.nengo.ai/nengo/examples.html

---

**Have fun exploring neural computation!** 🧠✨

