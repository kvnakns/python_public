import csv
import pandas

print()
print('----------csv.reader() function time-----------')
print()


df = pandas.read_csv('/<My path goes here>/FileDrop/customers-100.csv',
		header=0,
        index_col="Id",
		usecols=["Id", "Customer Id", "First Name","Last Name"], nrows=65)

print(df)


# Export the file to the defined directory
df.to_csv("/<My path goes here>/FileDrop/cleaned_customers-100_data.csv")

# Export the file to the defined directory - BUT, change to TAB deliminited
df.to_csv("/<My path goes here>/FileDrop/cleaned_customers-100_data_tab.csv", sep="\t")