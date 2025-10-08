v1 <- c(1, 4, 5)
v2 <- c(10, 20, 30, 40, 50)
arr1 <- array(c(v1, v2), dim = c(3, 3, 2)) # 2 matrices of 3x3
print(arr1)

col1 <- c("c1", "c2", "c3")
r1 <- c("r1", "r2", "r3")
mat_name <- c("mat1", "mat2", "mat3", "mat4")
arr2 <- array(c(v1, v2), dim = c(3, 3, 4), dimnames = list(r1, col1, mat_name))
print(arr2)

print(arr2[3, 2, 2]) # arr[3][2] of 2nsd matrix
print(arr2[, 2, 1]) # 2nd col of 1st matrix
print(arr2[, , 4]) # full 4th matrix

v1 <- c(1, 4, 5)
v2 <- c(10, 20, 30, 40, 50)
arr3 <- array(c(v1, v2), dim = c(3, 3, 2))
print(arr3)
arr4 <- arr1 + arr3
print(arr4)