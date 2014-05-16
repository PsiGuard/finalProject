# main.py is the driver for a choose-your-own-adventure game
# By: Joe Vander Ploeg
# Date: May 15, 2014
##############################################################

from random import randint  # Random number generator

def main():
	# Introduction and champion selection
	print "\nWelcome to the League of Legends interactive adventure game!\n"
	print "1) Nocturne\nClear Speed: 4   Mobility: 3   Damage: 4   Durability: 3   Crowd Control: 2\n"
	print "2) Amumu\nClear speed: 5   Mobility: 2   Damage: 2   Durability: 4   Crowd Control: 4\n"
	print "3) Kha'Zix\nClear speed: 3   Mobility: 3   Damage: 5   Durability: 2   Crowd Control: 2\n"
	print "4) Nautilus\nClear speed: 2   Mobility: 2   Damage: 1   Durability: 5   Crowd Control: 5\n"
	print "5) Fiddlesticks\nClear speed: 1   Mobility: 1   Damage: 3   Durability: 2   Crowd Control: 4\n"

	# Loops until a valid index is received from the user to select a champion, then builds a Champion object with the given stats
	while(True):
		index = input("Please select a champion by their index: ")
		if(index == 1):
			champion = Champion(4, 3, 4, 3, 2, 1, 0)
			print "You have chosen Nocturne."
			break
		elif(index == 2):
			champion = Champion(5, 2, 2, 4, 4, 1, 0)
			print "You have chosen Amumu."
			break
		elif(index == 3):
			champion = Champion(3, 3, 5, 2, 2, 1, 0)
			print "You have chosen Kha'Zix"
			break
		elif(index == 4):
			champion = Champion(2, 2, 1, 5, 5, 1, 0)
			print "You have chosen Nautilus"
			break
		elif(index == 5):
			champion = Champion(1, 1, 3, 2, 4, 1, 0)
			print "You have chosen Fiddlesticks"
			break
		else:
			print "Error: Invalid index\n"  # Restarts the loop and prompts for index again until index is valid

	# Variables for the first set of choices in the game
	choice1 = Choice(champion, "1) Invade the enemy red buff", randint(1,20), "damage", 12, 300)
	choice2 = Choice(champion, "2) Clear your wolves and red buff", randint(1,20), "clear", 8, 150)
	choice3 = Choice(champion, "3) Go directly to your red buff and clear it immediately", randint(1,20), "clear", 3, 80)

	# Builds the first event with a list of the three choices
	event1 = Event("\nYou are playing on blue side.  The game begins and both teams spread out along the river, defending each side of the jungle.  Neither team attempts to invade or fight at level one.  You start at your blue buff and notice that the enemy jungler also started at his blue.", [choice1, choice2, choice3])

	# Runs the event, printing the description and choices, then prompting the user for their choice and executing it
	event1.run()
	
	# Selection tree that outputs a result string based on the user's choice and its result
	if (event1.index == 1):
		if event1.outcome():
			print "\nSuccess!  You killed the enemy jungler and stole his buff. +300 gold!"
		else:
			print "\nFailed.  You invade but the enemy jungler is too strong and forces you to retreat."
	elif (event1.index == 2):
		if event1.outcome():
			print "\nSuccess!  You clear your camps and hit level 3 with double buff. +150 gold!"
		else:
			print "\nFailed.  The enemy jungler cleared your red buff and left before you got there."
	elif (event1.index == 3):
		if event1.outcome():
			print "\nSuccess!  You secure your red buff before continuing on to wraiths to hit level 3. +80 gold!"
		else:
			print "\nFailed.  The enemy jungler invaded as you reached your red buff and killed you."
	else:
		print "\nError: invalid index"

	champion.level += 2

	# **The following code to the end of main() was added after my presentation**

	# Variables for the second set of choices in the game
	choice4 = Choice(champion, "1) Gank top through the river", randint(1,20), "cc", 10, 300)
	choice5 = Choice(champion, "2) Gank mid through the river", randint(1,20), "mobility", 10, 300)
	choice6 = Choice(champion, "3) Keep clearing your jungle", randint(1,20), "clear", 4, 100)

	# Builds the second event with a list of the three choices
	event2 = Event("\nYou are now level 3 and are clearing your wolves.  You notice that both the enemy top lane and mid lane are pushed towards your towers.  Neither of your solo laners has much crowd control to pin their opponent down.", [choice4, choice5, choice6])

	# Runs the event, printing the description and choices, then prompting the user for their choice and executing it
	event2.run()
	
	# Selection tree that outputs a result string based on the user's choice and its result
	if (event2.index == 1):
		if event2.outcome():
			print "\nSuccess!  You killed the enemy top laner and pushed the wave into the tower. +300 gold!"
		else:
			print "\nFailed.  You try to gank top but the enemy top laner slips away without using any summoners."
	elif (event2.index == 2):
		if event2.outcome():
			print "\nSuccess!  You killed the enemy mid laner and pushed the wave into the tower. +300 gold!"
		else:
			print "\nFailed.  You try to gank mid but the enemy mid laner spots you and evades the gank without using any summoners."
	elif (event2.index == 3):
		if event2.outcome():
			print "\nSuccess!  You continue clearing your camps for some easy gold and experience.  +100 gold!"
		else:
			print "\nFailed.  You cleared too slowly and the enemy jungler was waiting for you at your wraiths and forced you back to base."
	else:
		print "\nError: invalid index"

	champion.level += 3

	# At level 6....
	if(index == 1):
		print "\nYou have reached level 6 and gained your ultimate, Paranoia.  Your mobility and damage have been increased."
		champion.mobility += 2
		champion.damage += 2
	elif(index == 2):
		print "\nYou have reached level 6 and gained your ultimate, Curse of the Sad Mummy.  Your durability and crowd control have been increased."
		champion.durability += 2
		champion.cc += 2
	elif(index == 3):
		print "\nYou have reached level 6 and gained your ultimate, Void Assault.  Your mobility and damage have been increased."
		champion.mobility += 2
		champion.damage += 2
	elif(index == 4):
		print "\nYou have reached level 6 and gained your ultimate, Depth Charge.  Your damage and crowd control have been increased."
		champion.damage += 1
		champion.cc += 1
	elif(index == 5):
		print "\nYou have reached level 6 and gained your ultimate, Crowstorm.  Your damage has been greatly increased along with your mobility."
		champion.damage += 2
		champion.mobility += 1

	# Variables for the third set of choices in the game
	choice7 = Choice(champion, "1) Gank top through the lane", randint(1,20), "cc", 7, 300)
	choice8 = Choice(champion, "2) Gank mid through the river", randint(1,20), "mobility", 8, 450)
	choice9 = Choice(champion, "3) Dive bottom and tank the tower for your laners", randint(1,20), "durability", 10, 750)
	choice10 = Choice(champion, "4) Invade the enemy jungle and try to kill their jungler", randint(1,20), "damage", 8, 450)

	# Builds the third event with a list of the three choices
	event3 = Event("\nYou are now level 6 and are considering where you should use your ultimate.  The enemy top lane is pushing again but mid lane is roughly centered.  Your bottom lane is pushed to the enemy tower and you spotted the enemy jungler with a deep ward as he heads towards his red buff.", [choice7, choice8, choice9, choice10])

	# Runs the event, printing the description and choices, then prompting the user for their choice and executing it
	event3.run()
	
	# Selection tree that outputs a result string based on the user's choice and its result
	if (event3.index == 1):
		if event3.outcome():
			print "\nSuccess!  You killed the enemy top laner and pushed the wave into the tower. +300 gold!"
		else:
			print "\nFailed.  You try to gank top but the enemy top laner survives while the enemy team groups to dragon."
	elif (event3.index == 2):
		if event3.outcome():
			print "\nSuccess!  You killed the enemy mid laner and grouped your team for an easy dragon. +450 gold!"
		else:
			print "\nFailed.  You were counter-ganked as you approached the gank and died, giving up a dragon to the enemy team."
	elif (event3.index == 3):
		if event3.outcome():
			print "\nSuccess!  You tank the tower and score a double kill, following up with a dragon for your team.  +750 gold!"
		else:
			print "\nFailed.  You die to the tower and the dive fails, opening up an opportunity for the enemy team to take dragon."
	elif (event3.index == 4):
		if event3.outcome():
			print "\nSuccess!  You quickly kill the enemy jungler and then group your team for a free dragon.  +450 gold!"
		else:
			print "\nFailed.  You were killed by the enemy jungler and the enemy team used the opportunity to take dragon."
	else:
		print "\nError: invalid index"

	# End of game results
	print "\nThe early game is over and both teams begin to group.  You made " + str(champion.gold) + " gold during the early game."
	
	if champion.gold < 750:
		print "\nYou still have some room to improve.  Try to use your champion's strengths efficiently to create a bigger advantage for your team."
	else:
		print "\nGreat job!  You had a solid early game impact and your team has a good shot of winning the game!"

	print "Thank you for playing!"

