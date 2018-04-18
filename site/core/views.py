from django.views.generic import *
from keras.models import load_model
from django.views.generic.base import TemplateView
import tensorflow as tf


class MainPage(TemplateView):
    template_name = 'core/main_page.html'
    model_cnn = load_model('/home/ubuntu/instagram/inceptionv3-final_5.model')
    graph = tf.get_default_graph()

