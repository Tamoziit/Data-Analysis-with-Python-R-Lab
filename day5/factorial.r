factorial_iterative <- function(n) {
  fact <- 1
  if (n == 0) {
    return(fact)
  }

  for (i in 1:n) {
    fact <- fact * i
  }
  fact
}

factorial_recursive <- function(n) {
  if (n == 0) {
    1
  } else if (n == 1) {
    1
  } else {
    n * factorial_recursive(n - 1)
  }
}

n <- as.integer(readline("Enter a no.: "))
cat("Factorial by Iterative Method =", factorial_iterative(n), "\n")
cat("Factorial by Recursive Method =", factorial_recursive(n), "\n")