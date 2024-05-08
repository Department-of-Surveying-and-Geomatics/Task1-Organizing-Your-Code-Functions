import matplotlib.pyplot as plt


def get_file(x_y_coordinates.txt):
    with open(x_y_coordinates.txt,'r') as file:
        data = file.readlines()
    return data


def plot_data(x_y_coordinates):
    x_coordinates = []
    y_coordinates = []

    for line in x_y_coordinates:
        data = line.strip().split(',')
        x_coordinates.append(float(data[0]))
        y_coordinates.append(float(data[1]))

        plt.scatter(x_y_coordinates)
        plt.xlabel('x coordinates')
        plt.ylabel('y coordinates')
        plt.title('scatter plot of data')
        plt.show()




