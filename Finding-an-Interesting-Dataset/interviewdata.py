import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

csv_data = pandas.read_csv("datascience_questions.csv")

print(csv_data)