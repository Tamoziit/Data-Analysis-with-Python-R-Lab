gcd <- function(n1, n2) {
  if (n1 %% n2 == 0) {
    n2
  } else {
    gcd(n2, n1 %% n2)
  }
}

gcd_n <- function(arr) {
  gcd_res <- arr[1]

  for (i in 2:length(arr)) {
    gcd_res <- gcd(gcd_res, arr[i])
  }

  gcd_res
}

arr <- scan(what = integer())
cat("GCD of", arr, "=", gcd_n(arr), "\n")
