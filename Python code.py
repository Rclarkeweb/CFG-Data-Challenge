# The CFG Python Data Analysis Challenge

# Import pandas module
import pandas as pd

# Import CSV module
import csv


# Create a function to perform all calculations
def challenge():
    # Select all data from dataset
    df = pd.read_csv('sales_dataset.csv')

    # TASK 1: Calculate the total sales for each product
    # Create a Total Sales Column
    # Calculate the total sales column by multiplying the sales by quantity sold and save to new column
    df['Total Sales'] = df['Sale Price'] * df['Quantity Sold']
    # Save Total Sales nto a variable
    total_sales = df[['Product Name', 'Total Sales']]

    # TASK 2: Determine the average sale price for each product category
    # Group the column category by categories and calculate the mean of the sale price
    average = df.groupby("Category")["Sale Price"].mean().round(2)

    # TASK 3: Identify the month with the highest sales and the month with the lowest sales
    # Month with the Highest Sales
    # Group data by month, calculate the sum of the total sales for each month, then only display the largest
    highest_month = df.groupby("Month")["Total Sales"].sum().nlargest(1)

    # Month with the Lowest Sales
    # Group data by month, calculate the sum of the total sales for each month, then only display the smallest
    lowest_month = df.groupby("Month")["Total Sales"].sum().nsmallest(1)

    # TASK 4: Determine which customers made the most purchases and how much they spent in total
    # Group data by Customer Name, sum of the total sales (sale price * quantity), save to a variable, only show top 3
    customer_sales_by_price_and_quantity = df.groupby("Customer Name")["Total Sales"].sum().nlargest(3)

    # Group the data by Customer Name, add up the Sale Price, save to a variable and only show the top 3
    # customer_sales_by_price = df.groupby("Customer Name")["Sale Price"].sum().nlargest(3)

    # Write analysis findings to a CSV file
    with open("Data_analysis.csv", "w", newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # Write and display headings and display data findings for each task
        csvfile.write("TASK 1: Calculate the total sales for each product \n")
        csvwriter.writerow([total_sales])
        csvfile.write("\n")
        csvfile.write("TASK 2: Determine the average sale price for each product category \n")
        csvwriter.writerow([average])
        csvfile.write("\n")
        csvfile.write("TASK 3: Identify the month with the highest sales and the month with the lowest sales \n")
        csvfile.write("Month with the Highest Sales \n")
        csvwriter.writerow([highest_month])
        csvfile.write("\n")
        csvfile.write("Month with the Lowest Sales \n")
        csvwriter.writerow([lowest_month])
        csvfile.write("\n")
        csvfile.write("TASK 4: Determine which customers made the most purchases and how much they spent in total \n")
        csvwriter.writerow([customer_sales_by_price_and_quantity])

    print('Finished')


challenge()
