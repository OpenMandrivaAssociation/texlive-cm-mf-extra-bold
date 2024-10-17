Name:		texlive-cm-mf-extra-bold
Version:	54512
Release:	2
Summary:	Extra Metafont files for CM
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cm-mf-extra-bold
License:	gpl pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cm-mf-extra-bold.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides bold versions of cmcsc, cmex, cmtex and
cmtt fonts (all parts of the standard computer modern font
distribution), as Metafont base files.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/tfm/public/cm-mf-extra-bold
%doc %{_texmfdistdir}/fonts/source/public/cm-mf-extra-bold

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
