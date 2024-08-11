from django.urls import path
from .views import index  # import index function from views

# urlpatterns = [
#     path('hello/', views.hello, name='hello'),
# ]

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index, name='index')
]