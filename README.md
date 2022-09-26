# live-feed-plot-using-matplotlib

> ## ***Documentation***
~~~
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
