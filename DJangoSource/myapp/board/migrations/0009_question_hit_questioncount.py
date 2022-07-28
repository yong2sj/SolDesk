# Generated by Django 4.0.6 on 2022-07-28 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_answer_voter_alter_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='hit',
            field=models.BigIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='QuestionCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.question')),
            ],
        ),
    ]