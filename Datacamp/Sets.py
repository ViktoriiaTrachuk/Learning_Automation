empty_set = set()
empty_dict = dict()
empty_dict = {}

dataScientist = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'])
#dataScientist = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
dataEngineer = set(['Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'])
#dataEngineer = {'Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'}

print(dataScientist)
print(dataEngineer)

graphicDesigner = {'InDesign', 'Photoshop', 'Acrobat', 'Premiere', 'Bridge'}
graphicDesigner.add('Illustrator')
print(graphicDesigner)
graphicDesigner.remove('Illustrator')
print(graphicDesigner)
graphicDesigner.discard('Git')
print(graphicDesigner)

#pop method to remove and return an arbitrary value from a set.
graphicDesigner.pop()
print(graphicDesigner)
graphicDesigner.clear()
print(graphicDesigner)

#.update() method automatically converts other data types into sets and adds them to the set. 

set1 = set([7, 10, 11, 13])
set2 = set([11, 8, 9, 12, 14, 15])
set3 = {'d', 'f', 'h'}

set1.update(set2)
print(set1)

set1 = set([7, 10, 11, 13])
set2 = set([11, 8, 9, 12, 14, 15])
set3 = {'d', 'f', 'h'}
set1.update(set3)
print(set1)

#Iterate through a Python Set

dataScientist = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}

for skill in dataScientist:
    print(skill)
#sorted(dataScientist)
print(dataScientist)
print(sorted(dataScientist))
print(sorted(dataScientist, reverse=True))
print(type(dataScientist))
print(type(sorted(dataScientist)))

#Remove Duplicates from a List in Python

#Option1

print(list(set([1, 2, 3, 1, 7])))
#[1, 2, 3, 1, 7] -this is the list(ordered, indexed, changeable, and allow duplicate values)
# (set([1, 2, 3, 1, 7]) - transforms list to set (unique that is do not allow duplicate values, unordered, unindexed, and unchangeable (can be added or removed only))
#list(set([1, 2, 3, 1, 7])) - converts set to list back but 1 is missing now

#Option2

def remove_duplicates(original):
    unique = []
    [unique.append(n) for n in original if n not in unique]
    return(unique)

print(remove_duplicates([1, 2, 3, 1, 7]))

#To measure performance time of test execution:
import timeit

# Approach 1: Execution time
print(timeit.timeit('list(set([1, 2, 3, 1, 7]))', number=10000))

# Approach 2: Execution time
print(timeit.timeit('remove_duplicates([1, 2, 3, 1, 7])', globals=globals(), number=10000))

#Python Set Operations
#Union, Intersection, Difference, Symetric Difference

dataScientist = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'])
dataEngineer = set(['Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'])

print(dataScientist.union(dataEngineer))
#to find out all the unique values in two sets

print(dataEngineer.intersection(dataScientist))
#set of all values that are values of both

print(dataScientist.difference(dataEngineer))
#all values of dataScientist that are not values of dataEngineer

print(dataScientist.symmetric_difference(dataEngineer))
#the set of all values that are values of exactly one of two sets, but not both.



