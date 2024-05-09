def get_file(choice):
    File_location = None
    if choice == 1:
        File_location = open("x_y_coordinates.txt", 'r')
    else:
        File=input("Enter new file location:")
        File_location= open(File , "r")
    return File_location
def plot_data():
    import matplotlib.pyplot as plt
    choice = input("Enter 1 to run saved file or 2 to enter new file:")
    my_file =get_file(choice)
    if my_file != None:
        x_coords =[]
        y_coords=[]
        #reads the first line skipping header
        my_file.readline()
        #loop that reads the remaining lines
        for line in my_file.readlines():
         #first elements to x-list and second element to y-list
            x_coords.append(float(line.split(', ')[0]))
            y_coords.append(float(line.split(', ')[1]))
        plt.style.use('dark_background')
        plt.xlabel("x-Coordinates")
        plt.ylabel("y-Coordinates")
        plt.title("Coordinates of 2D Point")
        plt.grid()
        plt.scatter(x_coords, y_coords, c="red", marker="v")
        scatter_plot = plt.show()
        return scatter_plot

plot_data()
