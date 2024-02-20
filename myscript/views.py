from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from script import models
import openai

openai.api_key = "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"


def login_page(req):
    return render(req,'login.html')


def post_login_page(req):
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(username=username, password=password)
    
        if user is not None:
            login(req,user)
            return redirect('index',user.id)
        else:
            return redirect('login')
    return redirect('login')
            



@login_required(login_url='/')
def home_page(req,uid):
    req.session['uid']= uid
    user_details = User.objects.get(id = uid)
    script_content = models.Scripts.objects.filter(user_id = uid , is_delete = False)
    
    data = {'user_details':user_details}
    data['script_content'] = script_content
    return render(req,'index.html',data)

@login_required(login_url='/')
def script_page(req,sid):
    uid  = req.session['uid']
    script_content = models.Scripts.objects.get(id = sid)
    
    user_details = User.objects.get(id = uid)
    data = {'user_details':user_details}
    data['content'] = script_content.script
    return render(req,'myscript.html',data)


@login_required(login_url='/')
def post_script_page(req,uid):
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
        
        content = script['choices'][0]['message']['content'].strip()
        save_script = models.Scripts(title = title, script = content, user_id = uid)
        save_script.save()
        user_details = User.objects.get(id = uid)
        data = {'user_details':user_details}
        data['content'] = content
          
        return render(req,'myscript.html',data)
    return redirect('index',uid)


@login_required(login_url='/')
def delete_script(req,sid):
    uid  = req.session['uid']
    if req.method == "POST":
        models.Scripts.objects.filter(id=sid).update(is_delete = True)
        return redirect('index',uid)
        
        
@login_required(login_url='/')
def log_out(req):
    if req.method == "POST":
        logout(req)
        return redirect('login')