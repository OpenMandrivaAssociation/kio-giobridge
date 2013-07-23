%define svn 1349920

Name:		kio-giobridge
Summary:	KIO-Giobridge is an optional adapter for KIO to use GIO/GVFS
Version:	0
Release:	0.%{svn}.1
Group:		Graphical desktop/KDE
# Unknown but let it be the same as for KDE libs
License:	GPLv2+
Url:		https://wiki.gnome.org/KioGioBridge
# http://websvn.kde.org/trunk/playground/ioslaves/kio-giobridge/
Source0:	%{name}-%{svn}.tar.bz2
# Qt and GTK have symbol conflicts
Patch0:		kio-giobridge-1349920-qtgtk.patch
BuildRequires:	cmake
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gio-2.0)

%description
The purpose of KIO-Giobridge is to let all desktop applications and file
managers share the same network transparency layer for working with network
file systems like FTP, SFTP, SMB, WEBDAV,... Therefore KDE4, Gtk and 3rd
party applications can access the same file-server resources without logging in
twice or facing other inconsistencies. At the moment we have two incompatible
network transparency systems, running in the same desktop session for different
groups of applications. Also, with the existence of two frameworks, a lot of
3rd party applications were locked out, as they didn't want to decide for one
of them.

KIO-Giobridge is an optional adapter for KIO to use the new GIO/GVFS (the
successor of Gnome-VFS) to handle the protocols mentioned above.  GIO/GVFS has
been chosen, because it's pretty independent from desktop specific libraries,
daemons and toolkits and only depends on D-Bus and GLib. Another advantage of
GIO/GVFS is its "stateful" mount daemons: All the communication to a certain
share is handled by a single mount daemon process. The life-cycle of those
mount daemons is user-controllable (mount/unmount), similar to kernel or FUSE
mounts.

KIO-Giobridge can be enabled/disabled with the kio-giobridge-mgr utility.

%files
%{_kde_bindir}/gvfs-daemon-query
%{_kde_bindir}/kio-giobridge-mgr
%{_kde_bindir}/kiogiobridge-unmount-gvfs
%{_kde_libdir}/kde4/kded_giobridgeremotedirnotify.so
%{_kde_libdir}/kde4/kio_giobridge.so
%{_kde_appsdir}/kio-giobridge-protocols
%{_kde_services}/ServiceMenus/giobridge-remote-unmount.desktop
%{_kde_services}/kded/giobridgeremotedirnotify.desktop
%{_kde_datadir}/mime/packages/giobridge-remote-gvfs-mount.xml

#------------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{svn}
%patch0 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

