#
# spec file for package patterns-openSUSE
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           patterns-openSUSE
Version:        13.1
Release:        0
Summary:        Patterns for Installation (full ftp tree)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
Source1:        create_macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl(URI::Escape)

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

%{expand:%(perl %{S:1})}

#BEGIN1
%package 32bit
%pattern_basetechnologies
Summary:        32-Bit Runtime Environment
Group:          Metapackages
Provides:       pattern() = 32bit
Provides:       pattern-icon() = yast-misc
Provides:       pattern-order() = 1140

%description 32bit
This pattern installs the 32-bit variant of all selected patterns, allowing you to execute 32-bit software.

%files 32bit
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/32bit.txt

%package 64bit
%pattern_basetechnologies
Summary:        64-Bit Runtime Environment
Group:          Metapackages
Provides:       pattern() = 64bit
Provides:       pattern-icon() = yast-misc
Provides:       pattern-order() = 1160

%description 64bit
This pattern installs the 64-bit variant of all selected patterns, allowing you to execute 64-bit software.

%files 64bit
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/64bit.txt

%package apparmor
%pattern_basetechnologies
Summary:        AppArmor
Group:          Metapackages
Provides:       pattern() = apparmor
Provides:       pattern-icon() = pattern-apparmor
Provides:       pattern-order() = 1100
Requires:       pattern() = basesystem
Recommends:     pattern() = apparmor_opt
# from data/APPARMOR
Requires:       apparmor-parser
Requires:       apparmor-profiles
Requires:       audit
Recommends:     yast2-apparmor
Recommends:     apparmor-utils
Suggests:       pam_apparmor


%description apparmor
AppArmor is an application security framework that provides mandatory access control for programs. It protects from exploitation of software flaws and compromised systems. It offers an advanced tool set that automates the development of per-program application security without requiring additional knowledge.

%files apparmor
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/apparmor.txt

%package apparmor_opt
%pattern_basetechnologies
Summary:        AppArmor
Group:          Metapackages
Provides:       pattern() = apparmor_opt
Provides:       pattern-icon() = apparmor%2Fapp_armor.png
Provides:       pattern-order() = 1080
Provides:       pattern-extends() = apparmor
Requires:       pattern() = basesystem
# from data/APPARMOR-OPT
Requires:       apparmor-docs


%description apparmor_opt
AppArmor is an application security framework that provides mandatory access control for programs. It protects from exploitation of software flaws and compromised systems. It offers an advanced tool set that automates the development of per-program application security without requiring additional knowledge.

%files apparmor_opt
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/apparmor_opt.txt

%package base
%pattern_basetechnologies
Summary:        Base System
Group:          Metapackages
Provides:       pattern() = base
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1020
Provides:       pattern() = basesystem
# from data/BASIS
Requires:       aaa_base
Requires:       dhcpcd
Requires:       hwinfo
Requires:       kbd
Requires:       kernel
Requires:       mkinitrd
Requires:       kmod-compat
Requires:       netcfg
Requires:       openssh
Requires:       procps
Requires:       pwdutils
Requires:       rpm
Requires:       openSUSE-release
Requires:       openSUSE-build-key
Requires:       sysconfig
Requires:       klogd
# enable NFS installation for minimal
Requires:       rpcbind
Requires:       polkit-default-privs
Requires:       polkit
Requires:       sbin_init
Requires:       util-linux
# which, time, adjtimex have been part of util-linux upto 12.3
# needs to be installed or packages fixed first
Requires:       adjtimex
Requires:       time
Requires:       which
%ifarch ppc
Recommends:     libbspe
Recommends:     spu-tools
# #739878 - install pdisk by default
Recommends:     pdisk
%endif
# provides init script to load cpufreq modules
Recommends:     pm-utils
# default init
Recommends:     systemd-sysvinit
# get it branded
Recommends:     branding-openSUSE
%ifarch %ix86 x86_64
Recommends:     grub2
%endif
%ifarch %ix86
Recommends:     grub2-i386-efi
%endif
%ifarch x86_64
Recommends:     grub2-x86_64-efi
Recommends:     shim
%endif
%ifarch ppc
Recommends:     lilo
%endif
Suggests:       grub
Suggests:       systemd-logger


%description base
This is the base runtime system.  It contains only a minimal multiuser booting system. For running on real hardware, you need to add additional packages and pattern to make this pattern useful on its own.

%files base
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/base.txt

%package books
%pattern_documentation
Summary:        Documentation
Group:          Metapackages
Provides:       pattern() = books
Provides:       pattern-icon() = pattern-documentation
Provides:       pattern-order() = 5200
# from data/BOOKS
Recommends:     opensuse-manuals_en
Recommends:     opensuse-startup_en-pdf
Suggests:       ImageMagick-doc
Suggests:       amavisd-new-docs
Suggests:       apache2-doc
Suggests:       apparmor-docs
Suggests:       bash-doc
Suggests:       bind-doc
Suggests:       digikam-doc
Suggests:       dhcp-doc
Suggests:       docbook-tdg
Suggests:       gcc-info
Suggests:       gcc46-info
Suggests:       gnome-devel-docs
Suggests:       gnome-user-docs
Suggests:       gnucash-docs
Suggests:       kernel-docs
Suggests:       kiwi-doc
Suggests:       man-pages
Suggests:       man-pages-fr
Suggests:       man-pages-it
Suggests:       man-pages-ja
Suggests:       man-pages-ko
Suggests:       man-pages-posix
Suggests:       man-pages-ru
Suggests:       nfs-doc
Suggests:       ntp-doc
Suggests:       perl-doc
Suggests:       php-doc
Suggests:       postfix-doc
Suggests:       postgresql-docs
Suggests:       python-doc
Suggests:       python3-doc
Suggests:       python-doc-pdf
Suggests:       python3-doc-pdf
Suggests:       samba-doc
Suggests:       selinux-doc
Suggests:       subversion-doc
Suggests:       texlive-doc
Suggests:       texlive-latex-doc
Suggests:       xorg-x11-doc
Suggests:       yast2-devel-doc
Suggests:       opensuse-manuals_de
Suggests:       opensuse-manuals_hu
Suggests:       opensuse-manuals_ru
Suggests:       opensuse-startup_de-pdf
Suggests:       opensuse-startup_ru-pdf


%description books
Help and Documentation, various books

%files books
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/books.txt

%package console
%pattern_basetechnologies
Summary:        Console Tools
Group:          Metapackages
Provides:       pattern() = console
Provides:       pattern-icon() = yast-system
Provides:       pattern-order() = 1120
# from data/CONSOLE
Requires:       mc
Requires:       w3m
Requires:       wodim
Recommends:     emacs-nox
Recommends:     mtools
Recommends:     sox
Recommends:     vorbis-tools
Suggests:       bsd-games
Suggests:       grepmail
Suggests:       irssi
Suggests:       links
Suggests:       nano
Suggests:       ncftp
Suggests:       minicom
Suggests:       mlocate
Suggests:       mutt
Suggests:       slrn
Suggests:       pinfo
Suggests:       vlock
Suggests:       alpine
Suggests:       pico
Suggests:       convert
Suggests:       ding
Suggests:       units
Suggests:       gcal
Suggests:       lftp
Suggests:       dar
Suggests:       par
Suggests:       makedev
# #378747
Suggests:       cryptconfig
Suggests:       cnetworkmanager


%description console
Applications useful for those using the console and no graphical desktop environment.

%files console
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/console.txt

%package devel_basis
%pattern_development
Summary:        Base Development
Group:          Metapackages
Provides:       pattern() = devel_basis
Provides:       pattern-icon() = pattern-basis-devel
Provides:       pattern-order() = 3140
Requires:       pattern() = basesystem
# from data/DEVEL-BASIS
Requires:       autoconf
Requires:       automake
Requires:       binutils 
Requires:       bison
Requires:       cpp
Requires:       cvs
Requires:       gcc
Requires:       flex
Requires:       gdbm-devel
Requires:       gettext-tools
Requires:       glibc-devel
Requires:       libtool
Requires:       m4
Requires:       make
Requires:       ncurses-devel
Requires:       patch
Requires:       makeinfo
Requires:       zlib-devel
Recommends:     bin86
Recommends:     db-devel
Recommends:     gcc-c++
Recommends:     gcc-info
Recommends:     glibc-info
Recommends:     gmp-devel
Recommends:     gperf
Recommends:     libaio-devel
Recommends:     libgcj-devel
Recommends:     libstdc++-devel
Recommends:     openldap2-devel
Recommends:     pam-devel
Recommends:     pkg-config
Recommends:     subversion
%ifarch ppc
Recommends:     itrace
%endif
# most of our packages use this tool
Recommends:     fdupes
# applying patches
Recommends:     patch
Recommends:     binutils-devel
Recommends:     e2fsprogs-devel
Recommends:     libapparmor-devel
Recommends:     libosip2-devel
Suggests:       build
# bnc#804006
Suggests:       osc
Suggests:       gcc-fortran
Suggests:       gcc-objc
# Matz thinks people want that
Suggests:       mpfr-devel
Suggests:       ccache
Suggests:       icecream
Suggests:       subversion-doc
Suggests:       wiggle
Suggests:       oprofile
Suggests:       libgssglue-devel
Suggests:       audit-devel
Suggests:       nasm


%description devel_basis
Minimal set of tools for compiling and linking applications.

%files devel_basis
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/devel_basis.txt

%package devel_C_C++
%pattern_development
Summary:        C/C++ Development
Group:          Metapackages
Provides:       pattern() = devel_C_C++
Provides:       pattern-icon() = pattern-basis-devel
Provides:       pattern-order() = 3240
Requires:       pattern() = devel_basis
# from data/DEVEL-C-C++
Recommends:     glibc-info
Recommends:     boost-devel
Recommends:     boost-jam
Recommends:     posix_cc
Recommends:     swig
Recommends:     valgrind
Recommends:     ltrace
Suggests:       ddd
# 403368
Suggests:       dejagnu
Suggests:       expect


%description devel_C_C++
Tools and libraries for software development using C/C++ and other derivative of the C programming language.

%files devel_C_C++
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/devel_C_C++.txt

%package devel_gnome
%pattern_development
Summary:        GNOME Development
Group:          Metapackages
Provides:       pattern() = devel_gnome
Provides:       pattern-icon() = pattern-gnome-devel
Provides:       pattern-order() = 3160
Requires:       pattern() = devel_C_C++
Requires:       pattern() = gnome_basis
# from data/DEVEL-GNOME
Recommends:     cairo-devel
Recommends:     clutter-devel
Recommends:     clutter-gst-devel
Recommends:     clutter-gtk-devel
Recommends:     evolution-data-server-devel
Recommends:     gdk-pixbuf-devel
Recommends:     glib2-devel
Recommends:     libgnome-desktop-3-devel
Recommends:     gnome-menus-devel
Recommends:     gnome-online-accounts-devel
Recommends:     gstreamer-0_10-devel
Recommends:     gstreamer-0_10-plugins-base-devel
Recommends:     gtk2-devel
Recommends:     gtk3-devel
Recommends:     gtksourceview-devel
Recommends:     gucharmap-devel
Recommends:     json-glib-devel
Recommends:     libcanberra-devel
Recommends:     libgdata-devel
Recommends:     libgnome-keyring-devel
Recommends:     libgsf-devel
Recommends:     libgtop-devel
Recommends:     libgweather-devel
Recommends:     libnotify-devel
Recommends:     librsvg-devel
Recommends:     libsoup-devel
Recommends:     libwebkitgtk-devel
Recommends:     libwnck-devel
Recommends:     pango-devel
Recommends:     tracker-devel
Recommends:     vte-devel
# Build tools
Recommends:     gnome-common
Recommends:     gnome-doc-utils-devel
Recommends:     gobject-introspection-devel
Recommends:     gtk-doc
Recommends:     intltool
Recommends:     itstool
Recommends:     vala
Recommends:     yelp-tools
Suggests:       python-gobject-devel


%description devel_gnome
GNOME development packages.

%files devel_gnome
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/devel_gnome.txt

%package devel_ide
%pattern_development
Summary:        Integrated Development Environments
Group:          Metapackages
Provides:       pattern() = devel_ide
Provides:       pattern-icon() = pattern-basis-devel
Provides:       pattern-order() = 3260
Requires:       pattern() = devel_basis
# from data/DEVEL-IDE
Recommends:     monodevelop
Suggests:       anjuta


%description devel_ide
Integrated Development Environments.

%files devel_ide
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/devel_ide.txt

%package devel_java
%pattern_development
Summary:        Java Development
Group:          Metapackages
Provides:       pattern() = devel_java
Provides:       pattern-icon() = pattern-basis-devel
Provides:       pattern-order() = 3300
# from data/DEVEL-Java
Recommends:     ant
Recommends:     ant-antlr
Recommends:     ant-apache-bcel
Recommends:     ant-apache-bsf
Recommends:     ant-apache-log4j
Recommends:     ant-apache-oro
Recommends:     ant-apache-regexp
Recommends:     ant-apache-resolver
Recommends:     ant-commons-logging
Recommends:     ant-javadoc
Recommends:     ant-javamail
Recommends:     ant-jdepend
Recommends:     ant-jmf
Recommends:     ant-junit
Recommends:     ant-manual
Recommends:     ant
Recommends:     ant-scripts
Recommends:     ant-swing
Recommends:     ant
Recommends:     log4j
Recommends:     xalan-j2
Recommends:     xerces-j2
Recommends:     xml-commons-apis
Recommends:     xml-commons-resolver
Recommends:     xml-commons-which10
Recommends:     java-1_7_0-openjdk
%ifarch %ix86
Recommends:     icedtea-web
%endif
Recommends:     java-1_5_0-gcj-compat-devel
Suggests:       gnu-jaf
Suggests:       jakarta-commons-beanutils
Suggests:       jakarta-commons-codec
Suggests:       jakarta-commons-collections
Suggests:       jakarta-commons-daemon
Suggests:       jakarta-commons-dbcp
Suggests:       jakarta-commons-digester
Suggests:       jakarta-commons-discovery
Suggests:       jakarta-commons-el
Suggests:       jakarta-commons-fileupload
Suggests:       jakarta-commons-httpclient3
Suggests:       jakarta-commons-lang
Suggests:       jakarta-commons-launcher
Suggests:       jakarta-commons-logging
Suggests:       jakarta-commons-modeler
Suggests:       jakarta-commons-pool
Suggests:       jakarta-commons-validator
Suggests:       javacc
Suggests:       jdepend
Suggests:       mysql-connector-java
# just an editor
Suggests:       jedit
Suggests:       java-1_7_0-openjdk-devel
Suggests:       mx4j
Suggests:       ant-javamail
Suggests:       geronimo-j2ee-1_4-apis


%description devel_java
Tools and libraries for software development using the Java programming language.

%files devel_java
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/devel_java.txt

%package devel_kde
%pattern_development
Summary:        KDE Development
Group:          Metapackages
Provides:       pattern() = devel_kde
Provides:       pattern-icon() = pattern-kde-devel
Provides:       pattern-order() = 3180
Requires:       pattern() = devel_C_C++
Recommends:     pattern() = devel_qt4
# from data/DEVEL-KDE
Recommends:     cmake
Recommends:     kdebase4-workspace-devel
Recommends:     alsa-devel
Recommends:     aspell-devel
Recommends:     avahi-compat-mDNSResponder-devel
Recommends:     cups-devel
Recommends:     cyrus-sasl-devel
Recommends:     doxygen
Recommends:     giflib-devel
Recommends:     icecream
Recommends:     ImageMagick-devel
Recommends:     krb5-devel
Recommends:     libao-devel
Recommends:     libattr-devel
Recommends:     libcurl-devel
Recommends:     libgpgme-devel
Recommends:     libidn-devel
Recommends:     libjpeg62-devel
Recommends:     libmal-devel
Recommends:     libopenssl-devel
Recommends:     libpisock-devel
Recommends:     libpng15-devel
Recommends:     libpng15-compat-devel
Recommends:     libpoppler-devel
Recommends:     libqimageblitz-devel
Recommends:     libqt4-devel
Recommends:     libsmbclient-devel
Recommends:     libsoprano-devel
Recommends:     libtiff-devel
Recommends:     libusb-compat-devel
Recommends:     libxklavier-devel
Recommends:     libxml2-devel
Recommends:     libxslt-devel
Recommends:     NetworkManager-devel
Recommends:     pcre-devel
Recommends:     libqt4-devel-doc
Recommends:     libSDL-devel
Recommends:     sqlite3-devel
Recommends:     strigi-devel
Recommends:     wv2-devel
Recommends:     libbz2-devel
Recommends:     ggz-client-libs-devel
Recommends:     libqca2-devel
Recommends:     libavahi-devel
Recommends:     libavahi-qt4-devel
Recommends:     libopenexr-devel
Recommends:     enchant-devel
Recommends:     fam-devel
Recommends:     libjasper-devel
Recommends:     clucene-core-devel
Recommends:     libpulse-devel
Recommends:     libraw1394-devel
Recommends:     python-devel
Recommends:     libical-devel
Recommends:     libmysqlclient-devel
Recommends:     libraptor-devel
Recommends:     openldap2-devel
Recommends:     gettext-tools
Recommends:     libgpod-devel
Recommends:     libmtp-devel
Recommends:     loudmouth-devel
Recommends:     libdvdread-devel
Recommends:     libgphoto2-devel
Recommends:     gstreamer-0_10-devel
Recommends:     libxine-devel
Recommends:     cups-devel
Recommends:     bluez-devel
Recommends:     libpoppler-qt4-devel
Recommends:     libkexiv2-devel
Recommends:     giflib-devel
Suggests:       libkdcraw-devel
Suggests:       libkipi-devel
Suggests:       freeglut-devel
Suggests:       graphviz
Suggests:       icecream-monitor
Suggests:       kdebase4-workspace-devel
Suggests:       libkdepimlibs4-devel
Suggests:       libkdegames-devel
Suggests:       libkmahjongg-devel
Suggests:       libvisual-devel
Suggests:       meanwhile-devel
Suggests:       net-snmp-devel
Suggests:       mono-kde4
Suggests:       ruby-kde4
Suggests:       python-kdebase4
Suggests:       libkonq-devel
Suggests:       antlr-devel
Suggests:       aqbanking-devel
Suggests:       audiofile-devel
Suggests:       avogadro-devel
Suggests:       cdparanoia-devel
Suggests:       chmlib-devel
Suggests:       cln-devel
Suggests:       commoncpp2-devel
Suggests:       fftw3-devel
Suggests:       file-devel
Suggests:       flac-devel
Suggests:       fribidi-devel
Suggests:       getdata-devel
Suggests:       ghostscript-devel
Suggests:       glew-devel
Suggests:       gpsd-devel
Suggests:       grantlee-devel
Suggests:       GraphicsMagick-devel
Suggests:       gsl-devel
Suggests:       gwenhywfar-devel
Suggests:       help2man
Suggests:       htmldoc
Suggests:       hunspell-devel
Suggests:       hwinfo-devel
Suggests:       kate-devel
Suggests:       kdesdk4-scripts
Suggests:       kdevelop4-devel
Suggests:       kdevelop4-pg-qt-devel
Suggests:       lensfun-devel
Suggests:       libalkimia-devel
Suggests:       libarchive-devel
Suggests:       libassuan-devel
Suggests:       libbluedevil-devel
Suggests:       libbonoboui-devel
Suggests:       libcap-ng-devel
Suggests:       libcdio-devel
Suggests:       libcfitsio-devel
Suggests:       libcppunit-devel
Suggests:       libdbusmenu-qt-devel
Suggests:       libdjvulibre-devel
Suggests:       libdmtx-devel
Suggests:       libeigen2-devel
Suggests:       libepub-devel
Suggests:       libesd-devel
Suggests:       libexempi-devel
Suggests:       libeXosip2-devel
Suggests:       libfli-devel
Suggests:       libgadu-devel
Suggests:       libgcal-devel
Suggests:       libgmm++-devel
Suggests:       libgnomecanvas-devel
Suggests:       libgnome-devel
Suggests:       libgudev-1_0-devel
Suggests:       libicu-devel
Suggests:       libindi-devel
Suggests:       libiodbc-devel
Suggests:       libiw-devel
Suggests:       libjack-devel
Suggests:       libkcddb4-devel
Suggests:       libkcompactdisc4-devel
Suggests:       libkdeedu4-devel
Suggests:       libkdevplatform-devel
Suggests:       libkface-devel
Suggests:       libkgeomap-devel
Suggests:       libksane-devel
Suggests:       libksuseinstall-devel
Suggests:       libktoblzcheck1-devel
Suggests:       libktorrent-devel
Suggests:       liblastfm-devel
Suggests:       liblazy-devel
Suggests:       liblcms2-devel
Suggests:       liblqr-devel
Suggests:       libmediawiki1
Suggests:       libmediawiki-devel
Suggests:       libmms-devel
Suggests:       libmono-2_0-devel
Suggests:       libmpcdec-devel
Suggests:       libmsn-devel
Suggests:       libmusicbrainz3-devel
Suggests:       libmusicbrainz-devel
Suggests:       libmygpo-qt-devel
Suggests:       libnetcdf-devel
Suggests:       libnetpbm-devel
Suggests:       libnl-1_1-devel
Suggests:       libnova-devel
Suggests:       libofx-devel
Suggests:       libogg-devel
Suggests:       liboil-devel
Suggests:       libopenbabel-devel
Suggests:       libotr-devel
Suggests:       libpackagekit-qt2-devel
Suggests:       libpackagekit-qt-devel
Suggests:       libpng12-devel
Suggests:       libpodofo-devel
Suggests:       libpqxx-devel
Suggests:       libpth-devel
Suggests:       libqalculate-devel
Suggests:       libqjson-devel
Suggests:       libqscintilla-devel
Suggests:       libraw-devel
Suggests:       librcps-devel
Suggests:       libsamplerate-devel
Suggests:       libselinux-devel
Suggests:       libsepol-devel
Suggests:       libsigc++2-devel
Suggests:       libsmokegen-devel
Suggests:       libsmokekde-devel
Suggests:       libsmokeqt-devel
Suggests:       libsndfile-devel
Suggests:       libspectre-devel
Suggests:       libspeechd-devel
Suggests:       libssh-devel
Suggests:       libtag-devel
Suggests:       libtheora-devel
Suggests:       libtidy-0_99-0-devel
Suggests:       libtunepimp-devel
Suggests:       libunicap-devel
Suggests:       libusbmuxd-devel
Suggests:       libv4l-devel
Suggests:       LibVNCServer-devel
Suggests:       libvorbis-devel
Suggests:       libwbxml2-devel
Suggests:       libwpd-devel
Suggests:       libwpg-devel
Suggests:       libxml++-devel
Suggests:       libyaz-devel
Suggests:       libzip-devel
Suggests:       linphone-devel
Suggests:       lirc-devel
Suggests:       lua-devel
Suggests:       marble-devel
Suggests:       mhash-devel
Suggests:       mono-qt4-devel
Suggests:       ocaml
Suggests:       ocaml-facile
Suggests:       okteta-devel
Suggests:       openconnect-devel
Suggests:       opencv-devel
Suggests:       openslp-devel
Suggests:       opensp-devel
Suggests:       pciutils-devel
Suggests:       perl-qt4-devel
Suggests:       postgresql-devel
Suggests:       python-kde4-devel
Suggests:       python-sip-devel
Suggests:       qhull-devel
Suggests:       qoauth-devel
Suggests:       qrencode-devel
Suggests:       QtZeitgeist-devel
Suggests:       qwt-devel
Suggests:       ruby-qt4-devel
Suggests:       sane-backends-devel
Suggests:       scons
Suggests:       speex-devel
Suggests:       subversion-devel
Suggests:       taglib-extras-devel
Suggests:       utempter-devel
Suggests:       valgrind-devel
Suggests:       xz-devel


%description devel_kde
KDE development packages.

%files devel_kde
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/devel_kde.txt

%package devel_kernel
%pattern_development
Summary:        Linux Kernel Development
Group:          Metapackages
Provides:       pattern() = devel_kernel
Provides:       pattern-icon() = pattern-basis-devel
Provides:       pattern-order() = 3320
Requires:       pattern() = devel_basis
# from data/DEVEL-Kernel
Recommends:     kernel-source
# bnc#582415
Recommends:     ctags
Recommends:     diffstat
Recommends:     git-core
Recommends:     indent
Recommends:     patchutils
Recommends:     quilt
Recommends:     gitk
Recommends:     git-email
Recommends:     kernel-syms
Suggests:       kernel-debug
Suggests:       gitk
Suggests:       kernel-docs
Suggests:       cscope


%description devel_kernel
Tools for Linux kernel development.

%files devel_kernel
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/devel_kernel.txt

%package devel_mono
%pattern_development
Summary:        .NET Development
Group:          Metapackages
Provides:       pattern() = devel_mono
Provides:       pattern-icon() = pattern-mono
Provides:       pattern-order() = 3220
# from data/DEVEL-Mono
Recommends:     mono-core
Recommends:     mono-devel
Recommends:     monodevelop
Recommends:     apache2-mod_mono
Recommends:     boo
Recommends:     dbus-1-mono
Recommends:     gsf-sharp
Recommends:     gtk-sharp2-complete
Recommends:     gtk-sharp2-doc
Recommends:     gtk-sharp2-gapi
Recommends:     gtksourceview-sharp2
Recommends:     ikvm
Recommends:     mono-basic
Recommends:     mono-data
Recommends:     mono-data-oracle
Recommends:     mono-data-postgresql
Recommends:     mono-data-sqlite
Recommends:     monodoc-core
Recommends:     mono-extras
Recommends:     mono-locale-extras
Recommends:     mono-nunit
Recommends:     mono-tools
Recommends:     mono-web
Recommends:     mono-winforms
Suggests:       mono-debugger
Suggests:       rsvg2-sharp
Suggests:       vte016-sharp


%description devel_mono
Tools and libraries for .NET development using Mono.

%files devel_mono
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/devel_mono.txt

