import sys
from PyQt5 import QtWidgets, uic
from mpmath import log10, ln, sqrt, fac
import decimal


def except_hook(cls, exception, traceback):  # PyQt5 doesn't output traceback errors by default
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    sys.excepthook = except_hook

qt_file = "Simple_Calculator.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_file)

# Define custom functions to act as a syntax-bridge between the name used in display and eval


def factorial(num: float) -> float:
    return fac(num)


def log(num: float) -> float:
    return log10(num)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Calculator")
        self.button_add.clicked.connect(self.clicked_add)
        self.button_minus.clicked.connect(self.clicked_minus)
        self.button_multiply.clicked.connect(self.clicked_multiply)
        self.button_divide.clicked.connect(self.clicked_divide)
        self.button_open_bracket.clicked.connect(self.clicked_open_bracket)
        self.button_close_bracket.clicked.connect(self.clicked_close_bracket)
        self.button_zero.clicked.connect(self.clicked_zero)
        self.button_one.clicked.connect(self.clicked_one)
        self.button_two.clicked.connect(self.clicked_two)
        self.button_three.clicked.connect(self.clicked_three)
        self.button_four.clicked.connect(self.clicked_four)
        self.button_five.clicked.connect(self.clicked_five)
        self.button_six.clicked.connect(self.clicked_six)
        self.button_seven.clicked.connect(self.clicked_seven)
        self.button_eight.clicked.connect(self.clicked_eight)
        self.button_nine.clicked.connect(self.clicked_nine)
        self.button_equals.clicked.connect(self.clicked_equals)
        self.button_clear.clicked.connect(self.clicked_clear)
        self.button_delete.clicked.connect(self.clicked_delete)
        self.button_decimal.clicked.connect(self.clicked_decimal)
        self.button_square_root.clicked.connect(self.clicked_square_root)
        self.button_factorial.clicked.connect(self.clicked_factorial)
        self.button_log_10.clicked.connect(self.clicked_log_10)
        self.button_log_e.clicked.connect(self.clicked_log_e)
        self.button_pi.clicked.connect(self.clicked_pi)
        self.button_e.clicked.connect(self.clicked_e)
        self.button_square.clicked.connect(self.clicked_square)
        self.button_power.clicked.connect(self.clicked_power)
        self.button_modulus.clicked.connect(self.clicked_modulus)
        self.button_exponential.clicked.connect(self.clicked_exponential)

        self.operators = ["+", "-", "x", "÷", "^"]
        # Map ordinary operators/symbols to Python syntax
        self.dictionary = {"^": " ** ",
                           "√": "sqrt",
                           "x": "*",
                           "÷": "/",
                           }

        self.setStyleSheet("background-color: rgb(0, 0, 0)")
        style_sheet_1 = "color: rgb(255,69,0); background-color: rgb(45, 45, 45); font-size: 18pt"
        style_sheet_2 = "color: rgb(255, 255, 255); background-color: rgb(45, 45, 45); font-size: 18pt"
        style_sheet_3 = "color: rgb(255, 255, 255); background-color: rgb(25, 25, 25); font-size: 18pt"

        self.label_display.setStyleSheet("color: rgb(255, 255, 0); background-color: rgb(0, 0, 0); font-size: 12pt")
        self.button_equals.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(255,69,0); font-size: 18pt")
        self.button_decimal.setStyleSheet(style_sheet_2)
        self.button_delete.setStyleSheet(style_sheet_2)
        self.button_clear.setStyleSheet(style_sheet_2)
        self.button_add.setStyleSheet(style_sheet_1)
        self.button_minus.setStyleSheet(style_sheet_1)
        self.button_multiply.setStyleSheet(style_sheet_1)
        self.button_divide.setStyleSheet(style_sheet_1)
        self.button_open_bracket.setStyleSheet(style_sheet_2)
        self.button_close_bracket.setStyleSheet(style_sheet_2)
        self.button_square_root.setStyleSheet(style_sheet_2)
        self.button_square.setStyleSheet(style_sheet_2)
        self.button_power.setStyleSheet(style_sheet_2)
        self.button_factorial.setStyleSheet(style_sheet_2)
        self.button_log_10.setStyleSheet(style_sheet_2)
        self.button_log_e.setStyleSheet(style_sheet_2)
        self.button_e.setStyleSheet(style_sheet_2)
        self.button_pi.setStyleSheet(style_sheet_2)
        self.button_zero.setStyleSheet(style_sheet_3)
        self.button_one.setStyleSheet(style_sheet_3)
        self.button_two.setStyleSheet(style_sheet_3)
        self.button_three.setStyleSheet(style_sheet_3)
        self.button_four.setStyleSheet(style_sheet_3)
        self.button_five.setStyleSheet(style_sheet_3)
        self.button_six.setStyleSheet(style_sheet_3)
        self.button_seven.setStyleSheet(style_sheet_3)
        self.button_eight.setStyleSheet(style_sheet_3)
        self.button_nine.setStyleSheet(style_sheet_3)
        self.button_modulus.setStyleSheet(style_sheet_2)
        self.button_exponential.setStyleSheet(style_sheet_2)
        self.grid_layout.setHorizontalSpacing(2)
        self.grid_layout.setVerticalSpacing(2)
        # self.label_display.adjustSize()

    def clicked_add(self) -> None:
        text: str = self.label_display.text()
        if text == "":  # Default to zero if text is empty
            self.label_display.setText(text + "0 + ")
        elif text.strip()[-1] in self.operators:  # Overrides previous operator
            new_text = text.strip().replace(text[-1], " + ")
            self.label_display.setText(new_text[:-1])
        else:
            self.label_display.setText(text + " + ")

    def clicked_minus(self) -> None:
        text: str = self.label_display.text()
        if text == "":
            self.label_display.setText(text + "0 - ")
        elif text.strip()[-1] in ["+", "-"]:
            """^, x and ÷ excluded for cases like 4 ^ -5, 4 x -5 and 4 ÷ -5 where the operators shouldn't be replaced"""
            new_text = text.strip().replace(text[-1], " - ")
            self.label_display.setText(new_text[:-1])
        else:
            self.label_display.setText(text + " - ")

    def clicked_multiply(self) -> None:
        text: str = self.label_display.text()
        if text == "":
            self.label_display.setText(text + "0 x ")
        elif text.strip()[-1] in self.operators:
            new_text = text.strip().replace(text[-1], " x ")
            self.label_display.setText(new_text[:-1])
        else:
            self.label_display.setText(text + " x ")

    def clicked_divide(self) -> None:
        text: str = self.label_display.text()
        if text == "":
            self.label_display.setText(text + "0 ÷ ")
        elif text.strip()[-1] in self.operators:
            new_text = text.strip().replace(text[-1], " ÷ ")
            self.label_display.setText(new_text[:-1])
        else:
            self.label_display.setText(text + " ÷ ")

    def clicked_open_bracket(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in [str(i) for i in range(0, 10)]:
            self.label_display.setText(text + " ( ")
        else:
            """If there isn't any operator before the bracket, default to multiplication"""
            self.label_display.setText(text + " x ( ")

    def clicked_close_bracket(self) -> None:
        text: str = self.label_display.text()
        self.label_display.setText(text + ")")

    def clicked_zero(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in ["π", "e"]:
            self.label_display.setText(text + "0")
        else:
            self.label_display.setText(text + " x 0")

    def clicked_one(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in ["π", "e"]:
            self.label_display.setText(text + "1")
        else:
            self.label_display.setText(text + " x 1")

    def clicked_two(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in ["π", "e"]:
            self.label_display.setText(text + "2")
        else:
            self.label_display.setText(text + " x 2")

    def clicked_three(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in ["π", "e"]:
            self.label_display.setText(text + "3")
        else:
            self.label_display.setText(text + " x 3")

    def clicked_four(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in ["π", "e"]:
            self.label_display.setText(text + "4")
        else:
            self.label_display.setText(text + " x 4")

    def clicked_five(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in ["π", "e"]:
            self.label_display.setText(text + "5")
        else:
            self.label_display.setText(text + " x 5")

    def clicked_six(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in ["π", "e"]:
            self.label_display.setText(text + "6")
        else:
            self.label_display.setText(text + " x 6")

    def clicked_seven(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in ["π", "e"]:
            self.label_display.setText(text + "7")
        else:
            self.label_display.setText(text + " x 7")

    def clicked_eight(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in ["π", "e"]:
            self.label_display.setText(text + "8")
        else:
            self.label_display.setText(text + " x 8")

    def clicked_nine(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in ["π", "e"]:
            self.label_display.setText(text + "9")
        else:
            self.label_display.setText(text + " x 9")

    def match_brackets(self, string) -> str:
        """Automatically closes bracket at the end
        Note that the expected order of operations may change because the bracket is added only at the end
        Useful when user forgets to close all brackets"""
        characters = [char for char in string]
        num_of_open_brackets = characters.count("(")
        num_of_closed_brackets = characters.count(")")
        difference = num_of_open_brackets - num_of_closed_brackets
        return string + ")" * difference  # Add the required number of brackets

    def replace_e(self, equation) -> str:
        """Separate method for replacing "e" because str.replace() doesn't work in cases like "123e+27", "9263e-7", etc.
        Here, e is used for decimal representation purposes and replacing it causes a syntax error"""
        characters = [char for char in equation]
        for i in range(0, len(characters)):
            if characters[i] == "e" and characters[i - 1] not in [str(j) for j in range(0, 10)] or i == 0 and characters[i] == "e":
                # If the char before e is not a digit, then e is being used in some operation and is replaced
                characters[i] = "2.718281828459045"
        new_equation = "".join(characters)
        return new_equation

    def clean_up(self) -> str:  # Make the equation ready for evaluation
        equation: str = self.label_display.text()
        # Replace general operators/symbols to Python syntax with the help of a dictionary
        characters: list = equation.split(" ")
        new: list = []
        for i in characters:
            function: str = self.dictionary.get(i, i)
            new += function
        new_equation: str = ""
        for j in new:
            new_equation += j
        new_equation = self.match_brackets(new_equation)

        new_equation = self.replace_e(new_equation)
        new_equation = new_equation.replace("π", "3.14_159_265_358_979")
        return new_equation

    def clicked_equals(self) -> None:
        new_equation: str = self.clean_up()
        characters: list = new_equation.split(" ")
        try:
            answer = eval(new_equation)
        except SyntaxError:
            self.label_display.setText("Invalid operation")
        except ZeroDivisionError:
            self.label_display.setText("Can't divide by zero")
        except ValueError:
            self.label_display.setText("Error")
        except OverflowError:
            self.label_display.setText("infinity")
        except TypeError:
            self.label_display.setText("Error")

        else:  # Runs only if no error
            if answer.imag == 0 and answer.real > 10_000_000_000_000_000:
                if "**" in characters:  # Decimal representation issues
                    d = decimal.Decimal(answer)
                    new_answer = str(format(d, ".6e"))
                    self.label_display.setText(new_answer.replace("j", "i"))  # i instead of j for complex numbers
                else:
                    new_answer = str(answer)
                    self.label_display.setText(new_answer.replace("j", "i"))
            else:
                new_answer = str(answer)
                self.label_display.setText(new_answer.replace("j", "i"))

    def clicked_clear(self) -> None:
        self.label_display.setText("")

    def clicked_delete(self) -> None:
        text: str = self.label_display.text()
        if text == "":
            self.label_display.setText("")
        elif text != "" and text[-1] != " ":
            self.label_display.setText(text[:-1])
        else:
            self.label_display.setText(text[:-2])  # To avoid pressing delete twice

    def clicked_decimal(self) -> None:
        text: str = self.label_display.text()
        if text == "":
            self.label_display.setText(text + "0.")  # If empty, default to 0.
        else:
            self.label_display.setText(text + ".")

    def clicked_square_root(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in [str(i) for i in range(0, 10)] + ["π", "e"]:
            self.label_display.setText(text + " √ ( ")
        else:
            self.label_display.setText(text + " x √ ( ")

    def clicked_factorial(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in [str(i) for i in range(0, 10)] + ["π", "e"]:
            self.label_display.setText(text + "factorial(")
        else:
            self.label_display.setText(text + " x factorial(")

    def clicked_log_e(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in [str(i) for i in range(0, 10)] + ["π", "e"]:
            self.label_display.setText(text + "ln(")
        else:
            self.label_display.setText(text + " x ln(")

    def clicked_log_10(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in [str(i) for i in range(0, 10)] + ["π", "e"]:
            self.label_display.setText(text + "log(")
        else:
            self.label_display.setText(text + " x log(")

    def clicked_pi(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in [str(i) for i in range(0, 10)] + ["π", "e"]:
            self.label_display.setText(text + "π")
        else:
            self.label_display.setText(text + " x " + "π")

    def clicked_e(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in [str(i) for i in range(0, 10)] + ["π", "e"]:
            self.label_display.setText(text + "e")
        else:
            self.label_display.setText(text + " x " + "e")

    def clicked_square(self) -> None:
        text: str = self.label_display.text()
        if text == "":
            self.label_display.setText("0 ^ 2")
        else:
            self.label_display.setText(text + " ^ 2")
            characters: list = text.split(" ")
            if " ( " in characters or " ) " in characters:
                answer = eval(text)
                self.label_display.setText(str(answer))

    def clicked_power(self) -> None:
        text: str = self.label_display.text()
        if text == "":
            self.label_display.setText("0 ^ ")
        else:
            self.label_display.setText(text + " ^ ")

    def clicked_modulus(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in [str(i) for i in range(0, 10)] + ["π", "e"]:
            self.label_display.setText(text + "abs( ")
        else:
            self.label_display.setText(text + " x abs( ")

    def clicked_exponential(self) -> None:
        text: str = self.label_display.text()
        if text == "" or text.strip()[-1] not in [str(i) for i in range(0, 10)] + ["π", "e"]:
            self.label_display.setText(text + " e ^ ")
        else:
            self.label_display.setText(text + " x e ^ ")


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
