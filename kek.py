class Converter():
    def __init__(self):
        """
        Конструктар класса ковертера, инициализирует массив величин __names и
        массив значений для преобразования величин
        """
        self.__names = []
        self.__quantitiesMult = []

    def addQuantities(self, name, arrFromQuant):
        """
        Добавление новой величены с передающимся именем и массивом преобразований для текущего размера матрицы
        :param name: имя величины
        :param arrFromQuant: массив преобразований в другие величины
        """
        if len(self.__quantitiesMult) == 0:
            self.__quantitiesMult.append([1])
        else:
            arrFromQuant = self.__checkSimilarWay(arrFromQuant)
            if len(arrFromQuant) > len(self.__quantitiesMult):
                arrFromQuant[len(arrFromQuant) - 1] = 1
            else:
                arrFromQuant.append(1)
            self.__quantitiesMult.append(arrFromQuant)
            self.__appendNewWay(arrFromQuant)
        self.__names.append(name)

    def __checkSimilarWay(self, arrFromQuant):
        """
        Поиск и добавление путей между величинами для конвертации если они возможны но не обозначены пользователем
        :param arrFromQuant: исходный массив конвертации
        :return: отредактированный массив конвертации
        """
        for i in range(len(arrFromQuant)):
            if arrFromQuant[i] == 0:
                for j in range(len(arrFromQuant)):
                    if arrFromQuant[j] != 0 and self.__quantitiesMult[i][j] != 0:
                        arrFromQuant[i] = arrFromQuant[j] / self.__quantitiesMult[i][j]
                        break
        return arrFromQuant

    def __appendNewWay(self, arrFromQuant):
        """
        Добавление нового массива преобразования в исходный массив преобразований
        :param arrFromQuant: массив преобразований для добавления
        """
        for i in range(len(self.__quantitiesMult) - 1):
            if len(arrFromQuant) > i and arrFromQuant[i] != 0:
                self.__quantitiesMult[i].append(1 / arrFromQuant[i])
            else:
                self.__quantitiesMult[i].append(0)

    def transferQuant(self, indexFrom, indexTo, valTransfer):
        """
        Перевод значения одной величины в другую
        :param indexFrom: индекс откуда нужно переводить
        :param indexTo: индекс куда нужно переводить
        :param valTransfer: значение которое нужно переводить
        :return: новое значение
        """
        return valTransfer * self.__quantitiesMult[indexFrom][indexTo]

    def getIdByName(self, name):
        """
        Получить индекс величины по имени
        :param name: имя по которому нужно получиьт индекс
        :return: индекс
        """
        return self.__names.index(name)

    def getNames(self):
        """
        Получить все имена величин
        :return: имена величин
        """
        return self.__names

    def getQuantities(self):
        """
        Получить массив величин конвертации
        :return: массив величин конвертации
        """
        return self.__quantitiesMult
