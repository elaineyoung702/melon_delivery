#creating a dictionary to reference day number and sales text files
days_dict = {1:"um-deliveries-20140519.txt",
                2:"um-deliveries-20140520.txt",
                3:"um-deliveries-20140521.txt"}


def display_melon_sales():
    """ looping through daily sales and printing totals per day """

    i = 1

    for key in days_dict: #looping through dictionary contianing day and txt file

        print("Day ", i)
        the_file = open(days_dict[i])

        for line in the_file: #looping through txt file line by line
            line = line.rstrip() #remove new line space at end of line
            words = line.split("|") #estabilsh list, divided by |

            melon = words[0]
            count = words[1]
            amount = words[2]

            print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))

        the_file.close() #close the current file

        i += 1

display_melon_sales()











# print("Day 1")
# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()

