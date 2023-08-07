import tensorflow as tf
from Processes import Load_TDBMI_data 

dataset_path = "/home/awmirma/Documents/AI/practice/Tumor_Detection_in_Brain_MRI_Images/Dataset/1_Simplified"
X_train, X_test, y_train, y_test = Load_TDBMI_data(dataset_path)

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32,(3,3),activation='relu' ,input_shape = (256,256,3)),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64 , activation='relu'),
    tf.keras.layers.Dense(1,activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))