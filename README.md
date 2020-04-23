# Serving an SPA through Starlette and FastAPI

Ideally an SPA would be served by a fast webserver, but if you're just adding some UI to an API,
it can be easier to serve it from the API itself. To do this, we need to solve two issues:

1. Serve the index.html to all unknown endpoints so the frontend can handle routing
2. Serve static assets

## Usage

1.  `poetry install`
2.  `poetry run uvicorn --reload app:app`

> todo: flesh out into a blog post
