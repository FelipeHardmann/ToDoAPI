from app.views import ToDoViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(f'', ToDoViewSet)
urlpatterns = router.urls

