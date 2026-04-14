.PHONY: admin-revision

admin:
	flet run src/admin.py

revision:
ifndef name
	$(error name is undefined. Usage: make build name=new_migration)
endif
	cd ./src
	alembic -c ../alembic.ini revision --autogenerate -m "$(name)"
