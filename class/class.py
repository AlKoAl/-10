all_patients = [] # списокьвсех больных
all_diseases = [] # список всех болезней
all_doctors = [] # список докторов


class Patient:
    def __init__(self, name, age, former_illness=[], disease=[]):
        self.name = name
        self.age = age
        self.former_illness = former_illness
        self.disease = disease

    def append_in_list(self):
        all_patients.append(self)

    def find_a_doctor(self):
        doc = {}
        for i in self.disease:
            for j in all_diseases:
                if i == j.name:
                    print(j.attending_physicians)
                    our_doctor = [input('Введите номер врача из предложенного списка:')]
                    time = input('Введите желаемое время приёма:')
                    if time in j.attending_physicians[our_doctor].schedule:
                        doc[j.attending_physicians[our_doctor]] = time



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
        self.who_was_sick = who_was_sick

    def append_in_list(self):
        all_diseases.append(self)

    def Attending_physicians(self): #
        for i in all_doctors:
            for k in i.specialization:
                if k == self.name and i not in self.attending_physicians:
                   self.attending_physicians.append(i)

    def Who_was_sick(self): #
        for i in all_patients:
            for k in i.disease:
                if k == self.name and i not in self.who_was_sick:
                    self.who_was_sick.append(i)


def list_of_something():  # список входных данных
    List = []
    k = str(input('Введите строку; если вы больше не будете ничего добавлять, введите 0'))
    while k != '0':
        List.append(k)
        k = str(input('Введите строку; если вы больше не будете ничего добавлять, введите 0'))
    return List


def creation_of_a_patient(): # создание объекта класса пациент
    name = input('Введите имя больного:')
    age = input('Введите возраст больного:')
    print('Введите болезни, которыми он болел:')
    former_illness = list_of_something()
    print('Введите то, чем он болеет:')
    disease = list_of_something()
    name = Patient(name, age, former_illness, disease)
    name.append_in_list()


def creation_of_a_doctor(): # создание объекта класса доктор
    name = input('Введите имя доктора:')
    print('Введите его специализацию:')
    specialization = list_of_something()
    print('Введите его график работы (пара чисел):')
    schedule = []
    for i in range(int(input('Введите начало рабочего дня:')), int(input('Его конец:')) + 1):
        schedule.append(i)
    name = Doctor(name, specialization, schedule)
    name.append_in_list()


def creation_of_a_desease(): # создание объекта болезнь
    name = input('Введите название болезни:')
    print('Введите симптомы болезни:')
    symptoms = list_of_something()
    print('Введите возможные методы лечения:')
    methods_of_treatment = list_of_something()
    name = Disease(name, symptoms, methods_of_treatment)
    # Добавить врачей и больных
    name.Attending_physicians()
    name.Who_was_sick()
    name.append_in_list()


def Verification_of_entrydcot(): # Проверка вхождения
    for i in all_diseases:
        for j in all_doctors:
            if j.specialization == i.name and j not in i.attending_physicians:
                i.attending_physicians.append(j)
