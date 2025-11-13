# Nengo Examples

Interactive neural network examples for learning the Nengo neural engineering framework.

## Installation

```bash
pip install nengo nengo_gui
```

## Quick Start

Run any example with:
```bash
nengo <filename>.py
```

For remote/container environments:
```bash
nengo <filename>.py -P 8081 -l '*' --unsecure -p "nengo" --no-browser
```

## Repository Structure

### `basic/` - Foundational Examples
- `01_basic_ensemble.py` - Single value representation
- `02_ensemble_with_radius.py` - Value range control
- `03_two_dimensional.py` - Multi-dimensional representation
- `04_computing_square.py` - Function computation (x²)
- `05_multiplication.py` - Nonlinear operations (a × b)
- `06_sine_wave.py` - Time-varying signals
- `07_communication_channel.py` - Information passing
- `08_addition.py` - Addition (a + b)
- `09_subtraction.py` - Subtraction (a - b)

### `nbel/` - Research Applications
- `2020_adaptive_arm_control.py` - Adaptive arm control
- `2021_inverse_kinematics.py` - Inverse kinematics solver
- `2024_adaptive_mpc.py` - Adaptive model predictive control
- `physics_spring.py` - Spring physics simulation

## Resources

- [Nengo Documentation](https://www.nengo.ai/nengo/)
- [Tutorial Videos](https://www.youtube.com/playlist?list=PLX-XEf1yTMrnjFt30RQ7X6k-dfhL1fIGq)
- [Forum](https://forum.nengo.ai/)

