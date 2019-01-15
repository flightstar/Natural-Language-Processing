def showData(data, names):
    i = 0
    while i < data.shape[0]:
        print(names[i] + ": ")
        j = 0
        while j < data.shape[1]:
            print(data[i][j])
            j += 1
        print("")
        i += 1

def Main():
    print("The sample data is: ")
    fname = 'data.csv'
    csv = numpy.genfromtxt(fname, dtype=str, delimiter=",")
    num_rows = csv.shape[0] # x axis in graphics computer
    num_cols = csv.shape[1] # y axis in graphics computer
    names = csv[:,0]
    data = numpy.genfromtxt(fname, usecols = range(1,num_cols), delimiter=",")
    print(names)
    print(str(num_rows) + "x" + str(num_cols))
    print(data)
    showData(data, names)
