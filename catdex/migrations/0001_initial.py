# Generated by Django 3.0.5 on 2020-04-14 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='catdex.Category')),
            ],
            options={
                'verbose_name': 'subcategory',
                'verbose_name_plural': 'subcategories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='cat/%Y/%m/%d')),
                ('gender', models.CharField(choices=[('암컷', '암컷'), ('수컷', '수컷')], db_index=True, max_length=200)),
                ('tnr', models.CharField(choices=[('중성화OK', '중성화OK'), ('중성화NO', '중성화NO')], db_index=True, max_length=200)),
                ('domain', models.CharField(choices=[('쪽문', '쪽문'), ('북문', '북문'), ('서문', '서문'), ('정문', '정문'), ('동문', '동문')], max_length=200)),
                ('color', models.CharField(choices=[('치즈', '치즈'), ('고등어', '고등어'), ('삼색', '삼색'), ('검정', '검정'), ('카오스', '카오스')], db_index=True, max_length=200)),
                ('intimacy', models.CharField(choices=[('상', '상'), ('중', '중'), ('하', '하')], db_index=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('subcategory', models.ManyToManyField(blank=True, related_name='cat', to='catdex.Subcategory')),
            ],
            options={
                'ordering': ['created'],
                'index_together': {('id', 'slug')},
            },
        ),
    ]
