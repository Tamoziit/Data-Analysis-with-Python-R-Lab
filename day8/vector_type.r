create_vector <- function(type, len) {
  vec <- vector(mode = type, length = len)
  for (i in 1:len) {
    value <- readline(paste("Enter", type, "for index", i, ": "))

    if (type == "numeric") {
      value <- as.numeric(value)
    } else if (type == "integer") {
      value <- as.integer(value)
    } else if (type == "logical") {
      value <- as.logical(value)
    } else if (type == "character") {
      value <- as.character(value)
    } else if (type == "complex") {
      value <- as.complex(value)
    }

    vec[i] <- value
  }

  vec
}

type <- readline("Enter type of the vector: ")
len <- readline("Enter length of the vector: ")

res <- create_vector(type, len)
print(res)
