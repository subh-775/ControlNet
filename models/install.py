import os

def download_controlnet_hed():
    url = ('https://huggingface.co/lllyasviel/ControlNet/'
           'resolve/main/models/control_sd15_hed.pth')
    download(url, 'models')