%package devel_perl
%pattern_development
Summary:        Perl Development
Group:          Metapackages
Provides:       pattern() = devel_perl
Provides:       pattern-icon() = pattern-basis-devel
Provides:       pattern-order() = 3340
# from data/DEVEL-Perl
Recommends:     perlref
Recommends:     perl-doc
Suggests:       perl-Algorithm-Diff
Suggests:       perl-AppConfig
Suggests:       perl-Authen-SASL
Suggests:       perl-Authen-SASL-Cyrus
Suggests:       perl-BIND-Conf_Parser
Suggests:       perl-BSD-Resource
Suggests:       perl-CDDB_get
Suggests:       perl-CGI-Application
Suggests:       perl-Carp-Assert
Suggests:       perl-Class-Accessor
Suggests:       perl-Class-Data-Inheritable
Suggests:       perl-Class-Date
Suggests:       perl-Class-MethodMaker
Suggests:       perl-Class-Multimethods
Suggests:       perl-Class-WhiteHole
Suggests:       perl-Config-General
Suggests:       perl-Config-IniFiles
Suggests:       perl-Convert-TNEF
Suggests:       perl-Convert-UUlib
Suggests:       perl-Crypt-Blowfish
Suggests:       perl-Crypt-CBC
Suggests:       perl-Crypt-SSLeay
Suggests:       perl-DBD-CSV
Suggests:       perl-DBD-ODBC
Suggests:       perl-DBD-Pg
Suggests:       perl-DBD-SQLite
Suggests:       perl-DBD-XBase
Suggests:       perl-DBD-mysql
Suggests:       perl-Devel-CoreStack
Suggests:       perl-Devel-Symdump
Suggests:       perl-Encode-HanExtra
Suggests:       perl-Encode-JIS2K
Suggests:       perl-ExtUtils-F77
Suggests:       perl-File-MMagic
Suggests:       perl-File-Tail
Suggests:       perl-Font-AFM
Suggests:       perl-GD
Suggests:       perl-GD-Graph3d
Suggests:       perl-GDGraph
Suggests:       perl-GDTextUtil
Suggests:       perl-Getopt-Mixed
Suggests:       perl-Gtk2
Suggests:       perl-HTML-Clean
Suggests:       perl-HTML-FillInForm
Suggests:       perl-HTML-Format
Suggests:       perl-HTML-SimpleParse
Suggests:       perl-HTML-Template
Suggests:       perl-HTML-Template-Expr
Suggests:       perl-HTML-Template-JIT
Suggests:       perl-HTML-Tree
Suggests:       perl-HTTP-DAV
Suggests:       perl-HTTPS-Daemon
Suggests:       perl-IPC-Run
Suggests:       perl-Image-Size
Suggests:       perl-Inline
Suggests:       perl-Inline-C
Suggests:       perl-Log-Dispatch
Suggests:       perl-Log-Log4perl
Suggests:       perl-MIME-Lite
Suggests:       perl-MLDBM
Suggests:       perl-MLDBM-Sync
Suggests:       perl-Mcrypt
Suggests:       perl-Module-Info
Suggests:       perl-Net-DNS
Suggests:       perl-Net-Daemon
Suggests:       perl-Net-IP
Suggests:       perl-Net-Jabber
Suggests:       perl-Net-Netmask
Suggests:       perl-Net-Server
Suggests:       perl-Net-Telnet
Suggests:       perl-PDL
Suggests:       perl-Params-Validate
Suggests:       perl-Parse-Yapp
Suggests:       perl-PerlMagick
Suggests:       perl-Pod-HtmlPsPdf
Suggests:       perl-PostScript-Simple
Suggests:       perl-Quantum-Superpositions
Suggests:       perl-RPC-XML
Suggests:       perl-SGMLS
Suggests:       perl-SOAP-Lite
Suggests:       perl-SQL-Statement
Suggests:       perl-Set-Crontab
Suggests:       perl-Set-Object
Suggests:       perl-Set-Scalar
Suggests:       perl-Socket6
Suggests:       perl-Template-Toolkit
Suggests:       perl-Text-CSV_XS
Suggests:       perl-Text-DelimMatch
Suggests:       perl-Text-Iconv
Suggests:       perl-Tie-Cache
Suggests:       perl-Time-modules
Suggests:       perl-Unicode-Map8
Suggests:       perl-Unicode-String
Suggests:       perl-XML-LibXML
Suggests:       perl-XML-Simple
Suggests:       perl-XML-Stream
Suggests:       perl-XML-XSLT
Suggests:       perl-YAML 
Suggests:       perl-libxml-perl
Suggests:       perl-Apache-AuthCookie
Suggests:       perl-Apache-AuthNetLDAP
Suggests:       perl-Apache-DBI
Suggests:       perl-Apache-Session
Suggests:       perl-Apache-SessionX
Suggests:       perl-Cairo
Suggests:       perl-Chart
Suggests:       perl-Convert-ASN1
Suggests:       perl-ExtUtils-Depends
Suggests:       perl-ExtUtils-PkgConfig
Suggests:       perl-FileHandle-Unget
Suggests:       perl-File-Type
Suggests:       perl-IO-String
Suggests:       perl-IO-Stty
Suggests:       perl-ldap
Suggests:       perl-ldap-ssl
Suggests:       perl-libconfigfile
Suggests:       perl-Mail-Mbox-MessageParser
Suggests:       perl-MIME-Types
Suggests:       perl-NetAddr-IP
Suggests:       perl-Net-IPv4Addr
Suggests:       perl-Net-SNMP
Suggests:       perl-NKF
Suggests:       perl-PDA-Pilot
Suggests:       perl-SNMP
Suggests:       perl-SVN-Simple
Suggests:       perl-Text-ChaSen
Suggests:       perl-Text-Kakasi
Suggests:       perl-Time-Duration
Suggests:       perl-Time-Period
Suggests:       perl-WeakRef
Suggests:       perl-XML-LibXSLT


%description devel_perl
Tools and libraries for software development using the Perl programming language.

%files devel_perl
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/devel_perl.txt

%package devel_python
%pattern_development
Summary:        Python Development
Group:          Metapackages
Provides:       pattern() = devel_python
Provides:       pattern-icon() = pattern-basis-devel
Provides:       pattern-order() = 3360
# from data/DEVEL-Python
Recommends:     pychecker
Recommends:     python
Recommends:     python-devel
Suggests:       eric
Suggests:       libxml2-python
Suggests:       libxslt-python
Suggests:       python-cairo-devel
Suggests:       python-gnome-devel
Suggests:       python-gobject2-devel
Suggests:       python-gtk-devel
Suggests:       python-ldap
Suggests:       python-qt4
Suggests:       python-wxWidgets
Suggests:       python-xml
Suggests:       treeline
Suggests:       python-dateutil
Suggests:       python-fcgi
Suggests:       python-gdbm
Suggests:       python-httplib2
Suggests:       python-pyOpenSSL
Suggests:       python-opensync
Suggests:       python-pam
Suggests:       python-pygame
Suggests:       python-pyserial
Suggests:       python-Twisted
Suggests:       python-zope.interface


%description devel_python
Tools and libraries for software development using the Python programming language.

%files devel_python
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/devel_python.txt

%package devel_python3
%pattern_development
Summary:        devel_python3
Group:          Metapackages
Provides:       pattern() = devel_python3
Provides:       pattern-icon() = pattern-basis-devel
Provides:       pattern-order() = 3359
# from data/DEVEL-Python3
Recommends:     python3
Recommends:     python3-devel
Suggests:       python3-lxml
Suggests:       python3-pip
Suggests:       python3-Cython
Suggests:       python3-setuptools
Suggests:       python3-requests
Suggests:       python3-pyOpenSSL
Suggests:       python3-pycrypto
Suggests:       python3-simplejson
Suggests:       python3-Sphinx
Suggests:       python3-docutils
Suggests:       python3-Jinja2
Suggests:       python3-coverage
Suggests:       python3-nose


%description devel_python3

%files devel_python3
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/devel_python3.txt

%package devel_qt4
%pattern_development
Summary:        Qt 4 Development
Group:          Metapackages
Provides:       pattern() = devel_qt4
Provides:       pattern-icon() = pattern-basis-devel
Provides:       pattern-order() = 3380
# from data/DEVEL-QT4
Recommends:     libqt4-devel
Recommends:     libqt4-devel-doc
Recommends:     libqt4-sql-sqlite
Recommends:     libQtWebKit-devel
Suggests:       libqt4-sql-mysql
Suggests:       libqt4-sql-postgresql
Suggests:       libqt4-sql-unixODBC
# bnc#515160
Suggests:       qt-creator


%description devel_qt4
Tools and libraries for software development using Qt 4, the latest version of the Qt toolkit.

%files devel_qt4
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/devel_qt4.txt

%package devel_rpm_build
%pattern_development
Summary:        RPM Build Environment
Group:          Metapackages
Provides:       pattern() = devel_rpm_build
Provides:       pattern-icon() = pattern-basis-devel
Provides:       pattern-order() = 3280
Requires:       pattern() = basesystem
# from data/DEVEL-RPM-Build-Environment
Requires:       rpm-build
Requires:       man
Requires:       netcfg
Recommends:     libtool
Suggests:       build
Suggests:       inst-source-utils
Suggests:       libsolv-devel


%description devel_rpm_build
Minimal set of tools and libraries for building packages using the RPM package manager.

%files devel_rpm_build
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/devel_rpm_build.txt

%package devel_ruby
%pattern_development
Summary:        Ruby Development
Group:          Metapackages
Provides:       pattern() = devel_ruby
Provides:       pattern-icon() = pattern-basis-devel
Provides:       pattern-order() = 3420
# from data/DEVEL-Ruby
Requires:       ruby
Requires:       rubygems
Suggests:       ruby-devel
Suggests:       ruby-doc-html
Suggests:       ruby-doc-ri
Suggests:       ruby-examples
Suggests:       ruby-fcgi
Suggests:       rubygem-mysql
Suggests:       rubygem-racc
Suggests:       ruby-test-suite
Suggests:       ruby-tk


%description devel_ruby
Tools and libraries for software development using the Ruby programming language.

%files devel_ruby
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/devel_ruby.txt

%package devel_tcl
%pattern_development
Summary:        Tcl/Tk Development
Group:          Metapackages
Provides:       pattern() = devel_tcl
Provides:       pattern-icon() = pattern-basis-devel
Provides:       pattern-order() = 3480
# from data/DEVEL-Tcl
Recommends:     tcl
Recommends:     tcl-devel
Recommends:     tk
Recommends:     tk-devel
Recommends:     bwidget
Recommends:     expect
Recommends:     frink
Recommends:     itcl
Recommends:     iwidgets
Recommends:     snack
Recommends:     tcllib
Recommends:     tcludp
Recommends:     tclx
Recommends:     tdom
Recommends:     tix
Recommends:     tkcon
Recommends:     tkimg
Recommends:     tktable
Recommends:     tls
# #387771
Recommends:     itcl-devel
Recommends:     itk
Recommends:     expect-devel
# #387771
Recommends:     tclplug
Suggests:       PgTcl
Suggests:       scotty
Suggests:       sqlite3-tcl
Suggests:       vtcl


%description devel_tcl
Tools and libraries for development using Tcl and Tk.

%files devel_tcl
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/devel_tcl.txt

%package devel_web
%pattern_development
Summary:        Web Development
Group:          Metapackages
Provides:       pattern() = devel_web
Provides:       pattern-icon() = pattern-basis-devel
Provides:       pattern-order() = 3440
Requires:       pattern() = lamp_server
# from data/DEVEL-Web
Recommends:     apache2-devel
Suggests:       html-dtd
Suggests:       iso_ent
Suggests:       latex2html
Suggests:       perl-CGI-Application
Suggests:       perl-HTML-Clean
Suggests:       perl-HTML-FillInForm
Suggests:       perl-HTML-Format
Suggests:       perl-HTML-SimpleParse
Suggests:       perl-HTML-Tagset
Suggests:       perl-HTML-Template
Suggests:       perl-HTML-Template-Expr
Suggests:       perl-HTML-Template-JIT
Suggests:       perl-HTML-Tree
Suggests:       perl-HTTP-DAV
Suggests:       perl-HTTPS-Daemon
Suggests:       perl-Pod-HtmlPsPdf
Suggests:       php5
Suggests:       php5-bcmath
Suggests:       php5-bz2
Suggests:       php5-calendar
Suggests:       php5-ctype
Suggests:       php5-curl
Suggests:       php5-dba
Suggests:       php5-devel
Suggests:       php5-dom
Suggests:       php5-exif
Suggests:       php5-fastcgi
Suggests:       php5-ftp
Suggests:       php5-gd
Suggests:       php5-gettext
Suggests:       php5-gmp
Suggests:       php5-iconv
Suggests:       php5-imap
Suggests:       php5-ldap
Suggests:       php5-mbstring
Suggests:       php5-mcrypt
Suggests:       php5-mysql
Suggests:       php5-odbc
Suggests:       php5-openssl
Suggests:       php5-pear
Suggests:       php5-pgsql
Suggests:       php5-shmop
Suggests:       php5-snmp
Suggests:       php5-sockets
Suggests:       php5-sysvsem
Suggests:       php5-sysvshm
Suggests:       php5-tidy
Suggests:       php5-wddx
Suggests:       php5-xsl
Suggests:       php5-zlib
Suggests:       tidy
Suggests:       xhtml-dtd
Suggests:       xmlcharent
Suggests:       apache2-worker
Suggests:       apache2-mod_tidy 
Suggests:       kfilereplace
Suggests:       kimagemapeditor
Suggests:       klinkstatus
Suggests:       kde3-quanta
Suggests:       kompozer
Suggests:       tomcat6
Suggests:       tomcat6-admin-webapps
Suggests:       tomcat6-webapps
Suggests:       html2text


%description devel_web
Tools and libraries for Web application development.

%files devel_web
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/devel_web.txt

%package devel_yast
%pattern_development
Summary:        YaST Development
Group:          Metapackages
Provides:       pattern() = devel_yast
Provides:       pattern-icon() = pattern-basis-devel
Provides:       pattern-order() = 3460
# from data/DEVEL-YaST
Recommends:     yast2-devtools
Recommends:     yast2-testsuite
# Bug 304645 gives the list below:
Recommends:     yast2-pkg-bindings-devel-doc
Recommends:     yast2-core-devel
Recommends:     yast2-devel-doc
Recommends:     yast2-installation-devel-doc
Recommends:     yast2-network-devel-doc
Recommends:     yast2-nis-server-devel-doc
Recommends:     yast2-printer-devel-doc
Recommends:     yast2-storage-devel
Recommends:     yast2-perl-bindings
Recommends:     yast2-python-bindings
Recommends:     yast2-ruby-bindings
Recommends:     subversion
Recommends:     libzypp-devel
Recommends:     yast2-libyui-devel
Recommends:     yast2-ycp-ui-bindings-devel
Recommends:     libyui-qt-devel
Recommends:     libyui-ncurses-devel
Suggests:       inst-source-utils
Suggests:       createrepo


%description devel_yast
Tools and libraries for developing YaST modules, the setup and configuration tool for openSUSE.

%files devel_yast
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/devel_yast.txt

%package dhcp_dns_server
%pattern_serverfunctions
Summary:        DHCP and DNS Server
Group:          Metapackages
Provides:       pattern() = dhcp_dns_server
Provides:       pattern-icon() = yast-dns-server
Provides:       pattern-order() = 3040
Requires:       pattern() = basesystem
# from data/DHCP_DNS
Recommends:     bind
Recommends:     dhcp-relay
Recommends:     dhcp-server
Recommends:     dhcp-tools
Recommends:     yast2-dhcp-server
Recommends:     yast2-dns-server
Recommends:     bind-doc


%description dhcp_dns_server
Software to set up a server for the Dynamic Host Configuration Protocol (DHCP) and the Domain Name System (DNS) services. DHCP provides configuration parameters to client computers to integrate them into a network, whereas DNS delivers information associated with domain names, in particular, the IP address.

%files dhcp_dns_server
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/dhcp_dns_server.txt

%package directory_server
%pattern_serverfunctions
Summary:        Directory Server (LDAP)
Group:          Metapackages
Provides:       pattern() = directory_server
Provides:       pattern-icon() = yast-ldap-server
Provides:       pattern-order() = 3060
Requires:       pattern() = basesystem
# from data/LDAP_SERVER
Recommends:     nss_ldap
Recommends:     openldap2
Recommends:     pam_ldap
Recommends:     yast2-ldap-server
%ifarch x86_64
Recommends:     nss_ldap-32bit
Recommends:     pam_ldap-32bit
%endif


%description directory_server
Software to set up a directory server with OpenLDAP. The Lightweight Directory Access Protocol (LDAP) is used to access online directory services. 

%files directory_server
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/directory_server.txt

%package e17
%pattern_graphicalenvironments
Summary:        Enlightment
Group:          Metapackages
Provides:       pattern() = e17
Provides:       pattern-icon() = pattern-e17
Provides:       pattern-order() = 1350
Requires:       pattern() = x11
Recommends:     pattern() = multimedia
Recommends:     pattern() = imaging
# from data/E17-BASIS
Requires:       e17
Recommends:     efreet
Recommends:     elementary
Recommends:     terminology
Recommends:     desktop-branding

# from data/COMMON-DESKTOP-OPT
# packages a GTK application
Recommends:     gutenprint
# MAYBE later lsb-graphics
Recommends:     icedtea-web
# give net shares
Recommends:     samba
# needs python-qt4, see#649280#14
Suggests:       hplip


%description e17
Enlightment Window Manager and applications

%files e17
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/e17.txt

%package enhanced_base
%pattern_basetechnologies
Summary:        Enhanced Base System
Group:          Metapackages
Provides:       pattern() = enhanced_base
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1060
Requires:       pattern() = basesystem
Recommends:     pattern() = apparmor
Recommends:     pattern() = yast2_basis
Recommends:     pattern() = enhanced_base_opt
Recommends:     pattern() = sw_management
# from data/ENHANCED-BASIS
# having a ftp command line client is good for moving log files
Recommends:     lukemftp
# needed for detecting software raid - required by yast2-storage too
Recommends:     mdadm
# #303857
Recommends:     kpartx
Recommends:     dmraid
# man by default (#304687)
Recommends:     man
# fuser (psmisc) by default (#304694)
Recommends:     psmisc
# firewall by default
Recommends:     SuSEfirewall2
# getfacl and setfacl
Recommends:     acl
# getattr and setattr
Recommends:     attr
# compressor is interesting
Recommends:     bzip2
# printing considered cool
Recommends:     cups-client
Recommends:     curl
Recommends:     cyrus-sasl-gssapi
Recommends:     cyrus-sasl-crammd5
Recommends:     cyrus-sasl-digestmd5
Recommends:     cyrus-sasl-plain
# bnc#430895
# cyrus-sasl-saslauthd
Recommends:     db-utils
Recommends:     diffutils
Recommends:     ethtool
Recommends:     e2fsprogs
Recommends:     eject
Recommends:     file
Recommends:     fillup
Recommends:     findutils
# /bin/ip considered useful
Recommends:     iproute2
# ping is required for network tests
Recommends:     iputils
# pager
Recommends:     less
# make it bunt
Recommends:     gfxboot
Recommends:     parted
Recommends:     mailx
Recommends:     genisoimage
# we want a ssh server to be available
Recommends:     openssh
Recommends:     perl-base
# we rely on cron for daily/hourly 
Recommends:     cronie
# create log file tars
Recommends:     tar
Recommends:     wget
# split out of ncurses
Recommends:     ncurses-utils
# we want a branded boot
Recommends:     plymouth-branding-openSUSE
# we want a branded grub2 too #757683
Recommends:     grub2-branding-openSUSE
# #302569
Recommends:     alsa-plugins
# useful for debugging
Recommends:     strace
Recommends:     lsof
# mount NTFS rw
Recommends:     ntfs-3g
# cups server for remote printing queues
Recommends:     cups
# delta rpms are considered cool for updates
Recommends:     deltarpm
Recommends:     autofs
Recommends:     bind-utils
# Make plymouth the new default bootsplash
Recommends:     plymouth
Recommends:     cyrus-sasl
Recommends:     dosfstools
Recommends:     gawk
Recommends:     gettext-runtime
Recommends:     glibc-locale
Recommends:     gpart
Recommends:     gpg2
Recommends:     gpm
Recommends:     hdparm
Recommends:     ifplugd
Recommends:     info
Recommends:     libatm1
Recommends:     master-boot-code
Recommends:     syslinux
Recommends:     netcat-openbsd
Recommends:     nfs-client
Recommends:     nfsidmap
Recommends:     nscd
Recommends:     ntfsprogs
Recommends:     openldap2-client
Recommends:     openslp
Recommends:     pciutils
%ifarch %ix86 x86_64
Recommends:     dmidecode
Recommends:     acpica
%endif
%ifarch %ix86 x86_64
Recommends:     microcode_ctl
%endif
Recommends:     pm-utils
Recommends:     postfix
Recommends:     pm-profiler
Recommends:     ppp
Recommends:     pptp
Recommends:     recode
Recommends:     release-notes-openSUSE
Recommends:     smp_utils
Recommends:     sg3_utils
Recommends:     lsscsi
Recommends:     sudo
Recommends:     timezone
Recommends:     udev
Recommends:     utempter
Recommends:     wireless-tools
# Our editor of choice
Recommends:     vim
Recommends:     xinetd
Recommends:     ntp
Recommends:     yp-tools
Recommends:     ypbind
%ifarch ppc
Recommends:     lilo
Recommends:     pdisk
Recommends:     powerpc32
# #303737
Recommends:     mouseemu
%endif
%ifarch x86_64
Recommends:     linux32
%endif
%ifarch x86_64
Recommends:     glibc-32bit
Recommends:     glibc-locale-32bit
Recommends:     numactl
%endif
# #375103
Recommends:     cifs-utils
# lsusb is good for debugging USB devices - #401593
Recommends:     usbutils
Recommends:     cryptsetup
# Bug 424707 - Feature "Command not found" for openSUSE by default
Recommends:     scout
Recommends:     command-not-found
Recommends:     lsb-release
# autoconfig new printers - bnc#808014
Recommends:     udev-configure-printer
Suggests:       reiserfs
# #594778
Suggests:       tmpwatch


%description enhanced_base
This is the enhanced base runtime system with lots of convenience packages.

%files enhanced_base
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/enhanced_base.txt

%package enhanced_base_opt
%pattern_basetechnologies
Summary:        Enhanced Base System
Group:          Metapackages
Provides:       pattern() = enhanced_base_opt
Provides:       pattern-icon() = yast-software
Provides:       pattern-order() = 1040
Provides:       pattern-extends() = enhanced_base
# from data/ENHANCED-BASIS-OPT
Recommends:     at
Recommends:     bc
Recommends:     bootcycle
Recommends:     cracklib-dict-full
Recommends:     OpenPrintingPPDs
Recommends:     dos2unix
Recommends:     ed
Recommends:     finger
# 304995
# fbset
Recommends:     groff
Recommends:     initviocons
%ifarch ppc
Recommends:     hfsutils
%endif
# Current systems suffer from entropy starvation
%ifarch %ix86 x86_64
Recommends:     haveged
%endif
Recommends:     irqbalance
Recommends:     joe
Recommends:     ksh
Recommends:     ksymoops
Recommends:     man-pages
Recommends:     man-pages-posix
Recommends:     manufacturer-PPDs
%ifarch x86_64
Recommends:     mcelog
%endif
Recommends:     mpt-status
Recommends:     pax
Recommends:     perl-TermReadLine-Gnu
Recommends:     prctl
Recommends:     procinfo
Recommends:     procmail
Recommends:     providers
Recommends:     rsync
Recommends:     sash
Recommends:     screen
Recommends:     setserial
Recommends:     sharutils
Recommends:     smartmontools
Recommends:     strace
Recommends:     tcpdump
Recommends:     tcsh
Recommends:     telnet
Recommends:     terminfo
Recommends:     vlan
Recommends:     w3m
Recommends:     wol
Recommends:     zisofs-tools
Recommends:     zsh
Suggests:       acpid
Suggests:       xz
Suggests:       zip
Suggests:       unzip
Suggests:       cpupower
Suggests:       delayacct-utils
Suggests:       hfsutils
Suggests:       jfsutils
Suggests:       ocfs2-tools
Suggests:       rsh
Suggests:       xfsprogs
Suggests:       smpppd
Suggests:       lynx
Suggests:       w3m-el
# #373195
Suggests:       checkinstall
Suggests:       pwgen
# delta apply
Suggests:       xdelta
# needed as soon as you want to do kerberos authentication
Suggests:       cyrus-sasl-gssapi
# tool for xfs
Suggests:       xfsdump
# #393589
Suggests:       open-iscsi
# #437252
Suggests:       pam_ssh
# for old installs
Suggests:       lilo
# used by yast2-iscsi-server
Suggests:       tgt
# DELL computers mainly #403270, but #441079
Suggests:       biosdevname
# bnc#388570
Suggests:       kerneloops
# #754959
%ifarch %ix86 x86_64
Suggests:       hyper-v
%endif
# alternative boot loaders
Suggests:       elilo
Suggests:       efibootmgr
# debugging boot
Suggests:       systemd-analyze


%description enhanced_base_opt
This is the enhanced base runtime system with lots of convenience packages.

%files enhanced_base_opt
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/enhanced_base_opt.txt

%package file_server
%pattern_serverfunctions
Summary:        File Server
Group:          Metapackages
Provides:       pattern() = file_server
Provides:       pattern-icon() = yast-nfs_server
Provides:       pattern-order() = 2900
Requires:       pattern() = basesystem
# from data/FILE-SERVER
Recommends:     nfsidmap
Recommends:     nfs-kernel-server
Recommends:     samba
Recommends:     yast2-nfs-server
Recommends:     yast2-samba-server
Recommends:     vsftpd
Recommends:     samba-client
Recommends:     samba-winbind
Recommends:     tftp
Recommends:     yast2-ftp-server
Recommends:     yast2-tftp-server
Suggests:       atftp


%description file_server
File services to host files so that they may be accessed or retrieved by other computers on the same network. This includes the FTP, SMB, and NFS protocols.

%files file_server
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/file_server.txt

%package fonts
%pattern_graphicalenvironments
Summary:        Fonts
Group:          Metapackages
Provides:       pattern() = fonts
Provides:       pattern-icon() = yast-x11
Provides:       pattern-order() = 1740
Recommends:     pattern() = fonts_opt
# from data/FONTS
Recommends:     ghostscript-fonts-std
Recommends:     xorg-x11-fonts-core
Recommends:     dejavu
Recommends:     ifnteuro
Recommends:     liberation-fonts
# needed for instsys
Suggests:       IPAGothic
Suggests:       IPAMincho
Suggests:       IPAPGothic
Suggests:       IPAPMincho
#IPAUIGothic
Suggests:       bitstream-vera


%description fonts
Base fonts and font configuration.

%files fonts
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/fonts.txt

%package fonts_opt
%pattern_graphicalenvironments
Summary:        Fonts
Group:          Metapackages
Provides:       pattern() = fonts_opt
Provides:       pattern-icon() = yast-x11
Provides:       pattern-order() = 1720
Provides:       pattern-extends() = fonts
# from data/FONTS-OPT
Recommends:     efont-unicode
Recommends:     ghostscript-fonts-other
Recommends:     intlfnts
Recommends:     xorg-x11-fonts
Recommends:     droid-fonts


%description fonts_opt
Base fonts and font configuration.

%files fonts_opt
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/fonts_opt.txt

%package games
%pattern_desktopfunctions
Summary:        Games
Group:          Metapackages
Provides:       pattern() = games
Provides:       pattern-icon() = yast-joystick
Provides:       pattern-order() = 1900
Requires:       pattern() = x11
# from data/GAMES
Suggests:       frozen-bubble
Suggests:       armagetron
Suggests:       circuslinux
Suggests:       csmash
Suggests:       solarwolf


