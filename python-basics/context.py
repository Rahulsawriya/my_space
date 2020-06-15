"""context: context is defined by the context manager, The primary motivation behind context managers is resource management.
Context managers allow you to allocate and release resources precisely when you want to. The most widely used example of context managers is the with statement.
Python developers have created a library named contextlib containing utilities regarding context managers."""


#File management using context manager :
class FileManager(): 
    def __init__(self, filename, mode): 
        self.filename = filename 
        self.mode = mode 
        self.file = None
          
    def __enter__(self): 
        self.file = open(self.filename, self.mode) 
        return self.file
      
    def __exit__(self, exc_type, exc_value, exc_traceback): 
        self.file.close() 
  
# loading a file  
with FileManager('test.txt', 'w') as f: 
    f.write('Test') 
  
print(f.closed)