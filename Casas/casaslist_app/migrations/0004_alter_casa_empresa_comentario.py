# Generated by Django 4.0.3 on 2022-04-01 15:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casaslist_app', '0003_rename_sitioweb_empresa_website_alter_casa_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='empresa',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='casas_list', to='casaslist_app.empresa'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('texto', models.CharField(max_length=250, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('casa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='casaslist_app.casa')),
            ],
        ),
    ]