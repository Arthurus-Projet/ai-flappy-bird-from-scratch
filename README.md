# ai-flappy-bird-from-scratch

Genetic algorithms  algorithms that use the principle of natural selection.

We select the best individuals for a given environment, then these individuals reproduce and some of their genes mutate, and we repeat the process.

🐤 Now how to apply it to flappy bird 

Each bird is modeled by a neural network, with 2 input neurons :
- Distance to nearest pipe 
- The vertical distance from the top of the nearest pipe

4 hidden neurons and 1 output neuron with a threshold function : 
- 1 : The bird jumps
- 0 : The bird doesn't jump

🔍 Selection : we will select the birds with the best score (fitness function)

🥚 Reproduction : we will create a new generation of birds by averaging their weight. Average the weights of 2 birds, creating 2 new birds, and repeat the process for all the birds.

🐣 Mutation : randomly modify certain weights

🐥 The new generation is now created, and the process is repeated until the birds never die.

<img width="806" height="1051" alt="image" src="https://github.com/user-attachments/assets/02bb015f-7bf2-4784-b099-6fbd297df75e" />


In this example, we can see that we are in generation 6 with 12 individuals alive.
