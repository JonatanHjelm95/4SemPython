import numpy as np
import matplotlib.pyplot as plt


neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}

def sort_by_size(areas):
    return sorted(areas.values())



#1,2,3
def get_area_size(filename):
    ndarray = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
    neighbSum = {}
    for n in neighb:
        mask = (ndarray[:,0] == 2015) & (ndarray[:,1] == n)
        mm = np.sum(ndarray[mask][:,4])
        neighbSum[n] = mm
    return neighbSum

#4
def area_chart():
    areaSizes = get_area_size('HandIn4/befkbhalderstatkode.csv')
    areaSizesSorted = sort_by_size(areaSizes)
    areaSizesSwap = dict([(value, key) for key, value in areaSizes.items()])
    areaNames = []
    for a in areaSizesSorted:
        areaNames.append(neighb[areaSizesSwap[a]])
    sortedNeigbh = {}
    y_pos = np.arange(len(areaSizes))
    plt.xticks(y_pos, areaNames)
    plt.bar(y_pos, areaSizesSorted, align='center', alpha=0.5)
    plt.ylabel('Area sizes')
    plt.show()

#5, 6
def amount_of_ppl_above_65():
    ndarray = np.genfromtxt('HandIn4/befkbhalderstatkode.csv', delimiter=',', dtype=np.uint, skip_header=1)
    #SWEDEN = 5120, NORWAY = 5110, FINLAND = 5104, ICELAND = 5106
    mask = (ndarray[:,0] == 2015) & (ndarray[:,2] > 65)
    nordicStateArray = [5120, 5110, 5104, 5106]
    maskedNdArray = ndarray[mask]
    nordicAmount = 0
    for n in nordicStateArray:
        nordicMask = (maskedNdArray[:,3] == n)
        nordicAmount += np.sum(maskedNdArray[nordicMask][:,4])
    amount_above_65 = np.sum(ndarray[mask][:,4])
    print('amount above 65', amount_above_65)
    print('amount of nordic-non-danes above 65', nordicAmount)

#7
def change_chart():
    ndarray = np.genfromtxt('HandIn4/befkbhalderstatkode.csv', delimiter=',', dtype=np.uint, skip_header=1)
    osterbro = []
    vesterbro = []
    year = []
    for i in range(1992, 2015):
        oMask = (ndarray[:,0] == i) & (ndarray[:,1] == 2)
        vMask = (ndarray[:,0] == i) & (ndarray[:,1] == 4)
        year.append(i)
        osterbro.append(np.sum(ndarray[oMask][:,4]))
        vesterbro.append(np.sum(ndarray[vMask][:,4]))
    y_pos = np.arange(len(osterbro))
    plt.xticks(y_pos, year)
    plt.plot(osterbro)
    plt.plot(vesterbro)
    plt.show()



if __name__ == '__main__':
    change_chart()
    #amount_of_ppl_above_65()
    #area_chart()    