Name:           mstflint
Summary:        Firmware Burning and Diagnostics Tools
Version:        4.10.0
Release:        8
License:        GPLv2+ or BSD
Url:            https://github.com/Mellanox/mstflint
Source:         https://github.com/Mellanox/%{name}/releases/download/v4.10.0-2/%{name}-%{version}.tar.gz
Patch0000:      0001-Fix-compile-errors.patch
Patch0001:      fix-return-local-addr.patch

BuildRequires:  libstdc++-devel zlib-devel rdma-core-devel gcc-c++ gcc
BuildRequires:  libcurl-devel boost-devel libxml2-devel openssl-devel
Obsoletes:      openib-mstflint <= 1.4 openib-tvflash <= 0.9.2 tvflash <= 0.9.0

%description
This package contains a burning tool and diagnostic tools for Mellanox
manufactured HCA/NIC cards. It also provides access to the relevant source
code. Please see the file LICENSE for licensing details.

%package_help

%prep
%autosetup -p1

%build
export CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS"
%configure --enable-fw-mgr
%make_build

%install
%make_install
strip %{buildroot}/%{_libdir}/mstflint/python_tools/*.so
%delete_la_and_a

%files
%doc README
%{_bindir}/*
%{_sysconfdir}/mstflint
%{_libdir}/mstflint
%{_datadir}/mstflint
%exclude %{_includedir}/

%files help
%{_mandir}/man1/*

%changelog
* Fri Sep 10 2021 Pengju Jiang <jiangpengju2@huawei.com>
- solve the strip problem of dark conversion compilation

* Tue Aug 4 2021 shdluan@163.com <shdluan@163.com> - 4.10.0-7
- fix return local addr

* Tue Jul 28 2020 lingsheng <lingsheng@huawei.com> - 4.10.0-6
- change the libibmad-devel to rdma-core-devel

* Tue May 19 2020 lizhenhua <lizhenhua12@huawei.com> - 4.10.0-5
- Fix compile errors for gcc9

* Wed Dec 11 2019 catastrowings <jianghuhao1994@163.com> - 4.10.0-4
- openEuler init
