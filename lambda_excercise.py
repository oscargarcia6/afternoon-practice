#Lambda Excercise 1

#Consider the List

prog_lang = [('Python', 3.8),
    ('Java', 13),
    ('JavaScript', 2019),
    ('Scala', 2.13)]


#1. Sort the list by each language's version in ascending order.
#[('Scala', 2.13), ('Python', 3.8), ('Java', 13), ('JavaScript', 2019)]
def sort_lang(prog_lang):
    return sorted(prog_lang, key = lambda x: x[1]) #returns list sorted by asc at index 1
print(sort_lang(prog_lang))

#2. Sort the list by the length of the name of each language in descending order.
#[('JavaScript', 2019), ('Python', 3.8), ('Scala', 2.13), ('Java', 13)]
def sortlen_lang(prog_lang):
    return sorted(prog_lang, key = lambda x:(len(x[0]), x[0]), reverse =True)
print(sortlen_lang(prog_lang))

#3. Filter the list so that it only contains languages with 'a' in it.
#[('Java', 13), ('JavaScript', 2019), ('Scala', 2.13)]
def filta(prog_lang):
    return list(filter(lambda x: 'a' in x[0], prog_lang))
print(filta(prog_lang))
#4. Filter the list so that it only contains languages whose version is in integer form.
#[('Java', 13), ('JavaScript', 2019)]
def fil_int(prog_lang):
    return list(filter(lambda x: type(x[1])==int ,prog_lang))
print(fil_int(prog_lang))
#5. Transform the list so that it contains the tuples in the form,
#("language in all lower case", length of the language string)
#[('python', 6), ('java', 4), ('javascript', 10), ('scala', 5)]
def low_len(prog_lang):
    return list(map(lambda x: x[0].lower(),prog_lang))
print(low_len(prog_lang))
#
       # (map(lambda x: x.lower(), items))
#6. Generate a tuple in the form,
#("All languages separated by commas","All versions separated by commas")
#('Python,Java,JavaScript,Scala', '3.8,13,2019,2.13')