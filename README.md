# snailz

A set of synthetic data generators for teaching data science
that has somehow morphed into a lesson on human-scale computing.

I recently posted on Mastodon:

> 1.  I'm going to write another tech book.
> 2.  If I do, it will be about evidence-based software engineering and/or how big tech companies operate like drug cartels.
> 3.  But I'm still thinking about "Human-Scale Software: A Guide for the 99.9% of Developers Who Don't Need Scalability"

So what would I use for #3?

1.  [SQLite](https://sqlite.org/) for storage.
    ([DuckDB](https://duckdb.org/) is cool, but I'm being deliberately conservative in my choices.)

1.  I wouldn't use an object-relational mapper:
    I've used [SQLAlchemy](https://www.sqlalchemy.org/) for years,
    but I think embedded SQL is easier to debug than an ORM for small-to-medium use cases.

1.  [Bottle](https://bottlepy.org/) on the back end
    because it has stayed small while [Flask](https://flask.palletsprojects.com/) keeps growing.
    Note that I wouldn't use type hints in the Python code:
    if I wanted to write Java, I'd write Java.

1.  [Ibis](http://www.dmulholl.com/docs/ibis/master/) templates
    because they're simpler than [Jinja](https://jinja.palletsprojects.com/).
    (See also [this post](https://third-bit.com/2024/02/25/community-norms/).)

1.  [mamba](https://mamba.readthedocs.io/),
    [ruff](https://docs.astral.sh/ruff/),
    and [uv](https://github.com/astral-sh/uv) for Python tooling.

1.  [Alpine.js](https://alpinejs.dev/) as a front-end framework
    because [htmx](https://htmx.org/) feels a bit left-field
    and [React](https://react.dev/) and [Vue](https://vuejs.org/) seem bent on cosplaying Enterprise Java.

1.  [npm](https://www.npmjs.com/),
    [Vite](https://vitejs.dev/),
    and [StandardJS](https://standardjs.com/) for JavaScript tooling.

1.  [Mantine](https://ui.mantine.dev/) for the UI,
    though I could be persuaded to stick to [Bootstrap](https://getbootstrap.com/).
    (I've never really gotten [Tailwind](https://tailwindcss.com/).)

1.  [Pa11y](https://pa11y.org/) for accessibility testing
    (because [the standalone version of WebAIM WAVE](https://wave.webaim.org/standalone) costs US$4000/year).

1.  [Netlify](https://www.netlify.com/) for deployment.

This list deliberately isn't [an entirely new stack](https://third-bit.com/2024/04/18/a-new-stack/),
but it's also not entirely conservative.
I know it should include a security auditing tool to sit beside Pa11y,
but while I've watched people use [Snyk](https://snyk.io/)
I don't have any experience with it or alternatives.

So much for tools:
what would I teach?
My learner persona is:

> 1.  Carter has a BSc in bioinformatics
>     and now works as a data scientist for a mid-sized therapeutics company.
> 1.  They know Python well enough to analyze data for their colleagues
>     and build dashboards using [Dash](https://dash.plotly.com/),
>     but only ever did a couple of assignments using JavaScript.
> 1.  Carter wants to build something to replace their company's aging PHP-based record keeping tools.
> 1.  Carter has an [idiopathic tremor](https://en.wikipedia.org/wiki/Essential_tremor)
>     that sometimes makes fine motor control difficult.
>     As a result,
>     they find many websites awkward or impossible to use
>     and strongly prefer typing to using a mouse or a touch screen,

1.  The motivating example would be a *laboratory information management system* (LIMS)
    designed to handle field samples and laboratory experiments.

1.  *Database schema design*:
    I'd start with something simple and extend it chapter by chapter.

1.  …which means the list above should have included a *database migration* tool like [Sqitch](https://sqitch.org/).

1.  Building a *command-line user interface* (CLUI) for administration, batch operations, and testing
    (which means adding [pytest](https://docs.pytest.org/) and [Click](https://click.palletsprojects.com/)
    to the list of tools.)

1.  *Authentication*:
    it's straightforward to add this to the CLUI,
    but will require something like [Flask-Login](https://flask-login.readthedocs.io/) for the web UI.
    I don't know of a framework-agnostic alternative,
    so I might have to revisit my decision to use Bottle.

1.  *Routing URLs* to handler functions
    (and redirecting when authentication is needed).

1.  *Permissions*,
    which means *user roles*.
    Again,
    [Flask-User](https://flask-user.readthedocs.io/) does this and I don't know of a framework-agnostic alternative,
    so yeah, Flask…

1.  *Generating pages from templates* and *form handling*.
    I hope we've all outgrown single-page applications,
    so *site architecture design* as a complement to schema design will need to be here.

1.  *Paging* for displaying large data sets and *plotting* for displaying data graphically.

1.  *Responsive web design* because most a lot of people use their phones more than their laptops
    (particularly when they're in the field).

1.  *Accessibility* because I'd be ashamed not to
    and because [I'm not getting any younger](https://educate.elsevier.com/book/details/9780128044674).

1.  *Security* is a hard one.
    [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing),
    [CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery),
    [SQL injection](https://en.wikipedia.org/wiki/SQL_injection),
    authentication,
    site certificates,
    and password management
    are all must-haves,
    but as [Mike Hoye](https://exple.tive.org/blarg/) has observed,
    what we really need to teach people is things like,
    "How to build websites that can't be exploited by abusive domestic partners."
    I really don't know what I could do here that wouldn't require a second book;
    I would try crowdsourcing it like [*The Architecture of Open Source Applications*](https://aosabook.org/),
    but that didn't go anywhere [the last time I tried it](https://third-bit.com/2024/01/23/the-votes-are-in/).

This book will probably never happen,
but probably isn't the same as definitely.
If you think of anything else that ought to be included,
please [let me know](mailto:gvwilson@third-bit.com).

Later:

-   Irving Reid pointed out that running the application is as important as building it,
    and suggested the lessons should include creating and restoring backups,
    deploying updates,
    and observability
    (which involves more than creating log messages that are findable, comprehensible, and informative,
    but that would be a good start).

-   Someone else (name unknown) felt that dependency maintenance should be on the list as well,
    i.e.,
    that there should be a lesson about vulnerability scans and automating checks for dependency updates.

-   Someone else (name also unknown) suggested that there ought to be a lesson on debugging full-stack applications,
    and that the lessons should show how to create good pull requests and how to review them.
    I strongly agree,
    but teaching verbs is a lot harder than teaching nouns,
    and this is already far too ambitious for something that would already take a year of unpaid work.
