from typing import Any, Dict, Optional

from ..error.illegal_attr_checker import IllegalAttrChecker
from ..error.uncallable_namespace import UncallableNamespace
from ..query_runner.query_runner import QueryRunner


class TopologicalLPRunner(UncallableNamespace, IllegalAttrChecker):
    def __init__(self, query_runner: QueryRunner, namespace: str):
        self._query_runner = query_runner
        self._namespace = namespace

    def _run_standard_function(
        self, node1: int, node2: int, config: Dict[str, Any]
    ) -> float:
        query = f"""
        MATCH (n1) WHERE id(n1) = {node1}
        MATCH (n2) WHERE id(n2) = {node2}
        RETURN {self._namespace}(n1, n2, $config) AS score
        """
        params = {"config": config}

        return self._query_runner.run_query(query, params)[0]["score"]  # type: ignore

    def adamicAdar(self, node1: int, node2: int, **config: Any) -> float:
        self._namespace += ".adamicAdar"
        return self._run_standard_function(node1, node2, config)

    def commonNeighbors(self, node1: int, node2: int, **config: Any) -> float:
        self._namespace += ".commonNeighbors"
        return self._run_standard_function(node1, node2, config)

    def preferentialAttachment(self, node1: int, node2: int, **config: Any) -> float:
        self._namespace += ".preferentialAttachment"
        return self._run_standard_function(node1, node2, config)

    def resourceAllocation(self, node1: int, node2: int, **config: Any) -> float:
        self._namespace += ".resourceAllocation"
        return self._run_standard_function(node1, node2, config)

    def sameCommunity(
        self, node1: int, node2: int, communityProperty: Optional[str] = None
    ) -> float:
        self._namespace += ".sameCommunity"
        community_property = f", '{communityProperty}'" if communityProperty else ""

        query = f"""
        MATCH (n1) WHERE id(n1) = {node1}
        MATCH (n2) WHERE id(n2) = {node2}
        RETURN {self._namespace}(n1, n2{community_property}) AS score
        """

        return self._query_runner.run_query(query)[0]["score"]  # type: ignore

    def totalNeighbors(self, node1: int, node2: int, **config: Any) -> float:
        self._namespace += ".totalNeighbors"
        return self._run_standard_function(node1, node2, config)
