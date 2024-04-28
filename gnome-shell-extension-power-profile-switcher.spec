%global uuid power-profile-switcher@eliapasquali.github.io

Name:          gnome-shell-extension-power-profile-switcher
Version:       {{{ git_dir_version }}}
Release:       1%{?dist}
Summary:       Gnome extension to automatically switch between power profiles based on power supply. 

Group:         User Interface/Desktops
License:       GPLv3
URL:           https://github.com/ublue-os/power-profile-switcher
Source0:       %{url}/archive/refs/heads/main.tar.gz
BuildArch:     noarch

BuildRequires: make
BuildRequires: unzip
BuildRequires: gettext
BuildRequires: gnome-shell
BuildRequires: glib2

Requires:    gnome-shell >= 3.12
%description
GNOME Shell extension to automatically switch between power profiles based on power supply

%prep
%autosetup -n power-profile-switcher-main

%install
gnome-extensions pack --extra-source=ui
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
unzip power-profile-switcher@eliapasquali.github.io.shell-extension.zip -d %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
glib-compile-schemas %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/schemas/

%files
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
{{{ git_dir_changelog }}}
