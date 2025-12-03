size <- 100000

die1 <- sample(1:6, size, replace = TRUE)
die2 <- sample(1:6, size, replace = TRUE)

sum_die <- die1 + die2
count <- sum(sum_die == 8)
prob <- count / size

cat("Simulated:", prob, "\n")
cat("Actual:", (5 / 36), "\n")