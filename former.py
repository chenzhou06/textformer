
# begin util
def compactLine(line, fill=" "):
    """replace spaces with one space"""
    out = ""
    words = line.split()
    for word in words:
        out += word + fill
    return out

def tr(text):
    """encompass text with tr tags"""
    return "<tr>{}</tr>".format(text)

def td(text):
    """encompass text with td tags"""
    return "<td>{}</td>".format(text)

def columnize(line):
    """columnize a line of text, encompass every word in a string with td tags"""
    return " ".join([td(word) for word in line.split()])

def columns(rows):
    """get columns from rows"""
    maxLen = max([len(row) for row in rows])
    for i in range(maxLen):
        col = []
        for row in rows:
            if i < len(row):
                col.append(row[i])
            else:
                col.append(" ")
        print(col)
        yield col

def lines(text):
    """split text into lines"""
    return [row.split() for row in text.split("\n")]
# end util


class Former(object):
    def __init__(self, config=None):
        self.config = config
        pass

    def insertLineBetweenPassage(self, text):
        text = text.split("\n")
        return "\n\n".join([line for line in text if line != ""])

    def trim(self, text):
        text = text.split("\n")
        return "\n".join([line.strip() for line in text])

    def concatenate(self, text):
        text = self.trim(text)
        out = ""

        for line in text.split("\n"):
            if line == "":
                out += "\n"
            else:
                out += line + " "
        return out

    def compact(self, text, use=" "):
        text = self.trim(text)
        out = ""
        for line in text.split("\n"):
            out += compactLine(line, fill=use) + "\n"
        return out

    def tabularize(self, text):
        return self.compact(text, use="\t")

    def tabularizeHTML(self, text):
        """tabularize text in HTML format"""
        text = self.trim(text)
        out = ""
        for line in text.split("\n"):
            out += tr(columnize(line))
        return out
            
    def removeSpaceAround(self, text, around="."):
        out = ""
        for line in text.split("\n"):
            ol = ""
            #
            words = line.split(around)
            lenwords = len(words)
            for i in range(lenwords):
                if i == lenwords-1:
                    ol += words[i].strip()
                else:
                    ol += words[i].strip() + around
            out += ol + "\n"
        return out

    def replace(self, text, old, new):
        return text.replace(old, new)



            

