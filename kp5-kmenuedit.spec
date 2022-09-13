#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.25.5
%define		qtver		5.15.2
%define		kpname		kmenuedit

Summary:	KDE menu editor
Name:		kp5-%{kpname}
Version:	5.25.5
Release:	2
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	b191a380f07282732d1596076d7b60a5
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-sonnet-devel
BuildRequires:	kp5-khotkeys-devel >= %{kdeplasmaver}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KDE Plasma menu editor.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmenuedit
%{_desktopdir}/org.kde.kmenuedit.desktop
%{_iconsdir}/hicolor/*/apps/kmenuedit.png
%{_datadir}/kmenuedit
%{_datadir}/kxmlgui5/kmenuedit
%{_datadir}/qlogging-categories5/kmenuedit.categories
%attr(755,root,root) %{_libdir}/kconf_update_bin/kmenuedit_globalaccel
%{_datadir}/metainfo/org.kde.kmenuedit.appdata.xml
