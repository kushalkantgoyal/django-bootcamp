# Generated by Django 2.1.3 on 2018-11-15 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0002_game_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('F', 'First Player to Move'), ('S', 'Second Player to Move'), ('W', 'First Player Wins'), ('L', 'Second Player Wins'), ('D', 'Draw')], default='F', max_length=1),
        ),
    ]
