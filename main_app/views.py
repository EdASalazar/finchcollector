from django.shortcuts import render

finches = [
    {'name': 'Gibson', 'bridge_pickup': 'humbucker'},
    {'name': 'Strat', 'bridge_pickup': 'single coil'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
    'finches': finches
})