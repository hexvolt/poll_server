from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from polls import views


router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'choices', views.ChoiceViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # REST framework urls
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls'))
]
