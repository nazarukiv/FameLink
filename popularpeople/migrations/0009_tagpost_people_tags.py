# Generated by Django 5.0.7 on 2024-08-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popularpeople', '0008_alter_people_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='people',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='popularpeople.tagpost'),
        ),
    ]
