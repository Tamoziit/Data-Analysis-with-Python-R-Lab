employees <- data.frame(Age = c(23, 21, 34, 44, 32),
                        Height = c(76, 62, 63, 69, 72),
                        Weight = c(50, 52, 80, 65, 70),
                        Gender = c("Female", "Female", "Male", "Male", "Female")) # nolint: line_length_linter.
print(employees)

# i)
print(employees$Weight)

# ii)
employees$Gender <- as.factor(employees$Gender)
print(employees$Gender)
employees$Gender <- as.numeric(employees$Gender)
print(employees$Gender)

# iii)
print(unique(employees$Age))

# iv)
print(sort(unique(employees$Age)))

# v)
employees$Height <- NULL
print(employees)