#ifndef NEURALNETWORK_H
#define NEURALNETWORK_H

#include <vector>

class NeuralNetwork {
private:
    int hidden_neurons;

    // Activation functions
    double relu(double x);
    double sigmoid(double x);
    int threshold(double x);

public:

    std::vector<std::vector<double>> first_layer_weights;
    std::vector<std::vector<double>> second_layer_weights;

    NeuralNetwork(int input_neurons, int hidden_neurons, int output_neurons);

    std::vector<double> first_layer_values;
    std::vector<double> second_layer_values;
    
    void print_weights();
    void print_second_layer_weights();
    void print_first_layer_values();
    void print_second_layer_values();

    std::vector<double> calculate_first_layer_values(std::vector<double> input_values);
    std::vector<double> calculate_second_layer_values();
    std::vector<double> forward_propagation(std::vector<double> input_values);
};

#endif // NEURALNETWORK_H
