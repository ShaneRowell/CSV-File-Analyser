#Author: SHANE ROWELL FERNANDO
#Date: 23/11/2024

# Task A: Input Validation
def is_leap_year(year): #This function validates if the year(YYYY) entered by the user is a leap year.
    # Checks if a year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def day_validation(): #This function validates the day(dd) entered by the user.
    while True:
        try:
            day = int(input("Please enter the day of the survey in the format dd: "))
            if day < 1 or day > 31:
                print("Out of range - values must be in the range 1 to 31.")
            else:
                return day
        except ValueError: #Error handling.
            print("Integer required")

def month_validation(): #This function validates the month(mm) entered by the user.
    while True:
        try:
            month = int(input("Please enter the month of the survey in the format MM: "))
            if month < 1 or month > 12:
                print("Out of range - values must be in the range 1 to 12.")
            else:
                return month
        except ValueError: #Error handling.
            print("Integer required")

def year_validation(): #This function validates the year(YYYY) entered by the user.
    while True:
        try:
            year = int(input("Please enter the year of the survey in the format YYYY: "))
            if year < 2000 or year > 2024:
                print("Out of range - values must be in the range 2000 to 2024.")
            else:
                return year
        except ValueError: #Error handling.
            print("Integer required")

def validate_date(day, month, year): #This function validates the date(dd/mm/yyyy) entered by the user for edge case scenarios.
    # list defining the maximum days in the given month using a if ladder.
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    elif month == 2:
        max_days = 29 if is_leap_year(year) else 28
    else: #Error handling.
        print("Invalid month.")
        return False

    if day < 1 or day > max_days:
        print(f"Invalid date - day must be in the range 1 to {max_days} for the given month and year.")
        return False
    return True
while True: #Calling the date functions
    day = day_validation()
    month = month_validation()
    year = year_validation()
    if validate_date(day, month, year):
        date = f"{day:02}/{month:02}/{year:04}" #Locally defining the date variable.
        break
    else:
        print("The entered date is not valid. Please enter the date again.")

date = f"{day:02}/{month:02}/{year:04}" #Globally defining the date variable to pass through process functions as a parameter.

# Task B: Processed Outcomes
import csv

def file_selection(): #This function validates the file name entered by the user.
    while True:
        try: #This try block is used for error handling checking if the file exist or not.
            file_name = input("Enter the Name of the csv file: ")
            f = open(file_name,"r")
            f.close()
            return file_name
            break
        except:
            print("File does not exist,(might have forgotten '.csv')")
    
def total_vehicles(file_name,date): #This function calculates the total numbers of vehicals for the selected date.
    with open(file_name, "r") as file: #with,open,as functions are used for more integrity rather than using manual file.open/close functions.
        data_reader = csv.reader(file)
        headers = next(data_reader)
        #Below code defines the specific variables to compare
        date_index = headers.index("Date") #This code skips the headers of the csv file when processing, will be used in all following functions.
        total_count = 0
        for row in data_reader:
            if row[date_index] == date:
                total_count = total_count +1
        
        print(f"The total number of vehicals recorded for this date is {total_count}.")
        return total_count

def total_trucks(file_name,date): #This function calculates the total numbers of trucks for the selected date.
    vehical = "Truck"
    with open(file_name, "r") as file:
        data_reader = csv.reader(file)
        headers = next(data_reader)
        #Below code defines the specific variables to compare
        vehical_type_index = headers.index("VehicleType")
        date_index = headers.index("Date")
        truck_count = 0
        for row in data_reader:
            # below code compares required feilds for the desired output and incrementing using a count variable.
            if row[date_index] == date and row[vehical_type_index] == vehical: 
                truck_count = truck_count +1
        print(f"The total number of trucks recorded for this date is {truck_count}.")
        return truck_count
        
def total_ev(file_name,date): #This function calculates the total numbers of electric vehicals for the selected date.
    electric = "TRUE"
    with open(file_name, "r") as file:
        data_reader = csv.reader(file)
        headers = next(data_reader)
        #Below code defines the specific variables to compare.
        electric_index = headers.index("elctricHybrid")
        date_index = headers.index("Date")
        ev_count = 0
        # below code compares required feilds for the desired output and incrementing using a count variable.
        for row in data_reader:
            if row[date_index] == date and row[electric_index] == electric:
                ev_count = ev_count +1
        print(f"The total number of electric vehicles recorded for this date is {ev_count}.")
        return ev_count 
        
