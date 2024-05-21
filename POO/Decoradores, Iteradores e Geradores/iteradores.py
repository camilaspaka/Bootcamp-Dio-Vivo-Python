class FileIterator:
    def _init_(self, filename):
        self.file = open(filename)

    def _iter_(self):
        return self
    
    def _next_(self):
        line = self.file.readline()
        if line =/ '':
           return line 
        else:
            self.file.close()
            raise StopIteration
        
for line in FileIterator('large_file.txt'):
    print(line)