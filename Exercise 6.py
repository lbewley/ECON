import numpy as np
import matplotlib.pyplot as plt

alphas = [0.0, 0.8, 0.9]
ts_length = 200

for alpha in alphas:
    x_values = []
    current_x = 0
    for i in range(ts_length + 1):
        x_values.append(current_x)
        current_x = alpha * current_x + np.random.randn()
    plt.plot(x_values, label='alpha = ' + str(alpha))
plt.legend()
plt.show()