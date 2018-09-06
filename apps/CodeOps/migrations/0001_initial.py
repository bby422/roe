# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-04 08:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log_Project_Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField(blank=True, default=None, null=True, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeid')),
                ('project_user', models.CharField(default=None, max_length=50, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe7\x94\xa8\xe6\x88\xb7')),
                ('project_name', models.CharField(default=None, max_length=100, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('project_content', models.CharField(default=None, max_length=100)),
                ('project_branch', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name=b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'opsmanage_log_project_config',
                'verbose_name': '\u9879\u76ee\u914d\u7f6e\u64cd\u4f5c\u8bb0\u5f55\u8868',
                'verbose_name_plural': '\u9879\u76ee\u914d\u7f6e\u64cd\u4f5c\u8bb0\u5f55\u8868',
            },
        ),
        migrations.CreateModel(
            name='Project_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'opsmanage_project_assets',
                'verbose_name': '\u9879\u76ee\u8d44\u4ea7\u8868',
                'verbose_name_plural': '\u9879\u76ee\u8d44\u4ea7\u8868',
                'permissions': (('can_read_project_assets', '\u8bfb\u53d6\u4ea7\u54c1\u7ebf\u6743\u9650'), ('can_change_project_assets', '\u66f4\u6539\u4ea7\u54c1\u7ebf\u6743\u9650'), ('can_add_project_assets', '\u6dfb\u52a0\u4ea7\u54c1\u7ebf\u6743\u9650'), ('can_delete_project_assets', '\u5220\u9664\u4ea7\u54c1\u7ebf\u6743\u9650')),
            },
        ),
        migrations.CreateModel(
            name='Project_Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_env', models.CharField(default=None, max_length=50, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe7\x8e\xaf\xe5\xa2\x83')),
                ('project_name', models.CharField(default=None, max_length=100, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('project_service', models.SmallIntegerField(verbose_name=b'\xe4\xb8\x9a\xe5\x8a\xa1\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('project_type', models.CharField(blank=True, max_length=20, null=True, verbose_name=b'\xe7\xbc\x96\xe8\xaf\x91\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('project_local_command', models.TextField(blank=True, default=None, null=True, verbose_name=b'\xe9\x83\xa8\xe7\xbd\xb2\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe8\xa6\x81\xe6\x89\xa7\xe8\xa1\x8c\xe7\x9a\x84\xe5\x91\xbd\xe4\xbb\xa4')),
                ('project_repo_dir', models.CharField(default=None, max_length=100, verbose_name=b'\xe6\x9c\xac\xe5\x9c\xb0\xe4\xbb\x93\xe5\xba\x93\xe7\x9b\xae\xe5\xbd\x95')),
                ('project_dir', models.CharField(default=None, max_length=100, verbose_name=b'\xe4\xbb\xa3\xe7\xa0\x81\xe7\x9b\xae\xe5\xbd\x95')),
                ('project_exclude', models.TextField(blank=True, default=None, null=True, verbose_name=b'\xe6\x8e\x92\xe9\x99\xa4\xe6\x96\x87\xe4\xbb\xb6')),
                ('project_address', models.CharField(default=None, max_length=100, verbose_name=b'\xe7\x89\x88\xe6\x9c\xac\xe4\xbb\x93\xe5\xba\x93\xe5\x9c\xb0\xe5\x9d\x80')),
                ('project_uuid', models.CharField(max_length=50, verbose_name=b'\xe5\x94\xaf\xe4\xb8\x80id')),
                ('project_repo_user', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'\xe4\xbb\x93\xe5\xba\x93\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('project_repo_passwd', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'\xe4\xbb\x93\xe5\xba\x93\xe5\xaf\x86\xe7\xa0\x81')),
                ('project_repertory', models.CharField(choices=[(b'git', 'git'), (b'svn', 'svn')], default=None, max_length=10, verbose_name=b'\xe4\xbb\x93\xe5\xba\x93\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('project_status', models.SmallIntegerField(blank=True, default=None, null=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\xbf\x80\xe6\xb4\xbb')),
                ('project_remote_command', models.TextField(blank=True, default=None, null=True, verbose_name=b'\xe9\x83\xa8\xe7\xbd\xb2\xe4\xb9\x8b\xe5\x90\x8e\xe6\x89\xa7\xe8\xa1\x8c\xe7\x9a\x84\xe5\x91\xbd\xe4\xbb\xa4')),
                ('project_user', models.CharField(default=None, max_length=50, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\x96\x87\xe4\xbb\xb6\xe5\xae\xbf\xe4\xb8\xbb')),
                ('project_model', models.CharField(choices=[(b'branch', 'branch'), (b'tag', 'tag')], default=None, max_length=10, verbose_name=b'\xe4\xb8\x8a\xe7\xba\xbf\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('project_audit_group', models.SmallIntegerField(blank=True, default=None, null=True, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\x8e\x88\xe6\x9d\x83\xe7\xbb\x84')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_config', to='CodeOps.Project_Assets')),
            ],
            options={
                'verbose_name_plural': '\u9879\u76ee\u7ba1\u7406\u8868',
                'db_table': 'opsmanage_project_config',
                'verbose_name': '\u9879\u76ee\u7ba1\u7406\u8868',
                'permissions': (('can_read_project_config', '\u8bfb\u53d6\u9879\u76ee\u90e8\u7f72\u6743\u9650'), ('can_change_project_config', '\u66f4\u6539\u9879\u76ee\u90e8\u7f72\u6743\u9650'), ('can_add_project_config', '\u6dfb\u52a0\u9879\u76ee\u90e8\u7f72\u6743\u9650'), ('can_delete_project_config', '\u5220\u9664\u9879\u76ee\u90e8\u7f72\u6743\u9650')),
            },
        ),
        migrations.CreateModel(
            name='Project_Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server', models.CharField(default=None, max_length=100, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8IP')),
                ('dir', models.CharField(default=None, max_length=100, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe7\x9b\xae\xe5\xbd\x95')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_number', to='CodeOps.Project_Config')),
            ],
            options={
                'db_table': 'opsmanage_project_number',
                'verbose_name': '\u9879\u76ee\u6210\u5458\u8868',
                'verbose_name_plural': '\u9879\u76ee\u6210\u5458\u8868',
            },
        ),
        migrations.CreateModel(
            name='Service_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_assets', to='CodeOps.Project_Assets')),
            ],
            options={
                'verbose_name_plural': '\u4e1a\u52a1\u5206\u7ec4\u8868',
                'db_table': 'opsmanage_service_assets',
                'verbose_name': '\u4e1a\u52a1\u5206\u7ec4\u8868',
                'permissions': (('can_read_service_assets', '\u8bfb\u53d6\u4e1a\u52a1\u8d44\u4ea7\u6743\u9650'), ('can_change_service_assets', '\u66f4\u6539\u4e1a\u52a1\u8d44\u4ea7\u6743\u9650'), ('can_add_service_assets', '\u6dfb\u52a0\u4e1a\u52a1\u8d44\u4ea7\u6743\u9650'), ('can_delete_service_assets', '\u5220\u9664\u4e1a\u52a1\u8d44\u4ea7\u6743\u9650')),
            },
        ),
        migrations.AlterUniqueTogether(
            name='service_assets',
            unique_together=set([('project', 'service_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='project_number',
            unique_together=set([('project', 'server')]),
        ),
        migrations.AlterUniqueTogether(
            name='project_config',
            unique_together=set([('project_env', 'project', 'project_name')]),
        ),
    ]