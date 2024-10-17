Name:		texlive-tableof
Version:	59837
Release:	2
Summary:	Tagging tables of contents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tableof
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tableof.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tableof.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tableof.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the commands to flag chapters or sections
(or anything else destined to become a TOC line). The command
\nexttocwithtags{req1,req2,...}{excl1,excl2,...} specifies
which tags are to be required and which ones are to be excluded
by the next \tableofcontents (or equivalent) command. In a
document that uses a class where \tableofcontents may only be
used once, the command
\tableoftaggedcontents{req1,req2,...}{excl1,excl2,...} may be
used to provide several tables.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tableof
%doc %{_texmfdistdir}/doc/latex/tableof
#- source
%doc %{_texmfdistdir}/source/latex/tableof

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
