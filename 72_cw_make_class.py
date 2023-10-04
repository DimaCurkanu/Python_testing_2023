def make_class(*args):
    class Data:
        def __init__(self, *data_list):
            for name, value in zip(args, data_list):
                setattr(self, name, value)
    return Data
'''
Solution from SergeDot
'''