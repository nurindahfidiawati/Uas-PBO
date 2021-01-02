from abc import ABC, abstractmethod

class login:
     def setUserPass (self,userName):
          pass

     def IsValiduser (self):
          pass

     def getUserName (self):
          pass

     def getPassword (self):
          pass

class masuk(login):
     def setUserPass(self, userName, password):
          self.userName = userName
          self.password = password

     def IsValiduser(self):
         return 'cek kembali username dan password'

     def getUserName(self):
          return self.userName 
          

     def getPassword(self):
         return self.password

