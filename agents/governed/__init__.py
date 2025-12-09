"""
Governed Agent Module - Constitutional Governance Implementation.

Provides runtime enforcement of governance policies:
- PersonaLock: Immutable agent identity (§1.2)
- ConstraintLoader: Profile loading with integrity hashing (§1.5)
- PlanValidator: Natural language plan validation (§1.6)
- ExecutionProxy: Sandboxed execution with policy enforcement
- GovernedCodingAgent: Complete governed agent implementation

Usage:
    from agents.governed import GovernedCodingAgent, ExecutionMode

    agent = GovernedCodingAgent.create(
        agent_id="my-agent",
        sandbox_root=Path("sandbox/"),
        governance_dir=Path("agents/governed/policies/"),
        mode=ExecutionMode.LIVE
    )

    result = agent.execute_task("read file test.py")
"""

from .constraint_loader import (
    ActionPolicy,
    ConstraintLoader,
    InheritanceError,
    LoadedProfile,
    LoaderError,
    ProfileConflictError,
    ProfileNotFoundError,
    ProfileValidationError,
)
from .execution_proxy import (
    ActionRequest,
    ActionResult,
    ActionType,
    AuditEntry,
    Decision,
    ExecutionMode,
    ExecutionProxy,
)
from .governed_agent import (
    ExecutionContext,
    GovernedCodingAgent,
    Violation,
    ViolationCode,
)
from .persona_lock import (
    AGENT_CAPABILITIES,
    AgentType,
    PersonaContext,
    PersonaLock,
    PersonaLockViolation,
    PersonaMismatchViolation,
    PersonaViolation,
)
from .plan_validator import (
    ActionCategory,
    ExtractedAction,
    Plan,
    PlanStep,
    PlanValidator,
    ToolCall,
    ValidationOutcome,
    ValidationResult,
)

__all__ = [
    # Constraint Loader
    "ConstraintLoader",
    "LoadedProfile",
    "LoaderError",
    "ProfileNotFoundError",
    "ProfileValidationError",
    "InheritanceError",
    "ProfileConflictError",
    "ActionPolicy",
    # Execution Proxy
    "ExecutionProxy",
    "ExecutionMode",
    "ActionType",
    "Decision",
    "ActionRequest",
    "ActionResult",
    "AuditEntry",
    # Plan Validator
    "PlanValidator",
    "Plan",
    "PlanStep",
    "ExtractedAction",
    "ToolCall",
    "ValidationOutcome",
    "ValidationResult",
    "ActionCategory",
    # Persona Lock
    "PersonaLock",
    "PersonaContext",
    "PersonaViolation",
    "PersonaLockViolation",
    "PersonaMismatchViolation",
    "AgentType",
    "AGENT_CAPABILITIES",
    # Governed Agent
    "GovernedCodingAgent",
    "ViolationCode",
    "Violation",
    "ExecutionContext",
]
