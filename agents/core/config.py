"""
Configuration constants for core reasoning systems.
"""

# Circuit Breaker Configuration
CIRCUIT_BREAKER_FAILURE_THRESHOLD = 5
CIRCUIT_BREAKER_RECOVERY_TIMEOUT = 30  # seconds

# Latency Budget (milliseconds)
LATENCY_BUDGET_REASONING_MS = 10000.0  # 10 seconds
LATENCY_BUDGET_TOOL_CALL_MS = 5000.0   # 5 seconds

# Calibration
CALIBRATION_MIN_SAMPLES = 10

# Feedback
FEEDBACK_LEARNING_RATE = 0.1
