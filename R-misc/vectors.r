a <- c(1, 0, 9, 8)
print(a)
b <- -3:5
print(b)

# sequence
sq <- seq(1, 5)
print(sq)
sq <- seq(1, 5, by = 0.5) # step up by .5 & not by default 1
print(sq)
sq <- seq(1, 4, length.out = 5) # equally divides 1 to 4 such that 5 nos. are printed out (by auto adjusting step up, here = 0.75) # nolint: line_length_linter.
print(sq)

# atomic vectors
numv <- c(12.3, 4.5, 6.9)
print(numv)
print(class(numv))
intv <- as.integer(c(1, 2, 3, 4))
print(intv)
print(class(intv))
intv2 <- c(12L, 4L, 6L) # auto-casting to integer
print(intv2)
print(class(intv2))

# indexing
vec <- c("Ram" = 12, "alex" = 32, "Mohan" = 31) # key = value # nolint
print(vec)
print(vec["alex"]) # access by key
print(vec[2]) # same as vec["alex"]

test <- c(1, 2, 3, 4)
print(test[c(TRUE, FALSE, FALSE, TRUE)]) # only prints values corresponding to TRUE # nolint

# Vector Ops
v1 <- c(1, 2, 3, 4)
v2 <- c("Ram", "Alex", "Mohan")
v3 <- c(v1, v2) # combining vectors
print(v3)

v1 <- c(1, 2, 3, 4, 8, 5)
v2 <- c(7, 5, 4, 3, 5, 0)
print(v1 + v2)
print(v1 / v2)

test2 <- c("Ram", "Alex", "Mohan", "Sohan")
print(test2[-2]) # prints all components of test2 except one at index 2
print(test2[2:4]) # range print
print(test2[c(2, 3)]) # prints the indices as specified in the nested vector
print(test2[c(2, 3, 1, 2)]) # repetition allowed

# naming of vector
z <- c("Ram", "Alex", "Mohan", "Sohan")
names(z) <- c("n1", "n2", "n3", "n4") # assigning names (codes) to each element of the vector # nolint
print(z)
print(z["n1"]) # indexing by name
