import os
from django.apps import AppConfig
from django.conf import settings
from keras.models import load_model

class MonitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'monitor'

class ModelConfig(AppConfig):
    name='model'
    MODEL_FILE = os.path.join(settings.MODELS, 'unet_model.h5')
    model = load_model(MODEL_FILE)
