TARGETS := $(shell ls SPECS/ | sed 's/\.spec//g')
VERIFY  := VERIFY/sources
RELEASE := alma+epel-9-x86_64
CONFIG  := /etc/mock/$(RELEASE).cfg
BUILT   := /var/lib/mock/$(RELEASE)/result/
REPO    := $(HOME)/.store/pkgs/rpms/
SRCREPO := $(REPO)/src/

all:
	$(error "pick target")

$(TARGETS):
	echo $(TOOLBOX) | grep -q '^rpms$$'
	cd SPECS && spectool -g -R $@.spec
	sha256sum $(shell find SOURCES/ -type f -path "*/$@*" | sort) > $(VERIFY)
	diff -u VERIFY/$@.sums $(VERIFY)
	cd SPECS && rpmbuild -bs $@.spec
	cd SRPMS && mock -r $(CONFIG) --rebuild $@-*
	cp $(BUILT)*.rpm $(REPO)
	mv $(REPO)*.src.rpm $(SRCREPO)
	rpmlint -r VERIFY/$@.rpmlint --strict $(REPO)$@-*
