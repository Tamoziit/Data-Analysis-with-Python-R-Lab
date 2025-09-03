curve(sin, 0, 2 * pi, xname = "theta", col = "blue")
curve(cos, 0, 2 * pi, add = TRUE, col = "red")

plot(c(0, 100), c(0, 100), xlab = "x", ylab = "y")

color <- readline("Preferred Colour: ")
x <- c(10, 50, 50, 10, 10)
y <- c(10, 10, 50, 50, 10)
lines(x, y, col = color)