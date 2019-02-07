# Generated by Django 2.1.5 on 2019-02-06 10:27
import os
from uuid import UUID

from django.db import migrations
from django.conf import settings
import os
from uuid import UUID

from django.conf import settings
from django.db import migrations

UPLOAD_ROOT = getattr(settings,"FORMS_BUILDER_UPLOAD_ROOT", None) or getattr(settings,"MEDIA_ROOT", None)


def move_files(apps, schema_editor):
    '''

    Move files into slug-named dirs
    '''
    Field = apps.get_model('forms', "Field")
    FieldEntry = apps.get_model('forms', "FieldEntry")



    for f in Field.objects.filter(field_type=9):
        for fe in FieldEntry.objects.filter(field_id=f.id):
            fuuid = fe.value.split("/")[1]
            try:
                UUID(fuuid)
                newname = os.path.join("forms", "%s_%s" % (f.form.id, f.form.slug), "%s_%s" % (fe.id, os.path.basename(fe.value)))
                try:
                    os.renames(UPLOAD_ROOT + fe.value, UPLOAD_ROOT + newname)
                except OSError as e:
                    print (e)
                    continue
                fe.value = newname
                fe.save(update_fields=['value'])

            except ValueError:
                continue

class Migration(migrations.Migration):
    dependencies = [
        ('forms', '0006_fieldentry_hashed'),
    ]

    operations = [
        migrations.RunPython(move_files)
    ]
