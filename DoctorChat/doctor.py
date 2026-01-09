"""Program: doctor.py
Author: Samantha
Conducts an interactive session of nondirective psychotherapy.
"""

import random

class Doctor:
    """Creates a doctor object"""

    def __init__(self, name = None):
        self.hedges = ("Please tell me more.",
          "Many of my patients tell me the same thing.",
          "Please continue.")
        self.qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ")
        self.replacements = {"i":"you", "me":"you", "my":"your",
                "we":"you", "us":"you", "mine":"yours", "am":"are"}
        self.name = name
        self.history = [] 

    def reply(self, sentence):
        """Builds and returns a reply to the sentence."""
        self.history.append(sentence) 
        probability = random.randint(1, 4)
    
        if probability == 1:
            return random.choice(self.hedges)
        elif probability == 3 and len(self.history) > 2:
            randomInt = random.randint(0, len(self.history) - 2)
            randomReply = self.history[randomInt] 
            return ("Previously, you said " + self.changePerson(randomReply))
        else:
            return random.choice(self.qualifiers) + self.changePerson(sentence)

    def changePerson(self, sentence):
        """Replaces first person pronouns with second person pronouns."""
        words = sentence.split()
        replyWords = []
        for word in words:
            replyWords.append(self.replacements.get(word.lower(), word))
        return " ".join(replyWords)

    
