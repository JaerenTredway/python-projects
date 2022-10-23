################## Class Definition Area ###########
class MyText:
    def __init__(self):
        self.__text = ''
    def setText(self, text):
        self.__text = text
    def getText(self):
        return self.__text
    def concatText(self, textToConcat):
        return self.__text +" "+textToConcat

##################### Main Part of Program ###########
text1 = MyText()
text1.setText("Text 1's text")

text2 = MyText()
text2.setText("Text 2's text")

print "Text 1: ",text1.getText()
print "Text 2: ",text2.getText()

userText = raw_input("Please input some text: ")

print "Text with user text 1: ",text1.concatText(userText)
print "Text with user text 2: ",text2.concatText(userText)
