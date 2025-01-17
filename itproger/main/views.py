from django.shortcuts import render

def index(request):
    data = {
        'title': 'Գլխավոր էջ',
    }
    return render(request, 'main/index.html', data)


def about(request):
    data = {
        'title': 'Մեր մասին',
    }
    return render(request, 'main/about.html', data)


def contacts(request):
    data = {
        'title': 'Կոնտակտներ',
    }
    return render(request, 'main/contacts.html', data)


