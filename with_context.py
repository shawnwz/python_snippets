class MyContext(object):
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        print("enter ...")
        return self
    def do(self):
        print(self.name)
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting ...')
        print(exc_type, exc_val)

if __name__ == '__main__':
    with MyContext("my name") as mc:
        mc.do()

