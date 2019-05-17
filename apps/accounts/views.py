from django.shortcuts import render,redirect
from django.views.generic.base import View
from apps.accounts.forms import SignupForm
from django.contrib.auth import authenticate,login,logout
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView



# Create your views here.
class SignupFormView(View):
    form= SignupForm()
    template_name="accounts/signup.html"

    def get(self,request):
        print(request.method)
        return render(request,self.template_name, {"form":self.form}) 

    def post(self,request):
        if request.method == "POST":
            #form=SignupForm()
            if self.form.is_valid():
                user = self.form.save(commit=False)
                print(form.cleaned_data)
                username = self.form.cleaned_data["username"]
                raw_password = self.form.cleaned_data["password1"]
                user.save()
                user=authenticate(username=username,password=raw_password)
                if user:
                    login(request,user)
                return redirect("success")

            else:
                print(form.errors)
                return render(request,self.template_name,{"form":form})
        else:
            return render(request,self.template_name,{"form":self.form})    


     
     
     