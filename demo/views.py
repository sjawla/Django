from django.conf import settings
from django.core.mail import send_mail,BadHeaderError
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Movie,Song
from django.template import loader
from django.contrib import auth
from django.views.decorators import csrf
from django.contrib.auth.forms import UserCreationForm
from .forms import MyRegistrationForm,ContactForm
# Create your views here.
def index(request):
	#return HttpResponse("<h1>welcome To my world</h1>") 
	#return render(request,'index.html',{}) 
	'''How to show data on pages of connecting database.
	
	'''
	all_movies=Movie.objects.all()
	for a in all_movies:
		#url='/detail/'+str(a.id)+'/'
	#	html='<a href=" '+url +' ">'+a.actor+'</a></br>','<a href=" '+url +' ">'+a.actor_movie+'</a></br>'
		#html='<a href=" '+url +' ">'+a.actor+'</a>&nbsp&nbsp&nbsp','<a href=" '+url +' ">'+a.actor_movie+'</a>&nbsp&nbsp&nbsp'
		'''
		other method
		template=loader.get_template('index.html')
		'''
		context={
		'all_movies':all_movies,
		}
		#return HttpResponse(template.render(context,request))
		return render(request,'index.html',context)
		#return HttpResponse(html)
def detail(request,movie_id):
	#return HttpResponse("<h1>welcome in id: "+str(movie_id)+"</h1>")
	'''
	on method to get 404 error 
	try:
		m1=Movie.objects.get(pk=movie_id)
	except Movie.DoesNotExist:
		raise Http404("This id in not vaild")
	return HttpResponse("<h1>welcome in id: "+str(movie_id)+"</h1>")	
'''
	m1=get_object_or_404(Movie,pk=movie_id)
	return render(request,'index1.html',{'m1':m1})
def about(request):
	return render(request,'about.html',{})	
	'''how to use template,show data using html page:-
	from django.template import loader
	''' 
def favourite(request,movie_id):
	m1=get_object_or_404(Movie,pk=movie_id)
	try:
		selected_song=m1.song_set.get(pk=request.POST['song'])
	except(KeyError,Song.DoesNotExist):
		return render(request,'index1.html',{'m1':m1,'error_message':"U did not select Song"})
	else:
		selected_song.is_favourite=True
		selected_song.save()
		return render(request,'index1.html',{'m1':m1})		
def login(request):
	c={}
	return render(request,'login.html',c)
def loggedin(request):
	return render(request,'loggedin.html',{'full_name':request.user.username})
def	auth_view(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	user= auth.authenticate(username=username,password=password)
	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/loggedin')
	else:
		return HttpResponseRedirect('/invalid')	
def invalid_login(request):
	return render(request,'invalid_login.html')

def logout(request):
	auth.logout(request)
	return render(request,'logout.html')


def register_user(request):
	if request.method== 'POST':
		form=MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/register_success')

	args={}
	#args.update(csrf(request))

	args['form']=MyRegistrationForm()

	return render(request,'register.html',args)

def register_success(request):
	return render(request,'register_success.html')		

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print email, message, full_name
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, form_email]
		contact_message = "%s: %s via %s"%( 
				form_full_name, 
				form_message, 
				form_email)

		try:
			send_mail(subject,contact_message, from_email, to_email, fail_silently=True)
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
		return redirect('/success')
        #return HttpResponseRedirect('/success')    
	context = {
		"form": form,
	}
		
	return render(request, "forms.html", context)
	

def success(request):
    return render(request,'success.html',{}) 

		