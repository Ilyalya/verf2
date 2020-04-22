import unittest
import string
import random
from kek import Converter


class TestMainConvert(unittest.TestCase):
    def testConverterNotNone(self):
        converter = Converter()
        self.assertIsNotNone(converter, "converter cant be None")

    def testCheckNamesNotNone(self):
        converter = Converter()
        self.assertIsNotNone(converter.getNames(), "names cant be None")

    def testNamesIsArr(self):
        converter = Converter()
        self.assertIsInstance(converter.getNames(), list, "name should have type list")

    def testQuantitiesNotNone(self):
        converter = Converter()
        self.assertIsNotNone(converter.getQuantities(), 'quantities cant be None')

    def testQuantitesIsArr(self):
        converter = Converter()
        self.assertIsInstance(converter.getQuantities(), list, "quantities should have type list")

    def testAddOneQuantites_m_emptyList(self):
        converter = Converter()
        converter.addQuantities("m", [])

        self.assertEqual(1, len(converter.getNames()), "count name should be 1")
        self.assertEqual("m", converter.getNames()[0], "zero elem should be m")

    def nameGenerator(self, sizeName=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(sizeName))

    def testCheckName100_Random_emptyList(self):
        converter = Converter()
        size = 100
        for i in range(size):
            name = self.nameGenerator()
            converter.addQuantities(name, [])
            self.assertEqual(i + 1, len(converter.getNames()), "count name should be " + str(i + 1))
            self.assertEqual(name, converter.getNames()[i], "zero elem should be m")

    def testNormalQuantAddOneQuantites_m_emptyList(self):
        converter = Converter()
        converter.addQuantities("m", [])

        self.assertEqual(1, len(converter.getQuantities()), "count quantities matrix should be 1")
        self.assertEqual(1, converter.getQuantities()[0][0], "should be 1")

    def testCheckQunat100_RandomName_randomList(self):
        converter = Converter()
        size = 100
        for i in range(size):
            name = self.nameGenerator()
            converter.addQuantities(name, [random.randint(0, 100)] * (i + 1))
            self.assertEqual(i + 1, len(converter.getNames()), "count name should be " + str(i + 1))
            self.assertEqual(name, converter.getNames()[i], "zero elem should be m")

            self.assertEqual(i + 1, len(converter.getQuantities()), "count quant should be " + str(i + 1))

            for k in range(i + 1):
                self.assertEqual(i + 1, len(converter.getQuantities()[k]))

    def testMainDiadQuant100_EmptyName_randomList(self):
        converter = Converter()
        size = 100
        for i in range(size):
            listAdd = [random.randint(0, 100)] * (i)
            converter.addQuantities("", listAdd)

            self.assertEqual(1, converter.getQuantities()[i][i], "quant diag should be 1")

    def testElemRelativeDiag100_EmptyName_randomList(self, size = 100):
        converter = Converter()
        for i in range(size):
            listAdd = [random.randint(0, size)] * (i)
            converter.addQuantities("", listAdd)

            for k in range(i + 1):
                for m in range(i + 1):
                    if (k < m):
                        if (converter.getQuantities()[k][m] != 0):
                            self.assertAlmostEqual(1, converter.getQuantities()[k][m] * converter.getQuantities()[m][k], msg="elem relative diag should be 1", delta=0.0000001)
                        else:
                            self.assertEqual(0, converter.getQuantities()[k][m] * converter.getQuantities()[m][k], msg="elem relative diag should be 0")


    def checkSimilarWay(self, matrixBase, arrFromQuant):
        resArr = [0] * len(arrFromQuant)
        for i in range(len(arrFromQuant)):
            resArr[i] = arrFromQuant[i]

        for i in range(len(resArr)):
            if resArr[i] == 0:
                for j in range(len(resArr)):
                    if resArr[j] != 0 and matrixBase[i][j] != 0:
                        resArr[i] = resArr[j] / matrixBase[i][j]
                        break
        resArr.append(1)
        return resArr

    def testSimilarWayQuant100_EmptyName_RandomListWithMoreZero(self, size=100):
        converter = Converter()
        for i in range(size):

            listAdd = [0] * (i)
            for k in range(i):
                if random.randint(0, 1) == 1:
                    listAdd[k] = random.randint(0, size)
            arrTest = self.checkSimilarWay(converter.getQuantities(), listAdd)
            converter.addQuantities("", listAdd)

            for k in range(i + 1):
                if len(arrTest) > 0:
                    self.assertAlmostEqual(arrTest[k], converter.getQuantities()[len(converter.getQuantities()) - 1][k], msg='elems shoud be equals (' + str(i) + ')', delta=0.0000000001)

    def testGetIdByName_10_NumName_ZeroParams(self):
        converter = Converter()
        for i in range(10):
            converter.addQuantities(str(i), [0] * i)

        for i in range(20):
            baseName = random.randint(0, 9)
            self.assertEqual(baseName, converter.getIdByName(str(baseName)))

    def testTransferQuant100_RandomValue(self):
        converter = Converter()
        for i in range(100):
            converter.addQuantities(str(i), [random.randint(0, 100)] * i)

        for i in range(1000):
            valueTest = random.randint(0, 1000) + random.random()
            indexFrom = random.randint(0, len(converter.getQuantities()) - 1)
            indexTo = random.randint(0, len(converter.getQuantities()) - 1)
            self.assertAlmostEqual(valueTest * converter.getQuantities()[indexFrom][indexTo], converter.transferQuant(indexFrom, indexTo, valueTest))
