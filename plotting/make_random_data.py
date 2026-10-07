import numpy as np

# Create x array of size 20 from 1 to 6
x = np.linspace(1, 6, 20)

# Create random y array from [0, 1] of size 20
y = np.random.rand(20)

# Save both arrays into a single .npy file as a tuple/dictionary or stacked array
with open("random_data.npy", "wb") as f:
    np.save(f, x)
    np.save(f, y)

print("Data successfully saved to random_data.npy")
