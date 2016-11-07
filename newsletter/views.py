from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from .models import Article
from django.http import HttpResponse


# Create your views here.
def home(request):
    title = 'Welcome'
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        print(request.POST['email'])
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if not instance.full_name:
            instance.full_name = "New full name"
        instance.save()
        context = {
            "title": "Thank you",
        }

    return render(request, 'home.html', context)


def contact(request):
    title = 'Contact Us'
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key, values in form.cleaned_data.items():
        #     print(key, values)
            # print(form.cleaned_data.get(key))
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        # print(full_name, email, message)
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, '2495894421@qq.com']
        contact_message = "%s: %s via %s"%(
            form_full_name,
            form_message,
            form_email)

        send_email = (subject, contact_message, from_email, to_email)

    context = {
        "form": form,
        "title": title,
        "title_align_center": title_align_center,
    }
    return render(request, "forms.html", context)


def article(request):
    post_list = Article.objects.all()
    context = {
        'post_list': post_list,
    }
    return render(request, 'article.html', context)


def detail(request, article_no):
    post = Article.objects.all()[int(article_no)]
    str = ("title = %s, category = %s, date_time = %s, content = %s" % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)