def total_TwoWheeled(file_name,date): #This function calculates the total numbers of two wheeled vehicles for the selected date.
    twoWheeled = ("Bicycle", "Motorcycle", "Scooter")
    with open(file_name, "r") as file:
        data_reader = csv.reader(file)
        headers = next(data_reader)
        #Below code defines the specific variables to compare.
        vehicle_type_index = headers.index("VehicleType")
        date_index = headers.index("Date")
        twoWheel_count = 0
        for row in data_reader:
            # below code compares required feilds for the desired output and incrementing using a count variable.
            if row[date_index] == date and row[vehicle_type_index] in twoWheeled: 
                twoWheel_count = twoWheel_count +1
        print(f"The total number of two wheeled vehicles recorded for this date is {twoWheel_count}.")
        return twoWheel_count

def leave_elm_buss(file_name,date): #This function calculates the total numbers of busses leaving Elm Avenue/Rabbit Road for the selected date.
   junction = "Elm Avenue/Rabbit Road"
   vehicle = "Buss"
   direction = "N"
   with open(file_name, "r") as file:
        data_reader = csv.reader(file)
        headers = next(data_reader)
        #Below code defines the specific variables to compare.
        vehicle_type_index = headers.index("VehicleType")
        date_index = headers.index("Date")
        junction_index = headers.index("JunctionName")
        direction_out_index = headers.index("travel_Direction_out")
        leave_count = 0
        for row in data_reader:
            # below code compares required feilds for the desired output and incrementing using a count variable.
            if row[date_index] == date and row[vehicle_type_index] == vehicle and row[junction_index]== junction and row[direction_out_index] == direction:
                leave_count = leave_count+1
        print(f"The total number Busses leaving Elm Avenue/Rabbit Road heading North is {leave_count}.")
        return leave_count

def total_not_turning(file_name, date):  #This function calculates the total numbers of vehicals not turning for the selected date.
    directions = ["N","S","E","W","NE","NW","SE","SW"]
    with open(file_name, "r") as file:
        data_reader = csv.reader(file)
        headers = next(data_reader)
        #Below code defines the specific variables to compare.
        date_index = headers.index("Date")
        direction_in_index = headers.index("travel_Direction_in")
        direction_out_index = headers.index("travel_Direction_out")
        same_direction_count = 0
        for row in data_reader:
            # below code compares required feilds for the desired output and incrementing using a count variable.
            if (row[date_index] == date and row[direction_in_index] in directions and row[direction_out_index] in directions and row[direction_in_index] == row[direction_out_index]):
                same_direction_count = same_direction_count+1
        print(f"The total number of vehicles through both junctions not turning left or right is {same_direction_count}.")
        return same_direction_count
    
def percentage_trucks(total_count, truck_count):  #This function calculates the percentage of trucks for the selected date.
    if truck_count > 0:
        truck_percentage = round((truck_count / total_count) * 100)
        print(f"The percentage of total vehicles recorded that are trucks is {truck_percentage}%")
    else:  #This else statement is to avoid zero division error.
        truck_percentage = 0
        print("The percentage of total vehicles recorded that are trucks is 0%")
    return round(truck_percentage)

def avg_bicycles_per_hour(file_name, date):  #This function calculates the average bicycles per four for the selected date.
    bicycle_count_per_hour = [0] * 24  # This code creates a list to count bicycles for each hour from 0 to 23 hours.
    with open(file_name, "r") as file:
        data_reader = csv.reader(file)
        headers = next(data_reader)
        #Below code defines the specific variables to compare.
        date_index = headers.index("Date")
        time_index = headers.index("timeOfDay")
        vehicle_type_index = headers.index("VehicleType")
        # below code compares required feilds for the desired output and incrementing using a count variable.
        for row in data_reader:
            if row[date_index] == date and row[vehicle_type_index] == "Bicycle":
                hour_first_digit = int(row[time_index].split(":")[0])  # Extracts the exact hour and ignores the miniute values
                bicycle_count_per_hour[hour_first_digit] += 1
    total_hours = sum(1 for count in bicycle_count_per_hour if count > 0) # This code will calculate the total total hours and average
    total_bicycles = sum(bicycle_count_per_hour)
    
    if total_hours > 0: #If function used for error handling.
        average_bicycles_per_hour = round(total_bicycles / total_hours)
    else:
        average_bicycles_per_hour = 0 #The else statement avoids zero division error.

    print(f"The average number of bicycles per hour for this date is {average_bicycles_per_hour}.")
    return average_bicycles_per_hour

