quotes = {}


class QuoteModel:
    def get_quote(slef, n):
        try:
            value = quotes[n]
        except IndexError as err:
            value = "Not found"
        return value


class QuoteTerminalView:
    def show(self, quote):
        print(f"and the quote is:{quote}")

    def error(self, msg):
        print(f"error:{msg}")

    def select_quote(self):
        return input('which quote number would you like to see?')

    class QuoteTerminalController:
        def __init__(self):
            self.model = QuoteModel()
            self.view = QuoteTerminalView()

        def run(self):
            valid_input = False
            while not valid_input:
                try:
                    n = self.view.select_quote()
                    n = int(n)
                    valid_input = True
                except ValueError:
                    self.view.error()
            quote = self.model.get_quote(n)
            self.view.show(quote)
