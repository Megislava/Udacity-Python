# #reading a file
# f = open('my_path/my_file.txt', 'r')
# file_data = f.read()
# f.close()

# #writing to a file
# f = open('my_path/my_file.txt', 'w')
# f.write("Hello there!")
# f.close()

# #with??
# with open('my_path/my_file.txt', 'r') as f:
#     file_data = f.read()

def create_cast_list(filename):
    cast_list = []
    with open("flying_circus_cast.txt") as cast:
        for line in cast:
            cast_list.append(line.split(",", maxsplit = 1)[0])
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)