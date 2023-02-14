dict_variable = {"a":"A","B":"b"}
dict_variable["c"] = "C"
dict_variable["D"] = "d"
dict_variable["e"] = "E"

print(dict_variable["a"]) # A
print(dict_variable["D"]) # d
print(dict_variable["b"]) # b에 해당하는 key가 없어 KeyError
