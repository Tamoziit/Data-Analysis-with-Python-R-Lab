print(abs(-5))
print(sqrt(45))
print(ceiling(5.6))
print(floor(5.6))

y <- c(1.5, 5.6, 8.6)
print(trunc(y)) # truncates (removes decimal part) all values of a vector

print(sin(5))
print(sinh(5))
print(log(5)) # log base e
print(log10(5))
print(log2(5))
print(exp(5))

a <- "1234567890"
print(substr(a, 3, 8)) # index starts from 1 (not 0) in R

s <- "YbjakD"
print(tolower(s))
print(toupper(s))

s2 <- c("abcd", "bcbd", "abcdbcbd")
pattern <- "^abc" # starts with abc
print(grep(pattern, s2)) # grep() from pattern searching

data <- c(0:10, 40) # 0, 1, 2, 3, ..., 10, 40
print(sum(data))
print(mean(data))
cat(max(data), min(data), "\n")
print(range(data)) # range of the vector
print(sd(data)) # Standard Deviation