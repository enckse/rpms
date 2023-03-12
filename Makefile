VERIFY  := VERIFY/sources
RELEASE := fedora-37-x86_64
CONFIG  := /etc/mock/$(RELEASE).cfg
BUILT   := /var/lib/mock/$(RELEASE)/result/
REPO    := $(PKGS_STORE)/rpms/
SRCREPO := $(REPO)/src/
SPECS   := $(shell ls SPECS/ | sed 's/\.spec//g')
GOMAKE  := SOURCES/go.Makefile

all:
	$(error "pick target")

metadata:
	@which createrepo
	if [ $(shell ls $(REPO)*.rpm | wc -l) -ne $(shell ls SPECS/ | wc -l) ]; then echo "rpm/specs count mismatch"; exit 1; fi
	if [ $(shell ls $(REPO)*.rpm | wc -l) -ne $(shell ls $(SRCREPO)*.rpm | wc -l) ]; then echo "src/rpm count mismatch"; exit 1; fi
	createrepo $(REPO)

clean:
	rm -f $(GOMAKE)
	rm -f SOURCES/*.tar.*

$(GOMAKE):
	make .go.make | grep -v "^make" > $(GOMAKE)

.go.make:
	@echo "GOFLAGS := $(GOFLAGS)"
	@echo
	@echo "all:"
	@printf "\tgo build \$$(GOFLAGS) -o \$$(BINARY) \$$(SRC)\n"
	@printf "\tstrip --strip-all \$$(BINARY)\n"

$(SPECS):
	make _build TARGET=$@ MOCK_OPTIONS="--enable-network"

_build: $(GOMAKE)
	mkdir -p BUILD BUILDROOT RPMS SRPMS
	@which spectool
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
