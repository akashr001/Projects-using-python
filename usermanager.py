from Models.User import User

class usermanager:

    __users=[]

    @classmethod
    def AddUser(cls, user):

      if isinstance(user,User):
          cls.__users.append(user)
          print("you have been successfully registered")
      else:
          print("invalid user")

    @classmethod
    def FindUser(cls,mailid,paswd):
        for User in cls.__users:
            if User.MailId == mailid and User.Password ==paswd:
                return User
