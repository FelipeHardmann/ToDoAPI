from django.db import models

class ToDo(models.Model):
    '''
        Referent class for ToDo
        - name
        - done
        - created_at
    '''
    name = models.CharField(max_length=120)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
