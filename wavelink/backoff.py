import time
import random


class ExponentialBackoff:
    """
    An implementation of the exponential backoff algirithm
    Provides a convenient interface to implement an exponential backoff for reconnecting or retrying transmissions in a distributed network.
    One instantiated, the delay method will return the next interval to wait for when retrying a connection or transmission.
    The maximum delay increases exponentally with each retry up to a maximum of 2^10 * base, and is reset if no more attempts are needed in a period of 2^11 * base seconds.
    Parameters
    ----------
    base : int
        The base delay in seconds. The first retry-delay will be up to this many seconds.
    integral: bool
        Set to True if whole periods of base is desireable, otherwise any number in between may be returned.
    """

    def __init__(self, base=1, *, integral=False):
        self.base = base

        self._exp = 0
        self._max = 10
        self._reset_time = base*2**11
        self._last_invocation = time.monotonic()

        rand = random.Random()
        rand.seed()

        self._randfunc = rand.randrange if integral else rand.uniform

    def delay(self):
        """
        Compute the next delay
        Returns the next delay to wait accroding to the exponential backoff algorithm. This is a value between 0 and base * 2^exp where exponents starts off at 1 and is incremented every invocation of this method up to a maximum of 10.
        If a peroid of more than base * 2^11 seconds has passed since the last retry, the exponent is reset to 1.
        """
        invocation = time.monotonic()
        interval = invocation - self._last_invocation
        self._last_invocation = invocation

        if interval > self._reset_time:
            self._exp = 0

        self._exp = min(self._exp + 1, self._max)
        return self._randfunc(0, self.base * 2**self._exp)
        
