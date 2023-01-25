VERIFY  := VERIFY/sources
RELEASE := alma+epel-9-x86_64
CONFIG  := /etc/mock/$(RELEASE).cfg
BUILT   := /var/lib/mock/$(RELEASE)/result/
REPO    := $(RPMS_STORE)/
SRCREPO := $(REPO)/src/

all:
	$(error "pick target")

metadata:
	if [ $(shell ls $(REPO)*.rpm | wc -l) -ne $(shell ls SPECS/ | wc -l) ]; then echo "rpm/specs count mismatch"; exit 1; fi
	if [ $(shell ls $(REPO)*.rpm | wc -l) -ne $(shell ls $(SRCREPO)*.rpm | wc -l) ]; then echo "src/rpm count mismatch"; exit 1; fi
	createrepo $(REPO)

staticcheck gopls lockbox goyq efmlsp:
	make _build TARGET=$@ MOCK_OPTIONS="--enable-network" RELEASE=fedora-37-x86_64

filebrowser:
	make _build TARGET=$@ MOCK_OPTIONS="--enable-network"

isync stagit khal:
	make _build TARGET=$@

_build:
	mkdir -p BUILD BUILDROOT RPMS SRPMS
	echo $(TOOLBOX) | grep -q '^rpms$$'
	rm -f SRPMS/$(TARGET)*
	cd SPECS && spectool -g -R $(TARGET).spec
	sha256sum SOURCES/$(TARGET)* > $(VERIFY)
	diff -u VERIFY/$(TARGET).sums $(VERIFY)
	cd SPECS && rpmbuild -bs $(TARGET).spec
	cd SRPMS && mock $(MOCK_OPTIONS) -r $(CONFIG) --rebuild $(TARGET)-*
	cp $(BUILT)*.rpm $(REPO)
	mv $(REPO)*.src.rpm $(SRCREPO)
	find $(REPO) -type f -name "*-debug*" -delete
	rpmlint -r VERIFY/$(TARGET).rpmlint --strict $(REPO)$(TARGET)-*
