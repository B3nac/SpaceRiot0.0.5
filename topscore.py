from gamedata import player

def highScore(self):
    
    """ Main program is here. """
    try:
        self.high_score_file = open("high_score.txt", "r")
        self.player.high_score = int(self.high_score_file.read())
        self.high_score_file.close()
        print("The high score is", self.player.high_score)
    except IOError:
        print("There is no high score yet.")
    except ValueError:
        print("I'm confused. Starting with no high score.")
    except ValueError:
        print("I don't understand what you typed.")
    if self.player.score > self.player.high_score:
        print("Woot! New high score!")
        try:
        #Write the file to disk
            self.high_score_file = open("high_score.txt", "w")
            self.high_score_file.write(str(self.player.score))
            self.high_score_file.close()
        except IOError:
        #Hm, can't write it.
            print("Too bad I couldn't save it.")
        else:
            print("Better luck next time.")
