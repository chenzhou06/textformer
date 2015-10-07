:Author: Chen Zhou

# Text Former

Current Version 0.1

This is an application for organizing text into a friendlier form.
In many situations, the text we received is illy organized. For example,
a passage copied from a PDF file is splitted by many linebreaks, which
usually need us to remove one by one. This application provide
a more elegant way to handle this kind of problems.

# Key Features
## Concatenate
<!--vid here-->
Joining different lines of text into one line of passage.
An empty line will be treated as a newline character.

## Tabularize
<!--vid here-->
Separate text into different columns so that we can copy it straight into Excel.

# Usage

* `trim` -- Remove leading and trailing whitespace of a line;
* `Concatenate` -- Joining different lines of strings into one line of passage;
* `Replace` -- Replace a character in the text. This function could be very useful
when the dots in the text is not standard so that the `Remove Space Around Dot` function
could not perform properly.
* `Remove Space Around Dot` -- Sometimes numbers in the text is splitted (by dots) 
in two parts, we could not tabularize it directly, otherwise the numbers will be divided
in two columns.
In this case, we should remove space around dots at first and then put each number together.
* `Tabularize` -- Separate text by whitespace into columns.

