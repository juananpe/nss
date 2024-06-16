# snailz

A set of synthetic data generators for teaching data science
that has somehow morphed into a lesson on human-scale computing.

I recently posted on Mastodon:

> 1.  I'm going to write another tech book.
> 2.  If I do, it will be about evidence-based software engineering and/or how big tech companies operate like drug cartels.
> 3.  But I'm still thinking about "Human-Scale Software: A Guide for the 99.9% of Developers Who Don't Need Scalability"

So what would I use for #3?

1.  [SQLite][sqlite] for storage.
    ([DuckDB][duckdb] is cool, but I'm being deliberately conservative in my choices.)
1.  I wouldn't use an object-relational mapper:
    I've used [SQLAlchemy][sqlalchemy] for years,
    but I think embedded SQL is easier to debug than an ORM for small-to-medium use cases.
1.  [Bottle][bottle] on the back end
    because it has stayed small while [Flask][flask] keeps growing
    (but see discussion below).
    Note that I wouldn't use type hints in the Python code:
    if I wanted to write Java, I'd write Java.
1.  [Ibis][ibis] templates
    because they're simpler than [Jinja][jinja].
    (See also [this post](https://third-bit.com/2024/02/25/community-norms/).)
1.  [mamba][mamba],
    [ruff][ruff],
    and [uv][uf] for Python tooling.
1.  [Alpine.js][alpine] as a front-end framework
    because [htmx][htmx] feels a bit left-field
    and [React][react] and [Vue][vue] seem bent on cosplaying Enterprise Java.
1.  [npm][npm],
    [Vite][vite],
    and [StandardJS][standardjs] for JavaScript tooling.
1.  [Mantine][mantine] for the UI,
    though I could be persuaded to stick to [Bootstrap][bootstrap].
    (I've never really gotten [Tailwind][tailwind].)
1.  [Pa11y][pa11y] for accessibility testing
    (because [the standalone version](https://wave.webaim.org/standalone) of [WebAIM WAVE][wave] costs US$4000/year).
1.  [Netlify][netlify] for deployment.

This list deliberately isn't [an entirely new stack](https://third-bit.com/2024/04/18/a-new-stack/),
but it's also not entirely conservative.
I know it should include a security auditing tool to sit beside Pa11y,
but while I've watched people use [Snyk][snyk]
I don't have any experience with it or alternatives.

So much for tools:
what would I teach?
My learner persona is:

> 1.  Carter has a BSc in bioinformatics
>     and now works as a data scientist for a mid-sized therapeutics company.
> 1.  They know Python well enough to analyze data for their colleagues
>     and build dashboards using [Dash][dash],
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
1.  …which means the list above should have included a *database migration* tool like [Sqitch][sqitch].
1.  Building a *command-line user interface* (CLUI) for administration, batch operations, and testing
    (which means adding [pytest][pytest] and [Click][click]
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

[alpine]: https://alpinejs.dev/
[ark]: https://www.dmulholl.com/docs/ark/main/
[atkinson]: https://brailleinstitute.org/freefont
[bootstrap]: https://getbootstrap.com/
[bottle]: https://bottlepy.org/
[bs4]: https://pypi.org/project/beautifulsoup4/
[click]: https://click.palletsprojects.com/
[dash]: https://dash.plotly.com/
[draw_io]: https://www.drawio.com/
[DuckDB]: https://duckdb.org/
[faker]: https://faker.readthedocs.io/
[flask]: https://flask.palletsprojects.com/
[geopy]: https://geopy.readthedocs.io/
[ghp]: https://pages.github.com/
[highlight_css]: https://numist.github.io/highlight-css/
[html5validator]: https://pypi.org/project/html5validator/
[htmx]: https://htmx.org/
[Ibis]: http://www.dmulholl.com/docs/ibis/master/
[jinja]: https://jinja.palletsprojects.com/
[mamba]: https://mamba.readthedocs.io/
[mantine]: https://ui.mantine.dev/
[navarro_danielle]: https://art.djnavarro.net/
[netlify]: https://www.netlify.com/
[npm]: https://www.npmjs.com/
[pa11y]: https://pa11y.org/
[plausible]: https://plausible.io/
[plotly]: https://plotly.com/
[polars]: https://pola.rs/
[pybtex]: https://pypi.org/project/pybtex/
[pytest]: https://docs.pytest.org/
[react]: https://react.dev/
[repo]: https://github.com/gvwilson/snailz
[ruff]: https://docs.astral.sh/ruff/
[snyk]: https://snyk.io/
[sqitch]: https://sqitch.org/
[sqlalchemy]: https://www.sqlalchemy.org/
[sqlite]: https://sqlite.org/
[stamps]: https://third-bit.com/colophon/
[standardjs]: https://standardjs.com/
[tailwind]: https://tailwindcss.com/
[uv]: https://github.com/astral-sh/uv
[vite]: https://vitejs.dev/
[vue]: https://vuejs.org/
[wave]: https://wave.webaim.org/
