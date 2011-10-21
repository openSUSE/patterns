#ARGS=--explain
ARCH=x86_64
YAST_PACKS=grub,yast2-installation,kernel-default

all: test_minimal

test_minimal: patterns.solv factory.solv
	./run \
		--arch $(ARCH) \
		--repo patterns \
		--repo factory \
		--packs pattern:minimal_base@patterns \
		--packs pattern:minimal_base-conflicts@patterns \
		--packs "$(YAST_PACKS)" \
		$(ARGS)

patterns.solv:
	repo2solv.sh . > patterns.solv

.PHONY: all test1
