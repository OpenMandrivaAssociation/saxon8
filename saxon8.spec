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

%define section free
%define resolverdir %{_sysconfdir}/java/resolver
%define stdname saxon8
%define gcj_support 1

Name:           saxon8
Version:        B.8.7
Release:        %mkrel 1.1.1
Epoch:          0
Summary:        Java  Basic XPath 2.0, XSLT 2.0, and XQuery 1.0 implementation
License:        MPL
Group:          Development/Java
URL:            http://saxon.sourceforge.net/
Source0:        http://download.sf.net/saxon/saxon-resources8-7.zip
Source1:        %{name}.saxon.script
Source2:                %{name}.saxonq.script
Source3:        %{name}.build.script
Source4:        %{stdname}.1
Source5:                %{stdname}q.1
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:        bea-stax-api
BuildRequires:  xml-commons-apis
BuildRequires:  xom
BuildRequires:  jdom >= 0:1.0-0.b7
BuildRequires:  java-javadoc
BuildRequires:  jdom-javadoc >= 0:1.0-0.b9.3jpp
Requires:                bea-stax-api
Requires:                bea-stax
Requires:       jaxp_parser_impl
Requires:       /usr/sbin/update-alternatives
Provides:       jaxp_transform_impl
%if %{gcj_support}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
BuildRequires:  java-devel
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Release 8.6 represents an important milestone in Saxonica's 
progressive implementation of the XPath 2.0, XSLT 2.0, and 
XQuery 1.0 specifications. Saxon 8.6 is aligned with the W3C 
Candidate Recommendation published on 3 November 2005. It is 
a complete and conformant implementation, providing all the 
mandatory features of those specifications and nearly all the 
optional features. 
Saxon is available in two versions. Saxon-B is a non-schema-aware 
processor, and is available as an open-source product, free of 
charge, from SourceForge. It is designed to conform to the basic 
conformance level of XSLT 2.0, and the equivalent level of 
functionality in XQuery 1.0. Saxon-SA is the schema-aware version 
of the package, and is available as a commercially supported 
product from Saxonica Limited. 

This package provides the Basic XSLT 2.0 and XQuery 1.0 processor.
Includes the command line interfaces and the JAVA APIs; also
includes a standalone XPath API that doesn't depend on JAXP 1.3. 


%package        manual
Summary:        Manual for %{name}
Group:          Development/Java

%description    manual
Manual for %{name}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java

%description    javadoc
Javadoc for %{name}.

%package        demo
Summary:        Demos for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    demo
Demonstrations and samples for %{name}.

%package        sql
Summary:        SQL support for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    sql
Supports XSLT extensions for accessing and updating a 
relational database from within a stylesheet. 

%package        jdom
Summary:        JDOM support for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jdom >= 0:1.0-0.b7

%description    jdom
Provides additional classes enabling Saxon to be used with 
JDOM trees. Supports using a JDOM document as the input or 
output of transformations and queries. Requires jdom.jar on 
the classpath. 

%package        dom
Summary:        DOM support for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
#Requires:       jdom >= 0:1.0-0.b7

%description    dom
Provides additional classes enabling Saxon to be used with 
the DOM Document Object Model. Supports using a DOM as the 
input or output of transformations and queries, and calling 
extension functions that use DOM interfaces to access a 
Saxon tree structure. Requires DOM level 3 (dom.jar, part 
of JAXP 1.3) to be on the classpath, if not running under 
JDK 1.5. 

%package        xom
Summary:        XOM support for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       xom

%description    xom
Provides additional classes enabling Saxon to be used with 
XOM trees. Supports using a XOM document as the input or 
output of transformations and queries. Requires xom.jar on 
the classpath. 

%package        xpath
Summary:        XPATH support for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    xpath
Provides support for the JAXP 1.3 XPath API. Requires the 
JAXP 1.3 version of jaxp-api.jar on the classpath, if not 
running under JDK 1.5. 

%package        scripts
Summary:        Utility scripts for %{name}
Group:          Development/Java
Requires:       jpackage-utils >= 0:1.5
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    scripts
Utility scripts for %{name}.


%prep
%setup -q -c
mkdir src
(cd src
unzip -q ../source.zip
find . -name CVS -exec rm -rf {} \;

# Clean up .NET classes
rm -rf net/sf/saxon/dotnet/)

