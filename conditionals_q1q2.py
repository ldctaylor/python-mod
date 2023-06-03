#Exercise 1 and 2
sara_has_helmet = False
rei_has_rope = True

if sara_has_helmet and rei_has_rope:
    print("Let's send it!")
elif sara_has_helmet and not rei_has_rope:
    print("Who's unprepared now, Rei??")
elif not sara_has_helmet and rei_has_rope:
    print("No way, my brain is my moneymaker!")
else:
    print("I guess let's just go hiking?")