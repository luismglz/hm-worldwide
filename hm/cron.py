from django.core.management import call_command

def backupDB():
    try:
        call_command('dbbackup --noinput --settings hm.backup')
        call_command('dbrestore --noinput --settings hm.restore')
    except:
        print('error')
        pass