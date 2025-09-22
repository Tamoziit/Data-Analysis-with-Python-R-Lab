df <- data.frame(ID = c(10, 11, 12, 13),
                 Name = c("Sai", "Ram", "Deepika", "Dipesh"),
                 DOB = as.Date(c("1990-10-02", "1981-03-24", "1987-06-14", "1985-08-16"))) # nolint

str(df)

print(df, row.names = TRUE)