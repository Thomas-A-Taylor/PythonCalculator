import tkinter as tk

# Variables
topFuncButtons = []
vertFuncButtons = []
numButtonRows = []
numButtons = []
finalNumButtons = []
window = tk.Tk()
topTextText = tk.StringVar()
bottomTextText = tk.StringVar()
numberStack = []
operatorStack = []


# button helper functions
def operatorToStack():
    # add the last character to operator stack
    operatorStack.append(bottomTextText.get()[-1])


def numberToStack():
    if not bottomTextText.get()[-1].isnumeric():
        numberStack.append(float(bottomTextText.get()[:-1]))
    else:
        numberStack.append(float(bottomTextText.get()))


def addToTop():
    topTextText.set(topTextText.get() + bottomTextText.get())
    bottomTextText.set("")


def moveToTop():
    topTextText.set(bottomTextText.get())
    bottomTextText.set("")


def isNumStackEmpty():
    return len(numberStack) == 0


def addMoveTop(empty):
    if empty:
        moveToTop()
    else:
        addToTop()


# button functions
def zero():
    bottomTextText.set(bottomTextText.get() + "0")


def one():
    bottomTextText.set(bottomTextText.get() + "1")


def two():
    bottomTextText.set(bottomTextText.get() + "2")


def three():
    bottomTextText.set(bottomTextText.get() + "3")


def four():
    bottomTextText.set(bottomTextText.get() + "4")


def five():
    bottomTextText.set(bottomTextText.get() + "5")


def six():
    bottomTextText.set(bottomTextText.get() + "6")


def seven():
    bottomTextText.set(bottomTextText.get() + "7")


def eight():
    bottomTextText.set(bottomTextText.get() + "8")


def nine():
    bottomTextText.set(bottomTextText.get() + "9")


def percent():
    bottomTextText.set(bottomTextText.get() + "%")
    if bottomTextText.get() == "%":
        topTextText.set("ERROR")


def decimal():
    if not bottomTextText.get() == "-" and not bottomTextText.get() == "":
        if bottomTextText.get().count(".") == 0:
            bottomTextText.set(bottomTextText.get() + ".")


def add():
    if not bottomTextText.get() == "-" and not bottomTextText.get() == "":
        if bottomTextText.get()[-1].isnumeric():
            bottomTextText.set(bottomTextText.get() + "+")
            empty = isNumStackEmpty()
            operatorToStack()
            numberToStack()
            addMoveTop(empty)


def subtract():
    if bottomTextText.get() == "":
        bottomTextText.set("-")
    else:
        if bottomTextText.get()[-1].isnumeric():
            bottomTextText.set(bottomTextText.get() + "-")
            empty = isNumStackEmpty()
            operatorToStack()
            numberToStack()
            addMoveTop(empty)


def divide():
    if not bottomTextText.get() == "-" and not bottomTextText.get() == "":
        if bottomTextText.get()[-1].isnumeric():
            bottomTextText.set(bottomTextText.get() + "/")
            empty = isNumStackEmpty()
            operatorToStack()
            numberToStack()
            addMoveTop(empty)


def multiply():
    if not bottomTextText.get() == "-" and not bottomTextText.get() == "":
        if bottomTextText.get()[-1].isnumeric():
            bottomTextText.set(bottomTextText.get() + "*")
            empty = isNumStackEmpty()
            operatorToStack()
            numberToStack()
            addMoveTop(empty)


def delete():
    bottomTextText.set(bottomTextText.get()[:-1])


def reset():
    topTextText.set("")
    bottomTextText.set("")
    operatorStack.clear()
    numberStack.clear()


