x1 <- as.numeric(readline("Enter x1: "))
y1 <- as.numeric(readline("Enter y1: "))
x2 <- as.numeric(readline("Enter x2: "))
y2 <- as.numeric(readline("Enter y2: "))

dist <- ((x2 - x1) ** 2.0 + (y2 - y1) ** 2.0) ** 0.5

formatted_text <- sprintf("Distance between (%f, %f) & (%f, %f) = %f", x1, y1, x2, y2, dist) # nolint: line_length_linter.
print(formatted_text, quote = FALSE)