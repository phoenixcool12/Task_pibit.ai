from django.apps import AppConfig


class ImguploadConfig(AppConfig):
    name = 'Imgupload'
    verbose_name = "My Brand New Application"

    # my_new_app/__init__.py


default_app_config = 'Imgupload.apps.MyNewAppConfig'
