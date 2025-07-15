from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, BlogViewSet, SkillViewSet, ContactViewSet, ServiceViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'contact', ContactViewSet, basename='contact')  # 👈 add this
router.register(r'services', ServiceViewSet)

urlpatterns = router.urls
