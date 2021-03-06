# Generated by Django 3.0 on 2021-01-23 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VisitedEvolutionChains',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_on', models.DateTimeField(auto_now=True, help_text='updated date', verbose_name='updated date')),
            ],
            options={
                'verbose_name': 'visited evolution chain',
                'verbose_name_plural': 'visited evolution chains',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='species name', max_length=50, verbose_name='name')),
                ('evolves_from', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pokemon.Species')),
            ],
            options={
                'verbose_name': 'species',
                'verbose_name_plural': 'species',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='pokemon name', max_length=50, verbose_name='name')),
                ('height', models.IntegerField(help_text='height', verbose_name='height')),
                ('weight', models.IntegerField(help_text='weight', verbose_name='weight')),
                ('hp', models.IntegerField(help_text='hp', verbose_name='hp')),
                ('attack', models.IntegerField(help_text='attack', verbose_name='attack')),
                ('defense', models.IntegerField(help_text='defense', verbose_name='defense')),
                ('special_attack', models.IntegerField(help_text='special attack', verbose_name='special attack')),
                ('special_defense', models.IntegerField(help_text='special defense', verbose_name='special defense')),
                ('speed', models.IntegerField(help_text='speed', verbose_name='speed')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pokemon.Species')),
            ],
            options={
                'verbose_name': 'pokemon',
                'verbose_name_plural': 'pokemons',
                'ordering': ['id'],
            },
        ),
    ]
