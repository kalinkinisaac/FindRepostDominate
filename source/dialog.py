import json

fp = open('paterns/paterns.json')

class Dialog:

    Commands = json.load(fp)
    ListCommands = dict()

    def parse(self, text):
        answer = str()
        for letter in text:
            if letter not in ('.', ',', '!', '?'):
                answer += letter
        return answer.split()

    def CheckCommand(self, text, command):
        i = 0
        answer = dict()
        answer['exist'] = False
        answer['poses'] = list()
        while i < len(text):
            if text[i] == command[0]:
                for j in range(0, len(command)):
                    if text[i+j] != command[j]:
                        return answer
                    answer['exist'] = True
                    return answer

    def command(self, text):
        text = self.parse(text)
        for name in self.Commands:
            for command in self.Commands[name]:
                answer = self.CheckCommand(text, command)
                if answer['exist']:
                    #if name not in self.ListCommands:
                    #    self.ListCommands[name] = list()
                    #for pose in answer['poses']:
                    return name