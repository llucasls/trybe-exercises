class Log:
    def __init__(self):
        self.__style_list = {
            "bold": "1",
            "italic": "3",
            "dim": "2",
            "underlined": "5",
            "strike": "9",
            "black": "30",
            "red": "31",
            "green": "32",
            "yellow": "33",
            "blue": "34",
            "magenta": "35",
            "cyan": "36",
            "white": "37",
            "bright_black": "90",
            "bright_red": "91",
            "bright_green": "92",
            "bright_yellow": "93",
            "bright_blue": "94",
            "bright_magenta": "95",
            "bright_cyan": "96",
            "bright_white": "97",
            "reset": "0",
        }

    def style(self, *args):
        style_args = args or ["reset"]
        style_code = [self.__style_list[index] for index in style_args]
        style_string = ";".join(style_code)
        return f"\x1b[{style_string}m"

    def success(self, message):
        style = self.style("bold", "green")
        reset = self.style("reset")
        print(f"{style}Success{reset}: {message}")

    def warn(self, message):
        style = self.style("bold", "yellow")
        reset = self.style("reset")
        print(f"{style}Warning{reset}: {message}")

    def error(self, message):
        style = self.style("bold", "red")
        reset = self.style("reset")
        print(f"{style}Error{reset}: {message}")


log = Log()
log.success("O sistema está funcionando")
log.warn("O sistema está lento")
log.error("O sistema está com erros")
