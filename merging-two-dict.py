basic_information = {"name":['karl','Lary'],"mobile":["0134567894","0123456789"]}
academic_information = {"grade":["A","B"]}
details = dict() ## Combines Dict

details = {key:value for data in (basic_information, academic_information) for key,value in data.items()}
print(details)

details = {**basic_information, **academic_information}
print(details)

details = basic_information.copy()
details.update(academic_information)
print(details)