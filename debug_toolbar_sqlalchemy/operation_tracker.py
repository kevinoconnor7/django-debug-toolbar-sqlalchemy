from sqlalchemy.event import listen
from operator import itemgetter
from django.conf import settings
from sqlalchemy.engine import Engine
import sys
import time

# the best timer function for the platform
if sys.platform == 'win32':
    _timer = time.clock
else:
    _timer = time.time

class _DebugQueryTuple(tuple):
    statement = property(itemgetter(0))
    parameters = property(itemgetter(1))
    start_time = property(itemgetter(2))
    end_time = property(itemgetter(3))

    @property
    def duration(self):
        return (self.end_time - self.start_time)*1000

    @property
    def is_slow(self):
        version_cutoff = getattr(
            settings,
            'DEBUG_TOOLBAR_SQLALCHEMY_SLOW_QUERY_TIME',
            1000
        )
        return (self.duration > version_cutoff)


    def __repr__(self):
        return '<query statement="%s" parameters=%r duration=%d>' % (
            self.statement,
            self.parameters,
            self.duration
        )

class OperationTracker(object):
    def __init__(self):
        self.queries = []

    def register(self):
        listen(Engine, 'before_cursor_execute', self.before_cursor_execute)
        listen(Engine, 'after_cursor_execute', self.after_cursor_execute)

    def before_cursor_execute(self, conn, cursor, statement, parameters,
        context, executemany):
        context._query_start_time = _timer()

    def after_cursor_execute(self, conn, cursor, statement, parameters,
        context, executemany):
        if self.queries is None:
            self.queries = []
        self.queries.append(_DebugQueryTuple((
            statement, parameters, context._query_start_time, _timer())))
