from email.mime import application
from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({
    # (htt-> django views is added by default)
})
