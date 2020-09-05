from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path("",views.userdashboard,name="Index"),
    path("dashboard",views.userdashboard,name="Userdashboard"),
    path("signup/<str:admin>",views.signup,name="signup"),
    path("login",views.login,name="login"),
    path("logout",views.userlogout,name="logout"),
    path("member/register",views.register_member,name="member_register"),
    # path("teacher/register",views.register_teacher,name="teacher_register"),
    path("home",views.home,name="home"),
    path("vault",views.vault,name="vault"),
    path("profile",views.profile,name="profile"),
    path("accept/teacher",views.teacher_accept,name="teacher_accept"),
    path("accept/student",views.student_accept,name="student_accept"),
    path("decline/teacher",views.teacher_decline,name="teacher_decline"),
    path("decline/student",views.student_decline,name="student_declinr"),
    path("chatroom",views.chatroom,name="chatroom"),
    path("chat",views.threads,name="threads"),
    path("generalsetting",views.generalsetting,name="generalsetting"),
    path("securitysetting",views.securitysetting,name="securitysetting"),
    path("contactsetting",views.contactsetting,name="contactsetting"),
    path("setting",views.setting,name="setting"),
    path("contacts",views.contacts,name="contacts"),
    path("editprofile",views.editprofile,name="editprofile"),
    path("editdp",views.editdp,name="editdp"),
    path("editcover",views.editcover,name="editcover"),
    path("post",views.post,name='post'),
    path("achievements/upload",views.achievements,name='achievements'),
    path("chat/<str:id>",views.chat,name='chat'),
    path("savechat",views.savechat,name='chat name'),
    path("delete/achievements/<int:id>",views.deleteachievements,name='deleteachievements'),
    path("viewprofile/S/<str:id>",views.profileForOthers,name='profileForOthers'),
    path("viewprofile/T/<str:id>",views.empprofileForOthers,name='empprofileForOthers'),
    path("review",views.review,name='review'),
    ]