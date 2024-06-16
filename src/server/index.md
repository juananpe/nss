---
title: "The Server"
tagline: "Handling web requests."
abstract: >
    FIXME
syllabus:
-   FIXME
---

[%fixme "write server chapter" %]

-   We defined and implemented a handful of CRUD operations in [%x clui %]
-   Next step is to write a server to perform those in response to web requests
    -   Don't handle HTTP requests directly
    -   Instead, use a framework like [Flask][flask] or [Bottle][bottle]
-   Each operation is identified by a URL and an HTTP method
    -   `GET` to fetch data
    -   `PUT` to create data
    -   `PATCH` to update data
    -   `DELETE` to… you can probably guess
-   Can return JSON data, formatted HTML, or either on request
    -   We will return JSON because it makes testing easier
    -   And because we want to show how to turn data into HTML in the client
-   For the moment, don't worry about authentication: just include user ID in the payload
    -   Over-the-web authentication will require an entire lesson
-   Translating operations is mostly mechanical once we figure out payload format
    -   This is why we separated the operations from the CLUI function
-   Error handling: aren't you glad we threw exceptions from low-level operations and did the handling higher up?
    -   Throw low, catch high
-   Logging: again, making it configurable in [%x clui %] pays off
    -   Human message in response, detailed message with internal details in log
-   Testing is easier than you might think
    -   Replace the actual server with a fake
    -   Faster and allows single-stepping in a debugger
