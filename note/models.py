from django.db.models import Model, CharField, TextField, ForeignKey, DateTimeField, CASCADE


class Category(Model):
    title = CharField(max_length=250)
    created = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title + ' (id=' + str(self.id) + ')'


class Note(Model):
    title = CharField(max_length=250)
    content = TextField(max_length=10000)
    category = ForeignKey(Category, related_name='notes', on_delete=CASCADE)
    created = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'notes'

    def __str__(self):
        return self.title + ' (id=' + str(self.id) + ')'
