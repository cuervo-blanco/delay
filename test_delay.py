import numpy as np
from delay_line import DelayLine


def test_delay_line():
    delay_length = 5
    delay_line = DelayLine(delay_length)
    
    input_signal = np.array([7, 6, 5, 4, 3, 2, 1])
    output_signal = np.zeros_like(input_signal)

    expected_output = np.array([0, 0, 0, 0, 0, 7, 6])  # Delay length = 5

    delay_line.process(input_signal, output_signal)

    assert np.array_equal(output_signal, expected_output), \
        f"Expected {expected_output}, but got {output_signal}"

    print("Test passed!")


if __name__ == "__main__":
    test_delay_line()
