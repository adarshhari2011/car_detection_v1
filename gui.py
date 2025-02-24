from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
model = load_model("gui\CDv2.h5")
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

root = Tk()

root.geometry("1000x700")
root.title("Car Brand Detector")

def upload_image():
    filepath = filedialog.askopenfilename()
    image = load_img(filepath,target_size = (256, 256), color_mode = 'rgb')
    image_array = img_to_array(image)
    images = np.array([image_array])
    print(images.shape)
    problabilaty = model.predict(images)
    prediction = np.argmax(problabilaty,axis=1)
    print(prediction)
    if prediction == 0:
        messagebox.showinfo("Prediction" , f"The prediction is Audi")
    elif prediction == 1:
        messagebox.showinfo("Prediction" , f"The prediction is Lamborghini")
    if prediction == 2:
        messagebox.showinfo("Prediction" , f"The prediction is Mercedes-Benz")

    prediction=("your prediction is", prediction)


upload_button = Button(root, text="Upload Image", command=upload_image,font=("Arial",14, "bold"), bg="black", fg="white")
upload_button.grid(row = 1, column = 2)




root.mainloop()
