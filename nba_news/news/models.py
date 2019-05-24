from django.db import models


class Post(models.Model):

    id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image_url = models.URLField()
    publish_date = models.DateTimeField()
    source_url = models.URLField()
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "post"
