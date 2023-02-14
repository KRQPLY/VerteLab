from numpy import zeros, uint8, squeeze
from .apps import ModelConfig
from skimage.transform import resize
from skimage.io import imread
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image


def generate_masks(images_list, model):
  IMG_HEIGHT = 256
  IMG_WIDTH = 256
  IMG_CHANNELS = 1
  images = zeros((len(images_list), IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=uint8)
  for idx, img in enumerate(images_list):
    input_img = resize(img, (IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), mode='constant', preserve_range=True)
    images[idx] = input_img
  prediction = model.predict(images, verbose=0)
  prediction = (prediction > 0.5).astype(uint8)
  return prediction*255

@csrf_exempt
def index(request):
  if request.method == 'POST':
    images_list = []
    files = request.FILES.getlist('images')
    for f in files:
      images_list.append(imread(f))
    model = ModelConfig.model
    masks = generate_masks(images_list, model)
    response = HttpResponse(content_type='image/png')
    mask = squeeze(masks[0], axis=2)
    img = Image.fromarray(mask)
    img.save(response, 'png')
    return response
  return HttpResponse(status=400)