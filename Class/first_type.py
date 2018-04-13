all_patients = []
all_diseases = []
all_doctors = []


class Patient:
    def __init__(self, name, age, former_illness=[], disease=[]):
        self.name = name
        self.age = age
        self.former_illness = former_illness
        self.disease = disease

    def append_in_list(self):
        all_patients.append(self)


class Doctor:
    def __init__(self, name, specialization, schedule=[], his_patients=[]):
        self.name = name
        self.specialization = specialization
        self.schedule = schedule
        self.patients = his_patients

    def append_in_list(self):
        all_doctors.append(self)


class Disease:
    def __init__(self, name, symptoms=[], methods_of_treatment=[],
                 attending_physicians=[], who_was_sick=[]):
        self.attending_physicians = attending_physicians
        self.symptoms = symptoms
        self.name = name
        self.methods_of_treatment = methods_of_treatment

    def append_in_list(self):
        all_diseases.append(self)

    def Attending_physicians(self):
        for i in all_doctors:
            if i.specialization == self.name:
                self.attending_physicians.append(self.name)


def list_of_something():
    List = []
    k = str(input('Введите строку, если вы больше не будете ничего добавлять, введите 0'))
    while k != '0':
        List.append(k)
        k = str(input('Введите строку, если вы больше не будете ничего добавлять, введите 0'))
    return List


def creation_of_a_patient():
    name = input('Введите имя больного:')
    age = input('Введите возраст больного:')
    print('Введите болезни, которыми он болел:')
    former_illness = list_of_something()
    print('Введите то, чем он болеет:')
    disease = list_of_something()
    name = Patient(name, age, former_illness, disease)
    name.append_in_list()


def creation_of_a_doctor():
    name = input('Введите имя доктора:')
    print('Введите его специализацию:')
    specialization = list_of_something()
    print('Введите его график работы (пара чисел):')
    schedule = []
    for i in range(int(input('Введите начало рабочего дня:')), int(input('Его конец:')) + 1):
        schedule.append(i)
    name = Doctor(name, specialization, schedule)
    name.append_in_list()


def creation_of_a_desease():
    name = input('Введите название болезни:')
    print('Введите симптомы болезни:')
    symptoms = list_of_something()
    print('Введите возможные методы лечения:')
    methods_of_treatment = list_of_something()
    name = Disease(name, symptoms, methods_of_treatment)
    # Добавить врачей и больных
    name.Attending_physicians()
    name.append_in_list()


creation_of_a_patient()
creation_of_a_doctor()
creation_of_a_desease()
print(all_diseases[0].attending_physicians)
