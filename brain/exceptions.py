class BrainException(Exception):
    """Base exception for Brain."""
    pass


class LLMGenerationError(BrainException):
    """Raised when all models fail to generate a response."""
    pass


class UnsupportedProviderError(BrainException):
    """Raised when an unsupported LLM provider is requested."""
    pass