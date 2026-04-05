admin:
	pyside6-rcc ./src/presentation/resources/admin.qrc -o src/presentation/resources/admin_rc.py
	watchmedo auto-restart --patterns="*.py" --recursive --signal SIGKILL -- python ./src/admin.py