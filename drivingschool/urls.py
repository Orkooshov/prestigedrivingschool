from django.urls import path

from drivingschool import views as v


urlpatterns = [
    path('', v.HomeTemplateView.as_view(), name='home'),
    path('login/', v.LoginView.as_view(), name='login'),
    path('logout/', v.logout, name='logout'),
    path('whoami/', v.whoami),
    path('student/', v.student_view, name='student'),
    path('instructor/', v.instructor_view, name='instructor'),
    path('tutor/', v.tutor_view, name='tutor'),
    path('about/', v.AboutUsTemplateView.as_view(), name='about_us'),
    path('contact/', v.ContactUsTemplateView.as_view(), name='contact_us'),
    path('pricing/', v.PricingTemplateView.as_view(), name='pricing'),
    path('call-application/', v.CallApplicationCreateView.as_view(),
         name='call_application'),
    path('group/<int:pk>/', v.GroupDetailView.as_view(), name='group_detail'),
    path('groups/', v.GroupListView.as_view(), name='group_list'),
    path('user/<slug:username>/', v.UserDetailView.as_view(), name='user_detail'),
    path('schedule-theory/', v.ScheduleTheoryListView.as_view(),
         name='schedule_theory_list'),
    path('schedule-practice/', v.SchedulePracticeListView.as_view(),
         name='schedule_practice_list'),
    path('instructors/', v.InstructorListView.as_view(), name='instructor_list'),
    path('user-edit/', v.UserUpdateView.as_view(), name='user_edit'),
    path('password-change/', v.PasswordUpdateView.as_view(), name='password_change'),
    path('report-theory/', v.get_report, name='report_theory')
]