class Champion:
	##############################################################################################################
	# Constructor for the Champion class																		 #
	# Receive: clear, mobility, damage, durability, cc, level, gold -- Integers that describe a champion's stats #
	##############################################################################################################
	def __init__(self, clear, mobility, damage, durability, cc, level, gold):
		self.clear = clear
		self.mobility = mobility
		self.damage = damage
		self.durability = durability
		self.cc = cc
		self.level = level
		self.gold = gold

# Tried out properties, but it looks like I don't really need them.
#	@property
#	def clear(self):
#		return self._clear
#
#	@clear.setter
#	def clear(self, clear):
#		self._clear = clear

class Event:
	########################################################
	# Constructor for the Event class					   #
	# Receive: description -- a string with the event text #
	#          choices -- a list of Choice objects         #
	########################################################
	def __init__(self, description, choices):
		self.description = description
		self.choices = choices
		self.index = 0

	def run(self):
		print self.description + '\n'

		for i in range(0, len(self.choices)):
			print self.choices[i].description

		self.index = input("Choose a course of action: ")
		self.choices[self.index-1].execute()

	######################################################################
	# outcome() returns whether the user's choice was successful or not. #
	# Return: True if the choice succeeds, otherwise False.              #
	# Precondition: run() must be run BEFORE calculating outcome         #
	######################################################################
	def outcome(self):
		return self.choices[self.index-1].success()

