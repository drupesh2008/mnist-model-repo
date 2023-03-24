import numpy as np
import cv2
import onnx
import onnxruntime as ort

# Sample Input Image Path
input_image_path = "SampleData/Input/seven.tif" 
# Read the image and do basic pre-processing as per model requirements
img = cv2.imread(input_image_path, -1)
img=np.expand_dims(img,axis=0)

# Load the Model
model = onnx.load("Models/model.onnx")

# Inference the model
session = ort.InferenceSession(model.SerializeToString())
ort_inputs = {session.get_inputs()[0].name: img}    
preds = session.run(None, ort_inputs)[0]               
print(np.argmax(preds))