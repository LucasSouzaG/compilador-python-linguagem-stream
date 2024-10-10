class Dictionary:
    dictionary = [("Corra", "for"),
              ("na", "in"),
              ("faca", ":"),
              ("AteoUltimoHomem", "while"),
              ("TopaOuNaoTopa ", "elif"),
              ("eAssimQueAcaba", "else:"),
              ("entao", ":"),
              ("batmanBegins", "if"),
              ("BobOConstrutor", "def"),
              (" e ", " and "),
              (" ou ", " or "),
              ("NaoDurma", "not"),
              ("(", "("),
              (")", ")"),
              ("SemMedoDaVerdade", "True"),
              ("FalsaIdentidade", "False"),
              ("theOffice", "print"),
              ("oRetornoDoJedi", "return"),
              ("Valente", "range"),
              (" ", " ")]

    stream_words = [word[0] for word in dictionary]
    py_words = [word[1] for word in dictionary]

    def __init__(self):
        pass
    
    def word_validation(self, word_to_validate):
        return word_to_validate in self.stream_wowrds