def equals():
    if len(numberStack) > 0 and not bottomTextText.get() == "":
        numberToStack()
        addToTop()
        while len(operatorStack) > 0:
            case = operatorStack.pop()
            match case:
                case "-":
                    second = numberStack.pop()
                    first = numberStack.pop()
                    numberStack.append(first - second)
                case "+":
                    second = numberStack.pop()
                    first = numberStack.pop()
                    numberStack.append(first + second)
                case "/":
                    second = numberStack.pop()
                    first = numberStack.pop()
                    numberStack.append(first / second)
                case "*":
                    second = numberStack.pop()
                    first = numberStack.pop()
                    numberStack.append(first * second)

        bottomTextText.set(str(numberStack.pop()))


# CREATE GUI
# create the screen output
screenFrame = tk.Frame()
topText = tk.Label(
    height=2,
    width=40,
    master=screenFrame,
    textvariable=topTextText
)
topText.pack(fill=tk.BOTH, expand=tk.TRUE)
bottomText = tk.Label(
    height=5,
    width=40,
    master=screenFrame,
    textvariable=bottomTextText
)
bottomText.pack(fill=tk.BOTH, expand=tk.TRUE)
screenFrame.pack(fill=tk.BOTH, expand=tk.TRUE)

# create button frame
buttonFrame = tk.Frame()

# create top functions
topFuncFrame = tk.Frame(master=buttonFrame)
for a in range(4):
    function = ""
    match a:
        case 0:
            text = "C"
            command = reset
        case 1:
            text = "/"
            command = divide
        case 2:
            text = "X"
            command = multiply
        case 3:
            text = "<-"
            command = delete
    topFuncButtons.append(tk.Button(
        text=text,
        width=10,
        height=5,
        bg="blue",
        fg="yellow",
        master=topFuncFrame,
        command=command,
    ))
    topFuncButtons[a].pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
topFuncFrame.pack(fill=tk.BOTH, expand=tk.TRUE)

# create numerical + func button frame
numFuncFrame = tk.Frame(master=buttonFrame)
numFuncFrame.pack(fill=tk.BOTH, expand=tk.TRUE)

# create the numerical buttons (1-9)
numFrame = tk.Frame(master=numFuncFrame)
for x in range(3):
    numButtonRows.append(tk.Frame(master=numFrame))
    numButtons.append([])
    for y in range(3):
        text = 7 - (x * 3) + y
        match text:
            case 1:
                command = one
            case 2:
                command = two
            case 3:
                command = three
            case 4:
                command = four
            case 5:
                command = five
            case 6:
                command = six
            case 7:
                command = seven
            case 8:
                command = eight
            case 9:
                command = nine
        numButtons[x].append(tk.Button(
            text=text,
            width=10,
            height=5,
            bg="blue",
            fg="yellow",
            master=numButtonRows[x],
            command=command
        ))
        numButtons[x][y].pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
    numButtonRows[x].pack(fill=tk.BOTH, expand=tk.TRUE)
numFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)

# create numerical buttons (0, ., %)
finalNumFrame = tk.Frame(master=numFrame)
for a in range(3):
    match a:
        case 0:
            text = "%"
            command = percent
        case 1:
            text = "0"
            command = zero
        case 2:
            text = "."
            command = decimal
    finalNumButtons.append(tk.Button(
        text=text,
        width=10,
        height=5,
        bg="blue",
        fg="yellow",
        master=finalNumFrame,
        command=command
    ))
    finalNumButtons[a].pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
finalNumFrame.pack(fill=tk.BOTH, expand=tk.TRUE)

# create the vertical operation buttons
vertFuncFrame = tk.Frame(master=numFuncFrame)
for a in range(3):
    height = 5
    match a:
        case 0:
            text = "-"
            command = subtract
        case 1:
            text = "+"
            command = add
        case 2:
            text = "="
            height = 11
            command = equals
    vertFuncButtons.append(tk.Button(
        text=text,
        width=10,
        height=height,
        bg="blue",
        fg="yellow",
        master=vertFuncFrame,
        command=command
    ))
    vertFuncButtons[a].pack(fill=tk.BOTH, expand=tk.TRUE)
vertFuncFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)

buttonFrame.pack(fill=tk.BOTH, expand=tk.TRUE)
window.mainloop()
