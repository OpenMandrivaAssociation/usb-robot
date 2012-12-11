Name:		usb-robot
Version:	0.2.0
Release:	1	
Summary:	USB Reverse engineering tools

Group:		Development/Other
License:	GPLv2
URL:		http://sourceforge.net/projects/usb-robot
Source0:	http://downloads.sourceforge.net/project/usb-robot/usb-robot/0.2.0/usb-robot-0.2.0.tar.gz

BuildRequires:	usb1-devel
BuildRequires:	libusb-devel
BuildRequires:	readline-devel

%description
usb-robot is a set of software tools for communicating with generic USB devices
from userspace using libusb. 

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%{_bindir}/%{name}-master
%{_bindir}/%{name}-slave
%doc README COPYING


%changelog
* Fri Dec 02 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.2.0-1
+ Revision: 737211
- BuildReq fix
- BuildReq fix
- imported package usb-robot

