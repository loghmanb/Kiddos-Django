from django.template import Origin, TemplateDoesNotExist
from django.template.loaders.base import Loader as BaseLoader

from pages.models import ElementTemplate

class Loader(BaseLoader):
    def get_template_sources(self, template_name):
        yield Origin(
            name=template_name,
            template_name=template_name,
            loader=self)

    def get_contents(self, origin):
        try:
            element_template = ElementTemplate.objects.get(name=origin.template_name)
            return element_template.structure
        except ElementTemplate.DoesNotExist:
            raise TemplateDoesNotExist(origin)