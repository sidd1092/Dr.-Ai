# can you please create me a GUI same as index.html using tkinter
# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Initialize the main application window
root = Tk()
root.geometry("800x800")
root.title("Disease Prediction System")

# Create a label widget for the title
myLabel = Label(root, text="Disease Prediction System")
myLabel.pack()

# Create a label widget for the input prompt
myLabel = Label(root, text="Enter Symptoms")
myLabel.pack()

# Create an entry widget for symptoms input
symptoms = Entry(root, width=50)
symptoms.pack()

# Define the action for the prediction button
def myClick():
    symptoms_text = symptoms.get()
    # Check if the input is not just the placeholder text
    if symptoms_text.lower() == "symptoms":
        messagebox.showinfo("Error", "Please enter your symptoms or check for misspelled words.")
    else:
        messagebox.showinfo("Prediction", "You have entered: " + symptoms_text)

# Create a button widget for predictions
myButton = Button(root, text="Predict", command=myClick)
myButton.pack()

# Run the application
root.mainloop()