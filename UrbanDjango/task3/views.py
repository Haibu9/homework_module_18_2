from django.shortcuts import render

# Create your views here.

def main_(request):
    return render(request, 'third_task/main_page.html')

def page_2(request):
    text1 = "Что-нибудь"
    text1_1 = "Что?"
    context = {
        'line_1': text1,
        'respond_1': text1_1
    }
    return render(request, 'third_task/page2.html', context)

def page_3(request):
    return render(request, 'third_task/page3.html')