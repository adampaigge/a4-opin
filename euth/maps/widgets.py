from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.forms.widgets import Widget
from django.template import loader
from django.utils.safestring import mark_safe


class MapChoosePolygonWidget(Widget):

    class Media:
        js = (staticfiles_storage.url('leaflet.js'),
              staticfiles_storage.url('leaflet.draw.js'),
              staticfiles_storage.url('js/custom/map_choose_polygon.js')
              )
        css = {'all': [
            staticfiles_storage.url('leaflet.css'),
            staticfiles_storage.url('leaflet.draw.css'),
        ]}

    def render(self, name, value, attrs):

        context = {
            'map_url': settings.BASE_MAP,
            'bbox': settings.MAP_BOUNDING_BOX,
            'name': name,
            'polygon': value
        }

        return mark_safe(
            loader.render_to_string(
                'euth_maps/map_choose_polygon_widget.html',
                context
            )
        )


class MapChoosePointWidget(Widget):

    def __init__(self, polygon, attrs=None):
        self.polygon = polygon
        super().__init__(attrs)

    class Media:
        js = (staticfiles_storage.url('leaflet.js'),
              staticfiles_storage.url('js/custom/map_choose_point.js'),
              )
        css = {'all': [
            staticfiles_storage.url('leaflet.css'),
        ]}

    def render(self, name, value, attrs):

        context = {
            'map_url': settings.BASE_MAP,
            'bbox': settings.MAP_BOUNDING_BOX,
            'name': name,
            'point': value,
            'polygon': self.polygon
        }

        return mark_safe(
            loader.render_to_string(
                'euth_maps/map_choose_point_widget.html',
                context
            )
        )
