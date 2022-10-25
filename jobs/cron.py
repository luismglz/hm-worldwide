from django.core.management import call_command
from apscheduler.schedulers.background import BackgroundScheduler

def backup_db():
    try:
        call_command('dumpdata', '-o', 'db.json')
        call_command('loaddata', '-i', 'db.json', '--database=restore')
    except Exception as e:
        print(str(e))
        pass

def run_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(backup_db, 'interval', minutes=1)
    try:
        print('start scheduler')
        scheduler.start()
    except KeyboardInterrupt:
        pass