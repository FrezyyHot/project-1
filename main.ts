input.onButtonPressed(Button.A, function () {
    testRunning = true
    startTime = input.runningTime()
    hazardTimer = 0
    sumLight = 0
    readingCount = 0
    basic.showIcon(IconNames.Yes)
    basic.pause(500)
})
input.onButtonPressed(Button.B, function () {
    if (readingCount > 0) {
        average = Math.round(sumLight / readingCount)
        basic.showNumber(average)
    } else {
        basic.showString("   No Data")
        basic.showIcon(IconNames.Happy)
    }
})
let average = 0
let readingCount = 0
let sumLight = 0
let hazardTimer = 0
let startTime = 0
let testRunning = false
basic.showIcon(IconNames.Happy)
loops.everyInterval(2000, function () {
    if (testRunning) {
        sumLight += input.lightLevel()
        readingCount += 1
        serial.writeLine("" + Math.round((input.runningTime() - startTime) / 1000) + "," + input.lightLevel())
    }
})
basic.forever(function () {
    if (testRunning) {
        if (input.runningTime() - startTime > 60000) {
            testRunning = false
            basic.showIcon(IconNames.Happy)
        } else if (input.lightLevel() < 25) {
            if (hazardTimer == 0) {
                hazardTimer = input.runningTime()
            }
            if (input.runningTime() - hazardTimer > 10000) {
                basic.showIcon(IconNames.Skull)
                testRunning = false
            } else {
                basic.showIcon(IconNames.Confused)
            }
        } else {
            hazardTimer = 0
            basic.showIcon(IconNames.Heart)
        }
    } else {
    	
    }
})
