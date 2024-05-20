#1
# Yo ba w yon lis nonb ki reprezante laj yon gwoup moun, ekri yon fonksyon Python ki pou kalkile mwayèn laj gwoup sa.
# ages = [23, 45, 34, 24, 26, 29, 31, 40, 38, 37]

import math
ages = [23, 45, 34, 24, 26, 29, 31, 40, 38, 37]
def mean(ag):
    moy=sum(ag)/len(ag)
    return(moy)
print(mean(ages))

#2
# Yo ba w yon lis nonb ki reprezante nòt yon gwoup etidyan ki pase yon tès, ekri yon fonksyon ki pou kalkile varyans nòt yo:
# scores = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
# V= ( Σ (x-μ)² ) / N

scores = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
def variance(scs):
    x=0
    moy=mean(scs)
    for i in scs:
       x=moy-i 
    vrc= x**2/len(scs)
    return vrc
print(variance(scores))


#3
# Yo ba w yon lis nonb ki reprezante pwa yon gwoup moun an kilogram, ekri yon fonksyon Python ki pou kalkile eka-tip lis pwa moun sa yo.
# weights = [68, 70, 75, 80, 72, 69, 78, 74, 73, 77] 
# σ(X)=√V(X) 

weights = [68, 70, 75, 80, 72, 69, 78, 74, 73, 77]  
def standdev(wgs):
    var=variance(wgs)
    ekatip=math.sqrt(var)
    return ekatip
print(standdev(weights))

#4
# Yo ba w yon lis ki reprezante salè yon lis anplwaye nan yon antrepriz, 
# ekri yon fonksyon Python ki ap kalkile mwayèn, varyans, ak eka-tip lis salè sa yo.
# incomes = [3000, 3200, 2900, 3100, 3050, 3000, 2950, 2800, 3150, 3300]

incomes = [3000, 3200, 2900, 3100, 3050, 3000, 2950, 2800, 3150, 3300]
def mve(ics):
    moy=mean(ics)
    var=variance(ics)
    ekatip=standdev(ics)
    return moy,var,ekatip
print(mve(incomes))

#5
# Sa se popilasyon vil pòtoprens sou 2 ane diferan, 
# ekri yon fonksyon Python ki ap kalkile pousantaj kwasans vil sa.
# population_2010 = 50000
# population_2020 = 65000

population_2010 = 50000
population_2020 = 65000
def growthpercent(pop1, pop2):
    kwasans=((pop2-pop1)/pop1)*100
    return kwasans
print(growthpercent(population_2010,population_2020))

#6
# Itilize fòmil kwasans eksponansyèl la, pou w predi popilasyon vil pòtoprens aprè yon kantite ane.
# Fòmil la se:
# P(f) = P(k) x (1 + r)**t
# p(k) => Popilasyon kounya 
# r => kwasans anyèl la
# t => kantite lane prediksyon an

population_2010 = 50000
population_2020 = 65000
def prediksyon(pop2,r,ktane):
    pred=pop2*(1+r)**(ktane)
    return pred
print(prediksyon(60000,0.3,10))

