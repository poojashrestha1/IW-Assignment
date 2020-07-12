#Tower of Hanoi

def tower_of_hanoi(num, source, destination, auxilliary):
    if num == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    tower_of_hanoi(num - 1, source, auxilliary, destination)
    print("\nMove disk", num, "from source", source, "to destination", destination)
    tower_of_hanoi(num - 1, auxilliary, destination, source)


num = 4
tower_of_hanoi(num, 'A', 'B', 'C')