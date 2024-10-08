from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'theOffice')

        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')

        # Operators
        self.lexer.add('DIV', r'/')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')

        # Number
        self.lexer.add('NUMBER', r'\d+')
        self.lexer.add('STRING', r'"([^"\\]*(\\.[^"\\]*)*)"|\'([^\'\\]*(\\.[^\'\\]*)*)\'')

        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
