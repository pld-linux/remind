Summary:	Remind is a full-featured calendar/alarm program
Summary(pl):	Remind jest kalendarzem przypominaj╠cym o zdarzeniach
Summary(ru_RU.KOI8-R):	Полноценный органайзер
Summary(uk_UA.KOI8-U):	Повноц╕нний ор╜анайзер
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
W peЁni funkcjonalny i wyposa©ony kalendarz przypominaj╠cy o zdarzeniach;
mo©liwo╤ci obejmuj╠ wyszukane operacje na datach, fazy ksiЙ©yca, wschody
i zachody sЁoЯca, kalendarz Hebrajski, alarmy, wyj╤cie w formacie
PostScript, graficzny interfejs w Tcl/Tk, wielojЙzyczne komunikaty i
wЁa╤ciw╠ obsЁugЙ wakacji.  DostЙpny m.in. dla platform UNIX, MS-DOS, OS/2.
Zawiera skrypty do tworzenia przyjemnego serwera WWW z kalendarzami.

%description -l ru_RU.KOI8-R
Полноценный органайзер с большими возможностями по манипуляции датами,
поддержкой вычисления фаз луны и времени заката/восхода, еврейским
календарем, предупреждениями, выводом в PostScript, дополнительным
графическим интерфейсом и надлежащей поддержкой праздников. Программа
доступна для UNIX, DOS, OS/2 и других платформ. Включает скрипты для
создания функционального сервера календаринга.

%description -l uk_UA.KOI8-U
Повноц╕нний ор╜анайзер ╕з великими можливостями щодо ман╕пуляц╕╖
датами, п╕дтримкою обчислення фаз м╕сяця та часу сходу та заходу
сонця, ╓врейським календарем, попередженнями, виводом у PostScript,
додатковим граф╕чним ╕нтерфейсом та належною п╕дтримкою свят. Програма
доступна для UNIX, DOS, OS/2 та ╕нших платформ. Включа╓ скрипти для
створення функц╕онального серверу календарин╜а.

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
