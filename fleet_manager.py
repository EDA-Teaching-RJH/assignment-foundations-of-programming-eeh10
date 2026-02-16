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

def add_member(names, ranks, divs, ids):
    name = input("Name: ")
    rank = input("Rank: ")
    div = input("Division: ")
    new_id = int(input("ID: "))

    if new_id in ids:
        print("ID exists")
        return

    # simple rank check
    valid = False
    if rank == "Captain":
        valid = True
    if rank == "Commander":
        valid = True
    if rank == "Lt. Commander":
        valid = True
    if rank == "Lieutenant":
        valid = True
    if rank == "Ensign":
        valid = True

    if valid == False:
        print("Bad rank")
        return

    names.append(name)
    ranks.append(rank)
    divs.append(div)
    ids.append(new_id)
    print("Added")

def remove_member(names, ranks, divs, ids):
    target = int(input("ID: "))

    if target in ids:
        i = ids.index(target)
        names.pop(i)
        ranks.pop(i)
        divs.pop(i)
        ids.pop(i)
        print("Removed")
    else:
        print("Not found")

def update_rank(names, ranks, ids):
    target = int(input("ID: "))

    if target in ids:
        i = ids.index(target)
        new_rank = input("New rank: ")
        ranks[i] = new_rank
        print("Updated")
    else:
        print("Not found")

def display_roster(names, ranks, divs, ids):
    print("\nRoster:")
    for i in range(len(names)):
        print(ids[i], names[i], ranks[i], divs[i])

def search_crew(names, ranks, divs, ids):
    term = input("Search: ")
    for i in range(len(names)):
        if term.lower() in names[i].lower():
            print(ids[i], names[i], ranks[i], divs[i])

def filter_by_division(names, divs):
    choice = input("Division: ")
    for i in range(len(names)):
        if divs[i] == choice:
            print(names[i])

def calculate_payroll(ranks):
    total = 0

    for r in ranks:
        if r == "Captain":
            total += 1000
        elif r == "Commander":
            total += 800
        elif r == "Lt. Commander":
            total += 600
        elif r == "Lieutenant":
            total += 400
        elif r == "Ensign":
            total += 200

    return total

def count_officers(ranks):
    c = 0
    for r in ranks:
        if r == "Captain" or r == "Commander":
            c += 1
    return c


def main():
    names, ranks, divs, ids = init_database()
    user = input("Your name: ")

    while True:
        choice = display_menu(user)

        if choice == "1":
            add_member(names, ranks, divs, ids)
        elif choice == "2":
            remove_member(names, ranks, divs, ids)
        elif choice == "3":
            update_rank(names, ranks, ids)
        elif choice == "4":
            display_roster(names, ranks, divs, ids)
        elif choice == "5":
            search_crew(names, ranks, divs, ids)
        elif choice == "6":
            filter_by_division(names, divs)
        elif choice == "7":
            print("Payroll:", calculate_payroll(ranks))
        elif choice == "8":
            print("Officers:", count_officers(ranks))
        elif choice == "9":
            break
        else:
            print("Invalid")


main()