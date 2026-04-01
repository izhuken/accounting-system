admin:
	pyside6-rcc ./src/presentation/resources/admin.qrc -o src/presentation/resources/admin_rc.py
	python ./src/admin.py