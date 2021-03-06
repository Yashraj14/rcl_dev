# Generated by Django 3.0.5 on 2020-05-06 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rcl', '0002_scorecard'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scorecard',
            options={'verbose_name_plural': 'Scorecard'},
        ),
        migrations.AddField(
            model_name='scorecard',
            name='overs_team_2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='scorecard',
            name='runs_team_2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='scorecard',
            name='team_name_2',
            field=models.ForeignKey(db_column='team_name_2', default='hello', on_delete=django.db.models.deletion.CASCADE, related_name='away', to='rcl.Teams'),
        ),
        migrations.AddField(
            model_name='scorecard',
            name='wickets_team_2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='overs_team_1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='runs_team_1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='team_name_1',
            field=models.ForeignKey(db_column='team_name_1', default='hello', on_delete=django.db.models.deletion.CASCADE, related_name='home', to='rcl.Teams'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='wickets_team_1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterModelTable(
            name='scorecard',
            table='Scorecard',
        ),
    ]
