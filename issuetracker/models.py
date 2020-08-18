from django.db import models

# Create your models here.
class IssueModel(models.Model):
    issue_type=[
        ('Ui','UI'),
        ('Functional','Functional'),
        ('DB','DB'),
        ('Other','Others')
    ]
    issue_status=[
        ('Open','Open'),
        ('Closed','Closed'),
        ('TBD','TBD')
        
    ]
    env=[
        ('Production','Production')
    ]
    desc=models.TextField(default=None)
    type=models.CharField(max_length=10,choices=issue_type,default='Functional')
    created_on=models.DateField(default=None)
    created_by=models.CharField(max_length=20,default=None)
    status=models.CharField(max_length=10,choices=issue_status,default='Open')
    logged_by=models.CharField(max_length=20,default=None)
    environment=models.CharField(max_length=20,choices=env,default='Prod')
    def __str__(self):
        return self.desc