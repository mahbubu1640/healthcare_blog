from django.shortcuts import render,redirect
from django.contrib import messages
from base.models import User,Doctor,Patient,BlogPost
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def Home(request):
    return render(request,'home.html')



def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # print('---user',user)
        if user is not None:
            login(request, user)
            if user.is_patient:
                return redirect('dashboard')
            elif user.is_doctor:
                return redirect('dashboard')
        else:
            messages.warning(request, "Invalid login credentials.")
            return redirect('login')

    return render(request,'login.html')


@login_required
def Dashboard(request):
    return render(request,'dashboard.html')


def Registration(request):
    if request.method=="POST":
        type=request.POST['data']
        if type=='patient':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            profile_picture = request.FILES['profile_picture']
            username = request.POST['user_name']
            email = request.POST['email']
            street = request.POST['street']
            state = request.POST['state']
            pincode = request.POST['pincode']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']

            if password != confirm_password:
               messages.warning(request, "Passwords do not match.")
               return redirect('registration')
               
        
            user = User.objects.create_user(username=username, password=password, email=email,
                                        first_name=first_name, last_name=last_name)
            user.img = profile_picture
            user.Address = street + state + pincode
            user.is_patient=True
            user.save()

            patient_data=Patient(user=user)
            patient_data.save()
            messages.success(request,"Sucessfully register your data!!!")


        else:
            first_name = request.POST['d_first_name']
            last_name = request.POST['d_last_name']
            profile_picture = request.FILES['d_profile_picture']
            username = request.POST['d_username']
            email = request.POST['d_email']
            street = request.POST['d_street']
            state = request.POST['d_state']
            pincode = request.POST['d_pincode']
            password = request.POST['d_password']
            confirm_password = request.POST['d_confirm_password']

            if password != confirm_password:
               messages.warning(request, "Passwords do not match.")
               return redirect('registration')
            
            user = User.objects.create_user(username=username, password=password, email=email,
                                    first_name=first_name, last_name=last_name)
            user.img = profile_picture
            user.Address = street + state + pincode
            user.is_doctor=True
            user.save()

            patient_data=Doctor(user=user)
            patient_data.save()
            messages.success(request,"Sucessfully register your data!!!")
        


    return render(request,'registration.html')



def Logout(request):
    logout(request)
    return redirect('login')



def Blog_post(request):
    if request.method== "POST":
        user=request.user
        title=request.POST['title']
        blog_img = request.FILES.get('blog_img')
        category = request.POST.get('select_category',None)
        summary = request.POST['summary']
        content = request.POST['content']
        draft=request.POST.get('select_category2')
        
        user_data=Doctor.objects.filter(user=user).first()
        
        blog_data_details=BlogPost(created_doctor=user_data,title=title,post_img=blog_img,category=category,summary=summary,content=content,is_draft=draft)
        blog_data_details.save()
        return redirect('dashboard')

    return render(request,'blog.html')



def BlogDetials(request):
    user=request.user
    if user.is_doctor:
        user_data=Doctor.objects.filter(user=user).first()

        blog_details=BlogPost.objects.filter(created_doctor=user_data).all()
        
    else:
        blog_details=BlogPost.objects.filter(is_draft='is_draft').all()
       

    return  render(request,'blogdetails.html',context={'blog_details':blog_details})