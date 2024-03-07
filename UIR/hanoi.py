
#todo Hanoi Tower for fixed size of n - 3 disks
def hanoi(source, target, auxiliary):
    print('Move disk 1 from source', source, 'to target', target)
    print('Move disk 2 from source', source, 'to auxiliary', auxiliary)
    print('Move disk 1 from target', target, 'to auxiliary', auxiliary)
    print('Move disk 3 from source', source, 'to target', target)
    print('Move disk 1 from auxiliary', auxiliary, 'to source', source)
    print('Move disk 2 from auxiliary', auxiliary, 'to target', target)
    print('Move disk 1 from source', source, 'to target', target)
    
hanoi('A', 'C', 'B')

print('-------------------')


#todo make hanoi tower method -  n disks
def hanoi(n, source, target, auxiliary):
    if n < 0:
        return "Wrong number of disks"
    if n == 1:
        print('Move disk 1 from source', source, 'to target', target)
        return
    hanoi(n-1, source, auxiliary, target)
    print('Move disk', n, 'from source', source, 'to target', target)
    hanoi(n-1, auxiliary, target, source)

hanoi(3, 'A', 'C', 'B')




