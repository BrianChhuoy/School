#part 1
'''
time= int(input("Enter number of seconds between 0 and 86,339:")) # In this seconds is the ref; And will convert to a whole number
hours= time//3600
minutes=(time%3600)//60
seconds=(time%3600)%60
print(time,"seconds is",hours,",hours",minutes,",minutes",seconds,",seconds.")
'''
#part 2
"""
population= 334205119 #given
time= 1685720 #calculated from Jan 1 to Jan 20 12:15:20
birth= time//7 #take the seconds then takes the quotient and ignores the remainders
death= time//13#take the seconds then takes the quotient and ignores the remainders
new= time//35#take the seconds then takes the quotient and ignores the remainders
pop= population +birth + new -death
print("On January 20, 2022 at 12:15:20 the US population was",pop)
"""
#part 3
"""
population= 334205119
time= int(input("Enter seconds since the beginning of year:"))
#below was from part 1 with the addition of the day u get 86400 when u multiply (60(sec)*60(min)*24(hour))
day= time//86400
hour= (time//3600)%24
minute= (time%3600)//60
second=(time%3600)%60
#below was copy from part 2
birth= time//7
death=time//13
new=time//35
pop=population+birth+new-death
print(day,"days,",hour,"hours,",minute,"minutes,",second,"seconds after the start of 2022,the total population was ",pop)
"""
#part 4
population = 334205119
time = int(input("Enter the amount of seconds since the beginning of the year:"))
day=time//86400
hour=(time//3600)%24
minute=(time%3600)//60
second=(time%3600)%60
birth= time//7
death=time//13
new=time//35
pop= population+birth+death+new
flap= int(((((pop+350)**2)-12)/50)**(1/5))
print(day,"days,",hour,"hours,",minute,"minutes,",second,"seconds after the start of 2022,the total population was ",pop)
print("The average amount of flapjacks eaten is",flap)