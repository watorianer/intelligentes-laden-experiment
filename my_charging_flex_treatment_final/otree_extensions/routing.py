from channels.routing import route_class
from .consumer import IndexTracker


channel_routing = [route_class(IndexTracker, path=IndexTracker.url_pattern)]