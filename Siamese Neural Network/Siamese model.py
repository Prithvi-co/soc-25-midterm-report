 import tensorflow as tf
from tensorflow.keras import layers, Model

def build_embedding_network(input_shape=(105, 105, 1)):
    inputs = tf.keras.Input(shape=input_shape)
    x = layers.Conv2D(64, (10,10), activation='relu')(inputs)
    x = layers.MaxPooling2D()(x)
    x = layers.Conv2D(128, (7,7), activation='relu')(x)
    x = layers.MaxPooling2D()(x)
    x = layers.Conv2D(128, (4,4), activation='relu')(x)
    x = layers.MaxPooling2D()(x)
    x = layers.Conv2D(256, (4,4), activation='relu')(x)
    x = layers.Flatten()(x)
    x = layers.Dense(4096, activation='sigmoid')(x)
    return Model(inputs, x, name="EmbeddingNetwork")

def build_siamese_model(input_shape=(105, 105, 1)):
    embedding_net = build_embedding_network(input_shape)

    input_a = tf.keras.Input(shape=input_shape, name='input_a')
    input_b = tf.keras.Input(shape=input_shape, name='input_b')

    emb_a = embedding_net(input_a)
    emb_b = embedding_net(input_b)

    # Distance metric (L1 distance)
    distance = tf.keras.layers.Lambda(lambda tensors: tf.abs(tensors[0] - tensors[1]))([emb_a, emb_b])
    outputs = layers.Dense(1, activation='sigmoid')(distance)

    model = Model(inputs=[input_a, input_b], outputs=outputs, name="SiameseNetwork")
    return model

if __name__ == "__main__":
    model = build_siamese_model()
    model.summary()
