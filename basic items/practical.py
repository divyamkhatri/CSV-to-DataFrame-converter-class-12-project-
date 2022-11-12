#Import Section
import pandas as pd
import numpy as np
import time
from matplotlib import pyplot as plt

#Default Path of CSV(in current folder)
path = "abc.csv"

#Basic SetUp
print("Do u want to use any other CSV file by default abc.csv is used")
ques = input("if u want to use then type y otherwise skip this:")

if ques == "y":
    additional_df = input(r"Enter path here:")
    try:
        pd.read_csv(additional_df)
        print("Your File has been succesfully imported!")
        path = additional_df
    except:
        print("path isn't valid")
        print("Here we are continuing with default dataframe")
else:
    print("ok,now")
    print("We are continuing with default DataFrame")

#DataFrame settings
base_df = pd.read_csv(path)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
time.sleep(2)
             

#Defining Methods

def show_df():
    print("Currently Showing DataFrame")
    print(base_df)
    



def df_without_index():
    print("DataFrame without indexes(row heading)")
    no_index_df = pd.read_csv(path,index_col=0)
    print(no_index_df)


    
def line_chart():
    print("All availble options of line charts are present here")
    print("Yaxis vs Xaxis")
    
    #Taking all Available columns heading as a value in a Chart
    index = base_df.columns


    #Making a sequence of all available options
    count = 1
    avail_opt = []
    for x_side in index:
        for y_side in index:
            if y_side == x_side:
                pass
            else:
                print(count,x_side,"vs",y_side)
                avail_opt.append([count,x_side,y_side])
                count += 1
    chart_choice = int(input("Enter any no against which you want to make a chart from above:"))

    #Now we will check that user has input a vaild option
    if chart_choice <= len(avail_opt):
        
        #Now we will take that row from avail_opt that we have make earlier
        a = avail_opt[(chart_choice-1)]
        print(a)
        
        #Now we will take names of columns which we need to plot
        verti_side = a[1]
        horiz_side = a[2]
        
        #retrivenig that columns from base_df 
        xaxis = base_df[horiz_side]
        yaxis = base_df[verti_side]
        
        #plotting the values
        plt.plot(xaxis,yaxis)
        plt.xlabel(horiz_side)
        plt.ylabel(verti_side)
        plt.show()
        
    else:
        print("Invaild Choice")


def multiple_line_chart():
    print("All availble options of line charts are present here")
    print("Yaxis vs Xaxis and Yaxis vs Xaxis")

    #Taking all Available columns heading as a value in a Chart
    columns = base_df.columns

    #Making a sequence of all available options
    count = 1
    avail_opt = []
    for x_side in columns:
        for y_side in columns:
            if y_side == x_side:
                pass
            else:
                #as we not want to print this in output
                #print(count,x_side,"vs",y_side)
                avail_opt.append([count,x_side,y_side])
                count += 1

    #Making a sequence for multiple line chart
    count_multi = 1
    avail_multi = []
    #Calculating how many times this loop can run
    
    for pair1 in avail_opt:
        for pair2 in avail_opt:
            if pair1 == pair2:
                pass
            else:
                if pair1[2] == pair2[2]:
                    print(count_multi,pair1,pair2)
                    avail_multi.append([count_multi,pair1,pair2])
                    count_multi += 1
                    
    chart_choice = int(input("Enter any no from above:"))
    if chart_choice <= len(avail_multi):

        #Now we will take that row from avail_multi that we have make earlier
        #Here a will store that values of two chart that we are plotting
        a = avail_multi[(chart_choice-1)]
        
        chart1 = a[1]
        chart2 = a[2]

        #Now we will plot 1st chart
        verti_side1 = chart1[1]
        horiz_side1 = chart1[2]

        xaxis1 = base_df[horiz_side1]
        yaxis1 = base_df[verti_side1]
        plt.plot(xaxis1,yaxis1)

        #Now we will plot 2nd chart
        verti_side2 = chart2[1]
        horiz_side2 = chart2[2]

        xaxis2 = base_df[horiz_side2]
        yaxis2 = base_df[verti_side2]

        plt.xlabel(horiz_side1)
        plt.ylabel((verti_side1,"and",verti_side2))
        plt.plot(xaxis2,yaxis2)
        plt.show()
       
    else:
        print("Invalid choice")
    


