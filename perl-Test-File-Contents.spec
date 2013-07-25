%define upstream_name    Test-File-Contents
%define upstream_version 0.21

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.21
Release:	1

Summary:	%{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-File-Contents-0.21.tar.gz

BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Diff)
BuildRequires:	perl(Module::Build)
BuildArch:	noarch

%description
%{upstream_name} perl module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes META.json META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


