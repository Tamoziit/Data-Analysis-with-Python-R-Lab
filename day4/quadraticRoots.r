a <- as.numeric(readline("Enter value of a: "))
b <- as.numeric(readline("Enter value of b: "))
c <- as.numeric(readline("Enter value of c: "))

dis <- (b * b) - (4.0 * a * c)

if (a == 0) {
  print("The Equation is linear")
  x <- -c / b
  cat("X =", x, "\n")
} else if (abs(dis) <= 1.00e-5) {
  print("Roots are real & identical")
  x <- -b / (2.0 * a)
  cat("1st Root =", x, "\n")
  cat("2nd Root =", x, "\n")
} else if (dis > 0) {
  print("Roots are real & distinct")
  x <- (-b + dis**0.5) / (2.0 * a)
  y <- (-b - dis**0.5) / (2.0 * a)
  cat("1st Root =", x, "\n")
  cat("2nd Root =", y, "\n")
} else {
  print("Roots are imaginary")
  real <- -b / (2.0 * a)
  img <- (abs(dis)**0.5) / (2.0 * a)
  formatted_text <- sprintf("1st Root = %f + %fi\n2nd Root = %f - %fi\n", real, img, real, img) # nolint: line_length_linter.
  cat(formatted_text)
}
