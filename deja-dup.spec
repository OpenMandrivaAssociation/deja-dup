Name:		deja-dup
Version:	47.0
Release:	1
Summary:	Simple backup tool and front-end for duplicity
Group:		Backup
License:	GPLv3+
URL:		https://welcome.gnome.org/app/DejaDup/
Source0:	https://gitlab.gnome.org/World/deja-dup/-/archive/%{version}/deja-dup-%{version}.tar.bz2
BuildRequires:	meson
BuildRequires:	gettext
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	appstream-util
BuildRequires:	pkgconfig(gtk4)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:	pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(libpeas-1.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libnautilus-extension-4)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(libsoup-3.0)
BuildRequires:	pkgconfig(packagekit-glib2)
BuildRequires:  pkgconfig(vapigen)
Requires:	duplicity
Requires:	python-gobject3
Requires:	adwaita-icon-theme
Requires:	dconf

%description
Déjà Dup is a simple backup tool. It hides the complexity of doing backups the
'right way' (encrypted, off-site, and regular) and uses duplicity as the
back-end.

Features:
 - Support for local, remote, or cloud backup locations, such as Amazon S3
 - Securely encrypts and compresses your data
 - Incrementally backs up, letting you restore from any particular backup
 - Schedules regular backups
 - Integrates well into your GNOME desktop

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

rm -rf %{buildroot}%{_datadir}/icons/Humanity/

%find_lang %{name} --with-gnome --with-man --all-name

%files -f %{name}.lang
%doc NEWS.md README.md
%{_bindir}/deja-*
%{_metainfodir}/org.gnome.DejaDup.metainfo.xml
%{_datadir}/applications/org.gnome.DejaDup.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.DejaDup.gschema.xml
%{_iconsdir}/hicolor/*/*/org.gnome.DejaDup*.{svg,png}
%{_libdir}/%{name}/
%{_mandir}/man1/deja-dup*.1*
%{_sysconfdir}/xdg/autostart/org.gnome.DejaDup.Monitor.desktop
%{_libexecdir}/%{name}/
%{_datadir}/dbus-1/services/org.gnome.DejaDup.service