%description games
A collection of games.

%files games
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/games.txt

%package gateway_server
%pattern_serverfunctions
Summary:        Internet Gateway
Group:          Metapackages
Provides:       pattern() = gateway_server
Provides:       pattern-icon() = yast-dsl
Provides:       pattern-order() = 3020
Requires:       pattern() = basesystem
# from data/GATEWAY
Recommends:     wireshark
Recommends:     ddclient
Recommends:     fetchmail
Recommends:     ipsec-tools
Recommends:     quagga
Recommends:     radvd
Recommends:     rarpd
Recommends:     squid3
Recommends:     squidGuard
Suggests:       wwwoffle
Suggests:       mirror


%description gateway_server
Software to set up a proxy, firewall, and gateway server, including a virtual private network (VPN) gateway.

%files gateway_server
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/gateway_server.txt

%package gnome
%pattern_graphicalenvironments
Summary:        GNOME Desktop Environment
Group:          Metapackages
Provides:       pattern() = gnome
Provides:       pattern-icon() = pattern-gnome
Provides:       pattern-order() = 1400
Requires:       pattern() = gnome_basis
Recommends:     pattern() = games
Recommends:     pattern() = imaging
Recommends:     pattern() = non_oss
Recommends:     pattern() = gnome_admin
Recommends:     pattern() = gnome_internet
Recommends:     pattern() = multimedia
Recommends:     pattern() = office
Recommends:     pattern() = gnome_utilities
# from data/GNOME-DESKTOP
#
# Official upstream
#
# #544192
Recommends:     alacarte
Recommends:     baobab
Recommends:     bijiben
# #302492
Recommends:     brasero
# bnc#366894
Recommends:     caribou
Recommends:     cheese
# #594593
Recommends:     empathy
Recommends:     eog
Recommends:     evince
Recommends:     evolution
Recommends:     file-roller
Recommends:     gcr-viewer
Recommends:     gedit
Recommends:     gnome-bluetooth
Recommends:     gnome-calculator
Recommends:     gnome-contacts
Recommends:     gnome-calculator
Recommends:     gnome-dictionary
Recommends:     gnome-documents
# #554954
Recommends:     gnome-disk-utility
Recommends:     gnome-font-viewer
Recommends:     gnome-maps
Recommends:     gnome-nettool
Recommends:     gnome-screenshot
Recommends:     gnome-system-monitor
# #447627
Recommends:     gnome-user-share
Recommends:     gucharmap
# #399801
Recommends:     mousetweaks
Recommends:     nautilus-sendto
Recommends:     orca
# #545263
Recommends:     seahorse
Recommends:     sushi
Recommends:     totem
Recommends:     totem-browser-plugin
Recommends:     vino
Recommends:     zenity
#
# Packages that really make sense
#
Recommends:     deja-dup
# Tool for advanced configuration of printers
Recommends:     system-config-printer-applet
Recommends:     system-config-printer
# #608156
Recommends:     tracker
Recommends:     tracker-gui
Recommends:     tracker-miner-evolution
#
# Telepathy connection managers
#
Recommends:     telepathy-gabble
Recommends:     telepathy-haze
Recommends:     telepathy-idle
Recommends:     telepathy-salut
Recommends:     telepathy-sofiasip
Suggests:       dasher
Suggests:       gconf-editor
Suggests:       gnome-backgrounds
# bnc#698250
Suggests:       gnome-color-manager


%description gnome
The GNOME desktop environment is an intuitive and attractive desktop for users.

%files gnome
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/gnome.txt

%package gnome_admin
%pattern_gnomedesktop
Summary:        GNOME Administration Tools
Group:          Metapackages
Provides:       pattern() = gnome_admin
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 2040
Provides:       pattern-extends() = gnome
Requires:       pattern() = x11
Requires:       pattern() = basesystem
# from data/GNOME-ADMIN
Recommends:     alacarte
# bnc#372207
Recommends:     vinagre


%description gnome_admin
Administration Tools e.g. for desktop lockdown

%files gnome_admin
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/gnome_admin.txt

%package gnome_basis
%pattern_graphicalenvironments
Summary:        GNOME Base System
Group:          Metapackages
Provides:       pattern() = gnome_basis
Provides:       pattern-icon() = pattern-gnome
Provides:       pattern-order() = 1440
Requires:       pattern() = x11
Requires:       pattern() = basesystem
Recommends:     pattern() = gnome_basis_opt
# from data/GNOME-BASIS
Requires:       gdm
Requires:       gnome-session
#
# Default sessions
# - Put in Recommends for now, to make sure the livecd will always build; but
#   ideally, should be in Requires
# - We also we explicitly put the packages required by those sessions, in case
#   gnome-session-*-session is not installable, to make sure the livecd is
#   somehow a bit usable
#
Recommends:     gnome-session-default-session
Recommends:     gnome-session-fallback-session
# default
Recommends:     gnome-settings-daemon
Recommends:     gnome-shell
#
# Low-level parts that we need
#
# bnc#430161
Recommends:     NetworkManager
Recommends:     dbus-1-x11
Recommends:     desktop-file-utils
# we want useful bug reports
Recommends:     gdb
Recommends:     gpg2
Recommends:     gpgme
Recommends:     input-utils
Recommends:     polkit-default-privs
Recommends:     samba
Recommends:     susehelp
#
# Branding
#
# #591535
Recommends:     gconf2-branding-openSUSE
Recommends:     gdm-branding-openSUSE
Recommends:     gio-branding-openSUSE
Recommends:     gnome-control-center-branding-openSUSE
Recommends:     gnome-menus-branding-openSUSE
Recommends:     gnome-panel-branding-openSUSE
Recommends:     gtk2-branding-openSUSE
Recommends:     gtk3-branding-openSUSE
Recommends:     hicolor-icon-theme-branding-openSUSE
Recommends:     libsocialweb-branding-openSUSE
Recommends:     desktop-branding
#
# Now the real packages
#
# #332596
Recommends:     gnome-keyring-pam
Recommends:     at-spi2-core
Recommends:     canberra-gtk-play
Recommends:     gnome-control-center
Recommends:     gnome-user-docs
Recommends:     gnome-icon-theme
Recommends:     gnome-icon-theme-extras
Recommends:     gnome-icon-theme-symbolic
Recommends:     gnome-keyring
Recommends:     gnome-menus
Recommends:     gnome-power-manager
Recommends:     gnome-screensaver
Recommends:     gnome-terminal
Recommends:     nautilus
Recommends:     NetworkManager-gnome
Recommends:     shared-mime-info
Recommends:     tango-icon-theme
Recommends:     xkeyboard-config
Recommends:     yelp
# Pulseaudio is the default sound server
Recommends:     pulseaudio-module-bluetooth
Recommends:     pulseaudio-module-gconf
Recommends:     pulseaudio-module-lirc
Recommends:     pulseaudio-module-x11
Recommends:     pulseaudio-module-zeroconf
Recommends:     pulseaudio-utils
# #509829
Recommends:     xdg-user-dirs-gtk
# we need something for xdg-su
Recommends:     libgnomesu

# from data/COMMON-DESKTOP
Recommends:     droid-fonts
Recommends:     MozillaFirefox
Recommends:     desktop-data-openSUSE
Recommends:     avahi
# bnc#508120
Recommends:     xdg-user-dirs
# bnc#598884
Suggests:       moonlight-plugin
# metalink downloader
Suggests:       aria2


%description gnome_basis
Base packages for the GNOME desktop environment.

%files gnome_basis
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/gnome_basis.txt

%package gnome_basis_opt
%pattern_graphicalenvironments
Summary:        GNOME Base System
Group:          Metapackages
Provides:       pattern() = gnome_basis_opt
Provides:       pattern-icon() = pattern-gnome
Provides:       pattern-order() = 1420
Provides:       pattern-extends() = gnome_basis
Requires:       pattern() = x11
Requires:       pattern() = basesystem
# from data/GNOME-BASIS-OPT
# #394406
Recommends:     dynamic-wallpaper-branding-openSUSE

# from data/COMMON-DESKTOP-OPT
# packages a GTK application
Recommends:     gutenprint
# MAYBE later lsb-graphics
Recommends:     icedtea-web
# give net shares
Recommends:     samba
# needs python-qt4, see#649280#14
Suggests:       hplip


%description gnome_basis_opt
Base packages for the GNOME desktop environment.

%files gnome_basis_opt
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/gnome_basis_opt.txt

%package gnome_games
%pattern_gnomedesktop
Summary:        GNOME Games
Group:          Metapackages
Provides:       pattern() = gnome_games
Provides:       pattern-icon() = pattern-gnome
Provides:       pattern-order() = 2100
Provides:       pattern-extends() = games
Supplements:    packageand(patterns-openSUSE-gnome:patterns-openSUSE-games)
# from data/GNOME-Games
Recommends:     aisleriot
Recommends:     gnome-games-recommended
Recommends:     phalanx
Suggests:       gnome-games-extra-data
Suggests:       gnuchess


%description gnome_games
GNOME Games

%files gnome_games
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/gnome_games.txt

%package gnome_ide
%pattern_gnomedesktop
Summary:        GNOME Integrated Development Environment
Group:          Metapackages
Provides:       pattern() = gnome_ide
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 2060
Provides:       pattern-extends() = devel_ide
Supplements:    packageand(patterns-openSUSE-gnome:patterns-openSUSE-devel_ide)
# from data/GNOME-IDE
Recommends:     anjuta
Recommends:     devhelp
Recommends:     glade
Suggests:       accerciser
Suggests:       anjuta-extras
Suggests:       ghex
Suggests:       giggle
Suggests:       gitg
Suggests:       gnome-devel-docs
Suggests:       meld
Suggests:       nemiver


%description gnome_ide
Development under GNOME

%files gnome_ide
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/gnome_ide.txt

%package gnome_imaging
%pattern_gnomedesktop
Summary:        GNOME Graphics
Group:          Metapackages
Provides:       pattern() = gnome_imaging
Provides:       pattern-icon() = package_graphics
Provides:       pattern-order() = 2140
Provides:       pattern-extends() = imaging
Supplements:    packageand(patterns-openSUSE-gnome:patterns-openSUSE-imaging)
Requires:       pattern() = gnome_basis
Recommends:     pattern() = gnome_imaging_opt
# from data/GNOME-IMAGE
#
# Official upstream
#
Recommends:     eog
#
# Packages that really make sense
#
Recommends:     shotwell
Recommends:     simple-scan
Suggests:       f-spot
Suggests:       gnome-photos


%description gnome_imaging
Handling of digital photos and graphics

%files gnome_imaging
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/gnome_imaging.txt

%package gnome_imaging_opt
%pattern_gnomedesktop
Summary:        GNOME Graphics
Group:          Metapackages
Provides:       pattern() = gnome_imaging_opt
Provides:       pattern-icon() = package_graphics
Provides:       pattern-order() = 2120
Provides:       pattern-extends() = imaging
Supplements:    packageand(patterns-openSUSE-gnome:patterns-openSUSE-imaging)
Requires:       pattern() = gnome_basis
# from data/GNOME-IMAGE-OPT
Recommends:     inkscape
Suggests:       dia
Suggests:       gthumb
Suggests:       xsane


%description gnome_imaging_opt
Handling of digital photos and graphics

%files gnome_imaging_opt
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/gnome_imaging_opt.txt

%package gnome_internet
%pattern_gnomedesktop
Summary:        GNOME Internet
Group:          Metapackages
Provides:       pattern() = gnome_internet
Provides:       pattern-icon() = package_network
Provides:       pattern-order() = 2420
Provides:       pattern-extends() = gnome
# from data/GNOME-Internet
#
# Official upstream
#
Recommends:     empathy
Recommends:     evolution
Recommends:     gnome-nettool
#
# Packages that really make sense
#
Recommends:     liferea
# bnc#533580
Recommends:     NetworkManager-openvpn-gnome
Recommends:     NetworkManager-pptp-gnome
Recommends:     NetworkManager-vpnc-gnome
# bnc#530416
Recommends:     transmission-gtk
# bnc#381620
Recommends:     xchat
#
# Official upstream
#
# bnc#366894
Suggests:       ekiga
Suggests:       epiphany
#
# Packages that can make sense
#
Suggests:       frogr
Suggests:       gftp
Suggests:       gwibber
Suggests:       pan
Suggests:       pidgin
Suggests:       smuxi
Suggests:       xchat-gnome


%description gnome_internet
GNOME Internet Applications

%files gnome_internet
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/gnome_internet.txt

%package gnome_laptop
%pattern_gnomedesktop
Summary:        GNOME Laptop
Group:          Metapackages
Provides:       pattern() = gnome_laptop
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 2160
Provides:       pattern-extends() = laptop
Supplements:    packageand(patterns-openSUSE-gnome:patterns-openSUSE-laptop)
Requires:       pattern() = gnome_basis
# from data/GNOME-LAPTOP
Recommends:     gnome-bluetooth
Suggests:       xournal


%description gnome_laptop
GNOME Tools designed specifically for use with laptop computers.

%files gnome_laptop
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/gnome_laptop.txt

%package gnome_multimedia
%pattern_gnomedesktop
Summary:        GNOME Multimedia
Group:          Metapackages
Provides:       pattern() = gnome_multimedia
Provides:       pattern-icon() = pattern-gnome
Provides:       pattern-order() = 2200
Provides:       pattern-extends() = multimedia
Supplements:    packageand(patterns-openSUSE-gnome:patterns-openSUSE-multimedia)
Recommends:     pattern() = gnome_multimedia_opt
# from data/GNOME-Multimedia
#
# GStreamer magic
#
# software.openSUSE.org/codecs      
Recommends:     gstreamer-plugins-base
Recommends:     gstreamer-plugins-bad
Recommends:     gstreamer-plugins-good
Recommends:     gstreamer-plugins-ugly
Recommends:     gstreamer-0_10-plugins-base
Recommends:     gstreamer-0_10-plugins-good
# bnc#445312
Recommends:     gstreamer-0_10-plugins-bad
Recommends:     gstreamer-0_10-plugins-ugly
# bnc#445314
Recommends:     gstreamer-utils
#
# Official upstream
#
Recommends:     totem
Recommends:     totem-browser-plugin
#
# Packages that really make sense
#
Recommends:     gnome-music
Recommends:     rhythmbox
#
# Packages that really make sense
#
Suggests:       paprefs
Suggests:       pavucontrol
Suggests:       pitivi
Suggests:       sound-juicer


%description gnome_multimedia
GNOME Multimedia

%files gnome_multimedia
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/gnome_multimedia.txt

%package gnome_multimedia_opt
%pattern_gnomedesktop
Summary:        GNOME Multimedia
Group:          Metapackages
Provides:       pattern() = gnome_multimedia_opt
Provides:       pattern-icon() = pattern-gnome
Provides:       pattern-order() = 2180
Provides:       pattern-extends() = multimedia
Supplements:    packageand(patterns-openSUSE-gnome:patterns-openSUSE-multimedia)
# from data/GNOME-Multimedia-OPT


%description gnome_multimedia_opt
GNOME Multimedia

%files gnome_multimedia_opt
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/gnome_multimedia_opt.txt

%package gnome_office
%pattern_gnomedesktop
Summary:        GNOME Office
Group:          Metapackages
Provides:       pattern() = gnome_office
Provides:       pattern-icon() = pattern-gnome
Provides:       pattern-order() = 2240
Provides:       pattern-extends() = office
Supplements:    packageand(patterns-openSUSE-gnome:patterns-openSUSE-office)
Requires:       pattern() = gnome_basis
Recommends:     pattern() = gnome_office_opt
# from data/GNOME-Office
#
# Official upstream
#
Recommends:     evolution
#
# Packages that really make sense
#
Recommends:     libreoffice-gnome
Recommends:     libreoffice-icon-theme-tango
Suggests:       abiword
Suggests:       evolution-ews
Suggests:       glabels
Suggests:       gnumeric
Suggests:       pinpoint
Suggests:       planner


%description gnome_office
GNOME Office

%files gnome_office
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/gnome_office.txt

%package gnome_office_opt
%pattern_gnomedesktop
Summary:        GNOME Office
Group:          Metapackages
Provides:       pattern() = gnome_office_opt
Provides:       pattern-icon() = pattern-gnome
Provides:       pattern-order() = 2220
Provides:       pattern-extends() = office
Supplements:    packageand(patterns-openSUSE-gnome:patterns-openSUSE-office)
Requires:       pattern() = gnome_basis
# from data/GNOME-Office-OPT
Recommends:     gnucash
Suggests:       grisbi


%description gnome_office_opt
GNOME Office

%files gnome_office_opt
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/gnome_office_opt.txt

%package gnome_utilities
%pattern_gnomedesktop
Summary:        GNOME Utilities
Group:          Metapackages
Provides:       pattern() = gnome_utilities
Provides:       pattern-icon() = pattern-gnome
Provides:       pattern-order() = 2280
Provides:       pattern-extends() = gnome
Requires:       pattern() = gnome_basis
# from data/GNOME-Utilities
#
# Official upstream
#
Recommends:     baobab
Recommends:     cheese
Recommends:     file-roller
Recommends:     gedit
Recommends:     gnome-calculator
Recommends:     gnome-dictionary
Recommends:     gnome-font-viewer
Recommends:     gnome-screenshot
Recommends:     gucharmap
Recommends:     nautilus-extension-seahorse
Recommends:     nautilus-sendto
Recommends:     seahorse
Recommends:     bijiben
#
# Packages that really make sense
#
Recommends:     gnome-tweak-tool
# thumbnailing in nautilus
Recommends:     gnome-web-photo
Recommends:     gsf-office-thumbnailer
#
# Official upstream
#
Suggests:       dasher
Suggests:       eog-plugins
Suggests:       gedit-plugins
Suggests:       hamster-applet
#
# Packages that can make sense
#
Suggests:       conduit
Suggests:       deja-dup
Suggests:       gnome-do
Suggests:       gtg
# #388570
Suggests:       kerneloops-applet
Suggests:       nautilus-share
Suggests:       pdfmod
Suggests:       synapse
Suggests:       tasque
Suggests:       the-board


%description gnome_utilities
GNOME Utilities

%files gnome_utilities
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/gnome_utilities.txt

%package gnome_yast
%pattern_basetechnologies
Summary:        YaST GNOME User Interfaces
Group:          Metapackages
Provides:       pattern() = gnome_yast
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1260
Provides:       pattern-extends() = yast2_basis
Supplements:    packageand(patterns-openSUSE-gnome:patterns-openSUSE-yast2_basis)
# from data/GNOME-YaST
Requires:       libyui-gtk-pkg
Requires:       yast2-control-center-gnome
# yast modules for the desktop
Recommends:     yast2-scanner
Recommends:     yast2-tv


%description gnome_yast
Graphical YaST user interfaces for the GNOME desktop.

%files gnome_yast
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/gnome_yast.txt

%package imaging
%pattern_desktopfunctions
Summary:        Graphics
Group:          Metapackages
Provides:       pattern() = imaging
Provides:       pattern-icon() = yast-x11
Provides:       pattern-order() = 1860
Requires:       pattern() = x11
Recommends:     pattern() = imaging_opt
# from data/IMAGE
Recommends:     gimp
Suggests:       exiftool


%description imaging
Handling of digital photos and graphics.

%files imaging
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/imaging.txt

%package imaging_opt
%pattern_desktopfunctions
Summary:        Graphics
Group:          Metapackages
Provides:       pattern() = imaging_opt
Provides:       pattern-icon() = package_graphics
Provides:       pattern-order() = 1840
Provides:       pattern-extends() = imaging
Requires:       pattern() = x11
# from data/IMAGE-OPT
Recommends:     AdobeICCProfiles
Recommends:     gimp-help
Suggests:       ufraw
Suggests:       gimp-ufraw
Suggests:       pfstools
Suggests:       pfstmo
Suggests:       pfscalibration
Suggests:       calibre


%description imaging_opt
Handling of digital photos and graphics.

%files imaging_opt
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/imaging_opt.txt

%package kde
%pattern_graphicalenvironments
Summary:        KDE Desktop Environment
Group:          Metapackages
Provides:       pattern() = kde
Provides:       pattern-icon() = pattern-kde4
Provides:       pattern-order() = 1340
Requires:       pattern() = kde4

%description kde
KDE is a powerful free software graphical desktop environment for Linux workstations. It combines ease of use, contemporary functionality, and outstanding graphical design with the technology of the Linux operating system.

%files kde
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/kde.txt

%package kde4
%pattern_graphicalenvironments
Summary:        KDE4 Desktop Environment
Group:          Metapackages
Provides:       pattern() = kde4
Provides:       pattern-icon() = pattern-kde4
Provides:       pattern-order() = 1520
Requires:       pattern() = kde4_basis
Recommends:     pattern() = kde4_internet
Recommends:     pattern() = multimedia
Recommends:     pattern() = office
Recommends:     pattern() = kde4_utilities
Recommends:     pattern() = imaging
Recommends:     pattern() = games
Recommends:     pattern() = non_oss
Provides:       pattern() = kde4
# from data/KDE4-DESKTOP
Recommends:     ark
Recommends:     kcalc
Recommends:     kgpg
Recommends:     ksnapshot
Recommends:     kwalletmanager
Recommends:     mozilla-kde4-integration
Recommends:     kio_mtp
Recommends:     kde4-print-manager
Suggests:       marble
Suggests:       kiosktool
Suggests:       kfloppy
Suggests:       ktimetracker
Suggests:       kalarm
Suggests:       kdeartwork4-wallpapers
Suggests:       kdebase4-wallpapers
Suggests:       krename
Suggests:       vym
Suggests:       kdeartwork4-decorations


%description kde4
KDE is a powerful free software graphical desktop environment for Linux workstations. It combines ease of use, contemporary functionality, and outstanding graphical design with the technology of the Linux operating system.

%files kde4
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/kde4.txt

%package kde4_admin
%pattern_kdedesktop
Summary:        KDE4 Administration Tools
Group:          Metapackages
Provides:       pattern() = kde4_admin
Provides:       pattern-icon() = pattern-kde4
Provides:       pattern-order() = 2320
Requires:       pattern() = kde4_basis
# from data/KDE4-ADMIN
Recommends:     kiosktool


%description kde4_admin
Administration Tools e.g. for desktop lockdown

%files kde4_admin
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/kde4_admin.txt

%package kde4_basis
%pattern_graphicalenvironments
Summary:        KDE4 Base System
Group:          Metapackages
Provides:       pattern() = kde4_basis
Provides:       pattern-icon() = pattern-kde4
Provides:       pattern-order() = 1600
Requires:       pattern() = x11
Requires:       pattern() = basesystem
# from data/KDE4-BASIS
Requires:       plasmoid-folderview
Requires:       kdebase4-session
Requires:       kdebase4-workspace
Requires:       dolphin
Requires:       kwin
Requires:       kwrite
# bnc#541820
Recommends:     susehelp
Recommends:     plasma-nm
Recommends:     plasma-addons
Recommends:     plasmoid-quickaccess
Recommends:     keditbookmarks
Recommends:     konqueror
Recommends:     konsole
Recommends:     kdebase4-nsplugin
Recommends:     kdepim4-wizards
Recommends:     kdenetwork4-filesharing
Recommends:     akregator
Recommends:     kaddressbook
Recommends:     kmail
Recommends:     kontact
Recommends:     korganizer
Recommends:     knotes
Recommends:     pinentry-qt4
Recommends:     kcm_gtk
Recommends:     yast2-control-center-qt
# we want useful bug reports
Recommends:     gdb
Recommends:     kdm
Recommends:     kio_iso
# bnc#430161
Recommends:     polkit-default-privs
# pulseaudio
Recommends:     pulseaudio
Recommends:     pulseaudio-module-bluetooth
Recommends:     pulseaudio-module-jack
Recommends:     pulseaudio-module-lirc
Recommends:     pulseaudio-module-x11
Recommends:     pulseaudio-module-zeroconf
Recommends:     pulseaudio-utils
Recommends:     alsa-plugins-pulse
Recommends:     kdepasswd
Recommends:     kvkbd
# bnc#605509
Recommends:     oxygen-gtk
Recommends:     synaptiks
Recommends:     skanlite
Recommends:     kwebkitpart
Recommends:     soprano-backend-redland
Recommends:     soprano-backend-virtuoso
Recommends:     desktop-branding
Suggests:       qtcurve-gtk2
Suggests:       qtcurve-kde4
# bnc#521177
Suggests:       yakuake
Suggests:       kdepim4
Suggests:       kjots
Suggests:       kepas
Suggests:       yakuake
Suggests:       kcron
Suggests:       ksystemlog

# from data/COMMON-DESKTOP
Recommends:     droid-fonts
Recommends:     MozillaFirefox
Recommends:     desktop-data-openSUSE
Recommends:     avahi
# bnc#508120
Recommends:     xdg-user-dirs
# bnc#598884
Suggests:       moonlight-plugin
# metalink downloader
Suggests:       aria2


%description kde4_basis
Base packages for the KDE4 desktop environment. KDE4 is the next major KDE release.

%files kde4_basis
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/kde4_basis.txt

%package kde4_edutainment
%pattern_kdedesktop
Summary:        KDE4 Education
Group:          Metapackages
Provides:       pattern() = kde4_edutainment
Provides:       pattern-icon() = package_edutainment
Provides:       pattern-order() = 2360
# from data/KDE4-Edutainment
Recommends:     blinken
Recommends:     marble
Recommends:     kalzium
Recommends:     kanagram
Recommends:     kbruch
Recommends:     kalgebra
Recommends:     kgeography
Recommends:     khangman
Recommends:     kig
Recommends:     kiten
Recommends:     klettres
Recommends:     kmplot
Recommends:     kstars
Recommends:     ktouch
Recommends:     parley
Recommends:     kwordquiz
Recommends:     step
Suggests:       kturtle


%description kde4_edutainment
Tools to teach kids with computers

%files kde4_edutainment
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/kde4_edutainment.txt

%package kde4_games
%pattern_kdedesktop
Summary:        KDE4 Games
Group:          Metapackages
Provides:       pattern() = kde4_games
Provides:       pattern-icon() = package_games
Provides:       pattern-order() = 2400
Provides:       pattern-extends() = games
Supplements:    packageand(patterns-openSUSE-kde4:patterns-openSUSE-games)
# from data/KDE4-Games
Recommends:     kpat
Recommends:     kmahjongg
Recommends:     kmines
Recommends:     kreversi
Recommends:     ksudoku
Suggests:       kblocks
Suggests:       katomic
Suggests:       bovo
Suggests:       navalbattle
Suggests:       kblackbox
Suggests:       kbounce
Suggests:       kbreakout
Suggests:       kdiamond
Suggests:       kgoldrunner
Suggests:       kiriki
Suggests:       kjumpingcube
Suggests:       kollision
Suggests:       kolorlines
Suggests:       knetwalk
Suggests:       kolf
Suggests:       konquest
Suggests:       kshisen
Suggests:       ksirk
Suggests:       kspaceduel
Suggests:       ksquares
# COME BACK PLEASE!! ktuberling
Suggests:       kubrick
Suggests:       lskat


