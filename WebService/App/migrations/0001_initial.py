# Generated by Django 2.1a1 on 2018-06-29 19:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
	    migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
	        name='Friendship',
	        fields=[
		        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
		        ('Friend', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Friend', to=settings.AUTH_USER_MODEL)),
		        ('User', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
	        ],
        ),
	    migrations.CreateModel(
		    name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
	            ('Owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
	    ),
	    migrations.CreateModel(
		    name='GalleryComment',
		    fields=[
			    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
			    ('UploadDateTime', models.DateTimeField(default=None, null=True)),
			    ('Text', models.CharField(max_length=1024)),
			    ('Gallery', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.Gallery')),
			    ('User', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
	    ),
	    migrations.CreateModel(
		    name='Like',
		    fields=[
			    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
		    ],
	    ),
	    migrations.CreateModel(
		    name='Photo',
		    fields=[
			    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
			    ('UploadDateTime', models.DateTimeField(auto_now_add=True, null=True)),
			    ('UUID', models.CharField(max_length=1024)),
			    ('Location', models.CharField(blank=True, default='', max_length=100, null=True)),
			    ('Description', models.CharField(blank=True, default='', max_length=1024, null=True)),
			    ('Gallery', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.Gallery')),
		    ],
	    ),
	    migrations.CreateModel(
		    name='PhotoComment',
		    fields=[
			    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
			    ('UploadDateTime', models.DateTimeField(auto_now_add=True, null=True)),
			    ('Text', models.CharField(max_length=1024)),
			    ('Photo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.Photo')),
			    ('User', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
		    ],
	    ),
	    migrations.CreateModel(
		    name='Profile',
		    fields=[
			    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
			    ('AuthService', models.CharField(blank=True, default='', max_length=100)),
			    ('AuthServiceUserId', models.PositiveIntegerField(blank=True, default=1)),
			    ('ProfilePhoto', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='App.Photo')),
			    ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
		    ],
	    ),
	    migrations.AddField(
		    model_name='like',
		    name='Photo',
		    field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.Photo'),
	    ),
	    migrations.AddField(
		    model_name='like',
		    name='User',
		    field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
