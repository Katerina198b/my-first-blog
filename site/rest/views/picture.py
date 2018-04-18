from core.models import Picture
from rest.serializers import PictureSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from base64 import b64decode
from uuid import uuid4
from django.http import JsonResponse
import sys
import argparse
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt
from keras.preprocessing import image
from keras.models import load_model
from keras.applications.inception_v3 import preprocess_input
from keras import backend as K

from core.views import *
def predict(model, img, target_size):
    """Run model prediction on image
    Args:
    model: keras model
    img: PIL format image
    target_size: (w,h) tuple
    Returns:
    list of predicted labels and their probabilities
    """
    if img.size != target_size:
        img = img.resize(target_size)

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    
    cl = ['Jewelry', 'boquets','desserts', 'kisses', 'trash']
    p = preds.argmax()
    return cl[p]


class PictureView(mixins.CreateModelMixin,
                                          mixins.RetrieveModelMixin,
                                          mixins.DestroyModelMixin,
                                          mixins.ListModelMixin,
                                          GenericViewSet):

    serializer_class = PictureSerializer

    #def perform_create(self, serializer):


    filter_fields = ('created_at', 'category')
    filter_backends = (DjangoFilterBackend,)
    model_cnn = None
    def get_queryset(self):
        return Picture.objects.all()

    def perform_create(self, serializer):
        
        file_obj = self.request.data['file']
        filename = file_obj._get_name()

        with default_storage.open('/home/ubuntu/django/pictureClassifier/site/super_uploads/'+filename, 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)
        
        im = Image.open('/home/ubuntu/django/pictureClassifier/site/super_uploads/'+filename)
        
        im = im.convert('RGB')
        #global model_cnn
        #if self.model_cnn is None:
        #    self.model_cnn = load_model('/home/ubuntu/instagram/inceptionv3-final_5.model')
        #MainPage.model_cnn = load_model('/home/ubuntu/instagram/inceptionv3-final_5.model')
        with MainPage.graph.as_default():
            pred = predict(MainPage.model_cnn,im,(299,299))
        print(pred)
        serializer.save(category=pred)







