import ariadne
from app.resolvers import message

type_defs = ariadne.load_schema_from_path('app/graphql/types')
gql_schema = ariadne.make_executable_schema(
    type_defs,
    message.mutation,
    message.subscription
)
