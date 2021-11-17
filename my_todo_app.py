def show_menu():
    print('\n MY TO-DO LIST MENU:')
    
    instructions = '\n1.Type "1" to add in the TO-DO LIST \n2.Type "2" to delete from the TO-DO LIST \n3.Type "3" to view TO-DO LIST \n4.Type "4" to update the TO-DO LIST \n5.Tyoe "5" to exit TO-DO LIST application'
    print(instructions)


my_todo_list = []

while True:
    show_menu()
    user_input = input('\nEnter your option(1,2,3,4,5): ')
    if user_input == '1':
        add_todo_item = input('Enter the activity to add in TO-DO LIST: ')
        my_todo_list.append(add_todo_item)
    elif user_input == '2':
        delete_item = input('Enter the activity you want to delete from TO-DO LIST: ')
        confirm = input('Are you sure want to delete {} from TO-DO LIST (Y/N) : '.format(delete_item)).lower()
        if confirm == 'y':
            if delete_item in my_todo_list:
                my_todo_list.remove(delete_item)
                print('Removed item: {}'.format(delete_item))
            else:
                print('{} Item not found'.format(delete_item))
    
    elif user_input == '3':
        print('\nMY TO-DO ACTIVITIES')
        print('---------------------')
        for each in my_todo_list:
            print(each)
    
    elif user_input == '4':
        item_name = input('Enter the activity to be updated: ')
        if item_name in my_todo_list:
            choice = input('Are you sure want to update {} from your TO-DO LIST (Y/N) : '.format(item_name)).lower()
            if choice == 'y':
                update_item = input('Enter the activity name you want to update {} with: '.format(item_name))
                ind = my_todo_list.index(item_name)
                my_todo_list[ind] = update_item
                print('Your activity is updated')
            else:
                print('Item not found') 

    elif user_input == '5':
        print('Exited from your TO-DO LIST')
        break
                
    else:
        print('Please enter a valid option')

print("GOOD BYE")