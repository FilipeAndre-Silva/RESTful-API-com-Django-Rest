# Generated by Django 3.2.9 on 2021-12-06 11:55

from django.db import migrations, models
import django.db.models.deletion
import imagens.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('historicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagensHistorico',
            fields=[
                ('id_imagem_historico', models.AutoField(primary_key=True, serialize=False)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to=imagens.models.imagens_historico)),
                ('id_historico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagens', to='historicos.historicos')),
            ],
        ),
    ]
