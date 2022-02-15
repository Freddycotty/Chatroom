from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack  #Manejar la session en Django Channels
import chat.routing

application = ProtocolTypeRouter({

    "websocket": AuthMiddlewareStack(  #AUTENTICACION DE RUTAS  
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),

})