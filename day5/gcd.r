gcd_iterative <- function(n1, n2) {
  if (n1 < n2) {
    min <- n1
  } else {
    min <- n2
  }

  gcd <- 1

  for (i in 2:min) {
    if (n1 %% i == 0 && n2 %% i == 0) {
      gcd <- i
    }
  }

  gcd
}

gcd_recursive <- function(n1, n2) {
  if (n1 %% n2 == 0) {
    n2
  } else {
    gcd_recursive(n2, n1 %% n2)
  }
}

n1 <- as.integer(readline("Enter 1st no.: "))
n2 <- as.integer(readline("Enter 2nd no.: "))

cat("GCD of", n1, "&", n2, "by Iterative method =", gcd_iterative(n1, n2), "\n")
cat("GCD of", n1, "&", n2, "by Recursive method =", gcd_recursive(n1, n2), "\n")
