import math
from pickle import FALSE
from sklearn import neighbors
import os
import os.path
import pickle
import face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder
import pandas as pd
from numpy import asarray, savetxt, loadtxt
import numpy as np
import shutil


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def train(train_dir, model_save_path="trained_knn_model.csv", n_neighbors=1, knn_algo='ball_tree', verbose=False):

    X = loadtxt(base_path+"output2.csv", delimiter=',').tolist()
    y = loadtxt(base_path+"output3.csv", dtype=str).tolist()

    # Loop through each person in the training set
    for class_dir in os.listdir(train_dir):
        if not os.path.isdir(os.path.join(train_dir, class_dir)):
            continue

        # Loop through each training image for the current person
        for img_path in image_files_in_folder(os.path.join(train_dir, class_dir)):
            image = face_recognition.load_image_file(img_path)
            face_bounding_boxes = face_recognition.face_locations(image)

            if len(face_bounding_boxes) != 1:
                pass
            else:
                # Add face encoding for current image to the training set
                X.append(face_recognition.face_encodings(image, known_face_locations=face_bounding_boxes)[0])
                y.append(class_dir)
    shutil.rmtree(base_path+"train")
    os.mkdir(base_path+"train")

    
    # Determine how many neighbors to use for weighting in the KNN classifier
    if n_neighbors is None:
        n_neighbors = int(round(math.sqrt(len(X))))

    pointX = asarray(X)
    d = np.array(y)
    pointY = d.reshape(d.shape[0], -1)

    savetxt(base_path + "output2.csv", pointX, delimiter=',')
    savetxt(base_path + "output3.csv", pointY, fmt='%s')

    knn_clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=knn_algo, weights='distance')
    knn_clf.fit(X, y)
    
    # Save the trained KNN classifier
    if model_save_path is not None:
        with open(model_save_path, 'wb') as f:
            pickle.dump(knn_clf, f)

    return knn_clf


if __name__ == "__main__":
    base_path = "/var/lib/jenkins/workspace/sucheol\'s/face_classifier/"
    flag = False
    # STEP 1: Train the KNN classifier and save it to disk
    # Once the model is trained and saved, you can skip this step next time.
    classifier = train(base_path+"train", model_save_path="trained_knn_model.csv", n_neighbors=1)



