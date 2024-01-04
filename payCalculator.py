# Define user input function
def userInput ():
  rateValid = False
  formatValid = False
  hourValid = False
  minutesValid = False
  preferHour = False
  preferHourMinute = False
  
  while rateValid == False:
    payRate = input ("Please enter your per hour rate without the dollar symbol:$")
    try:
      payRate = float (payRate)
      assert payRate >= 0
    except ValueError:
      print ()
      print ("Sorry, that entry was not valid. Let's try again by entering your per hour pay rate in the format of ##.## with no dollar symbol. \n")
      pass
    except AssertionError:
      print ()
      print ("Sorry, per hour pay rate cannot be less than zero. Let's try again by entering your per hour pay rate.\n")
      pass
    else:
      print ()
      print ("Thank you. You have entered:$", payRate,"per hour \n")
      print ("Let's proceed with the hours worked. \n")
      rateValid = True
  
  while formatValid == False:
    preferredFormat = input ("Do you prefer to enter your time format in hours or in hours and minutes? Please enter 1 if you prefer to enter in hours. Please enter 2 if you prefer to enter in hours and minutes:")
    try:
      assert preferredFormat == '1' or preferredFormat == '2'
    except AssertionError:
      print ()
      print ("Sorry, I don't understand your entry. Let's try again. \n")
      pass
    else:
      if preferredFormat == '1':
        preferHour = True
        print ()
      elif preferredFormat == '2':
        preferHourMinute = True
        print()
      formatValid = True
  
  while hourValid == False:
    if preferHour == True:
      hours = input ("Please enter the number of hours worked. For hours less than 1, you may enter decimal values such as .5 for half hour:")
      try:
        hours = float(hours)
        assert hours >= 0
      except ValueError:
        print ("Sorry, that entry was not valid. Let's try again by entering the number of hours worked, numerical value only. \n")
        pass
      except AssertionError:
        print ("Sorry, hours worked cannot be less than zero. Let's try again by entering the number of hours worked. \n")
        pass
      else:
        print()
        print ("Thank you. You have entered:", hours,"hours.")
        if hours > 40:
          overtime = True
          timeOver = hours - 40
          timeRegular = 40
          hourValid = True
          minutes = None
        else:
          overtime = False
          timeOver = 0
          timeRegular = hours
          hourValid = True
          minutes = None
        break
    
    elif preferHourMinute == True:
      hours = input ("Please enter the number of hours worked as whole number without decimals:")
      try:
        hours = int(hours)
        assert hours >= 0
      except ValueError:
        print ()
        print ("Sorry, that entry was not valid. Let's try again by entering the number of hours worked, numerical value only. \n")
        pass
      except AssertionError:
        print ()
        print ("Sorry, hours worked cannot be less than zero. Let's try again by entering the number of hours worked. \n")
      else:
        print ()
        print ("Thank you. You have entered:", hours,"hours. \n")
        hourValid = True
        while minutesValid == False:
          minutes = input ("Please enter the number of minutes worked:")
          try:
            minutes = int(minutes)
            assert minutes >= 0
          except ValueError:
            print ()
            print ("Sorry, that entry was not valid. Let's try again by entering the number of minutes worked, numerical value only. \n")
            pass
          except AssertionError:
            print ()
            print ("Sorry, minutes worked cannot be less than zero. Let's try again by entering the number of minutes worked. \n")
            pass
          else:
            try:
              assert minutes < 60
            except AssertionError:
              print ()
              print ("Sorry, but you have entered minute value that is either larger or equal to 60. Let's try again. \n")
              pass
            else:
              print ()
              print ("Thank you. You have entered:", minutes,"minutes.") 
              minutesToHour = (minutes/60)
              totalHours = hours + minutesToHour
              if totalHours > 40:
                timeOver = totalHours - 40
                timeRegular = 40
                minutesValid = True
              else:
                timeOver = 0
                timeRegular = hours
                minutesValid = True
  
  return (payRate, timeOver, timeRegular, [hours, minutes])
  
# Define calculation function
def calculatePay (rate, overtimeHours, regularHours):
  overtimeMultiplier = 1.5
  overtimeRate = rate * overtimeMultiplier
  overtimePay = overtimeHours * overtimeRate
  regularPay = regularHours * rate
  totalPay = regularPay + overtimePay
  return (totalPay, overtimeRate)
  

# Define main function
def main():
  print ("Welcome to the simple pay calculator!")
  print ("-------------------------------------")
  payRate, timeOver, timeRegular, timeWorked = userInput()
  hourWorked = timeWorked[0]
  minuteWorked = timeWorked[1]
  payment, overtimeRate = calculatePay (payRate, timeOver, timeRegular)
  print ("-------------------------------------")
  print ("Payment Summary")
  print ("=====================================")
  if minuteWorked == None:
    print ("You have worked", hourWorked, "hours.")
    print ("You have overtime of", round(timeOver,2), "hours.")
    print ("Your regular time rate is", round(payRate,2),"dollars per hour.")
    print ("Your overtime rate is", round(overtimeRate,2), "dollars per hour.")
    print ("=====================================")
    print ("Your total pay is", round(payment,2),"dollars")
  else:
    print ("You have worked", hourWorked, "hours and", minuteWorked, "minutes.")
    print ("You have overtime of", round(timeOver,2), "hours.")
    print ("Your regular time rate is", round(payRate,2),"dollars per hour.")
    print ("Your overtime rate is", round(overtimeRate,2), "dollars per hour.")
    print ("=====================================")
    print ("Your total pay is", round(payment,2),"dollars")
      
main()