def total_over_speed_limit(file_name,date):  #This function calculates the total numbers of vehicals over the speed limit for the selected date.
    with open(file_name, "r") as file:
        data_reader = csv.reader(file)
        headers = next(data_reader)
        #Below code defines the specific variables to compare.
        speed_index = headers.index("VehicleSpeed")
        speed_limit_index = headers.index("JunctionSpeedLimit")
        date_index = headers.index("Date")
        over_speed_limit_count = 0
        for row in data_reader:
            # below code compares required feilds for the desired output and incrementing using a count variable.
            if row[date_index] == date and ( float(row[speed_index]) > float(row[speed_limit_index]) ): #float function used to covert strings to float values.
                over_speed_limit_count = over_speed_limit_count +1
        print(f"The total number of vehicles over the speed limit recorded for this date is {over_speed_limit_count}.")
        return over_speed_limit_count

def vehicles_only_ElmAve(file_name,date): #This function calculates the total numbers of vehicals passing through Elm Avenue/Rabbit Road for the selected date.
    junction = "Elm Avenue/Rabbit Road"
    with open(file_name, "r") as file:
        data_reader = csv.reader(file)
        headers = next(data_reader)
        #Below code defines the specific variables to compare.
        junction_index = headers.index("JunctionName")
        date_index = headers.index("Date")
        ElmAve_count = 0
        # below code compares required feilds for the desired output and incrementing using a count variable.
        for row in data_reader:
            if row[date_index] == date and row[junction_index] == junction:
                ElmAve_count = ElmAve_count +1
        print(f"The total number of vehicles through Elm Avenue/Rabbit Road recorded for this date is {ElmAve_count}.")
        return ElmAve_count

def vehicles_only_HanHighway(file_name,date): #This function calculates the total numbers of vehicals passing through Hanley Highway/Westway for the selected date. 
    junction = "Hanley Highway/Westway"
    with open(file_name, "r") as file:
        data_reader = csv.reader(file)
        headers = next(data_reader)
        #Below code defines the specific variables to compare.
        junction_index = headers.index("JunctionName")
        date_index = headers.index("Date")
        HanHighway_count = 0
        # below code compares required feilds for the desired output and incrementing using a count variable.
        for row in data_reader:
            if row[date_index] == date and row[junction_index] == junction:
                HanHighway_count = HanHighway_count +1
        print(f"The total number of vehicles through Hanley Highway/Westway recorded for this date is {HanHighway_count}.")
        return HanHighway_count

def percentage_only_scooters_ElmAve(file_name,date,ElmAve_count): #This function calculates the percentage of vehicals that are scooters for the selected date.
    junction = "Elm Avenue/Rabbit Road"
    vehicle = "Scooter"
    with open(file_name, "r") as file:
        data_reader = csv.reader(file)
        headers = next(data_reader)
        #Below code defines the specific variables to compare.
        vehicle_type_index = headers.index("VehicleType")
        date_index = headers.index("Date")
        junction_index = headers.index("JunctionName")
        scooter_count = 0
        for row in data_reader: #If ladder is utilized for error handling.
            # below code compares required feilds for the desired output and incrementing using a count variable.
            if row[date_index] == date and row[vehicle_type_index] == vehicle and row[junction_index]== junction:
                scooter_count = scooter_count+1
        if scooter_count > 0:
            percentage_scooters = round((scooter_count/ElmAve_count)*100)
            print(f"{percentage_scooters}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.")
        else:
            percentage_scooters = 0 #This code prevents zero divison error.
            print("0% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.")
        return percentage_scooters
    
