# Generated by Django 2.1.5 on 2019-01-15 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(help_text='Enter a reason for the use of the domain (e.g. command-and-control)', max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Domain activity',
                'verbose_name_plural': 'Domain activities',
                'ordering': ['activity'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the client', max_length=100, unique=True, verbose_name='Client Name')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a domain name', max_length=100, unique=True, verbose_name='Name')),
                ('registrar', models.CharField(help_text='Enter the name of the registrar where this domain is registered', max_length=100, null=True, unique=True, verbose_name='Registrar')),
                ('dns_record', models.CharField(help_text='Enter domain DNS records', max_length=500, null=True, verbose_name='DNS Record')),
                ('health_dns', models.CharField(help_text='Domain health status based on passive DNS (e.g. Healthy, Burned)', max_length=100, null=True, verbose_name='DNS Health')),
                ('creation', models.DateField(help_text='Domain purchase date', verbose_name='Purchase Date')),
                ('expiration', models.DateField(help_text='Domain expiration date', verbose_name='Expiration Date')),
                ('all_cat', models.TextField(help_text='All categories applied to this domain', null=True, verbose_name='All Categories')),
                ('ibm_xforce_cat', models.CharField(help_text='Domain category as determined by IBM X-Force', max_length=100, null=True, verbose_name='IBM X-Force')),
                ('talos_cat', models.CharField(help_text='Domain category as determined by Cisco Talos', max_length=100, null=True, verbose_name='Cisco Talos')),
                ('bluecoat_cat', models.CharField(help_text='Domain category as determined by Bluecoat', max_length=100, null=True, verbose_name='Bluecoat')),
                ('fortiguard_cat', models.CharField(help_text='Domain category as determined by Fortiguard', max_length=100, null=True, verbose_name='Fortiguard')),
                ('opendns_cat', models.CharField(help_text='Domain category as determined by OpenDNS', max_length=100, null=True, verbose_name='OpenDNS')),
                ('trendmicro_cat', models.CharField(help_text='Domain category as determined by TrendMicro', max_length=100, null=True, verbose_name='TrendMicro')),
                ('mx_toolbox_status', models.CharField(help_text='Domain spam status as determined by MX Toolbox', max_length=100, null=True, verbose_name='MX Toolbox Status')),
                ('note', models.TextField(help_text='Domain-related notes, such as thoughts behind its purchase or how/why it was burned or retired', null=True, verbose_name='Notes')),
                ('burned_explanation', models.TextField(help_text='Reasons why the domain\'s health status is not "Healthy"', null=True, verbose_name='Health Explanation')),
            ],
            options={
                'verbose_name': 'Domain',
                'verbose_name_plural': 'Domains',
                'ordering': ['health_status', 'name'],
                'permissions': (('can_retire_domain', 'Can retire a domain'), ('can_mark_reserved', 'Can reserve a domain')),
            },
        ),
        migrations.CreateModel(
            name='DomainStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_status', models.CharField(help_text='Domain status type (e.g. Available)', max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Domain status',
                'verbose_name_plural': 'Domain statuses',
                'ordering': ['domain_status'],
            },
        ),
        migrations.CreateModel(
            name='HealthStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_status', models.CharField(help_text='Health status type (e.g. Healthy, Burned)', max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Health status',
                'verbose_name_plural': 'Health statuses',
                'ordering': ['health_status'],
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True, help_text='Enter the start date of the project', max_length=100, verbose_name='Start Date')),
                ('end_date', models.DateField(help_text='Enter the end date of the project', max_length=100, verbose_name='End Date')),
                ('note', models.TextField(help_text='Project-related notes, such as how the domain will be used/how it worked out', null=True, verbose_name='Notes')),
                ('slack_channel', models.CharField(help_text="Name of the Slack channel to be used for updates for this domain during the project's duration", max_length=100, null=True, verbose_name='Project Slack Channel')),
                ('activity_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.ActivityType')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Client')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Domain')),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Historical project',
                'verbose_name_plural': 'Historical projects',
                'ordering': ['client', 'domain'],
            },
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_type', models.CharField(help_text='Enter a project type (e.g. red team, penetration test)', max_length=100, unique=True, verbose_name='Project Type')),
            ],
            options={
                'verbose_name': 'Project type',
                'verbose_name_plural': 'Project types',
                'ordering': ['project_type'],
            },
        ),
        migrations.CreateModel(
            name='WhoisStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whois_status', models.CharField(help_text='WHOIS privacy status (e.g. Enabled, Disabled)', max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'WHOIS status',
                'verbose_name_plural': 'WHOIS statuses',
                'ordering': ['whois_status'],
            },
        ),
        migrations.AddField(
            model_name='history',
            name='project_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.ProjectType'),
        ),
        migrations.AddField(
            model_name='domain',
            name='domain_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.DomainStatus'),
        ),
        migrations.AddField(
            model_name='domain',
            name='health_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.HealthStatus'),
        ),
        migrations.AddField(
            model_name='domain',
            name='last_used_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='domain',
            name='whois_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.WhoisStatus'),
        ),
    ]
