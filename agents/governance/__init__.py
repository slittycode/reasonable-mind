"""
Lightweight governance layer exposed for tests.

These modules provide a minimal implementation focused on the behaviours
covered by the governance and shell injection test suites. The intent is to
mirror the API that tests expect while keeping the logic easy to audit.
"""
"""Governance utilities for process, execution, and plan validation."""

from .process_gate import ProcessGate, ProcessStage, StageResult
from .registry import ConstraintRegistry, ConstraintProfile
from .execution_proxy import (
    ExecutionProxy,
    ExecutionMode,
    ExecutionResult,
    ExecutionContext,
    create_execution_context,
)
from .plan_validator import (
    PlanValidator,
    Plan,
    PlanStep,
    ViolationType,
    ValidationResult,
    Violation,
)
from .plan_validator import PlanValidator, Plan, PlanStep, ViolationType

__all__ = [
    "ProcessGate",
    "ProcessStage",
    "StageResult",
    "ConstraintRegistry",
    "ConstraintProfile",
    "ExecutionProxy",
    "ExecutionMode",
    "ExecutionResult",
    "ExecutionContext",
    "create_execution_context",
    "PlanValidator",
    "Plan",
    "PlanStep",
    "ViolationType",
    "ValidationResult",
    "Violation",
]
