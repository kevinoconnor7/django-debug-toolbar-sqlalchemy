from debug_toolbar.panels import Panel
from debug_toolbar_sqlalchemy.operation_tracker import OperationTracker
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string

class SqlAlchemyDebugPanel(Panel):
    """ Panel that shows information about SQLAlchemy operations. """
    name = 'SQLAlchemy'
    has_content = True
    template = 'sqlalchemy-panel.html'

    def __init__(self, *args, **kwargs):
        super(SqlAlchemyDebugPanel, self).__init__(*args, **kwargs)
        self.tracker = OperationTracker()
        self.tracker.register()

    def nav_title(self):
        return _('SQLAlchemy')

    def nav_subtitle(self):
        if self.tracker:
            count = len(self.tracker.queries)
            return "%d %s" % (count, "query" if count == 1 else "queries")

        return "Unavailable"

    def title(self):
        return _('SQLAlchemy queries')

    def url(self):
        return ''

    @property
    def content(self):
        return render_to_string(
            self.template,
            {'queries': self.tracker.queries}
        )

