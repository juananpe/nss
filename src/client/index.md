---
title: "Displaying Data"
tagline: "A read-only interface."
abstract: >
    FIXME
syllabus:
-   FIXME
---

[%fixme "write display chapter" %]

-   [%x server %] gave us an API for fetching data as JSON
-   Turn that into HTML in the browser using [json2html][json2html] instead of rendering on the server ([%x template %])
    -   Would be easy to write our own utility, but why bother?
    -   The answer is, "Because now we have to audit that package for security"
-   Each page displays data as a table
    -   Some elements are links to other tables
-   Construct URLs with functions rather than template strings because we might change our minds
    -   A good design is one that makes plausible changes easy
    -   Which usually means making each decision in exactly one place
-   Note: could (should?) render on the server using [Jinja][jinja] or [Ibis][ibis], but we've decided to build it this way
    -   When people talk about "software architecture", this is the kind of decision they're talking about
-   Asynchronous execution
    -   Page loads, sends request, gets response, finishes rendering
    -   That potential delay is a good reason to render on the server
-   Testing with [Playwright][playwright]
