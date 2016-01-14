%global pkg_name plexus-archiver
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.4.2
Release:        4.9%{?dist}
Epoch:          0
Summary:        Plexus Archiver Component
License:        ASL 2.0
URL:            http://plexus.codehaus.org/plexus-components/plexus-archiver/
Source0:        https://github.com/sonatype/%{pkg_name}/archive/%{pkg_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix}plexus-containers-container-default
BuildRequires:  %{?scl_prefix}plexus-io
BuildRequires:  %{?scl_prefix}plexus-utils
BuildRequires:  %{?scl_prefix_java_common}apache-commons-compress


%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.


%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
Javadoc for %{pkg_name}.


%prep
%setup -q -n %{pkg_name}-%{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_file :%{pkg_name} plexus/archiver
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/plexus
%dir %{_javadir}/plexus
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Jan 16 2015 Michal Srb <msrb@redhat.com> - 0:2.4.2-4.9
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 0:2.4.2-4.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 0:2.4.2-4.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.4.2-4.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.4.2-4.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.4.2-4.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.4.2-4.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.4.2-4.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.4.2-4.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 02.4.2-4
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.4.2-3
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Jun 13 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:2.4.2-2
- Update to latest packaging guidelines
- Remove MIT license (only applies to test cases not binary rpm)

* Fri May 24 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.4.2-1
- Update to upstream version 2.4.2
- Remove patch for CVE-2012-2098 (accepted upstream)

* Thu Apr 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.3-1
- Update to upstream version 2.3
- Use apache-commons-compress for bzip2 (de)compression
- Resolves: CVE-2012-2098

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0:2.2-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Nov 23 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:2.2-4
- Add ASL 2.0 license text to packages

* Thu Nov 22 2012 Jaromir Capik <jcapik@redhat.com> - 0:2.2-3
- Migration to plexus-containers-container-default

* Mon Nov 19 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:2.2-2
- Fix source URL to be stable

* Wed Oct 10 2012 Alexander Kurtakov <akurtako@redhat.com> 0:2.2-1
- Update to upstream 2.2.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 18 2012 Alexander Kurtakov <akurtako@redhat.com> 0:2.1.1-1
- Update to latest upstream release.

* Wed Feb 15 2012 Alexander Kurtakov <akurtako@redhat.com> 0:2.1-1
- Update to latest upstream release.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 8 2011 Alexander Kurtakov <akurtako@redhat.com> 0:2.0.1-2
- BR maven-surefire-provider-junit4.

* Thu Sep 8 2011 Alexander Kurtakov <akurtako@redhat.com> 0:2.0.1-1
- Update to 2.0.1 version.

* Wed Jul 27 2011 Jaromir Capik <jcapik@redhat.com> - 0:1.2-2
- Removal of plexus-maven-plugin dependency (not needed)
- Minor spec file changes according to the latest guidelines

* Tue May 17 2011 Alexander Kurtakov <akurtako@redhat.com> 0:1.2-1
- Update to 1.2.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 6 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.1-1
- Update to 1.1.

* Mon Dec 28 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.4.a12.4
- Install depmap and pom to override common poms.

* Thu Dec 24 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.4.a12.3
- Really ignore test failures.

* Thu Dec 24 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.4.a12.2
- Ignore test failures.

* Wed Dec 23 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.4.a12.1
- Update to alpha 12.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.4.a7.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.3.a7.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.0-0.2.a7.1.2
- drop repotag
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:1.0-0.2.a7.1jpp.1
- Autorebuild for GCC 4.3

* Fri Jan 04 2008 Deepak Bhole <dbhole@redhat.com> 1.0-0.1.a7.1jpp.1
- Update to alpha 7

* Thu Feb 15 2007 Matt Wrigne <mwringe@redhat.com> - 0:1.0-0.1.a6.1jpp.1
- Fix rpmlint issues
- Version package to new jpp versioning standards
- Remove javadoc post and postun sections

* Mon Jun 19 2006 Deepak Bhole <dbhole@redhat.com> - 0:1.0-0.a6.1jpp
- Upgrade to 1.0-alpha-6

* Wed May 31 2006 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.a3.2jpp
- First JPP-1.7 release

* Mon Nov 07 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.a3.1jpp
- First JPackage build
