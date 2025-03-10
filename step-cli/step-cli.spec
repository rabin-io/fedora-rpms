Name:          step-cli
Version:       0.28.5
Release:       1%{?dist}
Summary:       A zero trust swiss army knife for working with X509, OAuth, JWT, OATH OTP, etc

License:       ASL 2.0
URL:           https://github.com/smallstep/cli/releases
Source0:       https://github.com/smallstep/cli/releases/download/v%{version}/step_linux_%{version}_amd64.tar.gz
ExclusiveArch: x86_64

%description
step is an easy-to-use CLI tool for building, operating, and automating Public
Key Infrastructure (PKI) systems and workflows. It's the client counterpart to
the step-ca online Certificate Authority (CA). You can use it for many common
crypto and X.509 operations—either independently, or with an online CA.

%prep
%autosetup -n step_%{version}

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 bin/step %{buildroot}/%{_bindir}/step

%files
%{_bindir}/step
%license LICENSE
%doc README.md

%changelog
* Sat Oct 18 2024 Johan Kok <johan@fedoraproject.org> - 0.28.5
- Bumped to 0.28.5