%description kde4_games
KDE4 Games

%files kde4_games
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/kde4_games.txt

%package kde4_ide
%pattern_kdedesktop
Summary:        KDE4 Integrated Development Environment
Group:          Metapackages
Provides:       pattern() = kde4_ide
Provides:       pattern-icon() = package_utilities
Provides:       pattern-order() = 2820
Provides:       pattern-extends() = devel_ide
Supplements:    packageand(patterns-openSUSE-kde4:patterns-openSUSE-devel_ide)
# from data/KDE4-IDE
Recommends:     kate
Recommends:     kdbg
Recommends:     kdevelop4
Recommends:     kde4-kapptemplate
Recommends:     lokalize
Recommends:     kde4-l10n-devel
Recommends:     cervisia
Recommends:     kcachegrind
Recommends:     kio_svn
Recommends:     kompare
Recommends:     umbrello
Suggests:       kdevelop4-plugins-php


%description kde4_ide
Development under KDE4

%files kde4_ide
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/kde4_ide.txt

%package kde4_imaging
%pattern_kdedesktop
Summary:        KDE Graphics
Group:          Metapackages
Provides:       pattern() = kde4_imaging
Provides:       pattern-icon() = package_graphics
Provides:       pattern-order() = 2540
Provides:       pattern-extends() = imaging
Supplements:    packageand(patterns-openSUSE-kde4:patterns-openSUSE-imaging)
Requires:       pattern() = kde4_basis
# from data/KDE4-IMAGE
Recommends:     gwenview
Recommends:     digikam
Recommends:     kipi-plugins
# kipi-plugins needs /usr/bin/jpegtran
Recommends:     libjpeg-turbo
Recommends:     okular
Recommends:     kio_kamera
Recommends:     kcolorchooser
Recommends:     kgamma
Recommends:     skanlite
Recommends:     kruler
Suggests:       koffice2-kpresenter
Suggests:       koffice2-krita
Suggests:       kolourpaint


%description kde4_imaging
Handling of digital photos and graphics

%files kde4_imaging
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/kde4_imaging.txt

%package kde4_internet
%pattern_kdedesktop
Summary:        KDE Internet
Group:          Metapackages
Provides:       pattern() = kde4_internet
Provides:       pattern-icon() = package_network
Provides:       pattern-order() = 2560
Provides:       pattern-extends() = kde4
# from data/KDE4-Internet
Recommends:     kdnssd
Recommends:     kget
Recommends:     kopete
# 297684 for these 2
Recommends:     krfb
Recommends:     krdc
Recommends:     konversation
Recommends:     ktorrent
Recommends:     choqok
# bnc#533580 
Recommends:     plasma-nm-openvpn
Recommends:     plasma-nm-vpnc
Recommends:     plasma-nm-pptp
Suggests:       kppp
Suggests:       knode
Suggests:       rekonq


%description kde4_internet
KDE Internet Applications

%files kde4_internet
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/kde4_internet.txt

%package kde4_laptop
%pattern_kdedesktop
Summary:        KDE Laptop
Group:          Metapackages
Provides:       pattern() = kde4_laptop
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 2580
Provides:       pattern-extends() = laptop
Supplements:    packageand(patterns-openSUSE-kde4:patterns-openSUSE-laptop)
Requires:       pattern() = basesystem
# from data/KDE4-LAPTOP
Recommends:     synaptiks


%description kde4_laptop
KDE Tools designed specifically for use with laptop computers.

%files kde4_laptop
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/kde4_laptop.txt

%package kde4_multimedia
%pattern_kdedesktop
Summary:        KDE Multimedia
Group:          Metapackages
Provides:       pattern() = kde4_multimedia
Provides:       pattern-icon() = package_multimedia
Provides:       pattern-order() = 2620
Provides:       pattern-extends() = multimedia
Supplements:    packageand(patterns-openSUSE-kde4:patterns-openSUSE-multimedia)
# from data/KDE4-Multimedia
Recommends:     amarok
Recommends:     k3b
Recommends:     kmix
Recommends:     kscd
Recommends:     kio_audiocd
Recommends:     PackageKit-gstreamer-plugin
Recommends:     kaffeine
Recommends:     phonon-backend-gstreamer-0_10
Recommends:     gstreamer-0_10-plugins-good
Suggests:       krecord
Suggests:       kdemultimedia4-thumbnailers
Suggests:       dragonplayer
Suggests:       juk


%description kde4_multimedia
KDE Multimedia

%files kde4_multimedia
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/kde4_multimedia.txt

%package kde4_office
%pattern_kdedesktop
Summary:        KDE Office
Group:          Metapackages
Provides:       pattern() = kde4_office
Provides:       pattern-icon() = package_wordprocessing
Provides:       pattern-order() = 2700
Provides:       pattern-extends() = office
Supplements:    packageand(patterns-openSUSE-kde4:patterns-openSUSE-office)
# from data/KDE4-Office
Recommends:     libreoffice-kde4
Recommends:     libreoffice-icon-theme-oxygen
Suggests:       scribus


%description kde4_office
KDE Office

%files kde4_office
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/kde4_office.txt

%package kde4_pure
%pattern_basetechnologies
Summary:        KDE System
Group:          Metapackages
Provides:       pattern() = kde4_pure
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 3490
Provides:       pattern-extends() = kde4_basis
Supplements:    packageand(patterns-openSUSE-kde4:patterns-openSUSE-kde4_basis)
Conflicts:      pattern() = gnome
# from data/KDE4-PURE


%description kde4_pure
KDE System

%files kde4_pure
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/kde4_pure.txt

%package kde4_utilities
%pattern_kdedesktop
Summary:        KDE Utilities
Group:          Metapackages
Provides:       pattern() = kde4_utilities
Provides:       pattern-icon() = package_utilities
Provides:       pattern-order() = 2860
Provides:       pattern-extends() = kde4
Recommends:     pattern() = kde4_utilities_opt
# from data/KDE4-Utilities
Recommends:     kdeartwork4-screensaver
Recommends:     bluedevil
Recommends:     sweeper
Recommends:     kmag
Recommends:     kmousetool
Recommends:     kcharselect
Recommends:     kompare
Suggests:       okteta
Suggests:       kteatime
Suggests:       ktux
Suggests:       amor
Suggests:       kdirstat


%description kde4_utilities
KDE Utilities

%files kde4_utilities
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/kde4_utilities.txt

%package kde4_utilities_opt
%pattern_kdedesktop
Summary:        KDE Utilities
Group:          Metapackages
Provides:       pattern() = kde4_utilities_opt
Provides:       pattern-icon() = package_utilities
Provides:       pattern-order() = 2840
Provides:       pattern-extends() = kde4
# from data/KDE4-UTILITIES-OPT
Recommends:     konqueror-plugins
Suggests:       rsibreak
Suggests:       speedcrunch
Suggests:       kchmviewer
Suggests:       kmouth
Suggests:       kremotecontrol
Suggests:       kdf
Suggests:       ktimer
Suggests:       kwikdisk
Suggests:       krusader
Suggests:       smb4k

# from data/COMMON-DESKTOP-OPT
# packages a GTK application
Recommends:     gutenprint
# MAYBE later lsb-graphics
Recommends:     icedtea-web
# give net shares
Recommends:     samba
# needs python-qt4, see#649280#14
Suggests:       hplip


%description kde4_utilities_opt
KDE Utilities

%files kde4_utilities_opt
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/kde4_utilities_opt.txt

%package kde4_yast
%pattern_basetechnologies
Summary:        YaST KDE User Interfaces
Group:          Metapackages
Provides:       pattern() = kde4_yast
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1300
Provides:       pattern-extends() = yast2_basis
Supplements:    packageand(patterns-openSUSE-kde4:patterns-openSUSE-yast2_basis)
# from data/KDE4-YaST
Requires:       libyui-qt-pkg
Requires:       yast2-control-center-qt
Requires:       yast2-theme-openSUSE-Oxygen
# yast modules for the desktop
Recommends:     yast2-scanner
Recommends:     yast2-tv


%description kde4_yast
Graphical YaST user interfaces for the KDE desktop.

%files kde4_yast
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/kde4_yast.txt

%package kvm_server
%pattern_serverfunctions
Summary:        KVM Host Server
Group:          Metapackages
Provides:       pattern() = kvm_server
Provides:       pattern-icon() = yast-uml
Provides:       pattern-order() = 3099
Requires:       pattern() = basesystem
# from data/KVM
Recommends:     kvm
Recommends:     vm-install
Recommends:     tightvnc
Recommends:     fontconfig
Recommends:     fonts-config
Recommends:     xorg-x11-fonts-core
Recommends:     efont-unicode
Recommends:     xorg-x11-xauth
Recommends:     bridge-utils
Recommends:     tftp
Recommends:     agfa-fonts
Recommends:     efont-unicode
Recommends:     xorg-x11-fonts
Recommends:     virt-viewer
Recommends:     virt-manager
Recommends:     libvirt-daemon-qemu
Suggests:       libvirt


%description kvm_server
Software to set up a server for configuring, managing, and monitoring virtual machines on a single physical machine.

%files kvm_server
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/kvm_server.txt

%package lamp_server
%pattern_serverfunctions
Summary:        Web and LAMP Server
Group:          Metapackages
Provides:       pattern() = lamp_server
Provides:       pattern-icon() = yast-http-server
Provides:       pattern-order() = 3000
Requires:       pattern() = basesystem
# from data/LAMP
Recommends:     apache2
Recommends:     yast2-http-server
Recommends:     apache2-doc
Recommends:     apache2-example-pages
Recommends:     apache2-mod_perl
Recommends:     apache2-mod_php5
Recommends:     apache2-mod_python
Recommends:     apache2-prefork
Recommends:     mariadb
Recommends:     php5-ctype
Recommends:     php5-dom
Recommends:     php5-iconv
Recommends:     php5-mysql
Suggests:       php5-gd
Suggests:       php5-mbstring
Suggests:       php5-zlib
Suggests:       php5-zip
# slightly out of place I admit
Suggests:       postgresql
Suggests:       postgresql-contrib
Suggests:       postgresql-server


%description lamp_server
Software to set up a Web server that is able to serve static, dynamic, and interactive content (like a Web shop). This includes Apache HTTP Server, the database management system MySQL, and scripting languages such as PHP, Python, Ruby on Rails, or Perl.

%files lamp_server
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/lamp_server.txt

%package laptop
%pattern_basetechnologies
Summary:        Laptop
Group:          Metapackages
Provides:       pattern() = laptop
Provides:       pattern-icon() = yast-bluetooth
Provides:       pattern-order() = 1200
Requires:       pattern() = basesystem
# from data/LAPTOP
Recommends:     pcmciautils
Recommends:     wpa_supplicant
# bnc#480879
Recommends:     crda
Recommends:     wireless-regdb
Recommends:     iw
Suggests:       irda
Suggests:       smbios-utils-python
Suggests:       powertop
# fate#303035
Suggests:       laptop-mode-tools


%description laptop
Tools designed specifically for laptop computers.

%files laptop
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/laptop.txt

%package leechcraft
%pattern_desktopfunctions
Summary:        leechcraft
Group:          Metapackages
Provides:       pattern() = leechcraft
Provides:       pattern-icon() = package_internet_webbrowser
Provides:       pattern-order() = 1248
Requires:       pattern() = x11
Requires:       pattern() = basesystem
Recommends:     pattern() = leechcraft_browser
Recommends:     pattern() = leechcraft_media
Recommends:     pattern() = leechcraft_messenger
Recommends:     pattern() = leechcraft_office
Recommends:     pattern() = leechcraft_utilities
Recommends:     pattern() = leechcraft_netutils
# from data/LC
Requires:       leechcraft-cstp


%description leechcraft

%files leechcraft
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/leechcraft.txt

%package leechcraft_browser
%pattern_desktopfunctions
Summary:        leechcraft_browser
Group:          Metapackages
Provides:       pattern() = leechcraft_browser
Provides:       pattern-icon() = package_internet_webbrowser
Provides:       pattern-order() = 1246
Requires:       pattern() = x11
Requires:       pattern() = basesystem
Recommends:     pattern() = leechcraft_utilities
# from data/LC-Browser
Requires:       leechcraft-cstp
Requires:       leechcraft-poshuku
Requires:       leechcraft-xproxy
Recommends:     leechcraft-anhero
Recommends:     leechcraft-advancednotifications
Recommends:     leechcraft-dbusmanager
Recommends:     leechcraft-dolozhee
Recommends:     leechcraft-knowhow
Recommends:     leechcraft-lackman
Recommends:     leechcraft-newlife
Recommends:     leechcraft-pintab
Recommends:     leechcraft-pogooglue
Recommends:     leechcraft-poshuku-autosearch
Recommends:     leechcraft-poshuku-cleanweb
Recommends:     leechcraft-poshuku-fatape
Recommends:     leechcraft-poshuku-filescheme
Recommends:     leechcraft-poshuku-fua
Recommends:     leechcraft-poshuku-keywords
Recommends:     leechcraft-poshuku-onlinebookmarks-delicious
Recommends:     leechcraft-poshuku-onlinebookmarks-readitlater
Recommends:     leechcraft-seekthru
Recommends:     leechcraft-summary
Recommends:     leechcraft-tabsessionmanager


%description leechcraft_browser

%files leechcraft_browser
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/leechcraft_browser.txt

%package leechcraft_media
%pattern_desktopfunctions
Summary:        leechcraft_media
Group:          Metapackages
Provides:       pattern() = leechcraft_media
Provides:       pattern-icon() = package_internet_webbrowser
Provides:       pattern-order() = 1252
Requires:       pattern() = x11
Requires:       pattern() = basesystem
Recommends:     pattern() = leechcraft_utilities
# from data/LC-Media
Requires:       leechcraft-lmp
Recommends:     leechcraft-advancednotifications
Recommends:     leechcraft-cstp
Recommends:     leechcraft-dbusmanager
Recommends:     leechcraft-deadlyrics
Recommends:     leechcraft-dolozhee
Recommends:     leechcraft-gacts
Recommends:     leechcraft-hotstreams
Recommends:     leechcraft-knowhow
Recommends:     leechcraft-lastfmscrobble
Recommends:     leechcraft-lmp-dumbsync
Recommends:     leechcraft-lmp-graffiti
Recommends:     leechcraft-lmp-mp3tunes
Recommends:     leechcraft-musiczombie
Recommends:     leechcraft-vgrabber
Recommends:     leechcraft-xproxy
Suggests:       leechcraft-anhero
Suggests:       leechcraft-kinotify
Suggests:       leechcraft-summary


%description leechcraft_media

%files leechcraft_media
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/leechcraft_media.txt

%package leechcraft_messenger
%pattern_desktopfunctions
Summary:        leechcraft_messenger
Group:          Metapackages
Provides:       pattern() = leechcraft_messenger
Provides:       pattern-icon() = package_internet_webbrowser
Provides:       pattern-order() = 1256
Requires:       pattern() = x11
Requires:       pattern() = basesystem
Recommends:     pattern() = leechcraft_utilities
# from data/LC-Messenger
Requires:       leechcraft-azoth
Requires:       leechcraft-xproxy
Recommends:     leechcraft-anhero
Recommends:     leechcraft-advancednotifications
Recommends:     leechcraft-azoth-acetamide
Recommends:     leechcraft-azoth-adiumstyles
Recommends:     leechcraft-azoth-autoidler
Recommends:     leechcraft-azoth-autopaste
Recommends:     leechcraft-azoth-birthdaynotifier
Recommends:     leechcraft-azoth-chathistory
Recommends:     leechcraft-azoth-depester
Recommends:     leechcraft-azoth-embedmedia
Recommends:     leechcraft-azoth-herbicide
Recommends:     leechcraft-azoth-hili
Recommends:     leechcraft-azoth-isterique
Recommends:     leechcraft-azoth-juick
Recommends:     leechcraft-azoth-keeso
Recommends:     leechcraft-azoth-lastseen
Recommends:     leechcraft-azoth-metacontacts
Recommends:     leechcraft-azoth-modnok
Recommends:     leechcraft-azoth-nativeemoticons
Recommends:     leechcraft-azoth-p100q
Recommends:     leechcraft-azoth-rosenthal
Recommends:     leechcraft-azoth-shx
Recommends:     leechcraft-azoth-standardstyles
Recommends:     leechcraft-azoth-vader
Recommends:     leechcraft-azoth-velvetbird
Recommends:     leechcraft-azoth-xoox
Recommends:     leechcraft-azoth-xtazy
Recommends:     leechcraft-azoth-zheet
Recommends:     leechcraft-cstp
Recommends:     leechcraft-dbusmanager
Recommends:     leechcraft-dolozhee
Recommends:     leechcraft-dumbeep
Recommends:     leechcraft-gacts
Recommends:     leechcraft-kinotify
Recommends:     leechcraft-knowhow
Recommends:     leechcraft-lackman
Recommends:     leechcraft-newlife
Recommends:     leechcraft-netstoremanager-googledrive
Recommends:     leechcraft-pintab
Recommends:     leechcraft-pogooglue
Recommends:     leechcraft-secman-simplestorage
Recommends:     leechcraft-seekthru
Recommends:     leechcraft-summary
Recommends:     leechcraft-tabsessionmanager


%description leechcraft_messenger

%files leechcraft_messenger
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/leechcraft_messenger.txt

%package leechcraft_netutils
%pattern_desktopfunctions
Summary:        leechcraft_netutils
Group:          Metapackages
Provides:       pattern() = leechcraft_netutils
Provides:       pattern-icon() = package_internet_webbrowser
Provides:       pattern-order() = 1254
Requires:       pattern() = x11
Requires:       pattern() = basesystem
Recommends:     pattern() = leechcraft_utilities
# from data/LC-NetUtils
Requires:       leechcraft-cstp
Requires:       leechcraft-xproxy
Recommends:     leechcraft-advancednotifications
Recommends:     leechcraft-aggregator-bodyfetch
Recommends:     leechcraft-anhero
Recommends:     leechcraft-bittorrent
Recommends:     leechcraft-blogique-metida
Recommends:     leechcraft-dbusmanager
Recommends:     leechcraft-dolozhee
Recommends:     leechcraft-knowhow
Recommends:     leechcraft-netstoremanager-googledrive
Recommends:     leechcraft-newlife
Recommends:     leechcraft-pogooglue
Recommends:     leechcraft-seekthru
Recommends:     leechcraft-summary


%description leechcraft_netutils

%files leechcraft_netutils
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/leechcraft_netutils.txt

%package leechcraft_office
%pattern_desktopfunctions
Summary:        leechcraft_office
Group:          Metapackages
Provides:       pattern() = leechcraft_office
Provides:       pattern-icon() = package_internet_webbrowser
Provides:       pattern-order() = 1250
Requires:       pattern() = x11
Requires:       pattern() = basesystem
Recommends:     pattern() = leechcraft_utilities
# from data/LC-Office
Requires:       leechcraft
Recommends:     leechcraft-advancednotifications
Recommends:     leechcraft-anhero
Recommends:     leechcraft-blogique-hestia
Recommends:     leechcraft-dbusmanager
Recommends:     leechcraft-dolozhee
Recommends:     leechcraft-knowhow
Recommends:     leechcraft-monocle-fxb
Recommends:     leechcraft-monocle-pdf
Recommends:     leechcraft-monocle-postrus
Recommends:     leechcraft-monocle-seen
Recommends:     leechcraft-otlozhu
Recommends:     leechcraft-popishu
Recommends:     leechcraft-summary


%description leechcraft_office

%files leechcraft_office
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/leechcraft_office.txt

%package leechcraft_utilities
%pattern_desktopfunctions
Summary:        leechcraft_utilities
Group:          Metapackages
Provides:       pattern() = leechcraft_utilities
Provides:       pattern-icon() = package_internet_webbrowser
Provides:       pattern-order() = 1244
Requires:       pattern() = x11
Requires:       pattern() = basesystem
# from data/LC-Utilities
Requires:       leechcraft
Recommends:     leechcraft-advancednotifications
Recommends:     leechcraft-anhero
Recommends:     leechcraft-auscrie
Recommends:     leechcraft-cstp
Recommends:     leechcraft-dbusmanager
Recommends:     leechcraft-dolozhee
Recommends:     leechcraft-dumbeep
Recommends:     leechcraft-gacts
Recommends:     leechcraft-glance
Recommends:     leechcraft-historyholder
Recommends:     leechcraft-kinotify
Recommends:     leechcraft-knowhow
Recommends:     leechcraft-lackman
Recommends:     leechcraft-networkmonitor
Recommends:     leechcraft-newlife
Recommends:     leechcraft-pintab
Recommends:     leechcraft-pogooglue
Recommends:     leechcraft-secman-simplestorage
Recommends:     leechcraft-seekthru
Recommends:     leechcraft-summary
Recommends:     leechcraft-tabsessionmanager
Recommends:     leechcraft-tabslist
Recommends:     leechcraft-xproxy


%description leechcraft_utilities

%files leechcraft_utilities
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/leechcraft_utilities.txt

%package lxde
%pattern_graphicalenvironments
Summary:        LXDE Desktop Environment
Group:          Metapackages
Provides:       pattern() = lxde
Provides:       pattern-icon() = pattern-lxde
Provides:       pattern-order() = 1280
Requires:       pattern() = x11
Recommends:     pattern() = lxde_office
Recommends:     pattern() = multimedia
Recommends:     pattern() = imaging
Recommends:     pattern() = remote_desktop
# from data/LXDE
Recommends:     lxappearance
Recommends:     lxdm
Recommends:     lxdm
Recommends:     lxde-common
Recommends:     lxde-common-branding-openSUSE
Recommends:     lxinput
Recommends:     lxmenu-data
Recommends:     lxmusic
Recommends:     lxpanel
Recommends:     lxrandr
Recommends:     lxsession
Recommends:     lxsession-edit
Recommends:     lxshortcut
Recommends:     lxtask
Recommends:     lxterminal
Recommends:     lxcc
Recommends:     menu-cache
Recommends:     nuoveXT2-icon-theme
Recommends:     openbox
Recommends:     obconf
Recommends:     pcmanfm
Recommends:     viewnior
Recommends:     beaver
Recommends:     xarchiver
Recommends:     galculator
Recommends:     gmixer
Recommends:     parcellite
Recommends:     xscreensaver
Recommends:     empathy
Recommends:     xchat
Recommends:     claws-mail
Recommends:     transmission-gtk
Recommends:     xdg-user-dirs-gtk
Recommends:     xfce4-power-manager
Recommends:     gconf2-branding-openSUSE
#xfburn, community asks for brasero
Recommends:     brasero
Recommends:     mtpaint
Recommends:     cheese
# #540627
Recommends:     xdg-utils
# #393956 + 450220 + 481468(xdm)
Recommends:     xorg-x11-essentials
Recommends:     xdm
# bnc#537362
Recommends:     gnome-packagekit
# #404447
Recommends:     gtk2-engine-murrine
# #440285
Recommends:     pinentry-gtk2
Recommends:     avahi
# #537365
# use gnomesu as su wrapper
Recommends:     libgnomesu
# we need a GPG GUI
Recommends:     seahorse
# We need a printer configuration util
Recommends:     system-config-printer
# And scanner one
Recommends:     simple-scan
# Video player and codecs
# do we need an LXDE_MULTIMEDIA pattern??
Recommends:     totem
Recommends:     totem-browser-plugin
# Use gtk UI for YaST
Recommends:     libyui-gtk-pkg
Recommends:     yast2-control-center-gnome
# Use NM by default
Recommends:     NetworkManager
Recommends:     NetworkManager-gnome
Recommends:     desktop-branding
Suggests:       lxlauncher
Suggests:       leafpad

# from data/COMMON-DESKTOP
Recommends:     droid-fonts
Recommends:     MozillaFirefox
Recommends:     desktop-data-openSUSE
Recommends:     avahi
# bnc#508120
Recommends:     xdg-user-dirs
# bnc#598884
Suggests:       moonlight-plugin
# metalink downloader
Suggests:       aria2

# from data/COMMON-DESKTOP-OPT
# packages a GTK application
Recommends:     gutenprint
# MAYBE later lsb-graphics
Recommends:     icedtea-web
# give net shares
Recommends:     samba
# needs python-qt4, see#649280#14
Suggests:       hplip


%description lxde
LXDE is a lightweight X11 desktop environment similiar to XFCE in its nature.

%files lxde
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/lxde.txt

%package lxde_laptop
%pattern_lxdedesktop
Summary:        LXDE Laptop
Group:          Metapackages
Provides:       pattern() = lxde_laptop
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 5160
Provides:       pattern-extends() = laptop
Supplements:    packageand(patterns-openSUSE-lxde:patterns-openSUSE-laptop)
Requires:       pattern() = lxde
# from data/LXDE-LAPTOP
Recommends:     gnome-bluetooth
Recommends:     gsynaptics


%description lxde_laptop
LXDE Tools designed specifically for use with laptop computers.

%files lxde_laptop
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/lxde_laptop.txt

%package lxde_office
%pattern_graphicalenvironments
Summary:        LXDE Office
Group:          Metapackages
Provides:       pattern() = lxde_office
Provides:       pattern-icon() = pattern-lxde
Provides:       pattern-order() = 1880
Provides:       pattern-extends() = office
Supplements:    packageand(patterns-openSUSE-lxde:patterns-openSUSE-office)
Requires:       pattern() = lxde
# from data/LXDE-Office
Recommends:     abiword
Recommends:     mupdf
Recommends:     gnumeric
Recommends:     goffice
%ifarch %ix86 x86_64
Suggests:       libreoffice-gnome
%endif


%description lxde_office
LXDE Office

%files lxde_office
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/lxde_office.txt

%package mail_server
%pattern_serverfunctions
Summary:        Mail and News Server
Group:          Metapackages
Provides:       pattern() = mail_server
Provides:       pattern-icon() = yast-mail-server
Provides:       pattern-order() = 2980
Requires:       pattern() = basesystem
# from data/MAIL_SERVER
Recommends:     cyrus-imapd
Recommends:     amavisd-new
Recommends:     mailman
Recommends:     clamav
Recommends:     fetchmail
Recommends:     postfix
Recommends:     procmail
Recommends:     spamassassin
Recommends:     inn
Recommends:     vacation
Suggests:       dovecot12
Suggests:       mlmmj
#pragma ignore
Suggests:       sendmail
Suggests:       bogofilter


%description mail_server
Software to set up electronic mail and message services to handle e-mail, mailing, and news lists, including a virus scanner to scan messages at the server level.

%files mail_server
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/mail_server.txt

