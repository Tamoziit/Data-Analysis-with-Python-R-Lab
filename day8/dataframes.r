# Dataframe
df <- data.frame(ID = c(1, 2, 3, 4, 5),
                 Name = c("AAA", "BBB", "CCC", "DDD", "EEE"),
                 Sub1 = c(56, 70, 90, 65, 96),
                 Sub2 = c(57, 70, 80, 70, 97),
                 Sub3 = c(58, 70, 70, 50, 98))

print(df)

df$Total <- df$Sub1 + df$Sub2 + df$Sub3
df$Average <- df$Total / 3
print(df)

df$Grade <- ifelse(df$Average >= 90, "O", ifelse(df$Average >= 80, "A", ifelse(df$Average >= 70, "B", ifelse(df$Average >= 60, "C", ifelse(df$Average >= 50, "D", "F"))))) # nolint: line_length_linter.
print(df)

df <- df[order(df$Average, decreasing = TRUE), ]
print(df)

# Stats
subjects <- df[, c("Sub1", "Sub2", "Sub3")]

stats <- data.frame(
  Subjects = names(subjects),
  Mean = sapply(subjects, mean),
  Median = sapply(subjects, median),
  Standard_Deviation = sapply(subjects, sd),
  Variance = sapply(subjects, var)
)

print(stats)