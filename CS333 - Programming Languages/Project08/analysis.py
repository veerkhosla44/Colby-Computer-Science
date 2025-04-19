import matplotlib.pyplot as plt

# Sample data for execution times for 5 runs
execution_times = {
    "parallel1": [3.3873, 3.3522, 3.3182, 3.2979, 3.2999],
    "parallel2": [1.1151, 0.7243, 0.8956, 1.1126, 1.1166],
    "parallel3": [0.0035, 0.0041, 0.0049, 0.0042, 0.0034],
    "parallel4": [0.0041, 0.0038, 0.0036, 0.0035, 0.0042],
    "parallel5": [0.0047, 0.0044, 0.0051, 0.0051, 0.0047],
    "parallel6": [0.0100, 0.0097, 0.0093, 0.0090, 0.0092]
}

def calculate_mean_of_middle_three(times):
    times_sorted = sorted(times)
    middle_three = times_sorted[1:4]  # Drops  min and max values
    mean = sum(middle_three) / len(middle_three)
    return mean

mean_execution_times = {program: calculate_mean_of_middle_three(times) for program, times in execution_times.items()}

# Display mean execution times
for program, mean_time in mean_execution_times.items():
    print(f"{program} Mean Execution Time: {mean_time:.4f} seconds")

# Plot  mean execution times
programs = list(mean_execution_times.keys())
mean_times = list(mean_execution_times.values())

plt.figure(figsize=(10, 6))
plt.bar(programs, mean_times, color='skyblue')
plt.xlabel('Program Versions')
plt.ylabel('Mean Execution Time (s)')
plt.title('Mean Execution Time of Different Parallel Implementations')
plt.xticks(rotation=45)
plt.show()
