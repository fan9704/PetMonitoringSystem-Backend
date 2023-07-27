from django.urls import path

from api.views.firebaseViews import FcmTokenAPI
from api.views.gptViews import AdviceAPIView
from api.views.loginViews import LoginView
from api.views.userViews import Register, LogoutAPI, EditProfileAPI, UserAPIView, OAuthUserRegisterAPI, \
    OAuthUserLoginAPI
from api.views.petViews import PetTypeRUDAPIView, PetTypeCLAPIView, PetRUDAPIView, PetListView, PetCreateAPIView, \
    PetQueryListView, PetCountAPIView, PetUploadImageAPIView
from api.views.machineViews import MachineListView, MachineRUDAPIView
from api.views.recordViews import RecordTypeListView, RecordByRecordType, RecordListCreateView, RecordRUDAPIView

urlpatterns = [
    # Account Routes
    path('account/register/', Register.as_view(), name='account-register'),
    path('account/login/', LoginView.as_view(), name='account-login'),
    path('account/logout/', LogoutAPI.as_view(), name='account-logout'),
    path('account/profile/edit/', EditProfileAPI.as_view(), name='account-profile-edit'),
    path('account/user/all/', UserAPIView.as_view(), name='account-list'),
    # OAuth Routes
    path('account/oauth/register/', OAuthUserRegisterAPI.as_view(), name='account-oauth-register'),
    path('account/oauth/login/', OAuthUserLoginAPI.as_view(), name='account-oauth-login'),
    # Pet Type Routes
    path('petType/<int:pk>/', PetTypeRUDAPIView.as_view(), name="petType-rud"),
    path('petType/', PetTypeCLAPIView.as_view(), name="petType-create-list"),
    # Pet Routes
    path('pet/<int:pk>/', PetRUDAPIView.as_view(), name='pet-rud'),
    path('pet/list/', PetListView.as_view(), name='pet-list'),
    path('pet/list/<str:pet_type>/', PetQueryListView.as_view(), name='pet-listByType'),
    path('pet/', PetCreateAPIView.as_view(), name="pet-create"),
    path('pet/count/petType/', PetCountAPIView.as_view(), name="pet-count"),
    path('pet/image/<int:pk>/', PetUploadImageAPIView.as_view(), name="pet-upload-image"),
    # Advice Routes
    path('advice/', AdviceAPIView.as_view(), name='advice'),
    # Machine Routes
    path('machine/<int:pk>/', MachineRUDAPIView.as_view(), name='machine-rud'),
    path('machine/list/', MachineListView.as_view(), name='machine-list'),
    # RecordType Routes
    path('recordType/list/', RecordTypeListView.as_view(), name="recordType-list"),
    # Record Routes
    path('record/', RecordListCreateView.as_view(), name='record-create-list'),
    path('record/<int:pk>/', RecordRUDAPIView.as_view(), name='record-retrieve-update-delete'),
    path('record/<str:record_type>/', RecordByRecordType.as_view({'get': 'recordType'}), name="recordType"),
    path('record/<str:record_type>/<str:pet_name>/', RecordByRecordType.as_view({'get': 'recordTypeAndPetName'}),
         name="record-listByRecordTypeAndPetName"),
    # Fcm Token Routes
    path('FcmToken/user/', FcmTokenAPI.as_view())
]
