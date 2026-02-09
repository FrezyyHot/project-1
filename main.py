def on_button_pressed_a():
    global testRunning, startTime, hazardTimer, sumLight, readingCount
    testRunning = True
    startTime = input.running_time()
    hazardTimer = 0
    sumLight = 0
    readingCount = 0
    basic.show_icon(IconNames.YES)
    basic.pause(500)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global average
    if readingCount > 0:
        average = Math.round(sumLight / readingCount)
        basic.show_number(average)
    else:
        basic.show_string("No Data")
input.on_button_pressed(Button.B, on_button_pressed_b)

currentLight = 0
average = 0
readingCount = 0
sumLight = 0
hazardTimer = 0
startTime = 0
testRunning = False
basic.show_icon(IconNames.HAPPY)

def on_every_interval():
    global currentLight, sumLight, readingCount
    if testRunning:
        currentLight = input.light_level()
        sumLight += currentLight
        readingCount += 1
        serial.write_line("" + str(Math.round((input.running_time() - startTime) / 1000)) + "," + str(currentLight))
loops.every_interval(2000, on_every_interval)

def on_forever():
    global testRunning, hazardTimer
    if testRunning:
        if input.running_time() - startTime > 60000:
            testRunning = False
            basic.show_icon(IconNames.HAPPY)
        elif currentLight < 25:
            if hazardTimer == 0:
                hazardTimer = input.running_time()
            if input.running_time() - hazardTimer > 10000:
                basic.show_icon(IconNames.SKULL)
                testRunning = False
                basic.pause(2000)
            else:
                basic.show_icon(IconNames.CONFUSED)
        else:
            hazardTimer = 0
            basic.show_icon(IconNames.HEART)
    else:
        basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever)
