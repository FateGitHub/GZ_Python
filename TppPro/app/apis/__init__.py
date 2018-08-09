from app.extensions import api
from .cityApi import CityResource
from .userApi import UserResource
from .activationApi import ActivationResource

api.add_resource(CityResource, '/cities/')
api.add_resource(UserResource, '/user/')
api.add_resource(ActivationResource, '/activation/')
