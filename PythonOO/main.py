import crypt
import datetime

class User:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self._salt = crypt.mksalt()
        self._password = self._crypt_pwd(password)

    def _crypt_pwd(self, password):
        return crypt.crypt(password, self._salt)

    def check_pwd(self, password):
        return self._password == self._crypt_pwd(password)

    def post(self, message):
        return Post(self, message)

class Post:
    def __init__(self, author, message):
        self.author = author
        self.message = message
        self.date = datetime.datetime.now()

    def format(self):
        date = self.date.strftime('le %d/%m/%Y à %H:%M:%S')
        return '<div><span>Par {} {}</span><p>{}</p></div>'.format(self.author.name, date, self.message)

if __name__ == '__main__':
    user = User(1, 'john', '12345')
    p = user.post('Salut à tous')
    print(user._password)
    print(p.format())