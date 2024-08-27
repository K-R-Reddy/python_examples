def flatten(lst):
    return [item for sublist in lst for item in sublist]
a=[[1,2,3,4],[9,7,5,3],[6,8],[10]]
print("Actual List is",a)
print("Flatten List is",flatten(a))
