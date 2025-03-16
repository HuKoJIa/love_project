from abc import ABC 
from typing import Generic, TypeVar

import didiator


QRes = TypeVar("QRes")

class Query(didiator.Query[QRes], ABC, Generic[QRes]):
    pass 

Q = TypeVar("Q", bound=Query)

class QueryHandler(didiator.QueryHandler[Q], ABC, Generic[Q, QRes]):
    pass 