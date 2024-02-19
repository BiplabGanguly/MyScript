from django.shortcuts import render,redirect
import openai

openai.api_key = "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"


def home_page(req):
    return render(req,'index.html')

def script_page(req):
    return render(req,'myscript.html')

def post_script_page(req):
    if req.method == "POST":
        title = req.POST['title']
        language = req.POST['language']
        synopsis = req.POST['synopsis']
        genre = req.POST['genre']
        plot = req.POST['plot']

        script = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                    {"role" : "user" , "content" : "create a full script" },
                    {"role" : "user" , "content" :  f"title: {title}"},
                    {"role" : "user" , "content" :  f"language of the script: {language}"},
                    {"role" : "user" , "content" : f"synopsis : {synopsis}" },
                    {"role" : "user" , "content" :  f"gonre : {genre}"},
                    {"role" : "user" , "content" :  f"plot : {plot}"}
            ]
        )
        data = {'content' : script['choices'][0]['message']['content'].strip()}
        return render(req,'myscript.html',data)
    
    return redirect('index')