def jordan_gauss(mx):

    mx_rows = len(mx)
    mx_cols = len(mx[0])

    for k in range(mx_cols - 1):

        if abs(mx[k][k]) < 0.00001:
            o = k + 1
            while True:
                if abs(mx[o][k]) > 0.00001 or o > mx_rows:
                    break
                o += 1
            mx[k], mx[o] = mx[o], mx[k] # swap rows

        for i in range(mx_rows):
            for j in range(k + 1, mx_cols):
                if i != k:
                    mx[i][j] = (mx[i][j] * mx[k][k] - mx[k][j] * mx[i][k]) / mx[k][k]

        for i in range(mx_rows):
            if i != k: mx[i][k] = 0

        for j in range(mx_cols - 1, k, -1):
            mx[k][j] = mx[k][j] / mx[k][k]

matrixx = [[1, -1, 1, 1],
          [1, 1, 1, -3],
          [1, 2, 4, -2]]

print(matrixx)
jordan_gauss(matrixx)
print(matrixx)