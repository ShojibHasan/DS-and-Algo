import turtle

screen = turtle.Screen()

answer = turtle.simpledialog.askstring("Send A Message To Meem","")

if answer is None or answer.lower().startswith('n'):
    print("Goodbye!")
    screen.clear()
    screen.bye()
else:
    print("Start!")

turtle.done()