from abc import ABC


class field(ABC):
    filetype = None


    def __init__(self, max_length=255, unique=None ):
        if unique is True :
            self.unique = 'UNIQUE'
        else:
            self.unique = ''

        if max_length :
            self.max_length = max_length

    def __repr__(self):
        column = []
        if self.filetype == 'VARCHAR':
            column.append(f'VARCHAR ({self.max_length})')
        else:
            column.append(self.filetype)
            column.append(self.unique)
        return ''.join(column).strip()



class Char(field):
    filetype = 'VARCHAR'
    def __init__(self,max_length=255, uniuqe = None):
        self.max_length = max_length
        self.unique = uniuqe
        super().__init__(max_length=max_length, unique=uniuqe)


class Text(field):
    filetype = 'TEXT'

    def __init__(self, uniuqe=None):
        self.unique = uniuqe
        super().__init__(unique=uniuqe)


class Integer(field):
    filetype = 'INTEGER'

    def __init__(self, uniuqe=None):
        self.unique = uniuqe
        super().__init__(unique=uniuqe)
