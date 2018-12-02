from django.contrib.auth.models import User
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Building(models.Model):
    locid = models.ForeignKey('Location', models.DO_NOTHING, db_column='LocID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'building'


class Camera(models.Model):
    secid = models.ForeignKey('Secsystem', models.DO_NOTHING, db_column='SecID')  # Field name made lowercase.
    alerts = models.IntegerField(db_column='Alerts', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'camera'


class Citizen(models.Model):
    citizenid = models.IntegerField(db_column='CitizenID', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=30)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=30)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    birthday = models.DateField(db_column='Birthday')  # Field name made lowercase.
    locid = models.ForeignKey('Location', models.DO_NOTHING, related_name='LocID')  # Field name made lowercase.
    homeid = models.ForeignKey('Location', models.DO_NOTHING, related_name='HomeID')  # Field name made lowercase.
    strikes = models.IntegerField(db_column='Strikes')  # Field name made lowercase.
    isalive = models.IntegerField(db_column='IsAlive')  # Field name made lowercase.
    income = models.IntegerField(db_column='Income')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'citizen'


class Contraband(models.Model):
    itemid = models.AutoField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40)  # Field name made lowercase.
    currentowner = models.ForeignKey(Citizen, models.DO_NOTHING, related_name='CurrentOwner', blank=True, null=True)  # Field name made lowercase.
    originalowner = models.ForeignKey(Citizen, models.DO_NOTHING, related_name='OriginalOwner', blank=True, null=True)  # Field name made lowercase.
    threatlevel = models.IntegerField(db_column='ThreatLevel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contraband'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Location(models.Model):
    locid = models.CharField(db_column='LocID', primary_key=True, max_length=4)  # Field name made lowercase.
    secid = models.ForeignKey('Secsystem', models.DO_NOTHING, db_column='SecID', blank=True, null=True)  # Field name made lowercase.
    threatlevel = models.IntegerField(db_column='ThreatLevel')  # Field name made lowercase.
    curfew = models.IntegerField(db_column='Curfew', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'location'


class Secsystem(models.Model):
    secid = models.IntegerField(db_column='SecID', primary_key=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'secsystem'


class Socialstanding(models.Model):
    citizenid = models.ForeignKey(Citizen, models.DO_NOTHING, db_column='CitizenID')  # Field name made lowercase.
    talents = models.CharField(db_column='Talents', max_length=40, blank=True, null=True)  # Field name made lowercase.
    charm = models.IntegerField(db_column='Charm')  # Field name made lowercase.
    score = models.IntegerField(db_column='Score')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'socialstanding'


class World(models.Model):
    clock = models.IntegerField(db_column='Clock')  # Field name made lowercase.
    datecount = models.DateField(db_column='DateCount')  # Field name made lowercase.
    humidity = models.IntegerField(db_column='Humidity')  # Field name made lowercase.
    temp = models.IntegerField(db_column='Temp')  # Field name made lowercase.
    precip = models.CharField(db_column='Precip', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'world'