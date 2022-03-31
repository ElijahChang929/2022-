function[array] = randomwalk(n);



x_bits = (rand(1,n) <= 0.5);
x_steps = 2 * x_bits - 1;
array = cumsum(x_steps);