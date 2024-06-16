---
title: "The Command Line"
tagline: "Defining operations."
abstract: >
    FIXME
syllabus:
-   FIXME
---

[%fixme "write command line chapter" %]

-   Why build a command-line user interface (CLUI)?
    -   Automate operations in a reproducible/auditable way
    -   Figure out what those operations should be
    -   Alternative is to build REST API and then wrap that
-   Simple tools can use `argparse`, but that becomes messy with sub-commands
-   Start by showing schema
    -   Let user select output format via `prettytable` module (Markdown, HTML, CSV, etc.)
-   Show entire table by name
    -   SQLite will tell us the column names and types, so we don't hard code those
    -   Design principle: is it easy to adapt code to plausible requirements changes?
-   Add authentication before adding create, update, and delete
    -   Username and password on the command line is easy but unsafe
    -   Prompt for password makes scripting impossible
    -   Asking the operating system who the user is doesn't work
    -   Token in a file or environment variable seems safest, but is clumsy for development
-   Options for create:
    -   Use `--arg value` for every field (lots of typing)
    -   Upload a CSV file (but what if you only have one record to add?)
    -   Specify name=value pairs on the command line
-   We also have to worry about database consistency
    -   Can't add plate until we've added its experiment
    -   Can't delete an experiment if there are still plates
    -   [%fixme "will SQLite constraints throw errors?" %]
-   Error handling
    -   Printing to `stderr` and halting is easy…
    -   …but what about multi-record insert: should the whole batch fail if any fail?
    -   And should messages always and only go to `stderr` or should they also be appended to a log file?
-   All of these problems will arise with web interface
    -   Which is why the subtitle of this chapter is "defining operations"
