### working out the Mean, Median, Mode and range of a data set.
##set of data is 4,3,6,8,2,9
##will push for standard deviation of a range of data sets
##will try make it dynamic so that we can edit the data sets

##we can cheat so we can import the statistics model and use that to generate the statistics, but that is not fun.
# Example of this process 

#import statistics  #imports the statistics maths module

data = [4, 3, 6, 8 ,2 ,9,]  #Data set, put into List format as this will allow us to work with multiple values (Pc is basically storing multiple values instead of just a single value)

#cheatmean = statistics.mean(data)   #define a variable called mean to store the mean value from the data
#print("The mean is " + str(cheatmean))

#This is alittle dull and also we dont fully understand what we are doing here, we cant ensure data intergrity because we cant ensure the process the Data goes through (we have essentially sent the numbers
#to a virtual external company to run with no clue as to what the company has done)
#lets make it all ourself.



#########   MEAN     ##################
mean = sum(data) / len(data) #here we are taking our data variable it holds all our data.
#Sum is the same as excel, it will add up all the values included within "data".
#Len stands for Length and will give us the length of a list of data since there is 6 numbers in our data set len(data) will return 6. Using this allows for more dynamic inputs 
#print("sum(data) = ", sum(data))
#print("len(data) = ", len(data))
#print("mean = ", mean)


######## MEDIAN ##############

sorted_data = sorted(data) #first we need to organise the data
data_length = len(sorted_data) #we are repeating ourself alittle typing len(data) lets just save that value so its easier to manipulate.
if data_length % 2 == 0: # the % returns the remainder so if % 2 is 0 then we have a even number of values and so we will need to take the difference
    difference =  (sorted_data[data_length//2] - sorted_data[data_length//2 - 1]) / 2
    median = sorted_data[data_length//2 - 1] + difference  #bit of maths to calculate the difference and we add it onto the middle value - 1
else:
    median = sorted_data[data_length//2] #if we have an odd number itll just give the middle value.

print("data = ", data)
print("sorted_data = ", sorted_data)
print("sorted_data[data_length//2 - 1] = ", sorted_data[data_length//2 - 1])
print("sorted_data[data_length//2] = ", sorted_data[data_length//2])
print("data_length = ", data_length)
print("difference = ", difference)
print("median = ", median)

######## MODE ##############

#lets elimiate the situation where they all appear as much as the other
data_set = set(data)  #sets are lists but without repeating values
if len(data_set) == len(data):
    mode = data_set
    mode = str(mode) + " No Value appears more than once" 
else:
    frequency = {} #this here is a  type of 'list' but called a dictionary  it contains what we call key value pairs
    for num in data:
        frequency[num] = frequency.get(num, 0) + 1
        max_frequency = max(frequency.values()) #grab the highest value that occurs within the dict
        mode = [num for num, freq in frequency.items() if freq == max_frequency] #here we compare the frequency each item appears if frequency is the same as the highest frequency
        #then we add it to a list called mode.
    print("frequency = ", frequency)
    print("max_frequency = ", max_frequency)

print("mode = ", mode)

######## RANGE ##############

range = max(data) - min(data) #explains itself 
print("max(data) = ", max(data))
print("min(data) = ", min(data))
print("range = ", range)


############### OUTCOMES ##################

print("range = ", range)
print("mode = ", mode)
print("median = ", median)
print("mean = ", mean)