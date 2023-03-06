from django.urls import path

from api.views.gptViews import AdviceAPIView
from api.views.userViews import Register, LoginAPI, LogoutAPI, EditProfileAPI,UserAPIView
from api.views.petViews import PetTypeRUDAPIView, PetTypeCLAPIView, PetRUDAPIView, PetListView, PetCreateAPIView
from api.views.machineViews import MachineListView, MachineRUDAPIView

urlpatterns = [
    # Account Routes
    path('account/register/', Register.as_view()),
    path('account/login/', LoginAPI.as_view()),
    path('account/logout/', LogoutAPI.as_view()),
    path('account/profile/edit', EditProfileAPI.as_view()),
    path('account/user/all',UserAPIView.as_view()),
    # Pet Type Routes
    path('petType/<int:pk>/', PetTypeRUDAPIView.as_view()),
    path('petType/', PetTypeCLAPIView.as_view()),
    # Pet Routes
    path('pet/<int:pk>/', PetRUDAPIView.as_view()),
    path('pet/list', PetListView.as_view()),
    path('pet/', PetCreateAPIView.as_view()),
    # Advice Routes
    path('advice/', AdviceAPIView.as_view()),

    # Nachine Routes
    path('machine/<int:pk>/', MachineRUDAPIView.as_view()),
    path('machine/list', MachineListView.as_view()),
]
