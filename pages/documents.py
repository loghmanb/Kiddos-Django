from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import BlogPost


@registry.register_document
class BlogPostDocument(Document):
    class Index:
        name = 'posts'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = BlogPost

        fields = [
            "title",
            "short_desc",
            "body",
            "tags",
            "id",
            "image",
        ]
