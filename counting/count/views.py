from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
# Create your views here.

def result(request):                        
    text=request.GET['fulltext']
    splitted_text=text.split()
    word_len = len(splitted_text)
    list_word=[]
    a={}
    
    for i in splitted_text:
        a[i] =splitted_text.count(i)
    
    
    return render(request, 'result.html',{
        'word_len':word_len,
        'text':text,
        'a':a,
    })