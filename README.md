# ozone
_Python script that combines two of my favorite things: **regex** and **pytz**_

## About and Usage

    import Ozone
    
    Ozone.ozonize("20.04.2020 16:00 CET GMT")

_The insides are held together by duct tape, but if you feed it a string in a format of:_

    DATE TIME (TIMEEND) TIMEZONE_INPUT TIMEZONE_OUTPUT ($FORMAT)
    
_It will convert the date and time, from and to the timezones provided and return a tuple with strings:_

    DATE TIME TIMEZONE_OUTPUT
    
_And optional:_

    DATE TIMEEND TIMEZONE_OUTPUT
    
_Format is optional, and if nothing is passed default is being used:_

    dd.mm.yyyy HH:MM (HH:MM) # 20.04.2020 16:20
    
_If you are using dates in different formats, you can pass the custom format at the end using $, and separating every item with a $_

_Available formats:_

 - $mdy
 
       04.20.2020
    
 - $ymd
 
       2020.04.20
    
 - $ydm
 
       2020.20.04
       
 - $Mdy
 
       Apr 20, 2020
    
 - $12
 
       04:00 PM
    
 - $24
 
       16:00

    
