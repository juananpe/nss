---
title: "Backup and Migration"
tagline: "Everything changes."
abstract: >
    FIXME
syllabus:
-   FIXME
---

[%fixme "write backup and migration chapter" %]

-   We added tables in [%x perm %] and we're about to implement create, update, and delete
-   So we need to back up our database and manage *migration*
    -   And yeah, it's weird that the verb "back up" is two words and the noun "backup" is one
-   Three approaches to backup
    -   Save the `.db` file
    -   Export as SQL
    -   Export as CSV
    -   We will use "export as SQL" because it's simpler than CSV and more readable than a `.db` file
-   Set up a regular task to do this (because humans are forgetful)
    -   `cron`'s syntax is annoying
    -   [%fixme "what to recommend instead of cron" %]
-   But wait: if we back up, change the database structure and/or code, and then restore, what happens?
-   Use [Sqitch][sqitch] to save the schema we had before we made our permission changes
-   Then use `sqitch add` to create our first migration
    -   `deploy/perms.sql`: modify the database forward
    -   `verify/perms.sql`: check the change
    -   `revert/perms.sql`: undo the change
-   Actions are recorded in a registry database
-   Finally, record the Sqitch tag in the database itself
    -   Makes database backups self-describing
-   We can now implement create and delete without losing sleep
    -   Again, create little objects that know how to write specific things
    -   Check that all the incoming record dicts have the right keys before trying the operation
