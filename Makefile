NAME = dtmf-dialer
VERSION = $(shell cat ./VERSION)
VERSIONED_NAME = $(NAME)-$(VERSION)
PYLINT = pylint-2

PREFIX = /usr
BINDIR = $(PREFIX)/bin
DATADIR = $(PREFIX)/share
DOCDIR = $(DATADIR)/doc/$(NAME)
ICONDIR = $(DATADIR)/icons/hicolor/scalable/apps/
DESKTOPFILEDIR=$(DATADIR)/applications

ICONSRCNAME = dtmf-dialer.svg
ICONDSTNAME = $(ICONSRCNAME)

release-dir:
	mkdir -p $(VERSIONED_NAME)

release-cp: release-dir
	cp -a AUTHORS COPYING debian $(NAME).svg $(NAME)-48x48.png $(NAME).desktop $(NAME).py Makefile README.md \
	VERSION $(VERSIONED_NAME)

archive: clean release-cp
	tar czf $(VERSIONED_NAME).tar.gz $(VERSIONED_NAME)

install-dirs:
	install -dD $(DESTDIR)$(BINDIR)
	install -dD $(DESTDIR)$(DOCDIR)
	install -dD $(DESTDIR)$(DATADIR)/applications

install: install-dirs
	install -Dpm 0755 $(NAME).py $(DESTDIR)$(BINDIR)/$(NAME).py
	install -Dpm 0644 -t $(DESTDIR)$(DOCDIR) AUTHORS COPYING README.md

	# icon
	install -Dpm 0644 $(ICONSRCNAME) $(DESTDIR)$(ICONDIR)/$(ICONDSTNAME)

	# desktop file
	desktop-file-install --dir=$(DESTDIR)$(DESKTOPFILEDIR) --vendor="" $(NAME).desktop

clean:
	find -name "*.pyc" | xargs rm -f
	rm -rf $(VERSIONED_NAME)

lint:
	$(PYLINT) -E $(NAME).py

.PHONY: clean archive install lint
