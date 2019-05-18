"""
Source:
https://natureofcode.com/book/chapter-10-neural-networks/
"""

import random


class Perceptron:
    """
    A perceptron is the simplest type of a neural network:
    A single node.
    Given two inputs x1 and x2, the preceptron outputs a value, depending on the weighting.
    """

    def __init__(self, nx=2, bias=0, c=0.01):
        """
        Create the preceptron.
        Parameters:
        nx = Number of inputs, standard is 2. One will be added as bias
        bias = Bias input starting value, standard value is 0, might change with evolution
        c = learning speed, default is 0.01
        """
        self.num_inputs = nx
        self.weights = []
        for _ in range(self.num_inputs):
            self.weights.append(random.randint(-1, 1))
        # bias gives a usefull output when all inputs are 0
        self.weights.append(bias)
        self.learning_rate = c

    def activate(self, result):
        """
        Activation function is simply: is it greater or smaller than 0?
        """
        if result > 0:
            return 1
        else:
            return -1

    def feedforward(self, inputs):
        """
        Processes the inputs and returns a single output
        """
        processsum = 0
        for i in range(len(inputs)):
            processsum = processsum + inputs[i] * self.weights[i]
        return self.activate(processsum)

    def train(self, inputs, desired):
        """
        Gets output for given input.
        Then compares to desired result.
        Adjusts weights if neccessary.
        """
        inputs.append(1)  # bias input
        guess = self.feedforward(inputs)
        error = desired - guess
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + \
                self.learning_rate * error * inputs[i]

    def debug_weights(self):
        """
        This debug function returns all current weights.
        """
        return self.weights

# this is purely test code:


if __name__ == '__main__':
    print("Example training code...")
    PTRON = Perceptron(2)
    x_pos = random.random() * 20 - 10
    y_pos = random.random() * 20 - 10
    test_inptus = [x_pos, y_pos]
    test_answer = 1
    if y_pos < 2*x_pos + 1:
        test_answer = -1
    PTRON.train(test_inptus, test_answer)