%package minimal_base
%pattern_basetechnologies
Summary:        Base System
Group:          Metapackages
Provides:       pattern() = minimal_base
Provides:       pattern-icon() = yast-sw_single
Provides:       pattern-order() = 5190
Requires:       pattern() = basesystem
Requires:       pattern() = yast2_install_wf
Requires:       pattern() = sw_management
Recommends:     pattern() = minimal_base-conflicts
# from data/MINIMAL
Recommends:     SuSEfirewall2
Recommends:     aaa_base-extras
Recommends:     autofs
Recommends:     bc
Recommends:     ca-certificates-mozilla
Recommends:     cracklib-dict-small
Recommends:     deltarpm
Recommends:     eject
Recommends:     ethtool
Recommends:     glibc-locale
Recommends:     haveged
Recommends:     hdparm
Recommends:     iputils
Recommends:     joe
Recommends:     less
Recommends:     linux32
Recommends:     lsof
Recommends:     lukemftp
Recommends:     netcat-openbsd
Recommends:     nfs-client
Recommends:     ntfs-3g
Recommends:     ntp
Recommends:     prctl
Recommends:     release-notes-openSUSE
Recommends:     rsync
Recommends:     strace
Recommends:     sudo
Recommends:     sysfsutils
Recommends:     tcsh
Recommends:     telnet
Recommends:     nscd
Recommends:     vim
Recommends:     w3m
Recommends:     wget
Recommends:     wireless-tools
Recommends:     wol


%description minimal_base
This is the base runtime system.  It contains only a minimal multiuser booting system. For running on real hardware, you need to add additional packages and pattern to make this pattern useful on its own.

%files minimal_base
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/minimal_base.txt

%package minimal_base-conflicts
%pattern_basetechnologies
Summary:        Base System
Group:          Metapackages
Provides:       pattern() = minimal_base-conflicts
Provides:       pattern-icon() = yast-sw_single
Provides:       pattern-order() = 5191
Requires:       pattern() = minimal_base
# from data/MINIMAL-CONFLICTS
Conflicts:      smtp_daemon
Conflicts:      perl-doc
Conflicts:      readline-doc
Conflicts:      bash-doc
Conflicts:      netpbm
# recommended by yast2-printer
Conflicts:      samba-client
Conflicts:      cups-client
Conflicts:      desktop-translations
# supplements into glib
Conflicts:      gsettings-backend-dconf
Conflicts:      glib-networking
Conflicts:      vim-data
# required by gio-branding
Conflicts:      desktop-data-openSUSE
# supplements yast2, not needed for ncurses only
Conflicts:      yast2-branding
# supplements libgio and wget (TODO)
Conflicts:      libproxy1-config-gnome3
# requires python
Conflicts:      zypper-log
# systemd recommends dbus-1-python
Conflicts:      python
# gtk3
Conflicts:      gtk3-branding
Conflicts:      gtk3-immodule-amharic
Conflicts:      gtk3-immodule-inuktitut
Conflicts:      gtk3-immodule-thai
Conflicts:      gtk3-immodule-tigrigna
Conflicts:      gtk3-immodule-vietnamese
Conflicts:      gvfs
Conflicts:      bundle-lang-gnome-extras-en
# requires X11
Conflicts:      openssh-askpass
# requires all kinds of perl modules
Conflicts:      xdg-utils


%description minimal_base-conflicts
This is the base runtime system.  It contains only a minimal multiuser booting system. For running on real hardware, you need to add additional packages and pattern to make this pattern useful on its own.

%files minimal_base-conflicts
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/minimal_base-conflicts.txt

%package misc_server
%pattern_serverfunctions
Summary:        Miscellaneous Server
Group:          Metapackages
Provides:       pattern() = misc_server
Provides:       pattern-icon() = yast-nfs_server
Provides:       pattern-order() = 2920
Requires:       pattern() = basesystem
# from data/MISC_SERVER
Recommends:     yast2-nis-server
Recommends:     openslp-server
Recommends:     yast2-instserver
Recommends:     yast2-iscsi-server
Recommends:     yast2-nis-server
Recommends:     yast2-slp-server


%description misc_server
Miscellaneous Server.

%files misc_server
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/misc_server.txt

%package multimedia
%pattern_desktopfunctions
Summary:        Multimedia
Group:          Metapackages
Provides:       pattern() = multimedia
Provides:       pattern-icon() = yast-tv
Provides:       pattern-order() = 1580
Recommends:     pattern() = multimedia_opt
# from data/MULTIMEDIA
Recommends:     yast2-sound
Recommends:     dvd+rw-tools
Recommends:     vorbis-tools
Suggests:       ripit
# maintained by coolo - must be good
Suggests:       abcde
Suggests:       gstreamer-0_10-plugins-good-extra
Suggests:       audacity
Suggests:       timidity
Suggests:       vdr
Suggests:       xawtv
Suggests:       flac


%description multimedia
Multimedia players, sound editing tools , video and image manipulation applications.

%files multimedia
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/multimedia.txt

%package multimedia_opt
%pattern_desktopfunctions
Summary:        Multimedia
Group:          Metapackages
Provides:       pattern() = multimedia_opt
Provides:       pattern-icon() = yast-tv
Provides:       pattern-order() = 1560
Provides:       pattern-extends() = multimedia
# from data/MULTIMEDIA-OPT
Recommends:     ImageMagick
Recommends:     mjpegtools
Suggests:       blender


%description multimedia_opt
Multimedia players, sound editing tools , video and image manipulation applications.

%files multimedia_opt
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/multimedia_opt.txt

%package network_admin
%pattern_serverfunctions
Summary:        Network Administration
Group:          Metapackages
Provides:       pattern() = network_admin
Provides:       pattern-icon() = yast-network
Provides:       pattern-order() = 2940
Requires:       pattern() = basesystem
# from data/NETWORK-ADMIN
Recommends:     nmap
Recommends:     quagga
Recommends:     tcpdump
Recommends:     whois
Recommends:     wireshark
Recommends:     arpwatch
Recommends:     iftop
Recommends:     nagios
Recommends:     mtr
Suggests:       mrtg
Suggests:       openvpn
Suggests:       opie
Suggests:       kismet
Suggests:       iptraf-ng
Suggests:       privoxy
Suggests:       pptpd
Suggests:       wondershaper
Suggests:       krb5
Suggests:       qinternet


%description network_admin
Tools for administering and debugging networks.

%files network_admin
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/network_admin.txt

%package non_oss
%pattern_proprietarysoftware
Summary:        Misc. Proprietary Packages
Group:          Metapackages
Provides:       pattern() = non_oss
Provides:       pattern-icon() = yast-addon
Provides:       pattern-order() = 3120
Requires:       pattern() = x11
Recommends:     pattern() = non_oss_opt
# from data/NON-OSS
%ifarch %ix86 x86_64
Recommends:     pullin-flash-player
%endif


%description non_oss
Packages that are proprietary and not under an Open Source license.

%files non_oss
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/non_oss.txt

%package non_oss_opt
%pattern_proprietarysoftware
Summary:        Misc. Proprietary Packages
Group:          Metapackages
Provides:       pattern() = non_oss_opt
Provides:       pattern-icon() = yast-addon
Provides:       pattern-order() = 3121
Provides:       pattern-extends() = non_oss
Requires:       pattern() = non_oss
# from data/NON-OSS-OPT
Recommends:     gst-fluendo-mp3
%ifarch %ix86 x86_64
Recommends:     flash-player
%endif
Recommends:     unrar
Suggests:       poppler-data
%ifarch %ix86
Suggests:       antivir-gui
Suggests:       antivir
%endif
Suggests:       AdobeICCProfiles
Suggests:       acroread
Suggests:       atmel-firmware
Suggests:       ipw-firmware
%ifarch %ix86 x86_64
Suggests:       iscan-firmware
%endif
Suggests:       moneyplex
Suggests:       opera
Suggests:       FZFangSong
Suggests:       FZHeiTi
Suggests:       FZKaiTi
Suggests:       FZKaiTiB
Suggests:       FZMingTiB
# needed for instsys
Suggests:       FZSongTi


%description non_oss_opt
Packages that are proprietary and not under an Open Source license.

%files non_oss_opt
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/non_oss_opt.txt

%package office
%pattern_desktopfunctions
Summary:        Office Software
Group:          Metapackages
Provides:       pattern() = office
Provides:       pattern-icon() = yast-keyboard
Provides:       pattern-order() = 1640
Recommends:     pattern() = office_opt
# from data/OFFICE
Recommends:     libreoffice
Recommends:     libreoffice-calc
Recommends:     libreoffice-draw
Recommends:     libreoffice-impress
Recommends:     libreoffice-writer


%description office
Office software for your desktop environment including LibreOffice.

%files office
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/office.txt

%package office_opt
%pattern_desktopfunctions
Summary:        Office Software
Group:          Metapackages
Provides:       pattern() = office_opt
Provides:       pattern-icon() = yast-keyboard
Provides:       pattern-order() = 1620
Provides:       pattern-extends() = office
# from data/OFFICE-OPT
# bug 592752
Suggests:       libreoffice-languagetool
Recommends:     libreoffice-math
Recommends:     libreoffice-base-extensions
Recommends:     libreoffice-calc-extensions
Recommends:     libreoffice-draw-extensions
Recommends:     libreoffice-impress-extensions
Recommends:     libreoffice-writer-extensions
Recommends:     libreoffice-converter


%description office_opt
Office software for your desktop environment including LibreOffice.

%files office_opt
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/office_opt.txt

%package print_server
%pattern_serverfunctions
Summary:        Print Server
Group:          Metapackages
Provides:       pattern() = print_server
Provides:       pattern-icon() = yast-printer
Provides:       pattern-order() = 2960
Requires:       pattern() = basesystem
# from data/PRINT_SERVER
Recommends:     cups
Recommends:     cups-backends
Recommends:     OpenPrintingPPDs
Recommends:     m2300w
Recommends:     splix
Recommends:     foomatic-filters
Recommends:     gutenprint
Recommends:     hplip
Recommends:     manufacturer-PPDs
Recommends:     samba
Suggests:       udev-configure-printer
Suggests:       poster
# print to bluetooth
Suggests:       bluez-cups
Suggests:       pbm2l7k


%description print_server
Software used to host print queues so that they may be accessed by other computers on the same network. LPD, CUPS, and SMB print servers and queues are supported.

%files print_server
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/print_server.txt

%package remote_desktop
%pattern_desktopfunctions
Summary:        Remote Desktop
Group:          Metapackages
Provides:       pattern() = remote_desktop
Provides:       pattern-icon() = yast-x11
Provides:       pattern-order() = 1920
# from data/REMOTE-DESKTOP
Recommends:     rdesktop
Recommends:     tsclient
Recommends:     tightvnc
Suggests:       krfb
Suggests:       krdc


%description remote_desktop
Tools to access a remote desktop.

%files remote_desktop
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/remote_desktop.txt

%package rest_cd_gnome
%pattern_desktopfunctions
Summary:        Remaining Software
Group:          Metapackages
Provides:       pattern() = rest_cd_gnome
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1940
Requires:       pattern() = apparmor
Requires:       pattern() = base
Requires:       pattern() = enhanced_base
Requires:       pattern() = fonts
Requires:       pattern() = gnome
Requires:       pattern() = gnome_basis
Requires:       pattern() = gnome_imaging
Requires:       pattern() = gnome_internet
Requires:       pattern() = gnome_laptop
Requires:       pattern() = gnome_yast
Requires:       pattern() = imaging
Requires:       pattern() = multimedia
Requires:       pattern() = sw_management
Requires:       pattern() = sw_management_gnome
Requires:       pattern() = x11
Requires:       pattern() = yast2_basis
Requires:       pattern() = yast2_install_wf
Requires:       pattern() = games
Requires:       pattern() = gnome_games
Requires:       pattern() = office
Requires:       pattern() = gnome_office
Requires:       pattern() = gnome_multimedia
Requires:       pattern() = gnome_utilities
# from data/REST-CD
%ifarch x86_64
Requires:       kernel-desktop
#else
Requires:       kernel-default
%endif
Requires:       kernel-firmware
# #327506
Recommends:     b43-fwcutter
# #304219
Recommends:     memtest86+
# adaptec-firmware (#298726)
Recommends:     adaptec-firmware
Recommends:     mpt-firmware
Recommends:     atmel-firmware
# DELL laptop support
Recommends:     smbios-utils-python
#lvm2 support (#301382)
Recommends:     lvm2
Recommends:     aspell-en
Recommends:     cifs-utils
Recommends:     input-utils
Recommends:     nss_ldap
Recommends:     pam_krb5
Recommends:     pam_ldap
Recommends:     krb5-client
# prefer the full version for installation
Recommends:     cracklib-dict-full
# filesystem(minix)
Recommends:     util-linux
# filesystem(ext2)
Recommends:     e2fsprogs
# filesystem(reiserfs)
Recommends:     reiserfs
# filesystem(jfs)
Recommends:     jfsutils
# filesystem(ntfs-3g)
Recommends:     ntfs-3g
# filesystem(xfs)
Recommends:     xfsprogs
# filesystem(vfat)
Recommends:     dosfstools
# crypto partitions
Recommends:     cryptsetup
# filesystem(btrfs)
Recommends:     btrfsprogs
%ifarch x86_64
# kernel modules
Recommends:     ndiswrapper-kmp-desktop
#else
Recommends:     ndiswrapper-kmp-default
%endif
# network
Recommends:     ndiswrapper
# bnc#548325
Recommends:     ipw-firmware
# supplements by modaliases
Recommends:     bluez-firmware
Recommends:     dvb
Recommends:     lomoco
Recommends:     pcmciautils
Recommends:     pam_fprint
# yast can configure quota - if present on medium (#348336)
Recommends:     quota
# enhances virtualbox speed (#365562)
Recommends:     virtualbox-guest-x11
# Firmware for ZD1211 based WLAN sticks
Recommends:     zd1211-firmware
# rescue
Recommends:     dd_rescue
# #396109
Recommends:     alsa-firmware
Recommends:     awesfx
# needed by yast2-storage for crypt partitions
Recommends:     pam_mount
# adding to LiveCD (bnc#419201)
Recommends:     rsync
Recommends:     smartmontools
# LiveCD accessible? (bnc#391327)
Recommends:     sbl
Recommends:     espeak
# give vim hates an editor
Recommends:     nano
# pull flash and mp3 also on livecd installs
Recommends:     pullin-fluendo-mp3
Recommends:     pullin-flash-player
# #494547 - just testing
Recommends:     manufacturer-PPDs
# needed to detect if a system is the same
Recommends:     dmidecode
# decompression to recover something
Recommends:     xz
Recommends:     zip
Recommends:     unzip
Recommends:     p7zip
# file system stuff
Recommends:     xfsdump
Recommends:     reiserfs
# fate#306643
Recommends:     mc 
# laptop stuff
Recommends:     irda
Recommends:     pcmciautils
Recommends:     wpa_supplicant
# bnc#480879
Recommends:     crda
Recommends:     wireless-regdb
Recommends:     iw
# bug#589416
Recommends:     virtualbox-guest-tools 
# bug#591085
Recommends:     open-vm-tools
# parted GUI
Recommends:     gparted
# bnc#728529
Recommends:     elilo
%ifarch x86_64
Recommends:     efibootmgr
%endif
# yast2-bootloader still suggests it (bnc#803401)
Recommends:     grub
# Backup and Copying utilites
Recommends:     gnu_ddrescue
Recommends:     lftp
Recommends:     grsync
# all xf86 drivers
Recommends:     xf86-video-ark
Recommends:     xf86-video-ast
Recommends:     xf86-video-ati
Recommends:     xf86-video-chips
Recommends:     xf86-video-cirrus
Recommends:     xf86-video-dummy
Recommends:     xf86-video-fbdev
Recommends:     xf86-video-glint
Recommends:     xf86-video-i128
Recommends:     xf86-video-intel
Recommends:     xf86-video-mach64
Recommends:     xf86-video-mga
Recommends:     xf86-video-modesetting
Recommends:     xf86-video-neomagic
Recommends:     xf86-video-nv
Recommends:     xf86-video-qxl
Recommends:     xf86-video-r128
Recommends:     xf86-video-savage
Recommends:     xf86-video-siliconmotion
Recommends:     xf86-video-sis
Recommends:     xf86-video-sisusb
Recommends:     xf86-video-tdfx
Recommends:     xf86-video-tga
Recommends:     xf86-video-v4l
Recommends:     xf86-video-vesa
Recommends:     xf86-video-vmware
Recommends:     xf86-video-voodoo

# from data/REST-CD-DESKTOP
# minimal set of yast modules
Requires:       yast2-country
Requires:       yast2-trans-stats
Requires:       yast2-storage
Requires:       yast2-bootloader
Requires:       yast2-proxy
Requires:       yast2-network
Requires:       yast2-hardware-detection
Requires:       yast2-x11
Recommends:     bundle-lang-common-en
Recommends:     susehelp_en
Recommends:     yast2-trans-cs
Recommends:     yast2-trans-da
Recommends:     yast2-trans-de
Recommends:     yast2-trans-en_GB
Recommends:     yast2-trans-en_US
Recommends:     yast2-trans-es
Recommends:     yast2-trans-fr
Recommends:     yast2-trans-hu
Recommends:     yast2-trans-it
Recommends:     yast2-trans-ja
Recommends:     yast2-trans-pl
Recommends:     yast2-trans-pt
Recommends:     yast2-trans-pt_BR
Recommends:     yast2-trans-ru
Recommends:     yast2-trans-stats
Recommends:     yast2-trans-sv
Recommends:     yast2-trans-zh_CN
Recommends:     yast2-trans-zh_TW
# required by yast2-dsl (#377472)
Recommends:     smpppd
Recommends:     sssd
%ifarch x86_64
Recommends:     sssd-32bit
%endif
Recommends:     gtk2-branding-openSUSE

# from data/REST-CD-GNOME
Recommends:     bundle-lang-gnome-en


%description rest_cd_gnome
Packages that are on CD but not in other patterns.

%files rest_cd_gnome
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/rest_cd_gnome.txt

%package rest_cd_kde4
%pattern_desktopfunctions
Summary:        Remaining Software
Group:          Metapackages
Provides:       pattern() = rest_cd_kde4
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1960
Requires:       pattern() = apparmor
Requires:       pattern() = base
Requires:       pattern() = enhanced_base
Requires:       pattern() = fonts
Requires:       pattern() = imaging
Requires:       pattern() = kde4
Requires:       pattern() = kde4_basis
Requires:       pattern() = kde4_imaging
Requires:       pattern() = kde4_internet
Requires:       pattern() = kde4_multimedia
Requires:       pattern() = kde4_utilities
Requires:       pattern() = kde4_yast
Requires:       pattern() = multimedia
Requires:       pattern() = sw_management
Requires:       pattern() = sw_management_kde4
Requires:       pattern() = x11
Requires:       pattern() = yast2_basis
Requires:       pattern() = yast2_install_wf
Requires:       pattern() = games
Requires:       pattern() = kde4_games
Requires:       pattern() = office
Requires:       pattern() = kde4_office
# from data/REST-CD
%ifarch x86_64
Requires:       kernel-desktop
#else
Requires:       kernel-default
%endif
Requires:       kernel-firmware
# #327506
Recommends:     b43-fwcutter
# #304219
Recommends:     memtest86+
# adaptec-firmware (#298726)
Recommends:     adaptec-firmware
Recommends:     mpt-firmware
Recommends:     atmel-firmware
# DELL laptop support
Recommends:     smbios-utils-python
#lvm2 support (#301382)
Recommends:     lvm2
Recommends:     aspell-en
Recommends:     cifs-utils
Recommends:     input-utils
Recommends:     nss_ldap
Recommends:     pam_krb5
Recommends:     pam_ldap
Recommends:     krb5-client
# prefer the full version for installation
Recommends:     cracklib-dict-full
# filesystem(minix)
Recommends:     util-linux
# filesystem(ext2)
Recommends:     e2fsprogs
# filesystem(reiserfs)
Recommends:     reiserfs
# filesystem(jfs)
Recommends:     jfsutils
# filesystem(ntfs-3g)
Recommends:     ntfs-3g
# filesystem(xfs)
Recommends:     xfsprogs
# filesystem(vfat)
Recommends:     dosfstools
# crypto partitions
Recommends:     cryptsetup
# filesystem(btrfs)
Recommends:     btrfsprogs
%ifarch x86_64
# kernel modules
Recommends:     ndiswrapper-kmp-desktop
#else
Recommends:     ndiswrapper-kmp-default
%endif
# network
Recommends:     ndiswrapper
# bnc#548325
Recommends:     ipw-firmware
# supplements by modaliases
Recommends:     bluez-firmware
Recommends:     dvb
Recommends:     lomoco
Recommends:     pcmciautils
Recommends:     pam_fprint
# yast can configure quota - if present on medium (#348336)
Recommends:     quota
# enhances virtualbox speed (#365562)
Recommends:     virtualbox-guest-x11
# Firmware for ZD1211 based WLAN sticks
Recommends:     zd1211-firmware
# rescue
Recommends:     dd_rescue
# #396109
Recommends:     alsa-firmware
Recommends:     awesfx
# needed by yast2-storage for crypt partitions
Recommends:     pam_mount
# adding to LiveCD (bnc#419201)
Recommends:     rsync
Recommends:     smartmontools
# LiveCD accessible? (bnc#391327)
Recommends:     sbl
Recommends:     espeak
# give vim hates an editor
Recommends:     nano
# pull flash and mp3 also on livecd installs
Recommends:     pullin-fluendo-mp3
Recommends:     pullin-flash-player
# #494547 - just testing
Recommends:     manufacturer-PPDs
# needed to detect if a system is the same
Recommends:     dmidecode
# decompression to recover something
Recommends:     xz
Recommends:     zip
Recommends:     unzip
Recommends:     p7zip
# file system stuff
Recommends:     xfsdump
Recommends:     reiserfs
# fate#306643
Recommends:     mc 
# laptop stuff
Recommends:     irda
Recommends:     pcmciautils
Recommends:     wpa_supplicant
# bnc#480879
Recommends:     crda
Recommends:     wireless-regdb
Recommends:     iw
# bug#589416
Recommends:     virtualbox-guest-tools 
# bug#591085
Recommends:     open-vm-tools
# parted GUI
Recommends:     gparted
# bnc#728529
Recommends:     elilo
%ifarch x86_64
Recommends:     efibootmgr
%endif
# yast2-bootloader still suggests it (bnc#803401)
Recommends:     grub
# Backup and Copying utilites
Recommends:     gnu_ddrescue
Recommends:     lftp
Recommends:     grsync
# all xf86 drivers
Recommends:     xf86-video-ark
Recommends:     xf86-video-ast
Recommends:     xf86-video-ati
Recommends:     xf86-video-chips
Recommends:     xf86-video-cirrus
Recommends:     xf86-video-dummy
Recommends:     xf86-video-fbdev
Recommends:     xf86-video-glint
Recommends:     xf86-video-i128
Recommends:     xf86-video-intel
Recommends:     xf86-video-mach64
Recommends:     xf86-video-mga
Recommends:     xf86-video-modesetting
Recommends:     xf86-video-neomagic
Recommends:     xf86-video-nv
Recommends:     xf86-video-qxl
Recommends:     xf86-video-r128
Recommends:     xf86-video-savage
Recommends:     xf86-video-siliconmotion
Recommends:     xf86-video-sis
Recommends:     xf86-video-sisusb
Recommends:     xf86-video-tdfx
Recommends:     xf86-video-tga
Recommends:     xf86-video-v4l
Recommends:     xf86-video-vesa
Recommends:     xf86-video-vmware
Recommends:     xf86-video-voodoo

# from data/REST-CD-DESKTOP
# minimal set of yast modules
Requires:       yast2-country
Requires:       yast2-trans-stats
Requires:       yast2-storage
Requires:       yast2-bootloader
Requires:       yast2-proxy
Requires:       yast2-network
Requires:       yast2-hardware-detection
Requires:       yast2-x11
Recommends:     bundle-lang-common-en
Recommends:     susehelp_en
Recommends:     yast2-trans-cs
Recommends:     yast2-trans-da
Recommends:     yast2-trans-de
Recommends:     yast2-trans-en_GB
Recommends:     yast2-trans-en_US
Recommends:     yast2-trans-es
Recommends:     yast2-trans-fr
Recommends:     yast2-trans-hu
Recommends:     yast2-trans-it
Recommends:     yast2-trans-ja
Recommends:     yast2-trans-pl
Recommends:     yast2-trans-pt
Recommends:     yast2-trans-pt_BR
Recommends:     yast2-trans-ru
Recommends:     yast2-trans-stats
Recommends:     yast2-trans-sv
Recommends:     yast2-trans-zh_CN
Recommends:     yast2-trans-zh_TW
# required by yast2-dsl (#377472)
Recommends:     smpppd
Recommends:     sssd
%ifarch x86_64
Recommends:     sssd-32bit
%endif
Recommends:     gtk2-branding-openSUSE

# from data/REST-CD-KDE
Recommends:     bundle-lang-kde-en


%description rest_cd_kde4
Packages that are on CD but not in other patterns.

%files rest_cd_kde4
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/rest_cd_kde4.txt

