# Generated by Django 4.2.7 on 2024-01-24 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vyziva', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredients',
            name='quatntity',
        ),
        migrations.AddField(
            model_name='recept',
            name='quatntity',
            field=models.CharField(choices=[('kg', 'kilogramů'), ('g', 'gramů'), ('dkg', 'dekagramů'), ('cup', 'cup'), ('cups', 'cups'), ('ml', 'mililitrů'), ('l', 'litrů'), ('polévková lžíce', 'polévková lžíce'), ('polévkových lžic', 'polévkových lžic'), ('kávová lžička', 'kávová lžička'), ('kávových lžiček', 'kávových lžiček'), ('kusy', 'kusy'), ('kus', 'kus'), ('kusů', 'kusů'), ('špetka', 'špetka'), ('hrst', 'hrst'), ('hrsti', 'hrsti')], default='', max_length=200),
        ),
    ]