from tkinter import *
from PIL import ImageTk, Image

large_font = ('Verdana', 20) # Font Type and Font Size

root = Tk()
root.title("My Pokedex")
root.iconbitmap("...") # Insert your icon path here

# Loading Images and creating a list
my_img1 = ImageTk.PhotoImage(Image.open("bulbasaur.png")) 
my_img2 = ImageTk.PhotoImage(Image.open("squirtle.png"))
my_img3 = ImageTk.PhotoImage(Image.open("pikachu.png"))

image_list = [my_img1, my_img2, my_img3]

# Defining the status of the image
status = Label(root, text = "Image 1 of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E)

my_label = Label(image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3)

# Forward Button
def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image = image_list[image_number - 1])
	button_forward = Button(root, text = " >> ", command = lambda: forward(image_number + 1))
	button_back = Button(root, text = " << ", command = lambda: back(image_number - 1))

# If you reach the last image, forward button should be disabled
	if image_number == 3:
		button_forward = Button(root, text = " >> ", state = DISABLED)

	my_label.grid(row = 0, column = 0, columnspan = 3)
	button_back.grid(row = 1, column = 0)
	button_forward.grid(row = 1, column = 2)

	status = Label(root, text = "Image " + str(image_number) + " of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E)
	status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)

# Back Button
def back(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image = image_list[image_number - 1])
	button_forward = Button(root, text = " >> ", command = lambda: forward(image_number + 1))
	button_back = Button(root, text = " << ", command = lambda: back(image_number - 1))

# If you reach the first image, back button should be disabled
	if image_number == 1:
		button_back = Button(root, text = " << ", state = DISABLED)

	my_label.grid(row = 0, column = 0, columnspan = 3)
	button_back.grid(row = 1, column = 0)
	button_forward.grid(row = 1, column = 2)

	status = Label(root, text = "Image " + str(image_number) + " of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E)
	status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)
	
# Drawing the buttons on the screen
button_back = Button(root, text = " << ", command = back, state = DISABLED)
button_exit = Button(root, text = " EXIT ", command = root.quit, relief = "solid") 
button_forward = Button(root, text = " >> ", command = lambda: forward(2))

button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2, pady = 10)

status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)

root.mainloop()
