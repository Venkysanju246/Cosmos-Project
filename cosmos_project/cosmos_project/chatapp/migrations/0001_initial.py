# Generated by Django 4.2.4 on 2023-08-28 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PDFDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('upload_date', models.DateTimeField()),
                ('embedding', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('profile_picture', models.ImageField(upload_to='profile_pics/')),
                ('join_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_messages', models.ManyToManyField(related_name='received_by', to='chatapp.message')),
                ('sent_messages', models.ManyToManyField(related_name='sent_by', to='chatapp.message')),
                ('uploaded_pdfs', models.ManyToManyField(blank=True, to='chatapp.pdfdocument')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chatapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='pdfdocument',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.user'),
        ),
        migrations.AddField(
            model_name='message',
            name='attachments',
            field=models.ManyToManyField(blank=True, to='chatapp.pdfdocument'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.user'),
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('participants', models.ManyToManyField(to='chatapp.user')),
            ],
        ),
    ]