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
        if term:
            if 'x' in term:
                coef, rest = term.split('x')
                coef = float(coef) if coef else 1.0
                coefficients[0] = coef
            elif 'y' in term:
                coef, rest = term.split('y')
                coef = float(coef) if coef else 1.0
                coefficients[1] = coef
            elif 'z' in term:
                coef, rest = term.split('z')
                coef = float(coef) if coef else 1.0
                coefficients[2] = coef
            else:
                constant = float(term)
    return coefficients, constant


def gauss_jacobi_algorithm(equations, initial_guesses, tolerance=1e-6, max_iterations=100):
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
            print("Equation:", j + 1)
            print("Sum:", sum_)
            print("Coefficient[j][j]:", parsed_equations[j][0][j])
            if parsed_equations[j][0][j] == 0:
                new_x[j] = np.nan  # Handle division by zero
            else:
                new_x[j] = (parsed_equations[j][1] - sum_) / parsed_equations[j][0][j]
            print("New value:", new_x[j])

        # Check convergence
        if np.allclose(new_x, x, atol=tolerance, equal_nan=True):
            break

        x = new_x
        results[i] = x.tolist()

    return results


