%global tl_name cm-mf-extra-bold
%global tl_revision 54512

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Extra Metafont files for CM
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cm/mf-extra/bold
License:	gpl pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cm-mf-extra-bold.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides bold versions of cmcsc, cmex, cmtex and cmtt fonts
(all parts of the standard computer modern font distribution), as
Metafont base files.

