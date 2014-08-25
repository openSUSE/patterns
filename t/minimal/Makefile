#ARGS=--explain
ARCH=x86_64
YAST_PACKS=grub2,yast2-installation,kernel-default,branding-openSUSE
FACTORY_REPO=repo-oss

all: test_minimal

test_minimal: patterns.solv factory.solv
	./run \
		--arch $(ARCH) \
		--repo patterns \
		--repo factory \
		--packs patterns-openSUSE-minimal_base@patterns \
		--packs patterns-openSUSE-minimal_base-conflicts@patterns \
		--packs "$(YAST_PACKS)" \
		$(ARGS)

patterns.solv: patterns-openSUSE/patterns-openSUSE.spec
	./createsolv
	rm -f patterns.solv
	ln -s patterns-openSUSE/patterns.solv patterns.solv

patterns-openSUSE/patterns-openSUSE.spec:
	osc co -c system:install:head/patterns-openSUSE

factory.solv: /var/cache/zypp/solv/$(FACTORY_REPO)/solv
	ln -s /var/cache/zypp/solv/$(FACTORY_REPO)/solv factory.solv

.PHONY: all
