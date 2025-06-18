def array_names(name_dict):
    full_names = [ ]
    for first, last in name_dict.items( ):
        full_name = f"{first_capitalize()} {laet.capitalize()}"
        full_name.append(full_name) 
    return full_names

persons = {
   "sawittcha": "jiamthanunkal",
   "chutinun": "yungmak",
   "pum": "geno"
}

print(array_of_names(persons))