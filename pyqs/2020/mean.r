get_mean <- function(vec) {
  n <- length(vec)
  total <- 0
  i <- 1

  repeat {
    total <- total + vec[i]
    i <- i + 1

    if (i > n) {
      break
    }
  }

  mean <- total / n
  mean
}

print(get_mean(c(2, 3, 4, 5, 6)))