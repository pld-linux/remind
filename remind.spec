Summary:	Remind is a full-featured calendar/alarm program
Summary(pl):	Remind jest kalendarzem przypominaj�cym o zdarzeniach
Summary(ru_RU.KOI8-R):	����������� ����������
Summary(uk_UA.KOI8-U):	�����æ���� �ҭ�������
Name:		remind
Version:	03.00.22
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://roaringpenguin.com/penguin/%{name}-%{version}.tar.gz
# Source0-md5:	5655ad8209f8453443d0b95658cd82ca
# Source0-size:	319556
Patch0:		%{name}-alt.patch
Patch1:		%{name}-missing_include.patch
URL:		http://roaringpenguin.com/penguin/open_source_remind.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Full-featured calendar/reminder program featuring sophisticated date
calculation, moon phases, sunrise/sunset, Hebrew calendar, alarms,
PostScript output, Tcl/Tk GUI front-end, multilingual messages, and
proper handling of holidays. Available for UNIX, MS-DOS, OS/2, and
other platforms. Includes scripts for making a nice WWW calendar
server.

%description
W pe�ni funkcjonalny i wyposa�ony kalendarz przypominaj�cy o zdarzeniach;
mo�liwo�ci obejmuj� wyszukane operacje na datach, fazy ksi�yca, wschody
i zachody s�o�ca, kalendarz Hebrajski, alarmy, wyj�cie w formacie
PostScript, graficzny interfejs w Tcl/Tk, wieloj�zyczne komunikaty i
w�a�ciw� obs�ug� wakacji.  Dost�pny m.in. dla platform UNIX, MS-DOS, OS/2.
Zawiera skrypty do tworzenia przyjemnego serwera WWW z kalendarzami.

%description -l ru_RU.KOI8-R
����������� ���������� � �������� ������������� �� ����������� ������,
���������� ���������� ��� ���� � ������� ������/�������, ���������
����������, ����������������, ������� � PostScript, ��������������
����������� ����������� � ���������� ���������� ����������. ���������
�������� ��� UNIX, DOS, OS/2 � ������ ��������. �������� ������� ���
�������� ��������������� ������� ������������.

%description -l uk_UA.KOI8-U
�����æ���� �ҭ������� �� �������� ������������ ���� ��Φ����æ�
������, Ц�������� ���������� ��� ͦ���� �� ���� ����� �� ������
�����, ���������� ����������, ��������������, ������� � PostScript,
���������� ���Ʀ���� ����������� �� �������� Ц�������� ����. ��������
�������� ��� UNIX, DOS, OS/2 �� ����� ��������. ������� ������� ���
��������� ����æ��������� ������� ���������έ�.

%package tkremind
Summary:	tkremind - Tcl/Tk GUI front-end for remind
Summary(pl):	tkremind - GUI dla remind w Tcl/Tk
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Requires:	tk

%description tkremind
tkremind - Tcl/Tk GUI front-end for remind.

%description tkremind -l pl
tkremind - GUI dla remind w Tcl/Tk.

%prep
%setup -q
#%patch0 -p1
%patch1 -p0

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/[ckr]*
%{_mandir}/man?/[ckr]*
%doc ACKNOWLEDGEMENTS README docs/README.UNIX docs/WHATSNEW.30 remind.lsm www scripts/remind-all.sh

%files tkremind
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tkremind
%{_mandir}/man?/tkremind*
