from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import random


# Create your views here.

def get_dog(reqest):
    if reqest.method == 'GET':
        os.chdir("C:\\Users\\ezdrlaz\\PycharmProjects\\dog_api_lazar_zdravkoski\\images\\Images")
        folds = os.listdir()

        random_breed = random.choice(folds)
        os.chdir("C:\\Users\\ezdrlaz\\PycharmProjects\\dog_api_lazar_zdravkoski\\images\\Images\\"+str(random_breed))
        pictures = os.listdir()
        random_pic = random.choice(pictures)
        path_to_pic = "C:\\Users\\ezdrlaz\\PycharmProjects\\dog_api_lazar_zdravkoski\\images\\Images\\"+str(random_breed)+"\\"+str(random_pic)
        response = json.dumps([{"random_breed" : random_breed[10:], "random_picture" : path_to_pic}])

        return HttpResponse(response, content_type='text/json')
