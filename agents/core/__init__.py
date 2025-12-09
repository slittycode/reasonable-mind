"""
Core logic modules for deterministic reasoning.

This package provides the foundational logic components:
- logic_engine: Propositional logic validation
- categorical_engine: Aristotelian syllogistic reasoning
- fallacy_detector: Pattern-based fallacy detection
"""

from .categorical_engine import CategoricalEngine, SyllogismType
from .fallacy_detector import (
    FallacyCategory,
    FallacyDetector,
    FallacyPattern,
    FallacySeverity,
)
from .logic_engine import ArgumentForm, LogicEngine, LogicResult

__all__ = [
    "LogicEngine",
    "ArgumentForm",
    "LogicResult",
    "CategoricalEngine",
    "SyllogismType",
    "FallacyDetector",
    "FallacyCategory",
    "FallacySeverity",
    "FallacyPattern",
]