class Choice:
	###############################################################################
	# Constructor for the Choice class                                            #
	# Receive: champion -- the Champion object to be altered                      #
	#          description -- the string describing the given choice              #
	#          base -- the base roll (random integer between 1 and 20)            #
	#          attribute -- the champion attribute to be used in the success roll #
	#          threshhold -- the roll required for the choice to be successful    #
	#          bounty -- the amount of gold gained by a successful choice         #
	###############################################################################
	def __init__(self, champion, description, base, attribute, threshHold, bounty):
		self.champion = champion
		self.description = description
		self.attribute = attribute
		self.threshHold = threshHold
		self.bounty = bounty
		self.base = base

	#################################################################################################
	# execute() calculates the result of the choice and increases the champion's gold if successful #
	# Return: True if the choice is successful, otherwise False                                     #
	#################################################################################################
	def execute(self):
		
		# Selection tree that adds the corresponding champion attribute to the base roll
		if(self.attribute == "clear"):
			self.base += self.champion.clear
		elif(self.attribute == "mobility"):
			self.base += self.champion.mobility
		elif(self.attribute == "damage"):
			self.base += self.champion.damage
		elif(self.attribute == "durability"):
			self.base += self.champion.durability
		elif(self.attribute == "cc"):
			self.base += self.champion.cc
		else:
			print "Error: attribute not found"

		# Calculates whether the roll + attribute meets/exceeds threshHold and succeeds or if the choice fails
		if self.base >= self.threshHold:
			self.champion.gold += self.bounty

	##################################################################
	# success() returns whether the choice was successful or not.    #
	# Return: True if the choice succeeds, otherwise False.          #
	# Precondition: execute() must be run BEFORE calculating success #
	##################################################################
	def success(self):
		return self.base >= self.threshHold


if __name__ == "__main__":
	main()
