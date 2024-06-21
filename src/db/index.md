---
title: "The Database"
tagline: "Create, read, update, and delete."
abstract: >
    FIXME
syllabus:
-   FIXME
---

-   Start with a simple model
    -   *Staff* (people) conduct *experiments* alone or together over one or more days
    -   Each *experiment* uses one or more *plates* on a particular date
    -   A *plate* may be *invalidated* by a single *staff* on a particular date
-   Relationships are as important as tables
    -   staff to experiment: many to many (implemented as a *join table*)
    -   experiment to plate: one to many
    -   invalidated to plate: zero or one to one
-   Every model is a lie
    -   Is someone who helped review a plate listed as an experimenter?
    -   We aren't listing a reason for invalidating a plate
    -   We create models to represent the world, but then those models shape our view of the world
-   Example SQL queries
    -   `all_staff_alpha.sql`: get all staff names alphabetical by surname
    -   `count_exp_by_staff.sql`: count experiments by staff ID
    -   `most_recent_invalidaters.sql`: who invalidated plates in the most recent batch
-   We can use an ORM to translate classes to tables and rows to objects
    -   [SQLModel][sqlmodel] is a good one
    -   `models.py`: just who performed which experiments
    -   But getting the plumbing right is hard
        -   Not least because the error messages are difficult to understand
    -   Does pay off when we need portability across databases
-   Take a human-scale approach instead
    -   Each query is a string containing SQL
        -   Always sort result so that we have a deterministic output to check in testing
    -   Put all those strings in a module
    -   Use a row factory to turn query result rows into dicts
    -   `run_queries.py`: use a bit of introspection to find queries
-   How do we test this?
    -   Our synthesized dataset is too big to be easily understood, and might change
    -   Create a smaller fixture as an in-memory database
    -   `test_queries.py`: create a database and fill it, then run tests
        -   Have to worry about schema drift
-   What if we don't want everything?
    -   Don't use Python string interpolation: SQL injection attacks
    -   `test_parameters.py`: select one staff's experiments using a parameter
-   Deleting records
    -   We need to cascade
    -   SQLite will do it for us (explore in the exercises)
    -   We'll do it manually
        -   Unsafe: program could fail in the middle
        -   Should modify SQL used to create tables to cascade delete
    -   `test_delete.py` checks the number of rows deleted: should also check surviving rows are correct
-   We have done this backward
    -   Should figure out what the interface needs to display and *then* come up with queries
    -   But building a few simple things lets us test our approach
    -   Good designers try to find flaws with their plans as early as possible [%b Schon1984 %]
