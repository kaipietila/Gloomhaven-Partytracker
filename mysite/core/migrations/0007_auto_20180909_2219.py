# Generated by Django 2.1.1 on 2018-09-09 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180909_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brute',
            name='party',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Party'),
        ),
        migrations.AlterField(
            model_name='cragheart',
            name='party',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Party'),
        ),
        migrations.AlterField(
            model_name='mindthief',
            name='party',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Party'),
        ),
        migrations.AlterField(
            model_name='paladin',
            name='party',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Party'),
        ),
        migrations.AlterField(
            model_name='scoundrel',
            name='party',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Party'),
        ),
        migrations.AlterField(
            model_name='tinkerer',
            name='party',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Party'),
        ),
    ]
