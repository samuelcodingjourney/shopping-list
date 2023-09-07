from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Gregorius Samuel Hutahaean',
        'class': 'PBP KKI'
    }

    return render(request, 'main.html', context)
