fibonacci_iterative_range <- function(start, end) {
  if (start <= 0 || end <= 0 || start > end) {
    stop("Invalid range")
  }

  if (end == 1) {
    return(1)
  }

  fib <- numeric(end)
  fib[1] <- 1
  fib[2] <- 1

  if (end >= 3) {
    for (i in 3:end) {
      fib[i] <- fib[i - 1] + fib[i - 2]
    }
  }

  fib[start:end]
}

fib_recursive <- function(n) {
  if (n == 1 || n == 2) return(1)
  fib_recursive(n - 1) + fib_recursive(n - 2)
}

fibonacci_recursive_range <- function(start, end) {
  if (start <= 0 || end <= 0 || start > end) {
    stop("Invalid range")
  }

  result <- numeric(end - start + 1)
  idx <- 1
  for (i in start:end) {
    result[idx] <- fib_recursive(i)
    idx <- idx + 1
  }

  result
}

start <- as.integer(readline("Enter starting pos.: "))
end <- as.integer(readline("Enter ending pos.: "))
cat("By Iterative Method =", fibonacci_iterative_range(start, end), "\n")
cat("By Recursive Method =", fibonacci_recursive_range(start, end), "\n")