# Generated by Django 4.2 on 2023-06-20 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
        migrations.CreateModel(
            name='Blog_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('post_img', models.ImageField(blank=True, null=True, upload_to='myimages')),
                ('category', models.CharField(choices=[('Mental health', 'Mental health'), ('heart disease', 'heart disease'), ('covid 19', 'covid 19'), ('immunitization', 'immunitization')], max_length=20)),
                ('summary', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('created_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.doctor')),
            ],
        ),
    ]
