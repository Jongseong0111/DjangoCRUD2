# Generated by Django 3.2.5 on 2021-07-20 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20210720_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(related_name='actors', to='movies.Movie'),
        ),
        migrations.DeleteModel(
            name='ActorMovie',
        ),
    ]
