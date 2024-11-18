import numpy as np

data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("brain_sample.csv", data_input, fmt="%d", delimiter=",")

import test_call_command

expected_output = np.zeros(20)
expected_output[-1] = 1

real_output = np.genfromtxt("brain_average.csv", delimiter=",")
np.testing.assert_array_equal(real_output, expected_output)
