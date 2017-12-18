ARCH=x86_64
RPMBUILD=rpmbuild
RPMFLAGS=-ba
SRCPATH=${HOME}/rpmbuild
SPECPATH=$(SRCPATH)/SPECS
SOURCESPATH=$(SRCPATH)/SOURCES
RPMPATH=$(SRCPATH)/RPMS/$(ARCH)
VERSION := $(shell grep "VERSION =" setup.py | cut -d"=" -f2 |sed -e 's/"//g' | sed -e 's/\s//')
LASTCOMMIT := $(shell git lg |head -n1| cut -d " " -f2)
tar: compile
	python setup.py sdist

# The tar file needs to be in the repo as the Mock environment doesn't have
# perl-Module-Install available to build it.
sources:
	cp dist/sapi-${VERSION}.tar.gz .
	tar xvzf sapi-${VERSION}.tar.gz > /dev/null 2>&1
	cp -r vendor sapi-${VERSION}
	cd sapi-${VERSION}/vendor && find . -type f -exec tar xvzf {} > /dev/null 2>&1 \; 
	cd sapi-${VERSION}/vendor && rm *.tar.gz
	tar cvzf sapi-${VERSION}.tar.gz sapi-${VERSION} > /dev/null 2>&1

koji:
	ssh aiadm koji build db7 --nowait --scratch "git+ssh://git@gitlab.cern.ch:7999/db/sapi_client.git#${LASTCOMMIT}"

local: 
	cp sapi-${VERSION}.tar.gz ~/rpmbuild/SOURCES
	rpmbuild -ba sapi_client.spec

clean:
	rm -f sapi-*.tar.gz
	rm -fr sapi-${VERSION}

