from django.contrib.auth import get_user_model
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.views import LoginView
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView, TemplateView
from .forms import SignUpForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .token import user_tokenizer
from django.conf import settings
from django.views import View



@login_required
def profile(request):
    user = request.user
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, instance=user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/account/profile/success")
    else:
        form = UpdateProfileForm(instance=user)

    return render(request, "account/profile_update.html", {"form": form})


def profile_success(request):
    return render(request, "account/profile_success.html")


class SiteLoginView(LoginView):
    template_name = "account/login.html"


class SiteSignupView(CreateView):
    USER = get_user_model()

    def get(self, request):
        return render(request, 'account/signup.html', {'form': SignUpForm()})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            token = user_tokenizer.make_token(user)
            user_id = urlsafe_base64_encode(force_bytes(user.id))
            url = 'http://127.0.0.1:8000' + reverse('account:confirm_email', kwargs={'user_id': user_id, 'token': token})
            message = get_template('account/acc_active_email.html').render({
                'confirm_url': url
            })
            mail = EmailMessage('The Movie Center Email Confirmation', message, to=[user.email],
                                from_email=settings.EMAIL_HOST_USER)
            mail.content_subtype = 'html'
            mail.send()

            return render(request, 'account/confirm_email_notification.html')

        return render(request, 'account/signup.html', {'form': form})


class ConfirmSignupView(View):

    def get(self, request, user_id, token):

        User = get_user_model()
        try:
            user_id = force_text(urlsafe_base64_decode(user_id))
            user = User.objects.get(pk=user_id)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and user_tokenizer.check_token(user, token):
            user.is_active = True
            user.save()
            return render(request, 'account/confirm_email_success.html')
        else:
            return HttpResponse('Activation link is invalid!')


class ConfirmEmailNotification(TemplateView):
    template_name = 'account/confirm_email_notification.html'


class ConfirmEmailSuccess(TemplateView):
    template_name =  'account/confirm_email_success.html'


