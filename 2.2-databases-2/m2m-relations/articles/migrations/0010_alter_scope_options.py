# Generated by Django 5.1 on 2024-08-24 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_rename_scopes_article_tags_alter_scope_article_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['-is_main'], 'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статьи'},
        ),
    ]
