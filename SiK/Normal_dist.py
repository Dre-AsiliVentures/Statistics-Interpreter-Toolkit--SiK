class normal:
    def __init__(self,values):
        self.values=values
        #self.mean=mean
        #self.median=median
        #self.mode=mode
        # self.mean=values.mean()
        # self.median=values.median()
        self.normal=normal=False
    def check_normal(values):
        normal=(values.mean()==values.median())
        print("Normal sries looks like: {}".format(normal))
        print("Thus the normal distribution is: {}".format(normal.all()))
        return normal.all()
