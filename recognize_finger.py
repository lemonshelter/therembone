import traitlets
from VGG_Demo.jetcam.utils import bgr8_to_jpeg
from IPython.display import display
import ipywidgets
from VGG_Demo.jetcam.csi_camera import CSICamera
import cv2
import torch
from torch import nn, optim
import numpy as np
import random
import sys
from VGG_Demo.src.vgg_local import VGG_LOCAL
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from PIL import Image
import gc

class RecognizeFinger:
    def __init__(self):
        self.model_path = "./final_weight.pth"
        self.model_ver = "VGG11"
        self.RPS_list = {"0":"オフ", "1":"低オクターブ", "2":"真ん中オクターブ", "3":"高オクターブ"}
        self.image_size = 32
        self.image
        # Set random seed for reproducibility
        self.random_seed = 9999
        random.seed(self.random_seed)
        np.random.seed(self.random_seed)
        torch.manual_seed(self.random_seed)
        # 使えるリソースを確認
        if torch.cuda.is_available():
            self.device = torch.device('cuda')
            torch.cuda.manual_seed(self.random_seed)
            torch.backends.cudnn.deterministic = True
        else:
            self.device = torch.device('cpu')
        # Preprocessing for test data
        self.test_transform = transforms.Compose([
            transforms.Residze((self.image_size, self.image_size)),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ])
        # Initialize and load model weights
        self.model = VGG_LOCAL(self.model_ver, classes=3, image_size=self.image_size).to(self.device)
        self.model.load_state_dict(torch.load(self.model_path))
        print("モデルの読み込み完了")
    
    def take_pic(self):
        camera = CSICamera(width=64, height=64, capture_device=0)
        # gc.collect()
        self.image = camera.read()
        image_path = "./image.jpg"
        cv2.imwrite(image_path, self.image)
        print("撮影が終わりました")
    
    def predict(self):
        input = self.test_transform(Image.fromarray(self.image))
        print("推論開始")
        self.model.eval()
        with torch.no_grad():
            input = input.to(self.device)
            output = self.model(input.unsqueeze(0))
        print(f'{self.RPS_list[torch.argmax(output)]}です')
        return int(output)


if __name__ == '__main__':
    recognize_finger = RecognizeFinger()
    recognize_finger.take_pic()
    predicted = recognize_finger.predict()
    prunt('predicted is ' + predicted)
    
