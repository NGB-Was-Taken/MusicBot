__all__ = ('TrackEnd',
           'TrackException',
           'TrackStuck',
           'TrackStart',
           'WebsocketClosed')


class TrackEnd:
    """Event dispatched on TrackEnd.
    Attributes
    ------------
    player: :class:`wavelink.player.Player`
        The player associated with the event.
    track: :class:`wavelink.player.Track`
        The track associated with the event.
    reason: str
        The reason the TrackEnd event was dispatched.
    """

    __slots__ = ('track', 'player', 'reason')

    def __init__(self, data: dict):
        self.track = data.get('track')
        self.player = data.get('player')
        self.reason = data.get('reason')

    def __str__(self):
        return 'TrackEndEvent'


class TrackException:
    """Event dispatched on TrackException.
    Attributes
    ------------
    player: :class:`wavelink.player.Player`
        The player associated with the event.
    track: :class:`wavelink.player.Track`
        The track associated with the event.
    error: str
        The error reason dispatched with the event.
    """

    __slots__ = ('track', 'player', 'error')

    def __init__(self, data: dict):
        self.track = data.get('track')
        self.player = data.get('player')
        self.error = data.get('error')

    def __str__(self):
        return 'TrackExceptionEvent'


class TrackStuck:
    """Event dispatched on TrackStuck.
    Attributes
    ------------
    player: :class:`wavelink.player.Player`
        The player associated with the event.
    track: :class:`wavelink.player.Track`
        The track associated with the event.
    threshold: int
        The threshold associated with the event.
    """

    __slots__ = ('track', 'player', 'threshold')

    def __init__(self, data: dict):
        self.track = data.get('track')
        self.player = data.get('player')
        self.threshold = int(data.get('thresholdMs'))

    def __str__(self):
        return 'TrackStuckEvent'


class TrackStart:
    """Event dispatched on TrackStart.
    Attributes
    ------------
    player: :class:`wavelink.player.Player`
        The player associated with the event.
    track: :class:`wavelink.player.Track`
        The track associated with the event.
    """

    __slots__ = ('track', 'player')

    def __init__(self, data: dict):
        self.track = data.get('track')
        self.player = data.get('player')

    def __str__(self):
        return 'TrackStartEvent'


class WebsocketClosed:
    """Event dispatched when a player disconnects from a Guild.
    Attributes
    ------------
    player: :class:`wavelink.player.Player`
        The player associated with the event.
    reason: str
        The reason the event was dispatched.
    code: int
        The websocket reason code.
    guild_id: int
        The guild ID associated with the disconnect.
    """

    __slots__ = ('player', 'reason', 'code', 'guild_id')

    def __init__(self, data: dict):
        self.player = data.get('player')
        self.reason = data.get('reason')
        self.code = data.get('code')
        self.guild_id = data.get('guildID')

    def __str__(self):
        return 'WebsocketClosedEvent'