Name:          minikube
Version:       1.22.0
Release:       1%{?dist}
Summary:       Minikube is a tool that makes it easy to run Kubernetes locally

Group:         Development Tools
URL:           https://github.com/kubernetes/minikube
License:       ASL 2.0
Source0:       https://github.com/kubernetes/minikube/releases/download/v%{version}/%{name}-linux-amd64
ExclusiveArch: x86_64
Requires:      docker-machine-driver-kvm2

%description
Minikube is a tool that makes it easy to run Kubernetes locally. Minikube
runs a single-node Kubernetes cluster inside a VM on your laptop for
users looking to try out Kubernetes or develop with it day-to-day.

%build

%prep
%setup -q -T -c

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Thu Jul 08 2021 Johan Kok <johan@fedoraproject.org> - 1.22.0-1
- Bumped to 1.22.0

* Fri Jun 18 2021 Johan Kok <johan@fedoraproject.org> - 1.21.0-1
- Bumped to 1.21.0

* Fri May 07 2021 Johan Kok <johan@fedoraproject.org> - 1.20.0-1
- Bumped to 1.20.0

* Sat Apr 10 2021 Johan Kok <johan@fedoraproject.org> - 1.19.0-1
- Bumped to 1.19.0

* Sat Mar 06 2021 Johan Kok <johan@fedoraproject.org> - 1.18.1-1
- Bumped to 1.18.1

* Tue Mar  2 2021 Johan Kok <johan@fedoraproject.org> - 1.18.0-1
- Bumped to 1.18.0

* Thu Feb  4 2021 Johan Kok <johan@fedoraproject.org> - 1.17.1-1
- Bumped to 1.17.1

* Sat Dec 19 2020 Johan Kok <johan@fedoraproject.org> - 1.16.0-1
- Bumped to 1.16.0

* Sat Nov 14 2020 Johan Kok <johan@fedoraproject.org> - 1.15.0-1
- Bumped to 1.15.0

* Wed Oct 28 2020 Johan Kok <johan@fedoraproject.org> - 1.14.2-1
- Bumped to 1.14.2

* Mon Oct 26 2020 Johan Kok <johan@fedoraproject.org> - 1.14.1-1
- Bump to 1.14.1

* Sat Oct 17 2020 Johan Kok <johan@fedoraproject.org> - 1.14.0-1
- Bump to 1.14.0

* Fri Sep  4 2020 Johan Kok <johan@fedoraproject.org> - 1.13.0-1
- Bump to 1.13.0

* Thu Aug 13 2020 Johan Kok <johan@fedoraproject.org> - 1.12.3-1
- Bump to 1.12.3

* Wed Aug 05 2020 Johan Kok <johan@fedoraproject.org> - 1.12.2-1
- Bump to 1.12.2

* Sat Jul 18 2020 Johan Kok <johan@fedoraproject.org> - 1.12.1-1
- Bump to 1.12.1

* Sat Jul 11 2020 Johan Kok <johan@fedoraproject.org> - 1.12.0-1
- Bump to 1.12.0

* Sat May 30 2020 Johan Kok <johan@fedoraproject.org> - 1.11.0-1
- Bump to 1.11.0

* Sun May 17 2020 Johan Kok <johan@fedoraproject.org> - 1.10.1-1
- Bump to 1.10.1

* Thu Apr 30 2020 Johan Kok <johan@fedoraproject.org> - 1.9.2-1
- Bump to 1.9.2

* Thu Feb 20 2020 Johan Kok <johan@fedoraproject.org> - 1.7.3-1
- Bump to 1.7.3

* Mon Feb 17 2020 Sergi Jimenez <tripledes@fedoraproject.org> - 1.7.2-1
- Bump to 1.7.2

* Tue Jan 14 2020 Sergi Jimenez <tripledes@fedoraproject.org> - 1.6.2-1
- Bump to 1.6.2

* Fri Dec 13 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.6.1-1
- Bump to 1.6.1

* Wed Nov  6 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.5.2-1
- Bump to 1.5.2

* Tue Jul  2 2019 Edu Minguez <edu@linux.com> - 1.2.0-1
- Bump to 1.2.0

* Tue Jun 11 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.1.1-1
- Bump to 1.1.1

* Mon Jun  3 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.1.0-1
- Bump to 1.1.0

* Fri May  3 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.0.1-1
- Bump to 1.0.1

* Sun Mar 31 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.0.0-1
- Bump to 1.0.0

* Tue Mar 12 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.35.0-1
- Bump to 0.35.0

* Tue Mar  5 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.34.1-1
- Bump to 0.34.1

* Mon Jan 21 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.33.1-1
- Bump to 0.33.1

* Sun Jan 13 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.32.0-1
- Bump to 0.32.0

* Wed Dec 12 2018 Sergi Jimenez <tripledes@fedoraproject.org> - 0.31.0-2
- Depend on docker-machine-driver-kvm2, as v1 is being deprecated.

* Wed Dec 12 2018 Sergi Jimenez <tripledes@fedoraproject.org> - 0.31.0-1
- Initial import