cp -p %{SOURCE3} ./build.xml
# cleanup unnecessary stuff we'll build ourselves
rm -rf docs/api
find . -name "*.jar" -exec rm {} \;
#for j in $(find . -name "*.jar"); do
#        mv $j $j.no
#done

%build
export CLASSPATH=$(build-classpath xml-commons-apis jdom xom bea-stax-api)
%{ant} \
  -Dj2se.javadoc=%{_javadocdir}/java \
  -Djdom.javadoc=%{_javadocdir}/jdom

%install
rm -rf $RPM_BUILD_ROOT

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/lib/%{stdname}.jar $RPM_BUILD_ROOT%{_javadir}/%{stdname}-%{version}.jar
cp -p build/lib/%{stdname}-xpath.jar $RPM_BUILD_ROOT%{_javadir}/%{stdname}-xpath-%{version}.jar
cp -p build/lib/%{stdname}-xom.jar $RPM_BUILD_ROOT%{_javadir}/%{stdname}-xom-%{version}.jar
cp -p build/lib/%{stdname}-sql.jar $RPM_BUILD_ROOT%{_javadir}/%{stdname}-sql-%{version}.jar
cp -p build/lib/%{stdname}-jdom.jar $RPM_BUILD_ROOT%{_javadir}/%{stdname}-jdom-%{version}.jar
cp -p build/lib/%{stdname}-dom.jar $RPM_BUILD_ROOT%{_javadir}/%{stdname}-dom-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr samples/* $RPM_BUILD_ROOT%{_datadir}/%{name}

# scripts
mkdir -p $RPM_BUILD_ROOT%{_bindir}
sed 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE1} \
  > $RPM_BUILD_ROOT%{_bindir}/%{stdname}
sed 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE2} \
  > $RPM_BUILD_ROOT%{_bindir}/%{stdname}q
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
sed 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE4} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/%{stdname}.1
sed 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE5} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/%{stdname}q.1

# jaxp_transform_impl ghost symlink
ln -s %{_sysconfdir}/alternatives \
  $RPM_BUILD_ROOT%{_javadir}/jaxp_transform_impl.jar
# jaxp_parser_impl ghost symlink
#ln -s %{_sysconfdir}/alternatives \
#  $RPM_BUILD_ROOT%{_javadir}/jaxp_parser_impl.jar

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
%if %{gcj_support}
%{update_gcjdb}
%endif
update-alternatives --install %{_javadir}/jaxp_transform_impl.jar \
  jaxp_transform_impl %{_javadir}/%{stdname}.jar 25

%preun
{
  [ $1 -eq 0 ] || exit 0
  update-alternatives --remove jaxp_transform_impl %{_javadir}/%{stdname}.jar
} >/dev/null 2>&1 || :

%if %{gcj_support}
%postun
%{clean_gcjdb}
%endif

%files
%defattr(0644,root,root,0755)
%{_javadir}/%{stdname}.jar
%{_javadir}/%{stdname}-%{version}.jar
%ghost %{_javadir}/jaxp_transform_impl.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/java*
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{stdname}-%{version}*
%endif

%files xpath
%defattr(0644,root,root,0755)
%{_javadir}/%{stdname}-xpath*
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{stdname}-xpath*
%endif

%files xom
%defattr(0644,root,root,0755)
%{_javadir}/%{stdname}-xom*
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{stdname}-xom*
%endif

%files sql
%defattr(0644,root,root,0755)
%{_javadir}/%{stdname}-sql*
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{stdname}-sql*
%endif

%files jdom
%defattr(0644,root,root,0755)
%{_javadir}/%{stdname}-jdom*
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{stdname}-jdom*
%endif

%files dom
%defattr(0644,root,root,0755)
%{_javadir}/%{stdname}-dom*
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{stdname}-dom*
%endif

%files manual
%defattr(0644,root,root,0755)
%doc doc/*.html

%files javadoc
%defattr(0644,root,root,0755)
%dir %doc %{_javadocdir}/%{name}
%doc %{_javadocdir}/%{name}-%{version}

%files demo
%defattr(0644,root,root,0755)
%{_datadir}/%{name}

%files scripts
%defattr(0755,root,root,0755)
%{_bindir}/%{stdname}
%{_bindir}/%{stdname}q
%attr(0644,root,root) %{_mandir}/man1/%{stdname}.1*
%attr(0644,root,root) %{_mandir}/man1/%{stdname}q.1*
