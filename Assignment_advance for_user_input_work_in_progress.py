"""
Replace the contents of this module docstring with your own details.
"""
PROGRAM_RUNNING = True # This global variable is here so when the menu selection of q aka quit is chosen
# it breaks out of the while loop in the main () shutting down the whole program

def write_csv_file (data_to_write):
    """ Basic Write to CSV function writes to the csv file with the data
     as it is imputted and then feed into from the main function """
    import csv
    with open('movies.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data_to_write)
        return

def Read_CSV_File(filename):
    """Basic CSV Reader, Reads a row and then does a new line puts the data into a tuple
    to then be passed back to the main() to then pass it to my  sort and print function
    running within a for loop so while there is a row it keeps reading them. Placing into a tuple so the data does not get corrupted
     when passing it from here to main then to my print and sort function"""
    import csv
    with open('movies.csv',newline='') as f:
        reader = csv.reader(f)
        index = /n
        filename = movies_list ()
        for row in reader:
            movies_list.append(row, index)
            return movies_list

def valid_user_input(valid_parameters, valid_type, selection_options):
    """This function gets acceptable parameters Menu selection options etc. is x>0 or a list of acceptable selections etc.) and type(int, or str etc.).
     It then asks for a input converts to lower case and returns that selection if it passes the checks placed on the type conditions and parameters.
    Else it tells you that your selection was invalid try choosing from one of these more acceptable options and to try again
     all of which is nested within a while loop so it keeps looping around until this condition has been meet"""
    while True:
        print(selection_options)
        menu_selection = input("Please enter in your selection here: ").lower()
        if menu_selection is valid_type and menu_selection in valid_parameters:
            return menu_selection
        elif menu_selection is valid_type and menu_selection is valid_parameters:
            return menu_selection
        else:
            print("Invalid input try using one of these choices:{}{}{}".format(valid_parameters, valid_type, selection_options))

def main():

    """ My main console where all of the program starts from and runs from it is the central hub that connects all of the pieces together"""
    print("Movies To Watch 1.0 - by Wade Sheedy")



    while PROGRAM_RUNNING == True:
        Menu = (      "Menu" 
                    "L - List Movies" 
                    "A - Add new movie" 
                    "W - Watch a movie" 
                    "Q - Quit")
        valid_type = str
        valid_selections = ('l', 'a', 'w', 'q')
        Menu_Selection = valid_user_input(valid_selections, valid_type, Menu)

        if Menu_Selection == l:
            898980
        elif Menu_Selection == a:
            year_valid_type = int
            year_valid_parameters = int > 0
            year_selection_options = "enter a year that is a integer and is greater then 0"
            year = valid_user_input(year_valid_parameters, year_valid_type, year_selection_options)
            title_validtype = str
            title_valid_parameters = ()
            title_selection_options ="please enter in the movies title"
            title = valid_user_input(title_valid_parameters,title_validtype,title_selection_options)
            genera_valid_type = str
            genera_valid_parameters = ('comedy', 'action', 'drama', 'romance', 'war', 'romantic comedy', 'sci-fi', 'crimer', 'thriller')
            genera_valid_selections = "Please enter the movies genera"
            genera = valid_user_input(genera_valid_parameters, genera_valid_type, genera_valid_selections)
            watched_valid_type = str
            watched_valid_parameters = ('y', 'n')
            watched_valid_selections = "Have you watched this movie allready? y/n"
            watched = valid_user_input(watched_valid_parameters,watched_valid_type,watched_valid_selections)
            new_movie = [title, year, genera, watched]
            write_csv_file(new_movie)
        elif Menu_Selection == w:
            213132312
        elif Menu_Selection == q:
            PROGRAM_RUNNING = False


if __name__ == '__main__':
    main()
