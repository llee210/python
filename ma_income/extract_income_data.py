# Lucy Lee
# February 2018
#
# Extracts median income and town names for each town in MA
# from input data grabbed from Boston Globe and put into txt file.
#
# Output data is formatted as a CSV with uppercase town names to match
# the capitalization of MassGIS shapefile for joining purposes.
#
# To view the source of the data in the text file:
# Open link below and right click > View Source
# The data are around line 7000 (as of 2/2018).
# They were copied and pasted from web to NotePad and saved as .txt
# https://www.bostonglobe.com/metro/2015/12/18/town-town-look-income-massachusetts/cFBfhWvbzEDp5tWUSfIBVJ/story.html
#
# Data is from ACS 2010 - 2014

###########
# create_inc_list
#
# This function reads in the TXT file and splits it by line (by town).
# Each town dictionary is evaluated and one of the town items is removed.
# The returned list has one tuple with town name and one tuple with
#     median income.
#
# Input is a the median_incomes TXT file.
#
###########

def create_inc_list(in_file):
    # Read in data
    try:
        f = open(in_file, "r")
    except IOError:
        print "Input file does not exist."
    
    str_inc = f.read()
    f.close()

    # Create list of strings (one item per town)
    inc_list = str_inc.split(",\n")

    # Edit first and last entries to remove extra [ and ] characters
    inc_list[0] = inc_list[0][1:]
    inc_list[-1] = inc_list[-1][:-2]
    
    # Iterate through the list of strings
    for i in range(len(inc_list)):

        # Convert each list element from str to dict
        inc_list[i] = eval(inc_list[i])

        # Get list of items in the dict
        inc_list[i] = inc_list[i].items()

        # Remove the third/last tuple from each list element
        inc_list[i] = inc_list[i][0:2]

    return inc_list


##########
# write_csv
#
# This function writes the the town name in capital letters and its median
#     income. Each town is one a new line.
#
# Input is the list returned by create_inc_list and the name of the output
#     file to be created.
#
##########

def write_csv(inc_list, out_file):
    f = open(out_file, 'w')

    for i in range(len(inc_list)):
        
        # Write the town name in uppercase to match MassGIS shapefile
        f.write(inc_list[i][1][1].upper() + ',')

        # Write the median income
        f.write(str(inc_list[i][0][1]))
        f.write('\n')

    f.close()

    print "Done! Check for", out_file


ma_town_inc = create_inc_list("median_incomes.txt")
write_csv(ma_town_inc, "ma_town_median_income.csv")
