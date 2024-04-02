# gauss_jacobi/gauss_jacobi.py

import numpy as np

def parse_equation(equation, num_variables):
    # Split the equation into coefficients and constant
    parts = equation.split("=")
    constant = float(parts[1])

    # Extract coefficients
    coefficients = [0.0] * num_variables
    terms = parts[0].split("+")
    for term in terms:
        term = term.strip()  # Remove leading/trailing whitespaces
        variable_index = term.find('x') if 'x' in term else (term.find('y') if 'y' in term else term.find('z'))
        if variable_index != -1:
            coef = term[:variable_index]
            if coef:
                coefficients[ord(term[variable_index]) - ord('x')] = float(coef)
        else:
            constant = float(term)

    return coefficients, constant






def gauss_jacobi_algorithm(equations, initial_guesses, max_iterations=100):
    # Parse equations and initial guesses
    parsed_equations = []
    variables = set()
    for eq in equations.strip().split('\n'):
        terms = eq.split("=")[0].split("+")
        for term in terms:
            variable = term.strip()[-1]
            variables.add(variable)
    num_variables = len(variables)
    # Parse equations and initial guesses
    parsed_equations = [parse_equation(eq, num_variables) for eq in equations.strip().split('\n')]

    # Convert initial guesses to list of floats if necessary
    if isinstance(initial_guesses, str):
        initial_guesses = [float(x) for x in initial_guesses.split()]

    # Extract number of variables
    results = {}
    x = np.array(initial_guesses)
    results[0] = x.tolist()

    for i in range(1, max_iterations + 1):
        new_x = np.zeros(num_variables)
        for j in range(num_variables):
            sum_ = 0
            for k in range(num_variables):
                if k != j:
                    sum_ += parsed_equations[j][0][k] * x[k]
            if parsed_equations[j][0][j] == 0:
                new_x[j] = np.nan  # Handle division by zero
            else:
                new_x[j] = (parsed_equations[j][1] - sum_) / parsed_equations[j][0][j]

        print("Iteration:", i)
        print("Equations:", parsed_equations)
        print("Current X:", x)
        print("New X:", new_x)

        x = new_x
        results[i] = x.tolist()

    return results









