from django.apps import AppConfig

def ready(self):
    import students.signals
    
class StudentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'students'

    def ready(self):
        import students.signals