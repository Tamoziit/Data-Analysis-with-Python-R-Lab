prime_numbers <- function(n) {
  if (n < 2) {
    integer(0)
  }

  is_prime <- rep(TRUE, n)
  is_prime[1] <- FALSE

  for (i in 2:floor(sqrt(n))) {
    if (is_prime[i]) {
      is_prime[seq(i * i, n, by = i)] <- FALSE
    }
  }

  primes <- which(is_prime)
  primes
}

cat(prime_numbers(25), "\n")