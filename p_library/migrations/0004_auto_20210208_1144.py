# Generated by Django 3.1.6 on 2021-02-08 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20210208_0933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='friend_take',
        ),
        migrations.AddField(
            model_name='friend',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='book', to='p_library.book', verbose_name='Книга'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='books', to='p_library.publisher', verbose_name='Издательство'),
        ),
    ]
