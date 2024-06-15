---
title: "The Database"
tagline: "Where data lives."
abstract: >
    FIXME
syllabus:
-   FIXME
---

[%fixme "write database chapter" %]

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
-   We can use an ORM to translate classes to tables and rows to objects
    -   SQLModel is a good one, but getting the plumbing right is hard
    -   Not least because the error messages are difficult to understand
-   Take a human-scale approach instead
    -   Each query is stored in its own `.sql` file (which allows us to run it directly for interactive testing)
    -   Load all of those queries into a dict at the start of the program
    -   Use a row factory to turn query result rows into dicts
    -   Figure out inserts and deletes later
-   We are doing this backward
    -   Should figure out what the interface needs to display and *then* come up with queries
    -   But we can build a few simple things to test our approach in minutes
-   How do we test this?
    -   Our synthesized dataset is too big to be easily understood, and might change
    -   Create a smaller fixture as an in-memory database
