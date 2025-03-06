from django.db import models

class Subject(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def str(self):
        return self.title

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

class TableType(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def str(self):
        return self.title

    class Meta:
        verbose_name = 'Table Type'
        verbose_name_plural = 'Table Types'

class Table(models.Model):
    start_time = models.TimeField()
    finish_time = models.TimeField()
    room = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    type = models.ForeignKey(TableType, on_delete=models.CASCADE, related_name='tables')

    def str(self):
        return f"{self.room} ({self.start_time} - {self.finish_time})"

    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'

class Group(models.Model):
    title = models.CharField(max_length=100)
    worker = models.ForeignKey('app_user.Teacher', on_delete=models.CASCADE, related_name='groups',null=True, blank=True)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='groups')
    active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    table = models.ForeignKey('Table', on_delete=models.SET_NULL, null=True, blank=True, related_name='groups')

    def str(self):
        return self.title

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'