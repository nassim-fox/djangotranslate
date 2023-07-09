from django.urls import path, include
from proA import views as aviews
from pro import views

urlpatterns = [
    path('', aviews.index, name='proA'),
      path('i18n/', include('django.conf.urls.i18n')), 
      path('language/activate/<language_code>/', views.ActivateLanguageView.as_view(), name='activate_language'),
]