cel1 <- as.numeric(readline("Enter temp. in Celcius: "))
fahr1 <- (9.0 * cel1) / 5.0 + 32.0
cat(cel1, "deg. Celcius =", fahr1, "deg. Fahrenheit\n")

fahr2 <- as.numeric(readline("Enter temp. in Fahrenheit: "))
cel2 <- (5.0 / 9.0) * (fahr2 - 32.0)
cat(fahr2, "deg. Fahrenheit =", cel2, "deg. Celcius\n")