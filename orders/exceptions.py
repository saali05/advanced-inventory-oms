class OrderError(Exception):
    """Base order exception."""


class InsufficientStockError(OrderError):
    """Raised when stock is insufficient."""


class InvalidOrderError(OrderError):
    """Raised when order data is invalid."""