def total_peak_hour_vehicals_HanHighway(file_name,date): #This function calculates the peak number of vehicals per hour passing through Hanley Highway/Westway for the selected date.
    junction_name = "Hanley Highway/Westway"
    vehicle_count_per_hour = [0] * 24 # creates a list to count vehicles per hour from 0 to 23hrs.
    with open(file_name, "r") as file:
        data_reader = csv.reader(file)
        headers = next(data_reader)
        #Below code defines the specific variables to compare.
        date_index = headers.index("Date")
        junction_index = headers.index("JunctionName")
        time_index = headers.index("timeOfDay")
        for row in data_reader:
            # below code compares required feilds and using split meathod to get the desired output while incrementing using a count variable. 
            if row[date_index] == date and row[junction_index] == junction_name:
                hour = int(row[time_index].split(":")[0])  # This code will extract the exact hour and ignores the miniute values
                vehicle_count_per_hour[hour] = vehicle_count_per_hour[hour] + 1
            peak_count = max(vehicle_count_per_hour) #Finds the maximum vehicle number for the hour for the defined date and junction.
            peak_hour = vehicle_count_per_hour.index(peak_count)
        print(f"The highest number of vehicles in an hour on Hanley Highway/Westway is {peak_count}.")
        return peak_count

def busiest_time_window_HanHighway(file_name, date): #This function calculates the buissiest time window of vehicles passing through Hanley Highway/Westway for the selected date.
    junction_name = "Hanley Highway/Westway"
    vehicle_count_per_hour = [0] * 24  # creates a list to count vehicles per hour from 0 to 23hrs.
    with open(file_name, "r") as file:
        data_reader = csv.reader(file)
        headers = next(data_reader)
        #Below code defines the specific variables to compare.
        date_index = headers.index("Date")
        junction_index = headers.index("JunctionName")
        time_index = headers.index("timeOfDay")
        for row in data_reader:
            # below code compares required feilds for the desired output and incrementing using a count variable.
            if row[date_index] == date and row[junction_index] == junction_name:
                hour = int(row[time_index].split(":")[0])  # will extract the exact hour and ignores the miniute values
                vehicle_count_per_hour[hour] += 1
    peak_count = max(vehicle_count_per_hour) #max function is used to find the highest value for vehicle count per hour.
    #Below 2 codes finds all hours with the peak traffic count. Code obtained from youtube
    peak_hours = [hour for hour, count in enumerate(vehicle_count_per_hour) if count == peak_count] #enumerate fuction is used to iterate and store index valuse of the elements in the list.
    time_ranges = [f"Between {hour}:00 and {hour + 1}:00" for hour in peak_hours]
    #Below code takes the time values from the list and turns them into a singular string and is output through the print function.
    print(f"The most vehicles through Hanley Highway/Westway were recorded between {', '.join(time_ranges)}.") 
    return time_ranges

def rain_hours(file_name, date): #This function calculates the total number of hours of rain for the selected date.
    from datetime import datetime, timedelta
    rainy_conditions = ["Light Rain", "Heavy Rain"]
    total_rain_duration = timedelta(0) #Time delta used to calculate the differnce between the times.
    previous_time = None #None function is used as a place holder.
    with open(file_name, "r") as file:
        data_reader = csv.DictReader(file)
        for row in data_reader:
            # below code compares required feilds for the desired output and incrementing using a count variable.
            if row["Date"] == date and row["Weather_Conditions"] in rainy_conditions:
                current_time = datetime.strptime(row["timeOfDay"], '%H:%M:%S') #Defines the format of the time values stored in the csv file.
                if previous_time:
                    duration = current_time - previous_time
                    total_rain_duration += duration
                previous_time = current_time
    total_hours = round(total_rain_duration.total_seconds() / 3600)
    print(f"The total number of hours of rain recorded on this date is {total_hours} hours.")
    return total_hours

