import csv
from triangle import triangle


class Result:
    def __init__(self, file):
        self._file = file
        self.fin_results = []
        self.res, self.dates = [], []
        self.tuple()
        self.make_res_csv()


    def create_triangle(self):
        """
         

      The Yield keyword in Python is similar to a return statement used for returning values or objects in Python. However, there is a slight difference. 
      The yield statement returns a generator object to the one who calls the function which contains yield, instead of simply returning a value. 
      it is checking on the file while looping through it by reading it

      first, it is reading the csv files and it is checking if theres any issues with it



        """
        with open(self._file, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            # Skip Headers
            next(csv_reader)
            c = 0
            for data in csv_reader:
                c += 1
                try:
                    if len(data) != 4:
                        print("Your file contains an error on line - ", c + 1, " - ", data)
                        print("Only the first four indexes will be used.")
                        print("\n")
                    # product, origin_year, development_year, incremental_value
                    yield triangle(data[0], data[1], data[2], data[3])
                except Exception as e:
                    print(e)


    def group_data_splitting(self):
        """
        using the for Loop through yielded data and the if statements
        Keep key as product and values as the rest and return by storing the
        origin_year, development_year and the incremental_value into the products
        which is a data structure call the dictionary
        
        """
        products = {}
        for objects in self.create_triangle():
            if objects.product not in products:
                products[objects.product] = [
                    [objects.origin_year, objects.development_year, objects.incremental_value]]
            else:
                products[objects.product] += [
                    [objects.origin_year, objects.development_year, objects.incremental_value]]

        return products

    def tuple(self):
        """

        It is storing all the data  (origin_date, development_date, incremental_val) into a single variable into the Data array
        Run self.do_calc on the data
        :return:
        """
        data = []
        for k, rows in self.group_data_splitting().items():
            for row in rows:
                item = (k, row[0], row[1], row[2])
                data.append(item)

        self.calculate_icremental_value(data)

    def calculate_icremental_value(self, data):
        """
       Append dates into self.dates 
        It is Looping through the data
        Check if products match
        Check if the origin and development year match and if statment is true append current incremental value
        Else check the num of iterations between origin and development year
        If its one, it will start the calculations manually,
        else if it will Run the self.icremental_value_iterations
        afterwords, it  Reading the last product of the data where 'data[-1]' it going in reverse
        repeats the same process with the last product of the data
        """
        for i in data:
            self.dates.append(int(i[1]))
            self.dates.append(int(i[2]))

        for i in range(len(data) - 1):
            if data[i][0] == data[i + 1][0]:
                if data[i][1] == data[i][2]:
                    self.res.append((data[i][0], data[i][3]))
                else:
                    iterations = int(data[i][2]) - int(data[i][1])
                    if iterations == 1:
                        self.res.append((data[i][0], float(data[i][3]) + float(data[i - 1][3])))
                    elif iterations > 1:
                        self.icremental_value_iterations(data, i, iterations)
            else:
                if data[i][1] == data[i][2]:
                    self.res.append((data[i][0], data[i][3]))
                else:
                    self.res.append((data[i][0], float(data[i][3]) + float(data[i - 1][3])))

        if data[-1][1] == data[-1][2]:
            self.res.append((data[-1][0], data[-1][3]))
        elif int(data[-2][1]) + 1 == int(data[-1][2]):
            self.res.append((data[-1][0], float(data[-1][3]) + float(data[-2][3])))
        else:
            inc_val = 0
            for i in range(int(data[-1][2]) - int(data[-1][1]) + 1):
                inc_val += float(data[-1 - i][3])
            self.res.append((data[-1][0], inc_val))

    def icremental_value_iterations(self, data, i, iter):
        """
        Loop through iteration range passed in
        Get the missing dates 
        the if statment is checking if the product is equal the iterations_range product
        and if the statement is true then it give out the incremental_val by adding the float variable from the data minus the value of the iterations_range
        expected_dates is getting a range list of number from the origin dates and the development dates
        then is will add the actual_datas an int by data minus the development year from the iterations_range
        afterwards, the missing_dates will get the variables from the actual_dates minus the actual_dates 

        Loop through the range for missing dates
        Check if the missing dates would equal development year
        If it is, append data
        Append normal incremetal_vals without missing dates at the end
        """
        actual_dates = []
        incremental_val = 0
        missing_dates = 0
        for iterations_range in range(iter + 1):
            if data[i][0] == data[i - iterations_range][0]:
                incremental_val += float(data[i - iterations_range][3])
            expected_dates = list(range(int(data[i][1]), int(data[i][2]) + 1))
            actual_dates.append(int(data[i - iterations_range][2]))
            missing_dates = list(set(expected_dates) - set(actual_dates))
        for p in range(len(missing_dates)):
            if missing_dates[p] == int(data[i][2]) - p - 1:
                self.res.append((data[i][0], incremental_val - float(data[i][3])))
        self.res.append((data[i][0], incremental_val))

    def format_results(self):
        """
        Loop through self.res and put all the revelant data together from icremental_value_iterations and the calculate_icremental_value methods. 
        Get the length of the max value into the dictionary from the group_data_splitting method.

        the long_val is returning the element in that array whose second element is larger than all of the other elements' second elements
        loop through data and check if the length of value is equal to max value,
        if it isnt, get the difference between the max val and length of current list
        and add 0's to the start.
        
        """
        data = {}
        for i in self.res:
            if i[0] not in data:
                data[i[0]] = [float(i[1])]
            else:
                data[i[0]] += [float(i[1])]

        long_val = max(data, key=lambda x: len(data[x]))

        for key, value in data.items():
            if len(data[key]) != len(data[long_val]):
                for i in range(len(data[long_val]) - len(data[key])):
                    data[key].insert(0, 0)
            print(key, value)
        print("\n")

        return data

    def make_res_csv(self):
        """
        Make new csv file and add it to the current folder with the result data inside
        print out that the file is made
        :return:
        """
        results = self.format_results()
        self.fin_results.append(results)
        with open("Result_File_" + self._file, 'w', newline='') as my_file:
            wr = csv.writer(my_file, quoting=csv.QUOTE_ALL)
            wr.writerow([min(self.dates), max(self.dates) - min(self.dates) + 1])
            for i, j in results.items():
                wr.writerow([i, ",".join(str(i) for i in j)])
            print("Result_File_" + self._file, "Created, Check your directory!")
