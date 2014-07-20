cd "C:\Program Files (x86)\Gettext"

rem update pot file & po
c:xgettext -j -d application -o application.pot -L Python application.py
c:xgettext -j -d application -i application.pot -l fr -o application.fr.po
c:msgfmt -o application.fr.mo -v application.fr.po

cd plugins/piratebox10
c:xgettext -j -d piratebox10 -o piratebox10.pot -L Python __init__.py
c:xgettext -j -d piratebox10 -i piratebox10.pot -l fr -o piratebox10.fr.po
c:msgfmt -o piratebox10.fr.mo -v piratebox10.fr.po

cd ..\..
