from rest_framework  import routers
from .api import ProveedorViewset, ExpedienteViewset

router = routers.DefaultRouter()

router.register('api/provedor', ProveedorViewset)
router.register('api/expediente', ExpedienteViewset)

urlpatterns = router.urls