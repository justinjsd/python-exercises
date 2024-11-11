# Write your solution here

def transpose(matrix: list):
    i = 0
    j = 0
    while i < len(matrix):
        j += i
        while j < len(matrix):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
            j += 1
        i += 1
        j = 0

if __name__ == "__main__":
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    transpose(matrix)
    print(matrix)