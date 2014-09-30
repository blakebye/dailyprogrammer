length = int(raw_input("How long is the list to be sorted? "))
list = []
for i in range(length):
    list.append(float(raw_input()))

def quicksort(values):
    if len(values) < 2:
        return values
    elif len(values) == 2:
        if values[0] > values[1]:
            values[0], values[1] = values[1], values[0]
        return values
    else:
        smaller = []
        greater = []
        sample = [values[0], values[len(values) / 2], values[len(values) - 1]]
        for invalid in (min(sample), max(sample)):
            sample.remove(invalid)
        pivot = sample.pop()
        values.remove(pivot)
        for v in values:
            if v <= pivot:
                smaller.append(v)
            else:
                greater.append(v)
        return quicksort(smaller) + [pivot] + quicksort(greater)

assert quicksort([]) == [], "empty list"
assert quicksort([1]) == [1], "one element list"
assert quicksort([2, 1]) == [1, 2], "two element list"
assert quicksort([3, 2, 1]) == [1, 2, 3], "odd number sort"
assert quicksort([1, 3, 5, 6, 4, 2]) == [1, 2, 3, 4, 5, 6], "even number sort"

print quicksort(list)
