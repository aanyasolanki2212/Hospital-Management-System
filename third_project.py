with open("hospital.txt","a") as f:
    hospital=[]
    print("This is a hospital management system")
    print("Here we have four features add patient , view patient, search patient, delete patient and exit")
    print("1. Add Patient")
    print("2. View Patient")
    print("3. Search Patient")
    print("4. Delete Patient")
    print("5. Exit")
    a=0
    while True:
        a=int(input("Enter what you want to do:    "))
        if a==1:
            patients=[]
            b=input("Enter patient name:   ")
            patients.append(b)
            c=int(input("Enter patient's age:   "))
            patients.append(c)
            d=input("Enter Patient's gender(f/m):   ")
            patients.append(d)
            hospital.append(patients)
        elif a==2:
            for i in hospital:
                print(f"Patient's name: {i[0]}, Patient's age: {i[1]}, Patient's gender:{i[2]}")
        elif a==3:
            e=input("Enter the patient's name you want to search:   ")
            for patient in hospital:
                if patient[0]==e:
                    print("The patient is found:   ")
                    break
            else:
                print("The patient is not found:   ")
        elif a==4:
            f=open("hospital.txt","w")
            q=input("Enter the patient you want to delete:  ")
            for patient in hospital:
                if patient[0]==q:
                    hospital.remove(patient)
                    print("The patient is deleted successfully!")
                    break
            else:
                print(f"The patient {q} is not found")
        elif a==5:
            break