%package rest_cd_x11
%pattern_desktopfunctions
Summary:        Remaining Software
Group:          Metapackages
Provides:       pattern() = rest_cd_x11
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1961
Requires:       pattern() = base
Requires:       pattern() = enhanced_base
Requires:       pattern() = sw_management
Requires:       pattern() = x11
Requires:       pattern() = fonts
# from data/REST-CD
%ifarch x86_64
Requires:       kernel-desktop
#else
Requires:       kernel-default
%endif
Requires:       kernel-firmware
# #327506
Recommends:     b43-fwcutter
# #304219
Recommends:     memtest86+
# adaptec-firmware (#298726)
Recommends:     adaptec-firmware
Recommends:     mpt-firmware
Recommends:     atmel-firmware
# DELL laptop support
Recommends:     smbios-utils-python
#lvm2 support (#301382)
Recommends:     lvm2
Recommends:     aspell-en
Recommends:     cifs-utils
Recommends:     input-utils
Recommends:     nss_ldap
Recommends:     pam_krb5
Recommends:     pam_ldap
Recommends:     krb5-client
# prefer the full version for installation
Recommends:     cracklib-dict-full
# filesystem(minix)
Recommends:     util-linux
# filesystem(ext2)
Recommends:     e2fsprogs
# filesystem(reiserfs)
Recommends:     reiserfs
# filesystem(jfs)
Recommends:     jfsutils
# filesystem(ntfs-3g)
Recommends:     ntfs-3g
# filesystem(xfs)
Recommends:     xfsprogs
# filesystem(vfat)
Recommends:     dosfstools
# crypto partitions
Recommends:     cryptsetup
# filesystem(btrfs)
Recommends:     btrfsprogs
%ifarch x86_64
# kernel modules
Recommends:     ndiswrapper-kmp-desktop
#else
Recommends:     ndiswrapper-kmp-default
%endif
# network
Recommends:     ndiswrapper
# bnc#548325
Recommends:     ipw-firmware
# supplements by modaliases
Recommends:     bluez-firmware
Recommends:     dvb
Recommends:     lomoco
Recommends:     pcmciautils
Recommends:     pam_fprint
# yast can configure quota - if present on medium (#348336)
Recommends:     quota
# enhances virtualbox speed (#365562)
Recommends:     virtualbox-guest-x11
# Firmware for ZD1211 based WLAN sticks
Recommends:     zd1211-firmware
# rescue
Recommends:     dd_rescue
# #396109
Recommends:     alsa-firmware
Recommends:     awesfx
# needed by yast2-storage for crypt partitions
Recommends:     pam_mount
# adding to LiveCD (bnc#419201)
Recommends:     rsync
Recommends:     smartmontools
# LiveCD accessible? (bnc#391327)
Recommends:     sbl
Recommends:     espeak
# give vim hates an editor
Recommends:     nano
# pull flash and mp3 also on livecd installs
Recommends:     pullin-fluendo-mp3
Recommends:     pullin-flash-player
# #494547 - just testing
Recommends:     manufacturer-PPDs
# needed to detect if a system is the same
Recommends:     dmidecode
# decompression to recover something
Recommends:     xz
Recommends:     zip
Recommends:     unzip
Recommends:     p7zip
# file system stuff
Recommends:     xfsdump
Recommends:     reiserfs
# fate#306643
Recommends:     mc 
# laptop stuff
Recommends:     irda
Recommends:     pcmciautils
Recommends:     wpa_supplicant
# bnc#480879
Recommends:     crda
Recommends:     wireless-regdb
Recommends:     iw
# bug#589416
Recommends:     virtualbox-guest-tools 
# bug#591085
Recommends:     open-vm-tools
# parted GUI
Recommends:     gparted
# bnc#728529
Recommends:     elilo
%ifarch x86_64
Recommends:     efibootmgr
%endif
# yast2-bootloader still suggests it (bnc#803401)
Recommends:     grub
# Backup and Copying utilites
Recommends:     gnu_ddrescue
Recommends:     lftp
Recommends:     grsync
# all xf86 drivers
Recommends:     xf86-video-ark
Recommends:     xf86-video-ast
Recommends:     xf86-video-ati
Recommends:     xf86-video-chips
Recommends:     xf86-video-cirrus
Recommends:     xf86-video-dummy
Recommends:     xf86-video-fbdev
Recommends:     xf86-video-glint
Recommends:     xf86-video-i128
Recommends:     xf86-video-intel
Recommends:     xf86-video-mach64
Recommends:     xf86-video-mga
Recommends:     xf86-video-modesetting
Recommends:     xf86-video-neomagic
Recommends:     xf86-video-nv
Recommends:     xf86-video-qxl
Recommends:     xf86-video-r128
Recommends:     xf86-video-savage
Recommends:     xf86-video-siliconmotion
Recommends:     xf86-video-sis
Recommends:     xf86-video-sisusb
Recommends:     xf86-video-tdfx
Recommends:     xf86-video-tga
Recommends:     xf86-video-v4l
Recommends:     xf86-video-vesa
Recommends:     xf86-video-vmware
Recommends:     xf86-video-voodoo

# from data/REST-CD-X11
Requires:       lightdm
Requires:       lightdm-gtk-greeter
Requires:       yast2-country
Requires:       yast2-trans-stats
Requires:       yast2-storage
Requires:       yast2-bootloader
Requires:       yast2-proxy
Requires:       yast2-network
Requires:       yast2-hardware-detection
Requires:       yast2-x11
#
# Additional applications for rescue CD
#
Requires:       file-roller
Requires:       leafpad
Requires:       midori
Requires:       mupdf
Requires:       gparted
Requires:       photorec
Requires:       ristretto
Requires:       xchat

# from data/XFCE-BASIS
# This defines a bare minimum Xfce desktop used, for example, as
# base for the openSUSE Rescue CD
Requires:       patterns-openSUSE-xfce_basis
Requires:       thunar
Requires:       xfce4-appfinder
Requires:       xfce4-mixer
Requires:       xfce4-notifyd
Requires:       xfce4-panel-plugin-mixer
Requires:       xfce4-panel
Requires:       xfce4-power-manager
Requires:       xfce4-session
Requires:       xfce4-settings
Requires:       xfconf
Requires:       xfdesktop
Requires:       xfwm4
Requires:       thunar-volman
#
# low level functionality
#
Recommends:     avahi
Recommends:     dbus-1-x11
# bnc#540627
Recommends:     xdg-utils
Recommends:     xdg-user-dirs-gtk
Recommends:     desktop-file-utils
Recommends:     shared-mime-info
Recommends:     NetworkManager
Recommends:     NetworkManager-gnome
# use gnomesu as su wrapper
Recommends:     libgnomesu
# bnc#440285
Recommends:     pinentry-gtk2
# For screenlocking to work in xfce
Recommends:     xscreensaver
Recommends:     xfce4-terminal
Recommends:     libxfce4ui-tools
Recommends:     xfce4-panel-plugin-xkb
#
# core desktop functionality
#
Recommends:     libyui-gtk-pkg
Recommends:     yast2-control-center-gnome
#
# branding
#
Suggests:       exo-branding-openSUSE
Suggests:       gconf2-branding-openSUSE
Suggests:       libgarcon-branding-openSUSE
Suggests:       libxfce4ui-branding-openSUSE
Suggests:       lightdm-gtk-greeter-branding-openSUSE
Suggests:       midori-branding-openSUSE
Suggests:       thunar-volman-branding-openSUSE
Suggests:       wallpaper-branding-openSUSE
Suggests:       xfce4-notifyd-branding-openSUSE
Suggests:       xfce4-panel-branding-openSUSE
Suggests:       xfce4-session-branding-openSUSE
Suggests:       xfce4-settings-branding-openSUSE
Suggests:       xfce4-splash-branding-openSUSE
Suggests:       xfdesktop-branding-openSUSE
Suggests:       xfwm4-branding-openSUSE
Suggests:       desktop-branding


%description rest_cd_x11
Packages that are on CD but not in other patterns.

%files rest_cd_x11
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/rest_cd_x11.txt

%package rest_core_dvd
%pattern_desktopfunctions
Summary:        Remaining Software
Group:          Metapackages
Provides:       pattern() = rest_core_dvd
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1982
Requires:       pattern() = base
Requires:       pattern() = enhanced_base
Requires:       pattern() = sw_management
Requires:       pattern() = x11
Requires:       pattern() = fonts
Requires:       pattern() = yast2_basis
Requires:       pattern() = yast2_install_wf
Recommends:     pattern() = voip
Recommends:     pattern() = x11_yast
# from data/REST-CORE-CD
%ifarch x86_64
Requires:       kernel-desktop
#else
Requires:       kernel-default
%endif
Requires:       kernel-firmware
#lvm2 support (#301382)
Recommends:     lvm2
# prefer the full version for installation
Recommends:     cracklib-dict-full
# filesystem(minix)
Recommends:     util-linux
# filesystem(ext2)
Recommends:     e2fsprogs
# filesystem(reiserfs)
Recommends:     reiserfs
# filesystem(jfs)
Recommends:     jfsutils
# filesystem(ntfs-3g)
Recommends:     ntfs-3g
# filesystem(xfs)
Recommends:     xfsprogs
# filesystem(vfat)
Recommends:     dosfstools
# crypto partitions
Recommends:     cryptsetup
# filesystem(btrfs)
Recommends:     btrfsprogs
%ifarch x86_64
Recommends:     efibootmgr
%endif
Recommends:     xf86-video-ati
Recommends:     xf86-video-cirrus
Recommends:     xf86-video-fbdev
Recommends:     xf86-video-intel
Recommends:     xf86-video-modesetting
Recommends:     xf86-video-neomagic
Recommends:     xf86-video-nv
Recommends:     xf86-video-qxl
Recommends:     xf86-video-v4l
Recommends:     xf86-video-vesa
Recommends:     xf86-video-vmware


%description rest_core_dvd
Packages that are on CD but not in other patterns.

%files rest_core_dvd
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/rest_core_dvd.txt

%package rest_dvd
%pattern_desktopfunctions
Summary:        Remaining Software
Group:          Metapackages
Provides:       pattern() = rest_dvd
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1980
Requires:       pattern() = apparmor
Requires:       pattern() = apparmor_opt
Requires:       pattern() = base
Requires:       pattern() = console
Requires:       pattern() = devel_C_C++
Requires:       pattern() = devel_basis
Requires:       pattern() = devel_gnome
Requires:       pattern() = devel_ide
Requires:       pattern() = devel_java
Requires:       pattern() = devel_kde
Requires:       pattern() = devel_kernel
Requires:       pattern() = devel_mono
Requires:       pattern() = devel_perl
Requires:       pattern() = devel_python
Requires:       pattern() = devel_qt4
Requires:       pattern() = devel_rpm_build
Requires:       pattern() = devel_ruby
Requires:       pattern() = devel_tcl
Requires:       pattern() = devel_web
Requires:       pattern() = dhcp_dns_server
Requires:       pattern() = directory_server
Requires:       pattern() = enhanced_base
Requires:       pattern() = enhanced_base_opt
Requires:       pattern() = file_server
Requires:       pattern() = fonts
Requires:       pattern() = fonts_opt
Requires:       pattern() = games
Requires:       pattern() = gateway_server
Requires:       pattern() = gnome
Requires:       pattern() = gnome_admin
Requires:       pattern() = gnome_basis
Requires:       pattern() = gnome_basis_opt
Requires:       pattern() = gnome_games
Requires:       pattern() = gnome_ide
Requires:       pattern() = gnome_imaging
Requires:       pattern() = gnome_imaging_opt
Requires:       pattern() = gnome_internet
Requires:       pattern() = gnome_laptop
Requires:       pattern() = gnome_multimedia
Requires:       pattern() = gnome_multimedia_opt
Requires:       pattern() = gnome_office
Requires:       pattern() = gnome_office_opt
Requires:       pattern() = gnome_utilities
Requires:       pattern() = gnome_yast
Requires:       pattern() = imaging
Requires:       pattern() = imaging_opt
Requires:       pattern() = kde
Requires:       pattern() = kde4
Requires:       pattern() = kde4_admin
Requires:       pattern() = kde4_basis
Requires:       pattern() = kde4_edutainment
Requires:       pattern() = kde4_games
Requires:       pattern() = kde4_ide
Requires:       pattern() = kde4_imaging
Requires:       pattern() = kde4_internet
Requires:       pattern() = kde4_laptop
Requires:       pattern() = kde4_multimedia
Requires:       pattern() = kde4_office
Requires:       pattern() = kde4_utilities
Requires:       pattern() = kde4_utilities_opt
Requires:       pattern() = kde4_yast
Requires:       pattern() = lamp_server
Requires:       pattern() = laptop
Requires:       pattern() = mail_server
Requires:       pattern() = misc_server
Requires:       pattern() = multimedia
Requires:       pattern() = multimedia_opt
Requires:       pattern() = network_admin
Requires:       pattern() = non_oss
Requires:       pattern() = office
Requires:       pattern() = office_opt
Requires:       pattern() = print_server
Requires:       pattern() = remote_desktop
Requires:       pattern() = sw_management
Requires:       pattern() = sw_management_gnome
Requires:       pattern() = sw_management_kde4
Requires:       pattern() = tabletpc
Requires:       pattern() = technical_writing
Requires:       pattern() = x11
Requires:       pattern() = x11_opt
# for now xen_server
Requires:       pattern() = xfce
Requires:       pattern() = xfce_basis
Requires:       pattern() = xfce_laptop
Requires:       pattern() = lxde
Requires:       pattern() = xfce_office
Requires:       pattern() = lxde_laptop
Requires:       pattern() = yast2_basis
Requires:       pattern() = yast2_install_wf
Recommends:     pattern() = x11_yast
Recommends:     pattern() = xen_server
Recommends:     pattern() = kvm_server
Recommends:     pattern() = minimal_base
Recommends:     pattern() = minimal_base-conflicts
Recommends:     pattern() = books
# from data/REST-DVD
# git hype (is a meta package dragging in everything else)
Recommends:     git
# qemu rocks
Recommends:     qemu
# needed for kiwi creation
Recommends:     kiwi-media-requires
Recommends:     squashfs
Recommends:     yast2-live-installer
Recommends:     gfxboot-devel
Recommends:     nbd
Recommends:     nbd-doc
Recommends:     kiwi-config-openSUSE
Recommends:     clicfs
## 306071
Recommends:     virtualbox
Recommends:     virtualbox-guest-kmp-default
Recommends:     vboxgtk
Recommends:     virtualbox-qt
# Internet Storage Name Service
Recommends:     yast2-isns
Recommends:     isns
# hylafax as requested by kkeil
Recommends:     hylafax
Recommends:     hylafax-client
Recommends:     capi4hylafax
# kiwi as requested by ms
Recommends:     kiwi
Recommends:     kiwi-desc-isoboot
Recommends:     kiwi-desc-netboot
Recommends:     kiwi-desc-oemboot
Recommends:     kiwi-desc-vmxboot
Recommends:     kiwi-pxeboot
Recommends:     kiwi-templates
# #301029
Recommends:     yast2-python-bindings
# kdump+tools
Recommends:     kdump
Recommends:     kexec-tools
Recommends:     yast2-kdump 
# #296387
Recommends:     xournal
# #297414, #304221
Recommends:     seamonkey
Recommends:     seamonkey-dom-inspector
Recommends:     seamonkey-irc
Recommends:     seamonkey-venkman
# feature 301945
Recommends:     yast2-add-on-creator
Recommends:     yast2-product-creator
Recommends:     createrepo
# kernel modules
Recommends:     omnibook-kmp-default
Recommends:     omnibook-kmp-xen
Recommends:     ndiswrapper-kmp-desktop
Recommends:     omnibook-kmp-desktop
Recommends:     vmware-guest-kmp-desktop
Recommends:     virtualbox-guest-kmp-desktop
# register your hardware
# no sync pattern
Recommends:     bluez-hcidump
Recommends:     libopensync-plugin-google-calendar
Recommends:     libopensync-plugin-moto
Recommends:     libopensync-plugin-python-module
Recommends:     libsyncml-tools
Recommends:     msynctool
Recommends:     unison
# could not find a better pattern
Recommends:     subversion-server
Recommends:     subversion-tools
Recommends:     sshfs
# FAX
Recommends:     capisuite
%ifarch ppc
# #381940
Recommends:     kernel-ppc64
# #387170
Recommends:     ps3-utils
Recommends:     gtkpbbuttons
Recommends:     pbbuttonsd
Recommends:     petitboot
Recommends:     powerprefs
%endif
# minimal korean support (bnc#390099)
Recommends:     unfonts
Recommends:     scim-hangul 
# #390825
Recommends:     kvm
# #391434
Recommends:     open-vm-tools
Recommends:     vmware-guest-kmp-default
# all kernel flavors we want to have
Recommends:     kernel-desktop
Recommends:     kernel-default
# bnc#431280 (Japanese fonts)
Recommends:     ttf-arphic-uming
# bnc#697047
Recommends:     siga
%ifarch x86_64 ppc
Recommends:     pam_krb5-32bit
Recommends:     pam_ldap-32bit
Recommends:     nss_ldap-32bit
%endif
%ifarch ppc64
Recommends:     pam_krb5-64bit
Recommends:     pam_ldap-64bit
Recommends:     nss_ldap-64bit
%endif
# bluncks 2nd baby
Recommends:     apport-gtk
Recommends:     apport-qt
# very special case - 442295
# supporting lib for non-oss
Recommends:     libstdc++33
Recommends:     qinternet
# meanwhile plugin (bnc#549711)
Recommends:     libpurple-meanwhile 
%ifarch x86_64
# bnc#581144
Recommends:     gtk2-32bit 
%endif
# bnc#605888
Recommends:     libvdpau1
# bnc#626952
Recommends:     quota-nfs
# dependencies of skype.rpm
Recommends:     libasound.so.2
Recommends:     libasound.so.2(ALSA_0.9)
Recommends:     libasound.so.2(ALSA_0.9.0rc4)
Recommends:     libc.so.6
Recommends:     libc.so.6(GLIBC_2.0)
Recommends:     libc.so.6(GLIBC_2.1)
Recommends:     libc.so.6(GLIBC_2.1.3)
Recommends:     libc.so.6(GLIBC_2.2)
Recommends:     libc.so.6(GLIBC_2.3)
Recommends:     libc.so.6(GLIBC_2.3.4)
Recommends:     libc.so.6(GLIBC_2.4)
Recommends:     libdbus-1.so.3
Recommends:     libdl.so.2
Recommends:     libdl.so.2(GLIBC_2.0)
Recommends:     libdl.so.2(GLIBC_2.1)
Recommends:     libfontconfig.so.1
Recommends:     libfreetype.so.6
Recommends:     libgcc_s.so.1
Recommends:     libgcc_s.so.1(GCC_3.0)
Recommends:     libgcc_s.so.1(GLIBC_2.0)
Recommends:     libglib-2.0.so.0
Recommends:     libgthread-2.0.so.0
Recommends:     libICE.so.6
Recommends:     libm.so.6
Recommends:     libm.so.6(GLIBC_2.0)
Recommends:     libpng12.so.0
Recommends:     libpthread.so.0
Recommends:     libpthread.so.0(GLIBC_2.0)
Recommends:     libpthread.so.0(GLIBC_2.1)
Recommends:     libpthread.so.0(GLIBC_2.2)
Recommends:     libpthread.so.0(GLIBC_2.3.2)
Recommends:     libQtCore.so.4
Recommends:     libQtDBus.so.4
Recommends:     libQtGui.so.4
Recommends:     libQtNetwork.so.4
Recommends:     libQtXml.so.4
Recommends:     librt.so.1
Recommends:     libSM.so.6
Recommends:     libstdc++.so.6
Recommends:     libstdc++.so.6(CXXABI_1.3)
Recommends:     libstdc++.so.6(GLIBCXX_3.4)
Recommends:     libstdc++.so.6(GLIBCXX_3.4.9)
Recommends:     libX11.so.6
Recommends:     libXcursor.so.1
Recommends:     libXext.so.6
Recommends:     libXfixes.so.3
Recommends:     libXinerama.so.1
Recommends:     libXi.so.6
Recommends:     libXrandr.so.2
Recommends:     libXrender.so.1
Recommends:     libXss.so.1
Recommends:     libXv.so.1
Recommends:     libz.so.1

# from data/REST-CD
%ifarch x86_64
Requires:       kernel-desktop
#else
Requires:       kernel-default
%endif
Requires:       kernel-firmware
# #327506
Recommends:     b43-fwcutter
# #304219
Recommends:     memtest86+
# adaptec-firmware (#298726)
Recommends:     adaptec-firmware
Recommends:     mpt-firmware
Recommends:     atmel-firmware
# DELL laptop support
Recommends:     smbios-utils-python
#lvm2 support (#301382)
Recommends:     lvm2
Recommends:     aspell-en
Recommends:     cifs-utils
Recommends:     input-utils
Recommends:     nss_ldap
Recommends:     pam_krb5
Recommends:     pam_ldap
Recommends:     krb5-client
# prefer the full version for installation
Recommends:     cracklib-dict-full
# filesystem(minix)
Recommends:     util-linux
# filesystem(ext2)
Recommends:     e2fsprogs
# filesystem(reiserfs)
Recommends:     reiserfs
# filesystem(jfs)
Recommends:     jfsutils
# filesystem(ntfs-3g)
Recommends:     ntfs-3g
# filesystem(xfs)
Recommends:     xfsprogs
# filesystem(vfat)
Recommends:     dosfstools
# crypto partitions
Recommends:     cryptsetup
# filesystem(btrfs)
Recommends:     btrfsprogs
%ifarch x86_64
# kernel modules
Recommends:     ndiswrapper-kmp-desktop
#else
Recommends:     ndiswrapper-kmp-default
%endif
# network
Recommends:     ndiswrapper
# bnc#548325
Recommends:     ipw-firmware
# supplements by modaliases
Recommends:     bluez-firmware
Recommends:     dvb
Recommends:     lomoco
Recommends:     pcmciautils
Recommends:     pam_fprint
# yast can configure quota - if present on medium (#348336)
Recommends:     quota
# enhances virtualbox speed (#365562)
Recommends:     virtualbox-guest-x11
# Firmware for ZD1211 based WLAN sticks
Recommends:     zd1211-firmware
# rescue
Recommends:     dd_rescue
# #396109
Recommends:     alsa-firmware
Recommends:     awesfx
# needed by yast2-storage for crypt partitions
Recommends:     pam_mount
# adding to LiveCD (bnc#419201)
Recommends:     rsync
Recommends:     smartmontools
# LiveCD accessible? (bnc#391327)
Recommends:     sbl
Recommends:     espeak
# give vim hates an editor
Recommends:     nano
# pull flash and mp3 also on livecd installs
Recommends:     pullin-fluendo-mp3
Recommends:     pullin-flash-player
# #494547 - just testing
Recommends:     manufacturer-PPDs
# needed to detect if a system is the same
Recommends:     dmidecode
# decompression to recover something
Recommends:     xz
Recommends:     zip
Recommends:     unzip
Recommends:     p7zip
# file system stuff
Recommends:     xfsdump
Recommends:     reiserfs
# fate#306643
Recommends:     mc 
# laptop stuff
Recommends:     irda
Recommends:     pcmciautils
Recommends:     wpa_supplicant
# bnc#480879
Recommends:     crda
Recommends:     wireless-regdb
Recommends:     iw
# bug#589416
Recommends:     virtualbox-guest-tools 
# bug#591085
Recommends:     open-vm-tools
# parted GUI
Recommends:     gparted
# bnc#728529
Recommends:     elilo
%ifarch x86_64
Recommends:     efibootmgr
%endif
# yast2-bootloader still suggests it (bnc#803401)
Recommends:     grub
# Backup and Copying utilites
Recommends:     gnu_ddrescue
Recommends:     lftp
Recommends:     grsync
# all xf86 drivers
Recommends:     xf86-video-ark
Recommends:     xf86-video-ast
Recommends:     xf86-video-ati
Recommends:     xf86-video-chips
Recommends:     xf86-video-cirrus
Recommends:     xf86-video-dummy
Recommends:     xf86-video-fbdev
Recommends:     xf86-video-glint
Recommends:     xf86-video-i128
Recommends:     xf86-video-intel
Recommends:     xf86-video-mach64
Recommends:     xf86-video-mga
Recommends:     xf86-video-modesetting
Recommends:     xf86-video-neomagic
Recommends:     xf86-video-nv
Recommends:     xf86-video-qxl
Recommends:     xf86-video-r128
Recommends:     xf86-video-savage
Recommends:     xf86-video-siliconmotion
Recommends:     xf86-video-sis
Recommends:     xf86-video-sisusb
Recommends:     xf86-video-tdfx
Recommends:     xf86-video-tga
Recommends:     xf86-video-v4l
Recommends:     xf86-video-vesa
Recommends:     xf86-video-vmware
Recommends:     xf86-video-voodoo

# from data/REST-DVD-SUGGESTS
# generated in the spec file

# from data/REST-DVD-RPMLIST
Requires:       cracklib-dict-full
Requires:       ttf-arphic-uming
Requires:       IPAGothic
Requires:       KhmerOS-fonts
Requires:       fonts-arabic
Requires:       fonts-thai
Requires:       indic-fonts
Requires:       lklug
Requires:       unfonts
Requires:       yast2-trans-af
Requires:       yast2-trans-ar
Requires:       yast2-trans-bg
Requires:       yast2-trans-bn
Requires:       yast2-trans-bs
Requires:       yast2-trans-ca
Requires:       yast2-trans-cs
Requires:       yast2-trans-cy
Requires:       yast2-trans-da
Requires:       yast2-trans-de
Requires:       yast2-trans-el
Requires:       yast2-trans-en_GB
Requires:       yast2-trans-en_US
Requires:       yast2-trans-es
Requires:       yast2-trans-et
Requires:       yast2-trans-fa
Requires:       yast2-trans-fi
Requires:       yast2-trans-fr
Requires:       yast2-trans-gl
Requires:       yast2-trans-gu
Requires:       yast2-trans-hi
Requires:       yast2-trans-hr
Requires:       yast2-trans-hu
Requires:       yast2-trans-id
Requires:       yast2-trans-it
Requires:       yast2-trans-ja
Requires:       yast2-trans-jv
Requires:       yast2-trans-ka
Requires:       yast2-trans-km
Requires:       yast2-trans-ko
Requires:       yast2-trans-lo
Requires:       yast2-trans-lt
Requires:       yast2-trans-mk
Requires:       yast2-trans-mr
Requires:       yast2-trans-nb
Requires:       yast2-trans-nl
Requires:       yast2-trans-pa
Requires:       yast2-trans-pl
Requires:       yast2-trans-pt
Requires:       yast2-trans-pt_BR
Requires:       yast2-trans-ro
Requires:       yast2-trans-ru
Requires:       yast2-trans-si
Requires:       yast2-trans-sk
Requires:       yast2-trans-sl
Requires:       yast2-trans-sr
Requires:       yast2-trans-sv
Requires:       yast2-trans-ta
Requires:       yast2-trans-th
Requires:       yast2-trans-tr
Requires:       yast2-trans-uk
Requires:       yast2-trans-vi
Requires:       yast2-trans-wa
Requires:       yast2-trans-xh
Requires:       yast2-trans-zh_CN
Requires:       yast2-trans-zh_TW
Requires:       yast2-trans-zu


%description rest_dvd
Packages that are on CD but not in other patterns.

%files rest_dvd
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/rest_dvd.txt

