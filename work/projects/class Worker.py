class WOrker:
    def __init__(self, name, job):
        self.name = name
        self.job = job


class Search_WOrker(WOrker):
    def __init__(self, name, job):
        super.__init__(self)


alan = WOrker('Alan', 'Boss')
alan.info_worker()







    