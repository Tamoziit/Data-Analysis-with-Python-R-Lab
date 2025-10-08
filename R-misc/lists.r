vec <- c(8, 9, 7, 6)
char_vec <- c("Ram", "Alex", "Mohan", "Sohan")
logic_vec <- c(TRUE, FALSE, FALSE, TRUE)
list1 <- list(vec, char_vec, logic_vec) # list allows heterogenous <DTypes>
print(list1)

lst2 <- list("A", "B", c(1, 2, 3, 4), TRUE, FALSE, 52L, 56.78)
print(lst2)

# naminng
lst3 <- list(c("A", "B", "C"), c(9, 8, 7), list("B.Tech", "MBA", "B.Sc"))
print(lst3)
names(lst3) <- c("Students", "Marks", "Courses")
print(lst3)

# Accessing list
print(lst3[3]) # by indexing
print(lst3["Marks"]) # by name
print(lst3$Students) # by $

# List -> Vector #nolint
lst4 <- list(5:9)
lst5 <- list(14:18)
print(lst4)
print(lst5)
vector1 <- unlist(lst4)
print(vector1)
print(class(vector1))
vector2 <- unlist(lst5)
print(vector2)
print(class(vector2))
print(vector1 + vector2) # after converting to vector, vector ops possible

# List merging
merge <- list(lst4, lst5)
print(merge)