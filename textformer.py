from PyQt4 import QtGui, QtCore
import sys
from PyQt4.Qt import QFont, QAction
from former import Former


# begin former
fmr = Former()
# end former

# begin font
uiFontWeight = 10
textFontWeight = 10
uiMenuFont = QFont("Segoe UI", uiFontWeight)
uiToolBarFont = QFont("Segoe UI", uiFontWeight)
textEditFont = QFont("Microsoft YaHei", textFontWeight)
# end font


class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__()
        self.setWindowTitle("Text Former")
        self.resize(500, 500)

        # begin actions
        transForm = QAction("Transform", self)
        self.connect(transForm, QtCore.SIGNAL("triggered()"), self.transForm)

        trimLine = QAction("Trim", self)
        trimLine.setToolTip("Remove leading and trailing whitespace")
        self.connect(trimLine, QtCore.SIGNAL("triggered()"), self.trimLine)

        concatenate = QAction("Concatenate", self)
        concatenate.setToolTip("Joining several lines of strings into one line")
        self.connect(concatenate, QtCore.SIGNAL("triggered()"), self.concatenate)

        insertLineBetweenPassage = QAction("Insert Line Between Passages", self)
        self.connect(insertLineBetweenPassage, QtCore.SIGNAL("triggered()"), self.insertLineBetweenPassage)

        compact = QAction("Compact", self)
        compact.setToolTip("Reduce spaces between words")
        self.connect(compact, QtCore.SIGNAL("triggered()"), self.compact)

        tabularize = QAction("Tabularize", self)
        tabularize.setToolTip("Transform text into a table which can be recognized by MS Excel")
        self.connect(tabularize, QtCore.SIGNAL("triggered()"), self.tabularize)

        removeSpaceAround = QAction("Remove Item Around Dot", self)
        removeSpaceAround.setToolTip("Remove Spaces Around Dot \'.\'")
        self.connect(removeSpaceAround, QtCore.SIGNAL("triggered()"), self.removeSpaceAround)

        replace = QAction("Replace", self)
        replace.setToolTip("Replace")
        self.connect(replace, QtCore.SIGNAL("triggered()"), self.replace)

        openFile = QAction("Open", self)
        self.connect(openFile, QtCore.SIGNAL("triggered()"), self.openFile)
        saveFile = QAction("Save", self)
        self.connect(saveFile, QtCore.SIGNAL("triggered()"), self.saveFile)
        # end actions

        # begin menubar
        menubar = self.menuBar()
        self.file = menubar.addMenu("&File")
        self.file.addAction(openFile)
        self.file.addAction(saveFile)
        # end menubar

        # begin toolbar
        toolbar = QtGui.QToolBar()
        toolbar2 = QtGui.QToolBar()
        toolbar.setFont(uiToolBarFont)
        toolbar2.setFont(uiToolBarFont)
        # toolbar.addAction(transForm)
        toolbar.addAction(trimLine)
        toolbar.addAction(concatenate)
        # toolbar.addAction(insertLineBetweenPassage)
        # toolbar.addAction(compact)
        
        
        toolbar2.addAction(replace)
        toolbar2.addAction(removeSpaceAround)
        toolbar2.addAction(tabularize)
        self.addToolBar(toolbar)
        self.addToolBar(toolbar2)
        # end toolbar

        # begin centralwidget
        self.textEdit = QtGui.QTextEdit()
        self.textEdit.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.textEdit.setFont(textEditFont)
        self.textEdit.setUndoRedoEnabled(True)
        self.textEdit.setText("Open a file or paste text here.")
        self.setCentralWidget(self.textEdit)
        # end centralwidge
        pass

    # begin util methods
    @property
    def textEditContent(self):
        return self.textEdit.toPlainText()

    def setTextEditContent(self, text):
        self.textEdit.setText(text)
        pass
    # end util methods

    def transForm(self):
        print(self.textEditContent)
        self.textEdit.setPlainText()
        pass

    def trimLine(self):
        out = fmr.trim(self.textEditContent)
        self.textEdit.setPlainText(out)
        pass
    
    def concatenate(self):
        out = fmr.concatenate(self.textEditContent)
        self.textEdit.setPlainText(out)
        pass

    def insertLineBetweenPassage(self):
        out = fmr.insertLineBetweenPassage(self.textEditContent)
        self.textEdit.setPlainText(out)
        pass

    def compact(self):
        out = fmr.compact(self.textEditContent)
        self.textEdit.setPlainText(out)
        pass

    def tabularize(self):
        out = fmr.tabularizeHTML(self.textEditContent)
        self.setTextEditContent(out)
        pass

    def removeSpaceAround(self, around="."):
        out = fmr.removeSpaceAround(self.textEditContent, around)
        self.setTextEditContent(out)
        pass

    def replace(self):
        dialog = DialogReplace()
        r = dialog.exec_()
        if r:
            out = fmr.replace(self.textEditContent, dialog.old, dialog.new)
            self.setTextEditContent(out)

    def openFile(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, "Open")
        if fileName:
            with open(fileName, "r") as f:
                self.setTextEditContent(f.read())

    def saveFile(self):
        fileName = QtGui.QFileDialog.getSaveFileName(self, "Save")
        if fileName:
            with open(fileName, "w") as f:
                f.write(self.textEditContent)





class DialogReplace(QtGui.QDialog):
    def __init__(self):
        super(DialogReplace, self).__init__()

        self.setWindowTitle("Replace")
        self.layout = QtGui.QHBoxLayout()
        self.setFont(uiToolBarFont)

        self.label1 = QtGui.QLabel("Replace")
        self.textField1 = QtGui.QLineEdit()
        self.label2 = QtGui.QLabel("with")
        self.textField2 = QtGui.QLineEdit()
        self.okButton = QtGui.QPushButton("OK")
        self.cancelButton = QtGui.QPushButton("Cancel")

        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.textField1)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.textField2)
        self.layout.addWidget(self.okButton,)
        self.layout.addWidget(self.cancelButton)

        self.connect(self.okButton, QtCore.SIGNAL("clicked()"), self.onOK)
        self.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.onCancel)

        self.setLayout(self.layout)

    def onOK(self):
        self.old = self.textField1.text()
        self.new = self.textField2.text()
        self.done(1)

    def onCancel(self):
        self.done(0)





app = QtGui.QApplication(sys.argv)
demo = Window()
demo.show()
app.exec_()
