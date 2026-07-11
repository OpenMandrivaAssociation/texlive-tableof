%global tl_name tableof
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4d
Release:	%{tl_revision}.1
Summary:	Tagging tables of contents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tableof
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tableof.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tableof.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tableof.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the commands to flag chapters or sections (or
anything else destined to become a TOC line). The command
\nexttocwithtags{req1,req2,...}{excl1,excl2,...} specifies which tags
are to be required and which ones are to be excluded by the next
\tableofcontents (or equivalent) command. In a document that uses a
class where \tableofcontents may only be used once, the command
\tableoftaggedcontents{req1,req2,...}{excl1,excl2,...} may be used to
provide several tables.

