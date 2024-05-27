Name: zed
Version: gitbuild.25.05.24
Release: 1%{?dist}
Summary: Zed, a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter

License: AGPL-3.0
URL: zed.dev
Source0: Zed

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root--%(%{__id_u} -n)

%description
Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter.

%install
install -Dm 755 %{SOURCE0} %{buildroot}/usr/bin/%{name}

%files
/usr/bin/%{name}
