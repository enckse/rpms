GOFLAGS := -trimpath -buildmode=pie -mod=readonly -modcacherw -buildvcs=false

all:
	go build $(GOFLAGS) $(MORE_FLAGS) -o $(BINARY) $(SRC)
	strip --strip-all $(BINARY)