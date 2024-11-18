import pytest
import numpy as np
from sagittal_average import run_averages

data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("brain_sample.csv", data_input, fmt="%d", delimiter=",")

expected_output = np.zeros(20)
expected_output[-1] = 1

run_averages(file_input="brain_sample.csv", file_output="brain_average.csv")

real_output = np.genfromtxt("brain_average.csv", delimiter=",")


def test_equality():
    np.testing.assert_array_equal(real_output, expected_output)
