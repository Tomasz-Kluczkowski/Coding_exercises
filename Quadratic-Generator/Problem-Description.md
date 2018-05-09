# Is an array Madvah array?

Quadratic equations come in the form y = ax^2 + bx + c. Substituting in different values of x gives us multiple coordinates/points on the graph of that quadratic.

Task:
Your job is to create a method called quadratic_enum (quadratic_gen in Python) that does the following:

Takes in three required parameters: a, b, and c, and two keyword/optional parameters, start and step. If start is not provided, it should be set as default to 0, and if step is not provided, its default value should be 1.
It should return an enumerator in Ruby/generator in Python which is dynamic and created based on the arguments taken in.
What the enumerator/generator must do:
Essentially, the method you write should return an enumerator/generator which, when called, should start by yielding [start, a(start)^2 + b(start) + c], where a, b, and c, are provided when the method was called. Then start should be incremented by step and continue the sequence.

Examples:
gen = quadratic_gen(1, 0, 0) # this is the equation of y = x^2
[next(gen) for _ in range(10)] # gives us [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]

gen = quadratic_gen(1, 0, 0, start= 2) # same equation, but with a different start point
[next(gen) for _ in range(10)] # gives us [[2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81], [10, 100], [11, 121]]

gen = quadratic_gen(1, 0, 0, step= 2) # same equation, with a new step value
[next(gen) for _ in range(10)] # gives us [[0, 0], [2, 4], [4, 16], [6, 36], [8, 64], [10, 100], [12, 144], [14, 196], [16, 256], [18, 324]]

gen = quadratic_gen(1, 0, 0, step= -1) # same equation, but tracing backwards
[next(gen) for _ in range(10)] # gives us [[0, 0], [-1, 1], [-2, 4], [-3, 9], [-4, 16], [-5, 25], [-6, 36], [-7, 49], [-8, 64], [-9, 81]]

gen = quadratic_gen(1, 0, 0, step= 0.5) # same equation, but step is now a float
[next(gen) for _ in range(10)] # gives us [[0, 0], [0.5, 0.25], [1.0, 1.0], [1.5, 2.25], [2.0, 4.0], [2.5, 6.25], [3.0, 9.0], [3.5, 12.25], [4.0, 16.0], [4.5, 20.25]]
The tests call Enumerable#take and Enumerable#next in Ruby, and next() in Python. Solutions are rounded to 6 decimal places to prevent rounding errors from causing problems. ```


#Looking for:
generator function quadratic_gen

#Specification:
- yield items calculating y coordinate of quadratic equation.
- input: a, b, c parameters for the equation
- input: start - starting x, optional, default 0
- input: step - interval for calculation, optional, default 1

- output: yields [x, y]

#Initial thoughts:
- check list length and eliminate those that cannot be Madvah Arrays due to incorrect length (they have too many / not enough items).
- make sure empty or single item list is rejected straight away.