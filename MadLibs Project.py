#need: adjective, noun, name
print('Welcome to my MadLibs game! Its ridiculous, youll love it!')
print('Have fun!!!')
print('')
adjective = input('Give us any adjective! What is the first thing that comes to mind?: ')
noun = input('Give us any noun! Remember: A Noun is a Person, Place, or Thing!: ')
noun2 = input('Give us another one! Dont think too hard!: ')
noun3 = input('One last time! I promise! (maybe...): ')
noun4 = input('I lied, hehe: ')
name = input('Give us the first name that comes to mind! It could be ANYTHING!: ')
color = input('This one is easy! Give us a color! Your favorite!: ')
body_part = input('Now give us a body part! Do your worst...: ')
animal = input('Any animal now!: ')

print('')
print('')
print('Enjoy your story!')
print('')
print('')
story1 =f"Once upon a time, in a magical forest filled with sparkling and {adjective} trees, lived a tiny {noun} 'named {name}. {name} wasnt like other {noun}s. They had a tail that was as fluffy as a {noun2} and loved to wear a tiny hat made of {noun3} ."
story2 =f"One sunny morning, while skipping through a field of {noun3} flowers, a rare and special kind, {name} spotted a peculiar sight. A baby {noun2} was perched on a giant {noun4}, crying its tiny, beady eyes out. They were a strange color, {name} noticed, a sort of {color}. {name} liked them very much." 
story3 = f"Without a moment's hesitation, {name} climbed a nearby tree using their {body_part} and gently scooped the baby into their arms. To {name}'s surprise, it was actually a {animal}!"
story4 = f"'Don't worry little one,' said {name}, 'I'll look after you'. And so began {name}'s adventure with the baby {animal} to reunite it with its family!"

print('')
print('')
print(story1)
print(story2)
print(story3)
print(story4)
print('')
print('The End!')
print('')
print('I hope you had fun (or at least ended more confused than when you started, haha)! This game was coded by me, Antanya Lindsay! Find me on github @a-lindsay21!')
print('Thank you for playing!')
