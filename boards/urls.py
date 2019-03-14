from django.urls import path
from . import views


app_name = 'boards'

urlpatterns = [
    path('<int:board_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:board_pk>/comments/', views.comments_create, name='comments_create'),
    # path('<int:pk>/update/', views.update, name='update'),  # GET(EDIT) / POST(UPDATE)
    path('<int:board_pk>/edit/', views.edit, name='edit'),
    path('<int:board_pk>/delete/', views.delete, name='delete'),  # POST로했을 때 delete가 되도록
    path('<int:board_pk>/', views.detail, name='detail'),
    # path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),    # GET으로 들어로면 (NEW) / POST로 들어오면 (CREATE)
    path('', views.index, name='index'),    
    # path('', views.jndex, name='jndex'),    
]