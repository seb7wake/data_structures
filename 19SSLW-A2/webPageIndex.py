class WebPageIndex():

    def __init__(self, file):
        self.path = file
        self.contents = ""
        with open (self.path, "r") as myfile:
            #read file
            self.contents += myfile.read()
            myfile.close()
        self.contents = self.contents.lower() #make lowercase
    
    def getCount(self, contents, s):
        # remove non-letters
        print(self.contents)
        wordList = self.contents.replace('\n', '').replace(".", "").replace('(', " ").replace(')', " ").replace('/', ' ').replace(',', '').split()
        # get a list of all words that match
        sList = [i for i in wordList if i == s]
        return len(sList)


if __name__ == '__main__': 
    wpi = WebPageIndex('data/doc2-graph.txt')
    print(wpi.getCount(wpi, 'or'))