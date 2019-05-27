import numpy as np

def levenshtein(x,y):
    #Initialisierung
    len_x = len(x)
    len_y = len(y)
    marix = np.zeros( (len_x, len_y) )

    #Trage Basisfaelle in die Matrix ein
    for i in range (0, len_x):
        matrix[i][0] = i

    for j in range (0, len_y):
        matrix[0][j] = j

    print("Matrix = ", matrix)

    #Fuelle den Rest der Matrix aus, entweder wird eine Stelle ersetzt,
    #geloescht oder eingefuegt
    for i in range (1, len_x):
        for j in range (1, len_y):
            matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j-1]+1,
                               matrix[i][j-1]+1, matrix[i-1][j]+1)

    return matrix[len_x-1][len_y-1]
