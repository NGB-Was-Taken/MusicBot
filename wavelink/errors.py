class WavelinkException(Exception):
    """Base Wavelink Exception."""
    
class NodeOccupied(WavelinkException):
    """Exception raised when node identifiers conflict."""

class InvalidIDProvided(WavelinkException):
    """Exception raised when an invalid ID is passesd somewhere in Wavelink."""

class ZeroConnectedNodes(WavelinkException):
    """Exception is raised when an operation is atemped with nodes, when there are None connected."""

class AuthorizationFaliture(WavelinkException):
    """Exception raised when an invalid password is provided to a node."""

class BuildTrackError(WavelinkException):
    """Exception raised when a track is failed to be decoded and re-built."""