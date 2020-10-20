from django_elasticsearch_dsl import DocType, Index
from .models import BlogPost

blogposts = Index('blogposts')


@blogposts.doc_type
class BlogPostDocument(DocType):
    class Meta:
        model = BlogPost

        fields = [
            "title",
            "short_desc",
            "body",
            "tag",
            "id",
            "image",
        ]
