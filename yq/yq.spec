Name:          yq
Version:       4.30.8
Release:       1%{?dist}
Summary:       A portable command-line YAML, JSON, XML, CSV and properties processor

License:       MIT
URL:           https://github.com/mikefarah/yq/releases
Source0:       https://github.com/mikefarah/yq/releases/download/v%{version}/yq_linux_amd64.tar.gz
ExclusiveArch: x86_64

%description
a lightweight and portable command-line YAML, JSON and XML processor. yq uses
jq like syntax but works with yaml files as well as json, xml, properties, csv
and tsv. It does not yet support everything jq does - but it does support the
most common operations and functions, and more is being added continuously.

%prep
%autosetup -c

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1/
%{__install} -m 755 yq_linux_amd64 %{buildroot}/%{_bindir}/%{name}
%{__install} -m 644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sat Feb 11 2023 Johan Kok <johan@fedoraproject.org> - 4.30.8-1
- Bumped to 4.30.8

* Mon Feb 06 2023 Johan Kok <johan@fedoraproject.org> - 4.30.4-2
- Update installed binaries

* Thu Nov 24 2022 Johan Kok <johan@fedoraproject.org> - 4.30.4-1
- Initial import
