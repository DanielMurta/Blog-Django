# Generated by Django 4.1.5 on 2023-01-09 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comentarios', '0002_comentario_comentario_comentario_email_comentario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.TextField(null=True, verbose_name='Comentário'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='email_comentario',
            field=models.EmailField(max_length=254, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='nome_comentario',
            field=models.CharField(max_length=150, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='usuario_comentario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
