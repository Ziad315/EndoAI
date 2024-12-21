#include Libraries
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyDB_W2sFelcVn5wG7UjKpx454c_d2x9I6U")

# Create a model
model = genai.GenerativeModel('gemini-1.5-flash')

# Create main application window
root = tk.Tk()
root.title("ENDOSCOPY-AI By Ziad Yakoot")

# Create a label to display the image
img_label = tk.Label(root)
img_label.pack()

# Create a text box to display the response
response_text_box = tk.Text(root, height=10, width=40)
response_text_box.pack()

# Create a function to handle image upload
def upload_image():
    try:
        # Open the image file
        img_path = askopenfilename()
        img = Image.open(img_path)

        # Resize the image
        img = img.resize((400, 400), Image.Resampling.LANCZOS)

        # Convert the image to Tkinter format
        img_tk = ImageTk.PhotoImage(img)

        # Remove the previous image
        img_label.config(image='')
        img_label.image = ''

        # Display the new image
        img_label.config(image=img_tk)
        img_label.image = img_tk

        # Generate content from the image
        response = model.generate_content([img])
        response.resolve()  # Wait for response
        response_text = response.text

        # Display the response in the text box
        response_text_box.delete(1.0, tk.END)
        response_text_box.insert(tk.END, response_text)

    
    except AttributeError as e:
        print("There is no such attribute:", e)

# Create a button to upload an image
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

# Run the application
root.mainloop()

