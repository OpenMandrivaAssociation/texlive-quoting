%global tl_name quoting
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1c
Release:	%{tl_revision}.1
Summary:	Consolidated environment for displayed text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/quoting
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quoting.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quoting.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quoting.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
As an alternative to the LaTeX standard environments quotation and
quote, the package provides a consolidated environment for displayed
text. First-line indentation may be activated by adding a blank line
before the quoting environment. A key-value interface (using kvoptions)
allows the user to configure font properties and spacing and to control
orphans within and after the environment.

