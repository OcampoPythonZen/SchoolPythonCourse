from statistics import mean


class AverageMensandWomen(object):

    age_list = []
    name_list = []
    gender_list = []

    def askNumberUsers(self, users: int) -> list:
        for i in range(users):
            name = input('Please Enter your name: ')
            self.name_list.append(name)
            age = int(input('Please type down your age: '))
            self.age_list.append(age)
            gender = input('Please Enter your gender: (m=man or w=woman)')
            self.gender_list.append(gender)
            print()

    def calculateAgeAverage(self) -> float:
        return mean(self.age_list)

    def calculateGenderPercentage(self) -> float:
        mens_percentage = self.gender_list.count('m')/len(self.gender_list)*100
        women_percentage = self.gender_list.count(
            'w')/len(self.gender_list)*100
        return f'The women percentage are {women_percentage}% and man are {mens_percentage}%'

    def showDataTable(self, users: int) -> list:
        print('------------------------')
        print("Name\tAge\tGender")
        print('------------------------')
        for i in range(users):
            print(self.name_list[i],'\t',self.age_list[i],'\t',self.gender_list[i],'\n')


if __name__ == '__main__':
    balance = AverageMensandWomen()
    users = int(input('Please enter the number of users to fill them: '))
    balance.askNumberUsers(users=users)
    print('Mean of Ages: ', balance.calculateAgeAverage())
    print(balance.calculateGenderPercentage())
    print("Printing the data typed:")
    balance.showDataTable(users=users)
