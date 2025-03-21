# Markov Weather Simulation

A Python project that simulates weather patterns using Markov chains and visualizes the results with matplotlib.

## Overview

This project demonstrates how to model weather transitions using a Markov process. The simulation tracks how weather changes from one state to another based on defined transition probabilities, offering a simple but effective way to model weather patterns over time.

## Features

- Simulates weather transitions between 5 states: sunny, partly cloudy, overcast, rainy, and snowy
- Uses a transition probability matrix to determine weather changes
- Generates and plots a sequence of weather states over a specified number of days
- Visualizes the simulation results using matplotlib

## Requirements

- Python 3.x
- NumPy (imported within code)
- Matplotlib (imported within code)

## How It Works

The program uses a Markov chain to simulate weather changes based on transition probabilities. Each weather state has a probability of transitioning to any other state:

1. Weather states are mapped to indices (0-4)
2. A 5×5 transition matrix defines the probability of moving from one state to another
3. Starting from an initial state, the simulation uses these probabilities to generate a sequence of weather states
4. The resulting sequence is plotted as a time series

## Transition Matrix

The transition probabilities are defined as follows:

| Current State \ Next State | Sunny | Partly Cloudy | Overcast | Rainy | Snowy |
|----------------------------|-------|---------------|----------|-------|-------|
| Sunny                      | 0.5   | 0.4           | 0.1      | 0     | 0     |
| Partly Cloudy              | 0.2   | 0.4           | 0.2      | 0.2   | 0     |
| Overcast                   | 0.1   | 0.3           | 0.2      | 0.4   | 0     |
| Rainy                      | 0     | 0.1           | 0.2      | 0.7   | 0     |
| Snowy                      | 0.1   | 0.3           | 0.3      | 0.1   | 0.2   |

## Usage

Run the script with Python:

```bash
python markov_weather_proj.py
```

The script will:
1. Display the mapping between weather states and their indices
2. Show the generated sequence of weather states for 50 days
3. Open a plot visualizing the weather transitions over time

## Customization

You can modify the code to:
- Change the initial weather state
- Adjust the number of simulation days
- Modify the transition probabilities to model different climate patterns

## Example Output

The script generates a line plot showing weather states over time, with each state represented by its position on the y-axis.

## Future Improvements

Potential enhancements for this project:
- Add seasonal variations to transition probabilities
- Implement temperature modeling alongside weather states
- Create more sophisticated visualization options
- Add input parameters for initial state and simulation length
