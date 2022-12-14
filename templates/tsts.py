# # Import the libraries
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
# from tensorflow.keras.models import Model
# from pathlib import Path
# from PIL import Image
# class FeatureExtractor:
#     def __init__(self):
#         # Use VGG-16 as the architecture and ImageNet for the weight
#         base_model = VGG16(weights='imagenet')
#         # Customize the model to return features from fully-connected layer
#         self.model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)
#     def extract(self, img):
#         # Resize the image
#         img = img.resize((224, 224))
#         # Convert the image color space
#         img = img.convert('RGB')
#         # Reformat the image
#         x = image.img_to_array(img)
#         x = np.expand_dims(x, axis=0)
#         x = preprocess_input(x)
#         # Extract Features
#         feature = self.model.predict(x)[0]
#         return feature / np.linalg.norm(feature)
# # Iterate through images (Change the path based on your image location)
# for img_path in sorted("<IMAGE DATABASE PATH LIST HERE>"):
#     print(img_path)
#     # Extract Features
#     feature = fe.extract(img=Image.open(img_path))
#     # Save the Numpy array (.npy) on designated path
#     feature_path = "<IMAGE FEATURE PATH HERE>.npy"
#     np.save(feature_path, feature)
    
import requests
import json



url = "https://google-image-search1.p.rapidapi.com/v2/"

querystring = {"q":"paris","hl":"en"}

headers = {
	"X-RapidAPI-Host": "google-image-search1.p.rapidapi.com",
	"X-RapidAPI-Key": "d1869f472amsh706c8dbcf4cf939p147e3bjsn048c5e14b83e"
}

response = requests.request("GET", url, headers=headers, params=querystring)


data = json.loads(response.text)
pages=[]
for i in range(0,100):
	pages.append(data["response"]["images"][i]["source"]["page"])

print(pages)
