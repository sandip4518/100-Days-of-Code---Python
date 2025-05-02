glob=1
def myfun():
    def in_(glob):
        glob+=1
        print(glob)
    glob=2
    in_(glob)
    print(glob)

myfun()
