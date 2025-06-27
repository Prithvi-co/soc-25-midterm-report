  import numpy as np
import tensorflow as tf
from models.siamese_model import build_siamese_model

# Initialize model
model = build_siamese_model()

# Simulate dummy grayscale images (105x105)
img1 = np.random.rand(1, 105, 105, 1)
img2 = np.random.rand(1, 105, 105, 1)

# Predict similarity
similarity_score = model.predict([img1, img2])
print("Predicted similarity score:", similarity_score[0][0])
