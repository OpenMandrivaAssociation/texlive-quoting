# revision 25474
# category Package
# catalog-ctan /macros/latex/contrib/quoting
# catalog-date 2012-02-22 10:43:42 +0100
# catalog-license lppl1.3
# catalog-version v0.1b
Name:		texlive-quoting
Version:	v0.1b
Release:	4
Summary:	Consolidated environment for displayed text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/quoting
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quoting.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quoting.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quoting.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> v0.1b-1
+ Revision: 780577
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v0.1a-2
+ Revision: 755572
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v0.1a-1
+ Revision: 719426
- texlive-quoting
- texlive-quoting
- texlive-quoting
- texlive-quoting

