Summary:	Remind is a full-featured calendar/alarm program
Summary(pl.UTF-8):	Remind - kalendarz przypominający o zdarzeniach
Summary(ru.UTF-8):	Полноценный органайзер
Summary(uk.UTF-8):	Повноцінний орґанайзер
Name:		remind
Version:	03.01.10
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.roaringpenguin.com/files/download/%{name}-%{version}.tar.gz
# Source0-md5:	f6f7829d3ac92e0d6d463c59b5e6ce3f
Patch0:		%{name}-fix_paths.patch
Patch1:		%{name}-missing_include.patch
URL:		http://www.roaringpenguin.com/products/remind
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Full-featured calendar/reminder program featuring sophisticated date
calculation, moon phases, sunrise/sunset, Hebrew calendar, alarms,
PostScript output, Tcl/Tk GUI front-end, multilingual messages, and
proper handling of holidays. Available for UNIX, MS-DOS, OS/2, and
other platforms. Includes scripts for making a nice WWW calendar
server.

%description -l pl.UTF-8
W pełni funkcjonalny i wyposażony kalendarz przypominający o
zdarzeniach; możliwości obejmują wyszukane operacje na datach, fazy
księżyca, wschody i zachody słońca, kalendarz Hebrajski, alarmy,
wyjście w formacie PostScript, graficzny interfejs w Tcl/Tk,
wielojęzyczne komunikaty i właściwą obsługę wakacji. Dostępny m.in.
dla platform UNIX, MS-DOS, OS/2. Zawiera skrypty do tworzenia
przyjemnego serwera WWW z kalendarzami.

%description -l ru.UTF-8
Полноценный органайзер с большими возможностями по манипуляции датами,
поддержкой вычисления фаз луны и времени заката/восхода, еврейским
календарем, предупреждениями, выводом в PostScript, дополнительным
графическим интерфейсом и надлежащей поддержкой праздников. Программа
доступна для UNIX, DOS, OS/2 и других платформ. Включает скрипты для
создания функционального сервера календаринга.

%description -l uk.UTF-8
Повноцінний орґанайзер із великими можливостями щодо маніпуляції
датами, підтримкою обчислення фаз місяця та часу сходу та заходу
сонця, єврейським календарем, попередженнями, виводом у PostScript,
додатковим графічним інтерфейсом та належною підтримкою свят. Програма
доступна для UNIX, DOS, OS/2 та інших платформ. Включає скрипти для
створення функціонального серверу календаринґа.

%package tkremind
Summary:	tkremind - Tcl/Tk GUI front-end for remind
Summary(pl.UTF-8):	tkremind - GUI dla remind w Tcl/Tk
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Requires:	tk

%description tkremind
tkremind - Tcl/Tk GUI front-end for remind.

%description tkremind -l pl.UTF-8
tkremind - GUI dla remind w Tcl/Tk.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/README.UNIX docs/WHATSNEW www 
%attr(755,root,root) %{_bindir}/[ckr]*
%{_mandir}/man?/[ckr]*

%files tkremind
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tkremind
%{_mandir}/man?/tkremind*
