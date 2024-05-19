with open('emd.csv', 'r') as file:
    lines = file.readlines()

header = lines.pop(0)

modalidades = []            #done
fitPeople = 0               #done
unfitPeople = 0             #done
athletesAgeCategories = {}  #done
totalpeople = 0             #done

for line in lines:
    campos = line.split(',')

    totalpeople += 1

    if campos[12] == "true": 
        fitPeople += 1
    elif campos[12] == "false": 
        unfitPeople += 1

    if campos[8] not in modalidades: 
        modalidades.append(campos[8])

    age = int(campos[5])

    age_category = f"[{((age-1)//5)*5}-{((age-1)//5)*5 + 4}]"

    if age_category not in athletesAgeCategories:
        athletesAgeCategories[age_category] = []
    athletesAgeCategories[age_category].append((campos[3], campos[4]))


fitPercentage = (fitPeople / totalpeople) * 100
unfitPercentage = (unfitPeople / totalpeople) * 100
modalidades.sort()

print("MODALIDADES")
print(modalidades)
print("Percentagem de Fits: ", fitPercentage)
print("Percentagem de Unfits: ", unfitPercentage)
print("CATEGORIAS")
for first, last in athletesAgeCategories.items():
    print(f"{first}, {last}")

