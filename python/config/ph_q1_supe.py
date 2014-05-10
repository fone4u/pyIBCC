import numpy as np

print 'Configuring IBCC'

#Include the simulations as training data.

def translateGold(gold):
    #turn the EBs and simulations into instances of "planet"
    gold[gold==2] = 1
    gold[gold==3] = 1
    gold[gold==-1] = 0
    return gold

scores = np.array([9, 10])
nScores = len(scores)
nClasses = 2
inputFile =   './data/PH data/PlanetHunters_3-26-14_Q1_ann_realAndSim.csv'
goldFile =    './data/PH data/PlanetHunters_3-26-14_Q1_light_curves_and_sims.csv'
outputFile =  './output/ph/output.csv'
confMatFile = './output/ph/confMat.csv'
classLabels=None#do this conversion in a spreadsheet due to bugs['candidate','planet','eb','simulation']
alpha0 = np.array([[1, 2], [2, 1]]) #for PH data
nu0 = np.array([10.0, 10.0])
trainIdFile = './data/PH data/PlanetHunters_3-26-14_Q1_simulations_IBCC.csv'
try:
    trainIds = np.genfromtxt(trainIdFile, delimiter=',', skip_header=1,usecols=[0,1],invalid_raise=True)
except Exception:
    trainIds = np.genfromtxt(trainIdFile, delimiter=',', skip_header=1)
trainIds = trainIds[:,0]

print 'Planet hunters 2-class config done.'