Name:		texlive-quoting
Version:	32818
Release:	2
Summary:	Consolidated environment for displayed text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/quoting
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quoting.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quoting.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quoting.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
As an alternative to the LaTeX standard environments quotation
and quote, the package provides a consolidated environment for
displayed text. First-line indentation may be activated by
adding a blank line before the quoting environment. A key-value
interface (using kvoptions) allows the user to configure font
properties and spacing and to control orphans within and after
the environment.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/quoting/quoting.sty
%doc %{_texmfdistdir}/doc/latex/quoting/README
%doc %{_texmfdistdir}/doc/latex/quoting/quoting.pdf
#- source
%doc %{_texmfdistdir}/source/latex/quoting/quoting.dtx
%doc %{_texmfdistdir}/source/latex/quoting/quoting.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
