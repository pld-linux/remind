Summary:	Remind is a full-featured calendar/alarm program
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
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%doc ACKNOWLEDGEMENTS README docs/README.UNIX docs/WHATSNEW.30 remind.lsm www scripts/remind-all.sh
