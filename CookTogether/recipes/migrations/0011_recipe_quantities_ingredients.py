# Generated by Django 5.0 on 2023-12-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_alter_recipe_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='quantities_ingredients',
            field=models.TextField(default='sorry'),
            preserve_default=False,
        ),
    ]