def bar_chart():
    print("All availble options of bar charts are present here")
    print("Yaxis vs Xaxis")
    
    #Taking all Available columns heading as a value in a Chart
    columns = base_df.columns

    #Making a sequence of all available options
    count = 1
    avail_opt = []
    for x_side in columns:
        for y_side in columns:
            if y_side == x_side:
                pass
            else:
                print(count,x_side,"vs",y_side)
                avail_opt.append([count,x_side,y_side])
                count += 1
                
    chart_choice = int(input("Enter any no against which you want to make a chart from above:"))

    #Now we will check that user has input a vaild option
    if chart_choice <= len(avail_opt):
        
        #Now we will take that row from avail_opt that we have make earlier
        a = avail_opt[(chart_choice-1)]
        print(a)
        
        #Now we will take names of columns which we need to plot
        verti_side = a[1]
        horiz_side = a[2]
        
        #retrivenig that columns from base_df 
        xaxis = base_df[horiz_side]
        yaxis = base_df[verti_side]
        
        #plotting the values
        plt.bar(xaxis,yaxis)
        plt.xlabel(horiz_side)
        plt.ylabel(verti_side)
        plt.show()
        
    else:
        print("Invaild Choice")



def sorting_data():
    print("By which criteria u want to sort")
    print("Currently available options are:")

    #Take and display names of available columns
    col_names = base_df.columns
    count = 1
    for avail_opt in col_names:
        print(count,avail_opt)
        count += 1

    #Taking input fom user of name of column
    option = int(input("Choose any one from above:"))
    print("===============================================")
    
    #Checking that enter output is from available output
    if option <= len(base_df.columns):
        #After checking we will extract that column
        choice = col_names[option-1]
        print("DataFrame is sorting by",choice)
        new_df = pd.DataFrame(base_df)
        print(new_df.sort_values([choice]))
    
    else:
        print("entered value is not in option")



def extracting_rows():
    print("What you want to do ?")
    print("1.Extracting top rows")
    print("2.Extracting bottom rows")
    choice = int(input("choose any one:"))
    if choice == 1:
        n = int(input("How Many Rows From Above:"))
        print(base_df.head(n))
    elif choice == 2:
        n = int(input("How Many Rows From bottom:"))
        print(base_df.tail(n))
        

    
#Running a valid loop
run = True
while run:
    time.sleep(4)
    #Various options that are to be displayed on Users Screen
    print("-------------------Python and CSV Connectivity-------------------")
    print("------------------Currently Available DataFrame------------------")
    print("")
    print("                      Your CSV file's Records                    ")
    print(base_df)
    print("")
    print("Choose any number to perform a task")
    print("Currently available options are:")
    print("========== Displaying Data ==========")
    print("1.Show DataFrame")
    print("2.Displaying DataFrame without indexes")
    print("======== Visualization of data ==========")
    print("3.Single Line Charts")
    print("4.Multiple Line Charts")
    print("5.Bar Charts")
    print("======== Additional Functions =======")
    print("6.Sorting data as per requirement")
    print("7.Reading top and bottom records as per users requirement")
    print("=====================================")
    
    #Taking inputs and executing it
    task = int(input("Now which function you need to perform: "))

    if task == 1:
        show_df()
    elif task == 2:
        df_without_index()
    elif task == 3:
        line_chart()
    elif task == 4:
        multiple_line_chart()
    elif task == 5:
        bar_chart()
    elif task == 6:
        sorting_data()
    elif task == 7:
        extracting_rows()
    else:
        print("Invalid Choice")

    