%package rest_dvd9
%pattern_desktopfunctions
Summary:        Remaining Software
Group:          Metapackages
Provides:       pattern() = rest_dvd9
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 3500
Requires:       pattern() = rest_dvd
Recommends:     pattern() = x11_yast
Recommends:     pattern() = xen_server
Recommends:     pattern() = kvm_server
Recommends:     pattern() = 32bit
Recommends:     pattern() = 64bit
Recommends:     pattern() = apparmor
Recommends:     pattern() = apparmor_opt
Recommends:     pattern() = base
Recommends:     pattern() = console
Recommends:     pattern() = devel_basis
Recommends:     pattern() = devel_C_C++
Recommends:     pattern() = devel_gnome
Recommends:     pattern() = devel_ide
Recommends:     pattern() = devel_java
Recommends:     pattern() = devel_kde
Recommends:     pattern() = devel_kernel
Recommends:     pattern() = devel_mono
Recommends:     pattern() = devel_perl
Recommends:     pattern() = devel_python
Recommends:     pattern() = devel_python3
Recommends:     pattern() = devel_qt4
Recommends:     pattern() = devel_rpm_build
Recommends:     pattern() = devel_ruby
Recommends:     pattern() = devel_tcl
Recommends:     pattern() = devel_web
Recommends:     pattern() = devel_yast
Recommends:     pattern() = dhcp_dns_server
Recommends:     pattern() = directory_server
Recommends:     pattern() = enhanced_base
Recommends:     pattern() = enhanced_base_opt
Recommends:     pattern() = file_server
Recommends:     pattern() = fonts
Recommends:     pattern() = fonts_opt
Recommends:     pattern() = games
Recommends:     pattern() = gateway_server
Recommends:     pattern() = gnome
Recommends:     pattern() = gnome_admin
Recommends:     pattern() = gnome_basis
Recommends:     pattern() = gnome_basis_opt
Recommends:     pattern() = gnome_games
Recommends:     pattern() = gnome_ide
Recommends:     pattern() = gnome_imaging
Recommends:     pattern() = gnome_imaging_opt
Recommends:     pattern() = gnome_internet
Recommends:     pattern() = gnome_laptop
Recommends:     pattern() = gnome_multimedia
Recommends:     pattern() = gnome_multimedia_opt
Recommends:     pattern() = gnome_office
Recommends:     pattern() = gnome_office_opt
Recommends:     pattern() = gnome_utilities
Recommends:     pattern() = gnome_yast
Recommends:     pattern() = imaging
Recommends:     pattern() = imaging_opt
Recommends:     pattern() = kde
Recommends:     pattern() = kde4
Recommends:     pattern() = kde4_admin
Recommends:     pattern() = kde4_basis
Recommends:     pattern() = kde4_edutainment
Recommends:     pattern() = kde4_games
Recommends:     pattern() = kde4_ide
Recommends:     pattern() = kde4_imaging
Recommends:     pattern() = kde4_internet
Recommends:     pattern() = kde4_laptop
Recommends:     pattern() = kde4_multimedia
Recommends:     pattern() = kde4_office
Recommends:     pattern() = kde4_utilities
Recommends:     pattern() = kde4_utilities_opt
Recommends:     pattern() = kde4_yast
Recommends:     pattern() = lamp_server
Recommends:     pattern() = laptop
Recommends:     pattern() = lxde
Recommends:     pattern() = lxde_laptop
Recommends:     pattern() = lxde_office
Recommends:     pattern() = mail_server
Recommends:     pattern() = misc_server
Recommends:     pattern() = multimedia
Recommends:     pattern() = multimedia_opt
Recommends:     pattern() = network_admin
Recommends:     pattern() = non_oss
Recommends:     pattern() = non_oss_opt
Recommends:     pattern() = office
Recommends:     pattern() = office_opt
Recommends:     pattern() = print_server
Recommends:     pattern() = remote_desktop
Recommends:     pattern() = rest_cd_gnome
Recommends:     pattern() = rest_cd_kde4
Recommends:     pattern() = rest_cd_x11
Recommends:     pattern() = rest_dvd
Recommends:     pattern() = rest_dvd9
Recommends:     pattern() = rest_promo_dvd
Recommends:     pattern() = sw_management
Recommends:     pattern() = sw_management_gnome
Recommends:     pattern() = sw_management_kde4
Recommends:     pattern() = tabletpc
Recommends:     pattern() = technical_writing
Recommends:     pattern() = voip
Recommends:     pattern() = x11
Recommends:     pattern() = x11_opt
Recommends:     pattern() = x11_yast
Recommends:     pattern() = x86
Recommends:     pattern() = xen_server
Recommends:     pattern() = xfce
Recommends:     pattern() = xfce_basis
Recommends:     pattern() = xfce_laptop
Recommends:     pattern() = xfce_office
Recommends:     pattern() = yast2_basis
Recommends:     pattern() = yast2_install_wf
# from data/REST-DVD9
Recommends:     netbeans
Recommends:     javamail-javadoc                               
Recommends:     IPAMincho                                           
Recommends:     IPAPGothic                                          
Recommends:     IPAPMincho                                          
Recommends:     bitstream-vera                                      
Recommends:     texlive-cjk
Recommends:     texlive-xetex
Recommends:     texlive-context
Recommends:     desktop-data-openSUSE-extra
Recommends:     xorg-x11-driver-video-radeonhd
Recommends:     netbeans
Recommends:     z88
Recommends:     lilypond-documentation
Recommends:     openclipart-png
Recommends:     libqt4-devel-doc-data


%description rest_dvd9
Packages that are on CD but not in other patterns.

%files rest_dvd9
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/rest_dvd9.txt

%package rest_promo_dvd
%pattern_desktopfunctions
Summary:        Remaining Software
Group:          Metapackages
Provides:       pattern() = rest_promo_dvd
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1981
Requires:       pattern() = apparmor
Requires:       pattern() = base
Requires:       pattern() = console
Requires:       pattern() = devel_basis
Requires:       pattern() = devel_C_C++
Requires:       pattern() = devel_rpm_build
Requires:       pattern() = dhcp_dns_server
Requires:       pattern() = directory_server
Requires:       pattern() = enhanced_base
Requires:       pattern() = enhanced_base_opt
Requires:       pattern() = file_server
Requires:       pattern() = fonts
Requires:       pattern() = games
Requires:       pattern() = gateway_server
Requires:       pattern() = gnome
Requires:       pattern() = gnome_admin
Requires:       pattern() = gnome_basis
Requires:       pattern() = gnome_games
Requires:       pattern() = gnome_ide
Requires:       pattern() = gnome_imaging
Requires:       pattern() = gnome_internet
Requires:       pattern() = gnome_laptop
Requires:       pattern() = gnome_multimedia
Requires:       pattern() = gnome_office
Requires:       pattern() = gnome_utilities
Requires:       pattern() = gnome_yast
Requires:       pattern() = imaging
Requires:       pattern() = imaging_opt
Requires:       pattern() = kde
Requires:       pattern() = kde4
Requires:       pattern() = kde4_admin
Requires:       pattern() = kde4_basis
Requires:       pattern() = kde4_edutainment
Requires:       pattern() = kde4_games
Requires:       pattern() = kde4_ide
Requires:       pattern() = kde4_imaging
Requires:       pattern() = kde4_internet
Requires:       pattern() = kde4_laptop
Requires:       pattern() = kde4_multimedia
Requires:       pattern() = kde4_office
Requires:       pattern() = kde4_utilities
Requires:       pattern() = kde4_yast
Requires:       pattern() = laptop
Requires:       pattern() = lxde
Requires:       pattern() = lxde_laptop
Requires:       pattern() = mail_server
Requires:       pattern() = misc_server
Requires:       pattern() = multimedia
Requires:       pattern() = network_admin
Requires:       pattern() = non_oss
Requires:       pattern() = office
Requires:       pattern() = remote_desktop
Requires:       pattern() = sw_management
Requires:       pattern() = sw_management_gnome
Requires:       pattern() = sw_management_kde4
Requires:       pattern() = x11
Requires:       pattern() = x11_opt
Requires:       pattern() = xfce
Requires:       pattern() = xfce_basis
Requires:       pattern() = xfce_laptop
Requires:       pattern() = xfce_office
Requires:       pattern() = yast2_basis
Requires:       pattern() = yast2_install_wf
Recommends:     pattern() = voip
Recommends:     pattern() = x11_yast
# from data/REST-DVD
# git hype (is a meta package dragging in everything else)
Recommends:     git
# qemu rocks
Recommends:     qemu
# needed for kiwi creation
Recommends:     kiwi-media-requires
Recommends:     squashfs
Recommends:     yast2-live-installer
Recommends:     gfxboot-devel
Recommends:     nbd
Recommends:     nbd-doc
Recommends:     kiwi-config-openSUSE
Recommends:     clicfs
## 306071
Recommends:     virtualbox
Recommends:     virtualbox-guest-kmp-default
Recommends:     vboxgtk
Recommends:     virtualbox-qt
# Internet Storage Name Service
Recommends:     yast2-isns
Recommends:     isns
# hylafax as requested by kkeil
Recommends:     hylafax
Recommends:     hylafax-client
Recommends:     capi4hylafax
# kiwi as requested by ms
Recommends:     kiwi
Recommends:     kiwi-desc-isoboot
Recommends:     kiwi-desc-netboot
Recommends:     kiwi-desc-oemboot
Recommends:     kiwi-desc-vmxboot
Recommends:     kiwi-pxeboot
Recommends:     kiwi-templates
# #301029
Recommends:     yast2-python-bindings
# kdump+tools
Recommends:     kdump
Recommends:     kexec-tools
Recommends:     yast2-kdump 
# #296387
Recommends:     xournal
# #297414, #304221
Recommends:     seamonkey
Recommends:     seamonkey-dom-inspector
Recommends:     seamonkey-irc
Recommends:     seamonkey-venkman
# feature 301945
Recommends:     yast2-add-on-creator
Recommends:     yast2-product-creator
Recommends:     createrepo
# kernel modules
Recommends:     omnibook-kmp-default
Recommends:     omnibook-kmp-xen
Recommends:     ndiswrapper-kmp-desktop
Recommends:     omnibook-kmp-desktop
Recommends:     vmware-guest-kmp-desktop
Recommends:     virtualbox-guest-kmp-desktop
# register your hardware
# no sync pattern
Recommends:     bluez-hcidump
Recommends:     libopensync-plugin-google-calendar
Recommends:     libopensync-plugin-moto
Recommends:     libopensync-plugin-python-module
Recommends:     libsyncml-tools
Recommends:     msynctool
Recommends:     unison
# could not find a better pattern
Recommends:     subversion-server
Recommends:     subversion-tools
Recommends:     sshfs
# FAX
Recommends:     capisuite
%ifarch ppc
# #381940
Recommends:     kernel-ppc64
# #387170
Recommends:     ps3-utils
Recommends:     gtkpbbuttons
Recommends:     pbbuttonsd
Recommends:     petitboot
Recommends:     powerprefs
%endif
# minimal korean support (bnc#390099)
Recommends:     unfonts
Recommends:     scim-hangul 
# #390825
Recommends:     kvm
# #391434
Recommends:     open-vm-tools
Recommends:     vmware-guest-kmp-default
# all kernel flavors we want to have
Recommends:     kernel-desktop
Recommends:     kernel-default
# bnc#431280 (Japanese fonts)
Recommends:     ttf-arphic-uming
# bnc#697047
Recommends:     siga
%ifarch x86_64 ppc
Recommends:     pam_krb5-32bit
Recommends:     pam_ldap-32bit
Recommends:     nss_ldap-32bit
%endif
%ifarch ppc64
Recommends:     pam_krb5-64bit
Recommends:     pam_ldap-64bit
Recommends:     nss_ldap-64bit
%endif
# bluncks 2nd baby
Recommends:     apport-gtk
Recommends:     apport-qt
# very special case - 442295
# supporting lib for non-oss
Recommends:     libstdc++33
Recommends:     qinternet
# meanwhile plugin (bnc#549711)
Recommends:     libpurple-meanwhile 
%ifarch x86_64
# bnc#581144
Recommends:     gtk2-32bit 
%endif
# bnc#605888
Recommends:     libvdpau1
# bnc#626952
Recommends:     quota-nfs
# dependencies of skype.rpm
Recommends:     libasound.so.2
Recommends:     libasound.so.2(ALSA_0.9)
Recommends:     libasound.so.2(ALSA_0.9.0rc4)
Recommends:     libc.so.6
Recommends:     libc.so.6(GLIBC_2.0)
Recommends:     libc.so.6(GLIBC_2.1)
Recommends:     libc.so.6(GLIBC_2.1.3)
Recommends:     libc.so.6(GLIBC_2.2)
Recommends:     libc.so.6(GLIBC_2.3)
Recommends:     libc.so.6(GLIBC_2.3.4)
Recommends:     libc.so.6(GLIBC_2.4)
Recommends:     libdbus-1.so.3
Recommends:     libdl.so.2
Recommends:     libdl.so.2(GLIBC_2.0)
Recommends:     libdl.so.2(GLIBC_2.1)
Recommends:     libfontconfig.so.1
Recommends:     libfreetype.so.6
Recommends:     libgcc_s.so.1
Recommends:     libgcc_s.so.1(GCC_3.0)
Recommends:     libgcc_s.so.1(GLIBC_2.0)
Recommends:     libglib-2.0.so.0
Recommends:     libgthread-2.0.so.0
Recommends:     libICE.so.6
Recommends:     libm.so.6
Recommends:     libm.so.6(GLIBC_2.0)
Recommends:     libpng12.so.0
Recommends:     libpthread.so.0
Recommends:     libpthread.so.0(GLIBC_2.0)
Recommends:     libpthread.so.0(GLIBC_2.1)
Recommends:     libpthread.so.0(GLIBC_2.2)
Recommends:     libpthread.so.0(GLIBC_2.3.2)
Recommends:     libQtCore.so.4
Recommends:     libQtDBus.so.4
Recommends:     libQtGui.so.4
Recommends:     libQtNetwork.so.4
Recommends:     libQtXml.so.4
Recommends:     librt.so.1
Recommends:     libSM.so.6
Recommends:     libstdc++.so.6
Recommends:     libstdc++.so.6(CXXABI_1.3)
Recommends:     libstdc++.so.6(GLIBCXX_3.4)
Recommends:     libstdc++.so.6(GLIBCXX_3.4.9)
Recommends:     libX11.so.6
Recommends:     libXcursor.so.1
Recommends:     libXext.so.6
Recommends:     libXfixes.so.3
Recommends:     libXinerama.so.1
Recommends:     libXi.so.6
Recommends:     libXrandr.so.2
Recommends:     libXrender.so.1
Recommends:     libXss.so.1
Recommends:     libXv.so.1
Recommends:     libz.so.1

# from data/REST-CD
%ifarch x86_64
Requires:       kernel-desktop
#else
Requires:       kernel-default
%endif
Requires:       kernel-firmware
# #327506
Recommends:     b43-fwcutter
# #304219
Recommends:     memtest86+
# adaptec-firmware (#298726)
Recommends:     adaptec-firmware
Recommends:     mpt-firmware
Recommends:     atmel-firmware
# DELL laptop support
Recommends:     smbios-utils-python
#lvm2 support (#301382)
Recommends:     lvm2
Recommends:     aspell-en
Recommends:     cifs-utils
Recommends:     input-utils
Recommends:     nss_ldap
Recommends:     pam_krb5
Recommends:     pam_ldap
Recommends:     krb5-client
# prefer the full version for installation
Recommends:     cracklib-dict-full
# filesystem(minix)
Recommends:     util-linux
# filesystem(ext2)
Recommends:     e2fsprogs
# filesystem(reiserfs)
Recommends:     reiserfs
# filesystem(jfs)
Recommends:     jfsutils
# filesystem(ntfs-3g)
Recommends:     ntfs-3g
# filesystem(xfs)
Recommends:     xfsprogs
# filesystem(vfat)
Recommends:     dosfstools
# crypto partitions
Recommends:     cryptsetup
# filesystem(btrfs)
Recommends:     btrfsprogs
%ifarch x86_64
# kernel modules
Recommends:     ndiswrapper-kmp-desktop
#else
Recommends:     ndiswrapper-kmp-default
%endif
# network
Recommends:     ndiswrapper
# bnc#548325
Recommends:     ipw-firmware
# supplements by modaliases
Recommends:     bluez-firmware
Recommends:     dvb
Recommends:     lomoco
Recommends:     pcmciautils
Recommends:     pam_fprint
# yast can configure quota - if present on medium (#348336)
Recommends:     quota
# enhances virtualbox speed (#365562)
Recommends:     virtualbox-guest-x11
# Firmware for ZD1211 based WLAN sticks
Recommends:     zd1211-firmware
# rescue
Recommends:     dd_rescue
# #396109
Recommends:     alsa-firmware
Recommends:     awesfx
# needed by yast2-storage for crypt partitions
Recommends:     pam_mount
# adding to LiveCD (bnc#419201)
Recommends:     rsync
Recommends:     smartmontools
# LiveCD accessible? (bnc#391327)
Recommends:     sbl
Recommends:     espeak
# give vim hates an editor
Recommends:     nano
# pull flash and mp3 also on livecd installs
Recommends:     pullin-fluendo-mp3
Recommends:     pullin-flash-player
# #494547 - just testing
Recommends:     manufacturer-PPDs
# needed to detect if a system is the same
Recommends:     dmidecode
# decompression to recover something
Recommends:     xz
Recommends:     zip
Recommends:     unzip
Recommends:     p7zip
# file system stuff
Recommends:     xfsdump
Recommends:     reiserfs
# fate#306643
Recommends:     mc 
# laptop stuff
Recommends:     irda
Recommends:     pcmciautils
Recommends:     wpa_supplicant
# bnc#480879
Recommends:     crda
Recommends:     wireless-regdb
Recommends:     iw
# bug#589416
Recommends:     virtualbox-guest-tools 
# bug#591085
Recommends:     open-vm-tools
# parted GUI
Recommends:     gparted
# bnc#728529
Recommends:     elilo
%ifarch x86_64
Recommends:     efibootmgr
%endif
# yast2-bootloader still suggests it (bnc#803401)
Recommends:     grub
# Backup and Copying utilites
Recommends:     gnu_ddrescue
Recommends:     lftp
Recommends:     grsync
# all xf86 drivers
Recommends:     xf86-video-ark
Recommends:     xf86-video-ast
Recommends:     xf86-video-ati
Recommends:     xf86-video-chips
Recommends:     xf86-video-cirrus
Recommends:     xf86-video-dummy
Recommends:     xf86-video-fbdev
Recommends:     xf86-video-glint
Recommends:     xf86-video-i128
Recommends:     xf86-video-intel
Recommends:     xf86-video-mach64
Recommends:     xf86-video-mga
Recommends:     xf86-video-modesetting
Recommends:     xf86-video-neomagic
Recommends:     xf86-video-nv
Recommends:     xf86-video-qxl
Recommends:     xf86-video-r128
Recommends:     xf86-video-savage
Recommends:     xf86-video-siliconmotion
Recommends:     xf86-video-sis
Recommends:     xf86-video-sisusb
Recommends:     xf86-video-tdfx
Recommends:     xf86-video-tga
Recommends:     xf86-video-v4l
Recommends:     xf86-video-vesa
Recommends:     xf86-video-vmware
Recommends:     xf86-video-voodoo

# from data/REST-DVD-RPMLIST
Requires:       cracklib-dict-full
Requires:       ttf-arphic-uming
Requires:       IPAGothic
Requires:       KhmerOS-fonts
Requires:       fonts-arabic
Requires:       fonts-thai
Requires:       indic-fonts
Requires:       lklug
Requires:       unfonts
Requires:       yast2-trans-af
Requires:       yast2-trans-ar
Requires:       yast2-trans-bg
Requires:       yast2-trans-bn
Requires:       yast2-trans-bs
Requires:       yast2-trans-ca
Requires:       yast2-trans-cs
Requires:       yast2-trans-cy
Requires:       yast2-trans-da
Requires:       yast2-trans-de
Requires:       yast2-trans-el
Requires:       yast2-trans-en_GB
Requires:       yast2-trans-en_US
Requires:       yast2-trans-es
Requires:       yast2-trans-et
Requires:       yast2-trans-fa
Requires:       yast2-trans-fi
Requires:       yast2-trans-fr
Requires:       yast2-trans-gl
Requires:       yast2-trans-gu
Requires:       yast2-trans-hi
Requires:       yast2-trans-hr
Requires:       yast2-trans-hu
Requires:       yast2-trans-id
Requires:       yast2-trans-it
Requires:       yast2-trans-ja
Requires:       yast2-trans-jv
Requires:       yast2-trans-ka
Requires:       yast2-trans-km
Requires:       yast2-trans-ko
Requires:       yast2-trans-lo
Requires:       yast2-trans-lt
Requires:       yast2-trans-mk
Requires:       yast2-trans-mr
Requires:       yast2-trans-nb
Requires:       yast2-trans-nl
Requires:       yast2-trans-pa
Requires:       yast2-trans-pl
Requires:       yast2-trans-pt
Requires:       yast2-trans-pt_BR
Requires:       yast2-trans-ro
Requires:       yast2-trans-ru
Requires:       yast2-trans-si
Requires:       yast2-trans-sk
Requires:       yast2-trans-sl
Requires:       yast2-trans-sr
Requires:       yast2-trans-sv
Requires:       yast2-trans-ta
Requires:       yast2-trans-th
Requires:       yast2-trans-tr
Requires:       yast2-trans-uk
Requires:       yast2-trans-vi
Requires:       yast2-trans-wa
Requires:       yast2-trans-xh
Requires:       yast2-trans-zh_CN
Requires:       yast2-trans-zh_TW
Requires:       yast2-trans-zu


%description rest_promo_dvd
Packages that are on CD but not in other patterns.

%files rest_promo_dvd
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/rest_promo_dvd.txt

%package sw_management
%pattern_basetechnologies
Summary:        Software Management
Group:          Metapackages
Provides:       pattern() = sw_management
Provides:       pattern-icon() = yast-sw_single
Provides:       pattern-order() = 1360
Recommends:     pattern() = sw_management_x11
# from data/SW-MANGEMENT
Requires:       zypper
Suggests:       pin


%description sw_management
This pattern provides a graphical application and a command line tool for keeping your system up to date.

%files sw_management
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/sw_management.txt

%package sw_management_gnome
%pattern_basetechnologies
Summary:        Package Management - Graphical Tools for GNOME
Group:          Metapackages
Provides:       pattern() = sw_management_gnome
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1780
Provides:       pattern-extends() = sw_management
Supplements:    packageand(patterns-openSUSE-gnome_basis:patterns-openSUSE-sw_management)
Requires:       pattern() = sw_management
Requires:       pattern() = x11
# from data/SW-MANGEMENT-GNOME
Recommends:     gnome-packagekit
Suggests:       libyui-gtk-pkg


%description sw_management_gnome
Package Management - Graphical Tools

%files sw_management_gnome
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/sw_management_gnome.txt

%package sw_management_kde4
%pattern_basetechnologies
Summary:        Package Management - Graphical Tools for KDE
Group:          Metapackages
Provides:       pattern() = sw_management_kde4
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1820
Provides:       pattern-extends() = sw_management
Supplements:    packageand(patterns-openSUSE-kde4_basis:patterns-openSUSE-sw_management)
Requires:       pattern() = sw_management
Requires:       pattern() = x11
# from data/SW-MANGEMENT-KDE4
Recommends:     apper
Suggests:       libyui-qt-pkg


%description sw_management_kde4
Package Management - Graphical Tools

%files sw_management_kde4
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/sw_management_kde4.txt

%package tabletpc
%pattern_basetechnologies
Summary:        TabletPC
Group:          Metapackages
Provides:       pattern() = tabletpc
Provides:       pattern-icon() = pattern-laptop
Provides:       pattern-order() = 2043
Requires:       pattern() = basesystem
# from data/TABLETPC
Recommends:     cellwriter
Recommends:     xorg-x11-driver-input
Recommends:     wacom-kmp
Recommends:     xournal
Recommends:     xstroke
Recommends:     eekboard


%description tabletpc
Tools designed specifically for use with TabletPCs.

%files tabletpc
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/tabletpc.txt

%package technical_writing
%pattern_desktopfunctions
Summary:        Technical Writing
Group:          Metapackages
Provides:       pattern() = technical_writing
Provides:       pattern-icon() = yast-messages
Provides:       pattern-order() = 2000
# from data/TECHNICAL-WRITING
Recommends:     nxml-mode
Recommends:     xmlto
Recommends:     docbook-dsssl-stylesheets
Recommends:     docbook-xsl-stylesheets
Recommends:     psutils
Recommends:     emacs
Recommends:     emacs-x11
Recommends:     xmlgraphics-fop
Recommends:     svg-schema
Recommends:     xslide
# General XML Packages
Recommends:     xmlgraphics-batik
Recommends:     dia
Recommends:     inkscape
Recommends:     mxml
Recommends:     sablot
Recommends:     saxon
#LATER xmlroff
Recommends:     xmlformat
Recommends:     xmlstarlet
# Packages Specific to DocBook
Recommends:     dbsplit-tools
#LATER docbook2odf
Recommends:     docbook_5
Recommends:     docbook5-xsl-stylesheets
Recommends:     docbook-xml-website
#LATER doclifter
Recommends:     susedoc
#LATER texi2db
#LATER wt2db
# Text Encoding Initiative
Recommends:     tei-xsl-stylesheets
Recommends:     tei-roma
Recommends:     texlive-scheme-tetex
Suggests:       lyx
Suggests:       texlive-cjk
Suggests:       texlive-metapost
Suggests:       texlive-omega
Suggests:       texlive-xetex
Suggests:       texlive-context
Suggests:       texlive-omega
Suggests:       texlive-xetex
Suggests:       texlive-tools
Suggests:       texlive-latex-doc
Suggests:       texlive-doc
# 441536
Suggests:       djvulibre


%description technical_writing
Authoring tools and editors for creating technical documentation.

%files technical_writing
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/technical_writing.txt

%package update_test
%pattern_basetechnologies
Summary:        Tests for the Update Stack
Group:          Metapackages
Provides:       pattern() = update_test
Provides:       pattern-icon() = yast-update
Provides:       pattern-order() = 1380
# from data/UPDATE-TEST
Recommends:     update-test-trival
Recommends:     update-test-affects-package-manager
Recommends:     update-test-security
Recommends:     update-test-interactive
Recommends:     update-test-optional
Recommends:     update-test-reboot-needed


%description update_test
Packages used for testing that the update stack works.  These tiny packages do not have any functionality themselves.

%files update_test
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/update_test.txt

%package voip
%pattern_desktopfunctions
Summary:        Voice Over IP Clients
Group:          Metapackages
Provides:       pattern() = voip
Provides:       pattern-icon() = yast-isdn
Provides:       pattern-order() = 2020
Requires:       pattern() = x11
# from data/VOIP
Recommends:     ekiga
Suggests:       kiax
Suggests:       linphone
Suggests:       mangler
Suggests:       twinkle


%description voip
Client applications for Internet telephony.

%files voip
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/voip.txt

