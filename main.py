import text as t
import functions as f

while 1:
    print(t.filter_menu)

    Filter = input("Select filter (or 0 to exit):\n")
    while Filter not in ['0', '1', '2', '3', '4']:  # Checking for correct answer
        Filter = input("You can only enter numbers from 0 to 4\n")

    if Filter == '0':  #Exit
        break

    print()
    print(t.filters_text[int(Filter)]["name"])
    print(t.filters_text[int(Filter)]["description"])

    In = input("Apply filter to text (Yes/No)? ")
    while In.lower() not in ['yes', 'no']:
        In = input("You can only enter Yes or No\n")

    if In.lower() == 'yes':
        In = input("Enter text to filter: ")
        if Filter == '1':
            print("Result: ", f.camel_filter(In))
        elif Filter == '2':
            print("Result: ", f.snake_filter(In))
        elif Filter == '3':
            print("Result: ", f.shouting_filter(In))
        else:
            print("Result: ", f.whispering_filter(In))

print()
print("Goodbye!")
