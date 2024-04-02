# views.py

from django.shortcuts import render
from .forms import GaussJacobiForm
from .gauss import gauss_jacobi_algorithm

def index(request):
    if request.method == 'POST':
        form = GaussJacobiForm(request.POST)
        if form.is_valid():
            equations = form.cleaned_data['equations']
            initial_guesses_str = form.cleaned_data['initial_guesses']
            iterations = form.cleaned_data['iterations']

            # Convert initial guess values from string to list of floats
            initial_guesses_list = [float(x.strip()) for x in initial_guesses_str.split(',')]

            results = gauss_jacobi_algorithm(equations, initial_guesses_list, iterations)

            return render(request, 'jacobi/result.html', {'results': results})
    else:
        form = GaussJacobiForm()
    return render(request, 'jacobi/index.html', {'form': form})
