# live-feed-plot-using-matplotlib

> ## ***Documentation***
~~~ python
NAME
    live_feed_plot

CLASSES
    builtins.object
        Stream

    class Stream(builtins.object)
     |  Methods defined here:
     |
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  close(self)
     |
     |  liveFeed(self, x, y, color='black', time=0.2)
     |      plot live (x,y) data
     |      Return live plot
     |
     |  makeFeed_DFC(self, data, color='black', time=0.2)
     |      plot live (data frame column) data
     |      Return live plot
     |      here DFC -> Data Frame Column
     |
     |  makeFeed_XY(self, x_data, y_data, color='black', time=0.2)
     |      plot live (list of x_data, list of y_data) data
     |      Return live plot
     |
     |  makeMultiFeed_XY(self, x_data, func_data, color=[], time=0.2)
     |      plot live (x_axis, list of function data)
     |      Return live plot
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
~~~

> ## ***Examples***
> ### .liveFeed
~~~ python
import matplotlib.pyplot as plt
import live_feed_plot as livePlot
import numpy as np

stream = livePlot.Stream()

def func(x):
    y = 10*x**2
    return y

for x in np.linspace(-4,4,100):
    stream.liveFeed(x,func(x),color="red",time=0.1)

stream.close()
plt.show()
~~~

> ### .makeFeed_XY
~~~ python
import matplotlib.pyplot as plt
import live_feed_plot as livePlot
import numpy as np

stream = livePlot.Stream()

dataX = np.linspace(0,10,200)
dataY = np.sin(dataX)

stream.makeFeed_XY(dataX, dataY,color="red",time=0.05)

stream.close()
plt.show()
~~~

> ### .makeFeed_DFC
~~~ python
import matplotlib.pyplot as plt
import live_feed_plot as livePlot
import pandas as pd 
import numpy as np

stream = livePlot.Stream()

glaxo = pd.read_csv("C:\\Users\Rupam\GLAXO.csv")[:100]
stream.makeFeed_DFC(glaxo["Close"],time=0.2)

stream.close()
plt.show()
~~~

> ### .makeMultiFeed_XY
~~~python
import matplotlib.pyplot as plt
import live_feed_plot as livePlot
import numpy as np

stream = livePlot.Stream()

x = np.linspace(0,10,100)
y1 = np.sin(x)
y2 = np.cos(x)

stream.makeMultiFeed_XY(x,[y1,y2],color=['red','green'],time=0.1)

stream.close()
plt.show()
~~~
