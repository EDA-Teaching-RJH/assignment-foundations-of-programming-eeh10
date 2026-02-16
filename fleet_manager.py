def init_database():
    names = ["Jean-Luc Picard", "William Riker", "Data", "Worf", "Beverly Crusher"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    divs = ["Command", "Command", "Operations", "Security", "Sciences"]
    ids = [1001, 1002, 1003, 1004, 1005]
    return names, ranks, divs, ids

def display_menu(user):
    print("\nLogged in as:", user)
    print("1 Add")
    print("2 Remove")
    print("3 Update Rank")
    print("4 Display")
    print("5 Search")
    print("6 Division")
    print("7 Payroll")
    print("8 Count Officers")
    print("9 Exit")
    choice = input("Choice: ")
    return choice