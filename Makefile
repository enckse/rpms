VERIFY  := VERIFY/sources
RELEASE := alma+epel-9-x86_64
CONFIG  := /etc/mock/$(RELEASE).cfg
BUILT   := /var/lib/mock/$(RELEASE)/result/
REPO    := $(HOME)/.store/pkgs/rpms/
SRCREPO := $(REPO)/src/

all:
	$(error "pick target")

staticcheck revive:
	make _build TARGET=$@ MOCK_OPTIONS="--enable-network" RELEASE=fedora-37-x86_64

filebrowser:
	make _build TARGET=$@ MOCK_OPTIONS="--enable-network"

isync stagit mblaze:
	make _build TARGET=$@

_build:
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