#Task C: Save results to text file
def save_results_to_file(date): #This function call all the functions and runs them.
    # Calling the File selection functions
    select_file = file_selection()
    file_name = select_file

    #Calling the Display outcomes
    num_vehicles = total_vehicles(select_file, date)
    num_trucks = total_trucks(select_file, date)
    num_ev = total_ev(select_file, date)
    num_twoWheeled = total_TwoWheeled(select_file, date)
    num_Bus_leave_elm_north = leave_elm_buss(select_file, date)
    num_vehicels_not_turning = total_not_turning(select_file, date)
    num_percentage_trucks = percentage_trucks(num_vehicles, num_trucks)
    num_bikes_per_hour = avg_bicycles_per_hour(select_file, date)
    num_over_speed_limit = total_over_speed_limit(select_file, date)
    num_only_ElmAve = vehicles_only_ElmAve(select_file, date)
    num_only_HanHighway = vehicles_only_HanHighway(select_file, date)
    scooter_percentage = percentage_only_scooters_ElmAve(select_file, date, num_only_ElmAve)
    peak_hour_vehicles = total_peak_hour_vehicals_HanHighway(select_file, date)
    busiest_time_window = busiest_time_window_HanHighway(select_file, date)
    num_rainy_hours = rain_hours(select_file, date)

    # Writes the processed outcome to the file "results.txt"
    with open("results.txt", "a") as file:
        file.write("*" * 40 + "\n")
        file.write(f"Data file selected is: {file_name}\n")
        file.write(f"The total number of vehicles recorded for this date is {num_vehicles}.\n")
        file.write(f"The total number of trucks recorded for this date is {num_trucks}.\n")
        file.write(f"The total number of electric vehicles recorded for this date is {num_ev}.\n")
        file.write(f"The total number of two-wheeled vehicles recorded for this date is {num_twoWheeled}.\n")
        file.write(f"The total number of buses leaving Elm Avenue/Rabbit Road heading North is {num_Bus_leave_elm_north}.\n")
        file.write(f"The total number of vehicles through both junctions not turning left or right is {num_vehicels_not_turning}.\n")
        file.write(f"The percentage of total vehicles recorded that are trucks is {num_percentage_trucks}%.\n")
        file.write(f"The average number of bicycles per hour for this date is {num_bikes_per_hour}.\n")
        file.write(f"The total number of vehicles over the speed limit recorded for this date is {num_over_speed_limit}.\n")
        file.write(f"The total number of vehicles through Elm Avenue/Rabbit Road recorded for this date is {num_only_ElmAve}.\n")
        file.write(f"The total number of vehicles through Hanley Highway/Westway recorded for this date is {num_only_HanHighway}.\n")
        file.write(f"{scooter_percentage}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.\n")
        file.write(f"The highest number of vehicles in an hour on Hanley Highway/Westway is {peak_hour_vehicles}.\n")
        file.write(f"The most vehicles through Hanley Highway/Westway were recorded between {busiest_time_window}.\n")
        file.write(f"The total number of hours of rain on this date is {num_rainy_hours} hours.\n")

    print("Results have been saved to results.txt.") #Informs the user that the code has been saved (or appeneded with regard to task E).

display_and_save = save_results_to_file(date)

#Task D: Display Histogram

