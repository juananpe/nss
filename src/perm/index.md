---
title: "Permissions"
tagline: "Who can do what."
abstract: >
    FIXME
syllabus:
-   FIXME
---

[%fixme "write permissions chapter" %]

-   Everyone can read everything in [%x db %]
-   If we're going to add create, update, and delete, we should add *permissions*
    -   The ability to perform an operation on a thing
-   Standard approach:
    -   An *actor* (person or similar) has zero or more *roles*
    -   Each *role* is a collection of pairs of *subject* and *permission*
    -   E.g., *Reader* role has *read* permission for all tables
-   Represent permissions in the database
-   But how to know which queries are going to do what to which tables?
    -   Store metadata in the on-disk query files (e.g., as embedded comments)
    -   Move our queries into our Python code (object with query and metadata)
    -   First approach requires us to write a parser, so it's probably a bad idea
    -   We can always export the SQL queries from our Python code for testing
    -   So some quick refactoring…
-   Add two tables
    -   `role` is a many-to-many join table
    -   `capabilities` defines what roles mean (with wildcard for "all tables")
    -   Load into memory at start of program and turn into lookup table
    -   Expect roles and capabilities to change infrequently, so can reload in our server once we have one
-   Implement as checking function that throws an exception
-   Notice that there isn't a widely-known Python library for handling permissions
-   And that it only works if we implement the check in our code
    -   Databases like PostgreSQL implement fine-grained permissions on tables and even rows
    -   But someone still has to set it up
    -   And if someone has access to the underlying `.db` file, the permissions in our Python are moot
