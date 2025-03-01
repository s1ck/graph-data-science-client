from .graph.graph_endpoints import GraphEndpoints
from .model.model_endpoints import ModelEndpoints
from .query_runner.query_runner import QueryRunner
from .system.system_endpoints import SystemEndpoints
from .utils.util_endpoints import UtilEndpoints


class DirectEndpoints(GraphEndpoints, ModelEndpoints, SystemEndpoints, UtilEndpoints):
    def __init__(self, query_runner: QueryRunner, namespace: str):
        super().__init__(query_runner, namespace)
