import textwrap
class FormattedText:
    def dispFormatText(self,strVal):
        print(textwrap.fill(strVal, width=50))

stringData = FormattedText()
strVal = input("Enter a Paragraph : ")
stringData.dispFormatText(strVal)

