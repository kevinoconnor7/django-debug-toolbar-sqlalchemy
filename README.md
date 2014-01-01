# Django Debug Toolbar SQLAlchemy

SQLAlchemy query information panel for Django Debug Toolbar.

## Setup

Once the package is installed you'll want to add the module to your installed apps:

	INSTALLED_APPS = (
		...
		'debug_toolbar_sqlalchemy',
		...
	)
	
	DEBUG_TOOLBAR_PANELS = (
		...
		'debug_toolbar_sqlalchemy.panel.SqlAlchemyDebugPanel',
		...
	)

The only optional setting there is to modify is ```DEBUG_TOOLBAR_SQLALCHEMY_SLOW_QUERY_TIME``` which defines the cutoff in milliseconds for which queries will be marked as being slow.

## License
This project is licensed on the GPLv3 license. The full license can be found in the LICENSE file.