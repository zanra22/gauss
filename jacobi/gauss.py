import numpy as np

def parse_equation(equation, num_variables):
    # Split the equation into coefficients and constant
    parts = equation.split("=")
    constant = float(parts[1])

    # Extract coefficients
    coefficients = [0.0] * num_variables
    terms = parts[0].replace('-', '+-').split('+')  # Split by '+' and replace '-' with '+-'
    for term in terms:
        term = term.strip()  # Remove leading/trailing whitespaces
        variable_index = term.find('x') if 'x' in term else (term.find('y') if 'y' in term else term.find('z'))
        if variable_index != -1:
            coef = term[:variable_index]
            if coef:
                variable_char = term[variable_index]
                variable_index = ord(variable_char) - ord('x')
                if coef == '-' or coef == '':
                    coefficients[variable_index] = -1.0  # Handle negative coefficient or implicit 1
                else:
                    coefficients[variable_index] = float(coef)
            else:
                coefficients[variable_index] = 1.0  # Handle implicit coefficient 1
        else:
            constant = float(term)  # Handle terms without variables

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

    # Initialize x with the initial guess
    x = np.array(initial_guesses)

    results = {}
    results[0] = x.tolist()

    for i in range(1, max_iterations + 1):
        new_x = np.zeros(num_variables)

        print("results", results[i-1])
        for j in range(num_variables):

            sum_ = parsed_equations[j][1]  # Include the constant term
            # print(sum_)
            for k in range(num_variables):
                # print(sum_)

                if k != j:

                    print(parsed_equations[j][0])
                    sum_ -= parsed_equations[j][0][k] * x[k]# Use the updated x values from the previous iteration
            if parsed_equations[j][0][j] == 0:
                new_x[j] = np.nan  # Handle division by zero
                x = new_x.copy()
            else:
                new_x[j] = sum_ / parsed_equations[j][0][j]

        print("new_x", new_x.copy())
        # Update x with the new values
        x = new_x.copy()
        results[i] = x.tolist()

    return results


