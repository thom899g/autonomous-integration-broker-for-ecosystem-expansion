from abc import ABC, abstractmethod
from typing import List, Optional
import logging

class APICriteria:
    """Encapsulates criteria for evaluating APIs."""
    def __init__(self, performance_score: float, reliability_score: float, cost: float):
        self.performance_score = performance_score
        self.reliability_score = reliability_score
        self.cost = cost

    def is_reliable(self) -> bool:
        """Checks if the API is reliable enough."""
        return self.reliability_score >= 0.8

class APISelectionStrategy(ABC):
    @abstractmethod
    def select_best(self, candidates: List[str]) -> Optional[str]:
        pass

class DefaultAPISelector(APISelectionStrategy):
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def select_best(self, candidates: List[str]) -> str:
        """Selects the best API based on performance and reliability."""
        try:
            # Simulated selection logic
            for api in candidates:
                criteria = self.knowledge_base.get_api_criteria(api)
                if criteria.is_reliable() and criteria.performance_score >= 0.9:
                    return api
            raise ValueError("No suitable API found.")
        except Exception as e:
            logging.error(f"API selection error: {str(e)}")
            raise APISelectionError(f"Failed to select API from candidates: {candidates}")