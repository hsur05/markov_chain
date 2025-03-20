import numpy as np
import matplotlib.pyplot as plt 

def weather_simulation(current_state, days, transition_matrix):
    state = current_state
    weather_history = [state]

    transition_probs = transition_matrix[current_state]

    for day in range(days):
        next_state = np.random.choice(range(0,5), p=transition_probs)

        weather_history.append(next_state)

    return weather_history


#define the states of weather
weather_states = [
    "sunny",
    "partly cloudy",
    "overcast",
    "rainy",
    "snowy"
]

#set an index to the states, create a dictionary
weather_state_to_index = {weather_state : index for index, weather_state in enumerate(weather_states)}
print(weather_state_to_index)

#transition matrix:
transition_matrix = np.array([
    [0.5, 0.4, 0.1, 0, 0], #sunny to s, p, o, r, sn
    [0.2, 0.4, 0.2, 0.2, 0], #partly cloudy to s, p, o, r, sn
    [0.1, 0.3, 0.2, 0.4, 0], #overcast to s, p, o, r, sn
    [0, 0.1, 0.2, 0.7, 0], #rainy to s, p, o, r, sn
    [0.1, 0.3, 0.3, 0.1, 0.2] #snowy to s, p, o, r, sn
])

#now to simulate the weather over days:
#choose current state, get the index, then use random generator to choose next state based on transition matrix probabilities
current_state = weather_state_to_index["snowy"]

transition_probs = transition_matrix[current_state]

next_state = np.random.choice(range(0,5),p=transition_probs)
#print(next_state) # output should print the next weather prediction based on the probability

#run the markov simulation function
weather_list = weather_simulation(current_state, 50, transition_matrix)
print(weather_list)


#plotting using matplotlib
#get x
days = range(len(weather_list))

# Plot the weather simulation
plt.figure(figsize=(10, 5))
plt.plot(days, weather_list, marker='o', linestyle='-', color='b', label="Weather State")

#create y-label
plt.yticks(ticks=range(5), labels=weather_states)

#labels and title
plt.title("Markov Weather Simulation Over 50 Days")
plt.xlabel("Day")
plt.ylabel("Weather")
plt.legend()
plt.grid(True)

#plot
plt.show()