import tkinter as tk
class TrafficHistogram:  #This histogram solution was developed using the assistance of Chatgpt. 
    def __init__(self, file_name):
        self.file_path = file_name

    def process_data(self):
        # Below code processes the csv file data to extract hourly vehicle counts for each junction.
        self.hourly_counts = {}
        self.junctions = set()

        # The below for loop initializes a list of hourly counts for each junction.
        for hour in range(24):
            self.hourly_counts[hour] = {}

        # Read csv file data
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                junction = row['JunctionName']
                hour = int(row['timeOfDay'].split(':')[0])

                self.junctions.add(junction)
                if junction not in self.hourly_counts[hour]:
                    self.hourly_counts[hour][junction] = 0
                self.hourly_counts[hour][junction] += 1

        self.junctions = sorted(self.junctions) #sort function used to sort the data.

    def create_histogram(self): #Creates a histogram showing side-by-side counts for all junctions for each hour.
        root = tk.Tk()
        root.title("Histogram")
        #below variables define histogram window characteristics.
        canvas_width = 1100
        canvas_height = 650
        canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
        canvas.pack(fill=tk.BOTH, expand=True)

        #below variables define bar graph characteristics.
        bar_width = 10
        spacing = 5
        padding = 60
        max_height = 400
        base_y = 500

        colors = ["lightgreen", "lightpink"] #Setting the colours for the bar graphs with respect of the 2 junctions.

        # Find the maximum count for scaling
        max_count = max(
            count for hour in self.hourly_counts.values() for count in hour.values()
        )
        scale_factor = max_height / max_count if max_count > 0 else 1

        for hour in range(24): #This for loop creates a list of hour values and used as the values for the x-axis.
            x_offset = padding + hour * (len(self.junctions) * (bar_width + spacing) + spacing)
            for i, junction in enumerate(self.junctions): #enumerate fuction is used to iterate and store index valuse of the elements in the list.
                count = self.hourly_counts[hour].get(junction, 0)
                bar_height = count * scale_factor

                x1 = x_offset + i * (bar_width + spacing)
                y1 = base_y - bar_height
                x2 = x1 + bar_width
                y2 = base_y

                canvas.create_rectangle(x1, y1, x2, y2, fill=colors[i % len(colors)], outline="black")
                if count > 0:
                    canvas.create_text(
                        x1 + bar_width / 2, y1 - 10, text=str(count), anchor=tk.S, font=("Arial", 8)
                    )

        # Addig hour labels to X-axis.
        for hour in range(24):
            x = padding + hour * (len(self.junctions) * (bar_width + spacing) + spacing) + (len(self.junctions) * (bar_width + spacing)) / 2
            canvas.create_text(x, base_y + 20, text=f"{hour:02d}", anchor=tk.N, font=("Arial", 10))

        # Adding legends for the junctions.
        for i, junction in enumerate(self.junctions):
            canvas.create_rectangle(800, 40 + i * 25, 820, 60 + i * 25, fill=colors[i % len(colors)], outline="black")
            canvas.create_text(830, 50 + i * 25, text=junction, anchor=tk.W, font=("Arial", 10))
        # Adding x-axis label.
        canvas.create_text(canvas_width / 2.25, base_y + 50, text="Hours 00:00 to 24:00", anchor=tk.N, font=("Arial", 12, "bold"))
        # Adding a title.
        canvas.create_text(canvas_width / 3.2, 20, text="Histogram of Vehicle Frequency for the selected file", font=("Arial", 14, "bold"), anchor=tk.N)
        # Creates and defines a solid line for the X-axis.
        canvas.create_line(padding, base_y, 950 - padding, base_y, fill="black", width=2)
        root.mainloop()

if __name__ == "__main__":
    # Get file name from the user to generate the histogram.
    def histogram_file_selection():
        while True:
            try:
                histogram_file_name = input("Enter the Name of the csv file to generate the histogram: ")
                f = open(histogram_file_name, "r") 
                f.close()
                return histogram_file_name
            except FileNotFoundError:  
                print("File does not exist. Please try again (might have forgotten '.csv').")

    # Calling the function to get the file name.
    histogram_file = histogram_file_selection()

    # Passing the user enterd file name to the TrafficHistogram class.
    histogram_app = TrafficHistogram(histogram_file)
    histogram_app.process_data()
    histogram_app.create_histogram()

#Task E: Code Loops to Handle Multiple CSV Files 
def validate_continue_input(day,month,year): #This task E is respect to now updated parts A,B,C,D :)
    while True:
        new_file = input('Press "Y" to load new dataset or "N" to quit: ')
        if new_file == "Y": #Creating and defing the control varaiable to continue.
            print("")
            print("*******************************")
            print("")
            #All fucntions are called again with the use of a while true loop.
            is_leap_year(year)
            validate_date(day, month, year)
            while True:
                day = day_validation()
                month = month_validation()
                year = year_validation()
                if validate_date(day, month, year):
                    date = f"{day:02}/{month:02}/{year:04}"
                    break
                else:
                    print("The entered date is not valid. Please enter the date again.")
            date = f"{day:02}/{month:02}/{year:04}" #Reassinging the new date variable.
            display_and_save = save_results_to_file(date) #Appends the new data to results.txt.
            histogram_file = histogram_file_selection()
            histogram_app = TrafficHistogram(histogram_file)
            histogram_app.process_data()
            histogram_app.create_histogram()

        elif new_file == "N": #Creating and defing the control varaiable to terminate the program.
            break
        else: #This else statement is used for error handling.
            print('Unidentified key word. Enter either "Y" or "N"')
            continue
    return new_file
        
new_file = validate_continue_input(day,month,year) #Calling Task E.

#Sites and sources used for code refferncing and debugging: Chatgpt,Google,Reddit(r/python,r/programming).
# if you have been contracted to do this assignment please do not remove this line

