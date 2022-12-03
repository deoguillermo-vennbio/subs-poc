from ariadne.asgi import GraphQL
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse

from app.graphql.schema import gql_schema
from app.utils.broadcaster import broadcast

app = Starlette(
    on_startup=[broadcast.connect],
    on_shutdown=[broadcast.disconnect]
)

@app.route('/')
async def homepage(request):
    return JSONResponse({'hello': 'worldsz'})

app.mount('/graphql', GraphQL(gql_schema, debug=True))
