from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import (authenticate, login as dj_login,
                                 logout as dj_logout)
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import (
    DetailView, ListView, TemplateView, CreateView, UpdateView, FormView)
from django.urls import reverse_lazy
from django.conf import settings

from drivingschool import models as m
from drivingschool.decorators import *
from drivingschool.forms import CustomPasswordChangeForm, EditPersonalInfoForm
from drivingschool import mixins
from drivingschool import forms
from drivingschool.utils import gen_report


class LoginView(TemplateView, mixins.ExtraContextMixin):
    form_class = forms.AuthenticationForm
    template_name = 'drivingschool/login.html'
    form = form_class()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect('/admin')
            return redirect('student')
        self.extra_context = {
            'form': self.form,
        }
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.form = self.form_class(request, data=request.POST)
        if self.form.is_valid():
            user = authenticate(request, **self.form.cleaned_data)
            dj_login(request, user)
        return self.get(request)


def logout(request):
    dj_logout(request)
    return redirect('home')


def whoami(request):
    return HttpResponse(str(request.user))


class PasswordUpdateView(UpdateView):
    form_class = CustomPasswordChangeForm
    template_name = 'drivingschool/password_change.html'
    def get_object(x): return x.request.user
    success_url = reverse_lazy('home')


class UserUpdateView(UpdateView):
    form_class = EditPersonalInfoForm
    template_name = 'drivingschool/user_form.html'
    def get_object(x): return x.request.user


class CallApplicationCreateView(CreateView):
    model = m.CallApplication
    fields = ['name', 'phone_number']
    success_url = reverse_lazy('home')


def tutor_view(request):
    return HttpResponse('teacher')


def get_report(request):
    gen_report()
    report_path = (settings.BASE_DIR) / 'table.docx'
    with open(report_path, 'rb') as test_file:
        response = HttpResponse(content=test_file)
    response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    response['Content-Disposition'] = 'attachment; filename=otchet.docx'
    return response


def instructor_view(request):
    return HttpResponse('instructor')


@login_required
def student_view(request):
    return render(request, 'drivingschool/student.html')


class HomeTemplateView(TemplateView, mixins.ExtraContextMixin):
    template_name = 'drivingschool/home.html'
    extra_context = {
        'header_selected_index': 0
    }


class AboutUsTemplateView(TemplateView, mixins.ExtraContextMixin):
    template_name = 'drivingschool/about_us.html'
    extra_context = {
        'header_selected_index': 2
    }


class ContactUsTemplateView(TemplateView, mixins.ExtraContextMixin):
    template_name = 'drivingschool/contact_us.html'
    extra_context = {
        'header_selected_index': 3
    }


class PricingTemplateView(TemplateView, mixins.ExtraContextMixin):
    template_name = 'drivingschool/pricing.html'
    extra_context = {
        'header_selected_index': 1
    }


class GroupListView(ListView, mixins.ExtraContextMixin):
    queryset = m.Group.objects.all()
    extra_context = {
        'header_selected_index': 0
    }


class GroupDetailView(DetailView, mixins.ExtraContextMixin):
    model = m.Group
    extra_context = {
        'header_selected_index': 0
    }


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'drivingschool/user_detail.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'


class SchedulePracticeListView(ListView, mixins.ExtraContextMixin):
    model = m.SchedulePractice
    template_name = 'drivingschool/schedule_practice_list.html'
    extra_context = {
        'header_selected_index': 2
    }


class ScheduleTheoryListView(ListView, mixins.ExtraContextMixin):
    model = m.Group
    template_name = 'drivingschool/schedule_theory_list.html'
    context_object_name = 'groups'
    extra_context = {
        'header_selected_index': 1
    }


class InstructorListView(ListView, mixins.ExtraContextMixin):
    model = m.Instructor
    context_object_name = 'instructors'
    extra_context = {
        'header_selected_index': 3
    }