%package x11
%pattern_graphicalenvironments
Summary:        X Window System
Group:          Metapackages
Provides:       pattern() = x11
Provides:       pattern-icon() = yast-x11
Provides:       pattern-order() = 1700
Requires:       pattern() = basesystem
Requires:       pattern() = enhanced_base
Requires:       pattern() = fonts
Recommends:     pattern() = x11_opt
Recommends:     pattern() = x11_yast
# from data/X11
Recommends:     xorg-x11-essentials
Recommends:     xkeyboard-config
Recommends:     xorg-x11-server
%ifarch x86_64
Recommends:     nss-mdns-32bit
%endif
# needed e.g. for nvidia drivers
Recommends:     x11-tools
Recommends:     xterm
Recommends:     ghostscript-x11
Recommends:     openssh-askpass
Recommends:     tightvnc
Recommends:     xorg-x11-driver-input
Recommends:     xorg-x11-driver-video
Recommends:     xorg-x11-libX11-ccache
# provides e.g. xdm
Recommends:     xorg-x11-essentials
Recommends:     xorg-x11-Xvnc
# people love having numlock configurable
Recommends:     numlockx
# improve glxinfo output (#301647)
Recommends:     freeglut
# #302566
Recommends:     x11-tools
# #353229 - drag in empty replacements
Recommends:     translation-update
# interesting for workstations too
%ifarch %ix86 x86_64
Recommends:     suspend
%endif
# chooce icewm-lite if you have a choice
Recommends:     icewm-lite
Recommends:     xorg-x11-xauth
# required by others
Suggests:       icewm-default
Suggests:       icewm-gnome
Suggests:       wine
Suggests:       fvwm2
Suggests:       fvwm-themes
Suggests:       wpa_supplicant-gui
Suggests:       xchat
Suggests:       gv
Suggests:       gvim
Suggests:       mmv
Suggests:       pmidi
Suggests:       xine-ui
Suggests:       xosview
# on security probation
Suggests:       xpdf-poppler
Suggests:       xosd
# #394406
Suggests:       desktop-data-openSUSE-extra
Suggests:       xorg-x11-driver-video-radeonhd
Suggests:       xorg-x11-driver-video-unichrome


%description x11
The X Window System provides the only standard platform-independent networked graphical window system bridging the heterogeneous platforms in today's enterprise: from network servers to desktops, thin clients, laptops, and handhelds, independent of operating system and hardware.

%files x11
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/x11.txt

%package x11_opt
%pattern_graphicalenvironments
Summary:        X Window System
Group:          Metapackages
Provides:       pattern() = x11_opt
Provides:       pattern-icon() = yast-x11
Provides:       pattern-order() = 1680
Provides:       pattern-extends() = x11
Requires:       pattern() = basesystem
Requires:       pattern() = enhanced_base
Requires:       pattern() = fonts
# from data/X11-OPT
Recommends:     freeglut
Recommends:     xdmbgrd
Recommends:     xtermset
Suggests:       tk
Suggests:       unclutter
Suggests:       xlockmore
Suggests:       WindowMaker
Suggests:       WindowMaker-applets
Suggests:       WindowMaker-themes
Suggests:       MozillaThunderbird
# #389816
Suggests:       xorg-x11-server-sdk


%description x11_opt
The X Window System provides the only standard platform-independent networked graphical window system bridging the heterogeneous platforms in today's enterprise: from network servers to desktops, thin clients, laptops, and handhelds, independent of operating system and hardware.

%files x11_opt
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/x11_opt.txt

%package x11_yast
%pattern_basetechnologies
Summary:        YaST User Interfaces
Group:          Metapackages
Provides:       pattern() = x11_yast
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1320
Provides:       pattern-extends() = yast2_basis
Supplements:    packageand(patterns-openSUSE-x11:patterns-openSUSE-yast2_basis)
Conflicts:      pattern() = gnome
Conflicts:      pattern() = kde4
# from data/X11-YaST
Recommends:     libyui-qt-pkg
Recommends:     yast2-control-center-qt
# yast modules for the desktop
Recommends:     yast2-scanner
Recommends:     yast2-tv


%description x11_yast
Graphical YaST user interfaces for minimal X desktop.

%files x11_yast
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/x11_yast.txt

%package x86
%pattern_basetechnologies
Summary:        x86 Runtime Environment
Group:          Metapackages
Provides:       pattern() = x86
Provides:       pattern-icon() = yast-misc
Provides:       pattern-order() = 1180

%description x86
This will install the 32-bit variant of all selected patterns. This allows to execute 32-bit software.

%files x86
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/x86.txt

%package xen_server
%pattern_serverfunctions
Summary:        Xen Virtual Machine Host Server
Group:          Metapackages
Provides:       pattern() = xen_server
Provides:       pattern-icon() = yast-uml
Provides:       pattern-order() = 3080
Requires:       pattern() = basesystem
# from data/XEN
Recommends:     bridge-utils
Recommends:     vm-install
Recommends:     xen
Recommends:     xen-libs
Recommends:     xen-tools
%ifarch x86_64 %ix86
Recommends:     kernel-xen
%endif
Recommends:     virt-manager
Recommends:     xen-doc-html
Recommends:     xterm
Recommends:     yast2-vm
Recommends:     virt-viewer
Recommends:     libvirt-daemon-xen
# #382423
Suggests:       install-initrd
Suggests:       libvirt


%description xen_server
Software to set up a server for configuring, managing, and monitoring virtual machines on a single physical machine.

%files xen_server
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/xen_server.txt

%package xfce
%pattern_graphicalenvironments
Summary:        XFCE Desktop Environment
Group:          Metapackages
Provides:       pattern() = xfce
Provides:       pattern-icon() = pattern-xfce
Provides:       pattern-order() = 1760
Requires:       pattern() = x11
Requires:       pattern() = xfce_basis
Recommends:     pattern() = xfce_office
Recommends:     pattern() = multimedia
Recommends:     pattern() = imaging
# from data/XFCE
Recommends:     lightdm
Recommends:     lightdm-gtk-greeter
Recommends:     leafpad
Recommends:     gcalctool
Recommends:     ristretto
Recommends:     MozillaThunderbird
Recommends:     orage
Recommends:     file-roller
Recommends:     evince
Recommends:     totem
Recommends:     totem-browser-plugin
Recommends:     alacarte
Recommends:     seahorse
Recommends:     thunar-plugin-archive
Recommends:     thunar-plugin-media-tags
Recommends:     xfce4-screenshooter
Recommends:     pidgin
Recommends:     brasero
Recommends:     sound-juicer
Recommends:     rhythmbox
Recommends:     simple-scan
Recommends:     shotwell
Recommends:     gucharmap
Recommends:     xfce4-dict
Recommends:     xfce4-panel-plugin-notes
Recommends:     tracker
Recommends:     tracker-gui
Recommends:     remmina
Recommends:     remmina-plugin-xdmcp
Recommends:     remmina-plugin-rdp
Recommends:     remmina-plugin-vnc
Recommends:     transmission-gtk
Recommends:     gnome-games
# Additional applications
# ease debugging
#
Recommends:     gdb
Recommends:     system-config-printer
Recommends:     system-config-printer-applet
# bnc#537362
Recommends:     gnome-packagekit
Recommends:     pk-update-icon
# bnc#537365
Recommends:     gnome-keyring
Recommends:     gnome-keyring-pam
#
# core desktop functionality
#
Recommends:     xfce4-taskmanager
Recommends:     thunar-volman
Recommends:     tumbler
Suggests:       xfce4-dev-tools
Suggests:       xfce4-panel-plugin-battery
Suggests:       xfce4-panel-plugin-cellmodem
Suggests:       xfce4-panel-plugin-clipman
Suggests:       xfce4-panel-plugin-cpufreq
Suggests:       xfce4-panel-plugin-cpugraph
Suggests:       xfce4-panel-plugin-datetime
Suggests:       xfce4-panel-plugin-dict
Suggests:       xfce4-panel-plugin-diskperf
Suggests:       xfce4-panel-plugin-eyes
Suggests:       xfce4-panel-plugin-fsguard
Suggests:       xfce4-panel-plugin-genmon
Suggests:       xfce4-panel-plugin-mailwatch
Suggests:       xfce4-panel-plugin-mount
Suggests:       xfce4-panel-plugin-mpc
Suggests:       xfce4-panel-plugin-netload
Suggests:       xfce4-panel-plugin-notes
Suggests:       xfce4-panel-plugin-places
Suggests:       xfce4-panel-plugin-quicklauncher
Suggests:       xfce4-panel-plugin-radio
Suggests:       xfce4-panel-plugin-screenshooter
Suggests:       xfce4-panel-plugin-sensors
Suggests:       xfce4-panel-plugin-smartbookmark
Suggests:       xfce4-panel-plugin-systemload
Suggests:       xfce4-panel-plugin-timeout
Suggests:       xfce4-panel-plugin-timer
Suggests:       xfce4-panel-plugin-verve
Suggests:       xfce4-panel-plugin-wavelan
Suggests:       xfce4-panel-plugin-weather
Suggests:       xfwm4-themes
Suggests:       xfce4-vala

# from data/COMMON-DESKTOP-OPT
# packages a GTK application
Recommends:     gutenprint
# MAYBE later lsb-graphics
Recommends:     icedtea-web
# give net shares
Recommends:     samba
# needs python-qt4, see#649280#14
Suggests:       hplip


%description xfce
Xfce is a lightweight desktop environment for various *NIX systems.

%files xfce
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/xfce.txt

%package xfce_basis
%pattern_graphicalenvironments
Summary:        XFCE Base System
Group:          Metapackages
Provides:       pattern() = xfce_basis
Provides:       pattern-icon() = pattern-xfce
Provides:       pattern-order() = 1759
Provides:       pattern-extends() = xfce
Requires:       pattern() = x11
Requires:       pattern() = basesystem
# from data/XFCE-BASIS
# This defines a bare minimum Xfce desktop used, for example, as
# base for the openSUSE Rescue CD
Requires:       thunar
Requires:       xfce4-appfinder
Requires:       xfce4-mixer
Requires:       xfce4-notifyd
Requires:       xfce4-panel-plugin-mixer
Requires:       xfce4-panel
Requires:       xfce4-power-manager
Requires:       xfce4-session
Requires:       xfce4-settings
Requires:       xfconf
Requires:       xfdesktop
Requires:       xfwm4
Requires:       thunar-volman
#
# low level functionality
#
Recommends:     avahi
Recommends:     dbus-1-x11
# bnc#540627
Recommends:     xdg-utils
Recommends:     xdg-user-dirs-gtk
Recommends:     desktop-file-utils
Recommends:     shared-mime-info
Recommends:     NetworkManager
Recommends:     NetworkManager-gnome
# use gnomesu as su wrapper
Recommends:     libgnomesu
# bnc#440285
Recommends:     pinentry-gtk2
# For screenlocking to work in xfce
Recommends:     xscreensaver
Recommends:     xfce4-terminal
Recommends:     libxfce4ui-tools
Recommends:     xfce4-panel-plugin-xkb
#
# core desktop functionality
#
Recommends:     libyui-gtk-pkg
Recommends:     yast2-control-center-gnome
#
# branding
#
Suggests:       exo-branding-openSUSE
Suggests:       gconf2-branding-openSUSE
Suggests:       libgarcon-branding-openSUSE
Suggests:       libxfce4ui-branding-openSUSE
Suggests:       lightdm-gtk-greeter-branding-openSUSE
Suggests:       midori-branding-openSUSE
Suggests:       thunar-volman-branding-openSUSE
Suggests:       wallpaper-branding-openSUSE
Suggests:       xfce4-notifyd-branding-openSUSE
Suggests:       xfce4-panel-branding-openSUSE
Suggests:       xfce4-session-branding-openSUSE
Suggests:       xfce4-settings-branding-openSUSE
Suggests:       xfce4-splash-branding-openSUSE
Suggests:       xfdesktop-branding-openSUSE
Suggests:       xfwm4-branding-openSUSE
Suggests:       desktop-branding

# from data/COMMON-DESKTOP
Recommends:     droid-fonts
Recommends:     MozillaFirefox
Recommends:     desktop-data-openSUSE
Recommends:     avahi
# bnc#508120
Recommends:     xdg-user-dirs
# bnc#598884
Suggests:       moonlight-plugin
# metalink downloader
Suggests:       aria2


%description xfce_basis
Base packages for the XFCE Desktop Environment

%files xfce_basis
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/xfce_basis.txt

%package xfce_laptop
%pattern_xfcedesktop
Summary:        XFCE Laptop
Group:          Metapackages
Provides:       pattern() = xfce_laptop
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 5180
Provides:       pattern-extends() = laptop
Supplements:    packageand(patterns-openSUSE-xfce:patterns-openSUSE-laptop)
Requires:       pattern() = xfce
Requires:       pattern() = xfce_basis
# from data/XFCE-LAPTOP
Recommends:     gsynaptics
Recommends:     xfce4-panel-plugin-brightness


%description xfce_laptop
XFCE Laptop

%files xfce_laptop
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/xfce_laptop.txt

%package xfce_office
%pattern_graphicalenvironments
Summary:        XFCE Office
Group:          Metapackages
Provides:       pattern() = xfce_office
Provides:       pattern-icon() = yast-x11
Provides:       pattern-order() = 2241
Provides:       pattern-extends() = office
Supplements:    packageand(patterns-openSUSE-xfce:patterns-openSUSE-office)
Requires:       pattern() = xfce
Requires:       pattern() = xfce_basis
# from data/XFCE-Office
%ifarch %ix86 x86_64
Recommends:     libreoffice-gnome
%endif


%description xfce_office
XFCE Office

%files xfce_office
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/xfce_office.txt

%package yast2_basis
%pattern_basetechnologies
Summary:        YaST System Administration
Group:          Metapackages
Provides:       pattern() = yast2_basis
Provides:       pattern-icon() = yast
Provides:       pattern-order() = 1220
# from data/YAST_BASIS
Requires:       yast2
Requires:       yast2-country
Requires:       yast2-firewall
Requires:       yast2-hardware-detection
Requires:       yast2-installation
Requires:       yast2-ldap
Requires:       yast2-mail
Requires:       libyui-ncurses-pkg
Requires:       yast2-network
Requires:       yast2-online-update
Requires:       yast2-online-update-frontend
Requires:       yast2-packager
Requires:       yast2-pam
Requires:       yast2-perl-bindings
Requires:       yast2-pkg-bindings
Requires:       yast2-services-manager
Requires:       yast2-security
Requires:       yast2-storage
Requires:       yast2-sysconfig
Requires:       yast2-theme-openSUSE
Requires:       yast2-transfer
Requires:       yast2-tune
Requires:       yast2-update
Requires:       yast2-users
Requires:       yast2-xml
Recommends:     yast2-inetd
Recommends:     yast2-iscsi-client
Recommends:     yast2-kerberos-client
Recommends:     yast2-ldap-client
Recommends:     yast2-metapackage-handler
Recommends:     yast2-nfs-client
Recommends:     yast2-nis-client
Recommends:     yast2-ntp-client
Recommends:     yast2-printer
Recommends:     yast2-slp
Recommends:     yast2-sudo
# see the discussion in #386473
Recommends:     yast2-samba-client
Recommends:     yast2-samba-server
# #388892
Recommends:     yast2-vm
# #542936
Recommends:     yast2-packager-webpin
Suggests:       yast2-online-update-configuration
Suggests:       yast2-product-creator
Suggests:       autoyast2
Suggests:       autoyast2-installation
Suggests:       inst-source-utils
Suggests:       libyui-qt-pkg
Suggests:       libyui-gtk-pkg
Suggests:       yast2-autofs
Suggests:       yast2-drbd
Suggests:       yast2-firstboot
Suggests:       yast2-mail-plugins
Suggests:       yast2-multipath
Suggests:       yast2-phone-services
Suggests:       yast2-snapper
# #381365
Suggests:       yast2-squid
# see extra-packages for reasons
Suggests:       star
Suggests:       sbl
Suggests:       Mesa
Suggests:       i4l-isdnlog
Suggests:       ypserv
Suggests:       ntp
Suggests:       ntp-doc
Suggests:       star
Suggests:       alevt
Suggests:       kradio
Suggests:       motv
Suggests:       nxtvepg
Suggests:       v4l-tools
Suggests:       install-initrd
# for yast2-scanner
Suggests:       sane-backends             // mandatory
Suggests:       hplip                     // optionally
Suggests:       iscan-free                // optionally, open source, derived from iscan
# themeing for hardcore KDE lovers
Suggests:       yast2-theme-openSUSE-Crystal
Suggests:       yast2-theme-openSUSE-Oxygen
Suggests:       ivtv
Suggests:       ivtv-firmware
# required by yast2-storage
Suggests:       pam_mount
%ifarch x86_64
Suggests:       pam_fp-32bit
%endif
%ifarch ppc64
Suggests:       pam_fp-64bit
%endif
# yast2-sound
Suggests:       alsa-firmware 
Suggests:       alsa-tools
# yast2-printer
Suggests:       ncpfs              // printing via novell ipx
# yast2-kdump
%ifarch ppc
Suggests:       kernel-kdump
%endif
Suggests:       yast2-fingerprint-reader
Suggests:       sssd
Suggests:       snapper
# FATE 304350
Suggests:       sblim-sfcb
Suggests:       cim-schema


%description yast2_basis
YaST tools for basic system administration.

%files yast2_basis
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/yast2_basis.txt

%package yast2_install_wf
%pattern_basetechnologies
Summary:        YaST Installation Packages
Group:          Metapackages
Provides:       pattern() = yast2_install_wf
Provides:       pattern-icon() = yast
Provides:       pattern-order() = 1240
# from data/YAST_INSTALL_WF
Requires:       yast2-installation
Requires:       libyui-ncurses-pkg
Requires:       yast2-network
Requires:       yast2-users
# bnc#535101
Requires:       yast2-bootloader
# required to write ntp.conf (bnc#723018)
Requires:       yast2-ntp-client
Suggests:       autoyast2-installation
Suggests:       yast2-firewall
Suggests:       yast2-kerberos-client
Suggests:       yast2-ldap
Suggests:       yast2-ldap-client
Suggests:       yast2-nfs-client
Suggests:       yast2-nis-client
Suggests:       yast2-printer
Suggests:       yast2-samba-client
Suggests:       yast2-slp
Suggests:       yast2-tv
Suggests:       yast2-update
Suggests:       autoyast2
%ifarch x86_64
Suggests:       samba-client-32bit
Suggests:       samba-winbind-32bit
%endif
%ifarch ppc64
Suggests:       pam_fp-64bit
Suggests:       pam_krb5-64bit
Suggests:       nss_ldap-64bit
Suggests:       pam_ldap-64bit
Suggests:       samba-client-64bit
Suggests:       samba-winbind-64bit
%endif
Suggests:       tgt


%description yast2_install_wf
YaST tools for installing your system.

%files yast2_install_wf
%dir /usr/share/doc/packages/patterns-openSUSE
/usr/share/doc/packages/patterns-openSUSE/yast2_install_wf.txt

#END1

%prep

%build

%install
#BEGIN2
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/
echo 'This file marks the pattern 32bit to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/32bit.txt
echo 'This file marks the pattern 64bit to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/64bit.txt
echo 'This file marks the pattern apparmor to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/apparmor.txt
echo 'This file marks the pattern apparmor_opt to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/apparmor_opt.txt
echo 'This file marks the pattern base to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/base.txt
echo 'This file marks the pattern books to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/books.txt
echo 'This file marks the pattern console to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/console.txt
echo 'This file marks the pattern devel_basis to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/devel_basis.txt
echo 'This file marks the pattern devel_C_C++ to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/devel_C_C++.txt
echo 'This file marks the pattern devel_gnome to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/devel_gnome.txt
echo 'This file marks the pattern devel_ide to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/devel_ide.txt
echo 'This file marks the pattern devel_java to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/devel_java.txt
echo 'This file marks the pattern devel_kde to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/devel_kde.txt
echo 'This file marks the pattern devel_kernel to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/devel_kernel.txt
echo 'This file marks the pattern devel_mono to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/devel_mono.txt
echo 'This file marks the pattern devel_perl to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/devel_perl.txt
echo 'This file marks the pattern devel_python to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/devel_python.txt
echo 'This file marks the pattern devel_python3 to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/devel_python3.txt
echo 'This file marks the pattern devel_qt4 to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/devel_qt4.txt
echo 'This file marks the pattern devel_rpm_build to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/devel_rpm_build.txt
echo 'This file marks the pattern devel_ruby to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/devel_ruby.txt
echo 'This file marks the pattern devel_tcl to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/devel_tcl.txt
echo 'This file marks the pattern devel_web to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/devel_web.txt
echo 'This file marks the pattern devel_yast to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/devel_yast.txt
echo 'This file marks the pattern dhcp_dns_server to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/dhcp_dns_server.txt
echo 'This file marks the pattern directory_server to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/directory_server.txt
echo 'This file marks the pattern e17 to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/e17.txt
echo 'This file marks the pattern enhanced_base to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/enhanced_base.txt
echo 'This file marks the pattern enhanced_base_opt to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/enhanced_base_opt.txt
echo 'This file marks the pattern file_server to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/file_server.txt
echo 'This file marks the pattern fonts to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/fonts.txt
echo 'This file marks the pattern fonts_opt to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/fonts_opt.txt
echo 'This file marks the pattern games to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/games.txt
echo 'This file marks the pattern gateway_server to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/gateway_server.txt
echo 'This file marks the pattern gnome to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/gnome.txt
echo 'This file marks the pattern gnome_admin to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/gnome_admin.txt
echo 'This file marks the pattern gnome_basis to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/gnome_basis.txt
echo 'This file marks the pattern gnome_basis_opt to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/gnome_basis_opt.txt
echo 'This file marks the pattern gnome_games to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/gnome_games.txt
echo 'This file marks the pattern gnome_ide to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/gnome_ide.txt
echo 'This file marks the pattern gnome_imaging to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/gnome_imaging.txt
echo 'This file marks the pattern gnome_imaging_opt to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/gnome_imaging_opt.txt
echo 'This file marks the pattern gnome_internet to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/gnome_internet.txt
echo 'This file marks the pattern gnome_laptop to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/gnome_laptop.txt
echo 'This file marks the pattern gnome_multimedia to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/gnome_multimedia.txt
echo 'This file marks the pattern gnome_multimedia_opt to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/gnome_multimedia_opt.txt
echo 'This file marks the pattern gnome_office to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/gnome_office.txt
echo 'This file marks the pattern gnome_office_opt to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/gnome_office_opt.txt
echo 'This file marks the pattern gnome_utilities to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/gnome_utilities.txt
echo 'This file marks the pattern gnome_yast to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/gnome_yast.txt
echo 'This file marks the pattern imaging to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/imaging.txt
echo 'This file marks the pattern imaging_opt to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/imaging_opt.txt
echo 'This file marks the pattern kde to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/kde.txt
echo 'This file marks the pattern kde4 to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/kde4.txt
echo 'This file marks the pattern kde4_admin to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/kde4_admin.txt
echo 'This file marks the pattern kde4_basis to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/kde4_basis.txt
echo 'This file marks the pattern kde4_edutainment to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/kde4_edutainment.txt
echo 'This file marks the pattern kde4_games to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/kde4_games.txt
echo 'This file marks the pattern kde4_ide to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/kde4_ide.txt
echo 'This file marks the pattern kde4_imaging to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/kde4_imaging.txt
echo 'This file marks the pattern kde4_internet to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/kde4_internet.txt
echo 'This file marks the pattern kde4_laptop to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/kde4_laptop.txt
echo 'This file marks the pattern kde4_multimedia to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/kde4_multimedia.txt
echo 'This file marks the pattern kde4_office to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/kde4_office.txt
echo 'This file marks the pattern kde4_pure to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/kde4_pure.txt
echo 'This file marks the pattern kde4_utilities to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/kde4_utilities.txt
echo 'This file marks the pattern kde4_utilities_opt to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/kde4_utilities_opt.txt
echo 'This file marks the pattern kde4_yast to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/kde4_yast.txt
echo 'This file marks the pattern kvm_server to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/kvm_server.txt
echo 'This file marks the pattern lamp_server to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/lamp_server.txt
echo 'This file marks the pattern laptop to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/laptop.txt
echo 'This file marks the pattern leechcraft to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/leechcraft.txt
echo 'This file marks the pattern leechcraft_browser to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/leechcraft_browser.txt
echo 'This file marks the pattern leechcraft_media to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/leechcraft_media.txt
echo 'This file marks the pattern leechcraft_messenger to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/leechcraft_messenger.txt
echo 'This file marks the pattern leechcraft_netutils to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/leechcraft_netutils.txt
echo 'This file marks the pattern leechcraft_office to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/leechcraft_office.txt
echo 'This file marks the pattern leechcraft_utilities to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/leechcraft_utilities.txt
echo 'This file marks the pattern lxde to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/lxde.txt
echo 'This file marks the pattern lxde_laptop to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/lxde_laptop.txt
echo 'This file marks the pattern lxde_office to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/lxde_office.txt
echo 'This file marks the pattern mail_server to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/mail_server.txt
echo 'This file marks the pattern minimal_base to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/minimal_base.txt
echo 'This file marks the pattern minimal_base-conflicts to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/minimal_base-conflicts.txt
echo 'This file marks the pattern misc_server to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/misc_server.txt
echo 'This file marks the pattern multimedia to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/multimedia.txt
echo 'This file marks the pattern multimedia_opt to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/multimedia_opt.txt
echo 'This file marks the pattern network_admin to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/network_admin.txt
echo 'This file marks the pattern non_oss to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/non_oss.txt
echo 'This file marks the pattern non_oss_opt to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/non_oss_opt.txt
echo 'This file marks the pattern office to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/office.txt
echo 'This file marks the pattern office_opt to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/office_opt.txt
echo 'This file marks the pattern print_server to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/print_server.txt
echo 'This file marks the pattern remote_desktop to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/remote_desktop.txt
echo 'This file marks the pattern rest_cd_gnome to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/rest_cd_gnome.txt
echo 'This file marks the pattern rest_cd_kde4 to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/rest_cd_kde4.txt
echo 'This file marks the pattern rest_cd_x11 to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/rest_cd_x11.txt
echo 'This file marks the pattern rest_core_dvd to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/rest_core_dvd.txt
echo 'This file marks the pattern rest_dvd to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/rest_dvd.txt
echo 'This file marks the pattern rest_dvd9 to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/rest_dvd9.txt
echo 'This file marks the pattern rest_promo_dvd to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/rest_promo_dvd.txt
echo 'This file marks the pattern sw_management to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/sw_management.txt
echo 'This file marks the pattern sw_management_gnome to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/sw_management_gnome.txt
echo 'This file marks the pattern sw_management_kde4 to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/sw_management_kde4.txt
echo 'This file marks the pattern tabletpc to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/tabletpc.txt
echo 'This file marks the pattern technical_writing to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/technical_writing.txt
echo 'This file marks the pattern update_test to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/update_test.txt
echo 'This file marks the pattern voip to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/voip.txt
echo 'This file marks the pattern x11 to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/x11.txt
echo 'This file marks the pattern x11_opt to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/x11_opt.txt
echo 'This file marks the pattern x11_yast to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/x11_yast.txt
echo 'This file marks the pattern x86 to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/x86.txt
echo 'This file marks the pattern xen_server to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/xen_server.txt
echo 'This file marks the pattern xfce to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/xfce.txt
echo 'This file marks the pattern xfce_basis to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/xfce_basis.txt
echo 'This file marks the pattern xfce_laptop to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/xfce_laptop.txt
echo 'This file marks the pattern xfce_office to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/xfce_office.txt
echo 'This file marks the pattern yast2_basis to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/yast2_basis.txt
echo 'This file marks the pattern yast2_install_wf to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-openSUSE/yast2_install_wf.txt
#END2

%changelog

