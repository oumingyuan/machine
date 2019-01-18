from numpy.random import rand
from matplotlib import pyplot
import pandas

dataFrame = pandas.DataFrame(rand(10, 4), columns=['A', 'B', 'C', 'D'])

dataFrame.plot.bar()
# dataFrame.plot.barh()
# dataFrame.plot.bar(stacked=True)


pyplot.show()
