#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: eaa4f711da30
#
# Source0 file verified with key 0xEE0F9065BCB8B678 (janwas@google.com)
#
Name     : highway
Version  : 1.2.0
Release  : 1
URL      : https://github.com/google/highway/releases/download/1.2.0/highway-1.2.0.tar.gz
Source0  : https://github.com/google/highway/releases/download/1.2.0/highway-1.2.0.tar.gz
Source1  : https://github.com/google/highway/releases/download/1.2.0/highway-1.2.0.tar.gz.asc
Source2  : EE0F9065BCB8B678.pkey
Summary  : Additions to Highway: dot product, image, math, sort
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: highway-lib = %{version}-%{release}
Requires: highway-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : gnupg
BuildRequires : googletest-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Efficient and performance-portable vector software
[//]: # (placeholder, do not remove)

%package dev
Summary: dev components for the highway package.
Group: Development
Requires: highway-lib = %{version}-%{release}
Provides: highway-devel = %{version}-%{release}
Requires: highway = %{version}-%{release}

%description dev
dev components for the highway package.


%package lib
Summary: lib components for the highway package.
Group: Libraries
Requires: highway-license = %{version}-%{release}

%description lib
lib components for the highway package.


%package license
Summary: license components for the highway package.
Group: Default

%description license
license components for the highway package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) EE0F9065BCB8B678' gpg.status
%setup -q -n highway-1.2.0
cd %{_builddir}/highway-1.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1725913967
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DHWY_SYSTEM_GTEST=ON \
-DINSTALL_GTEST=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1725913967
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/highway
cp %{_builddir}/highway-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/highway/58853eb8199b5afe72a73a25fd8cf8c94285174b || :
cp %{_builddir}/highway-%{version}/LICENSE-BSD3 %{buildroot}/usr/share/package-licenses/highway/8ef530850989072e75f6f743a03e377de4392a68 || :
cp %{_builddir}/highway-%{version}/debian/copyright %{buildroot}/usr/share/package-licenses/highway/7363889d9c7364f41a37d3efa2ec375bc836d916 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/hwy/abort.h
/usr/include/hwy/aligned_allocator.h
/usr/include/hwy/base.h
/usr/include/hwy/cache_control.h
/usr/include/hwy/contrib/algo/copy-inl.h
/usr/include/hwy/contrib/algo/find-inl.h
/usr/include/hwy/contrib/algo/transform-inl.h
/usr/include/hwy/contrib/bit_pack/bit_pack-inl.h
/usr/include/hwy/contrib/dot/dot-inl.h
/usr/include/hwy/contrib/image/image.h
/usr/include/hwy/contrib/math/math-inl.h
/usr/include/hwy/contrib/matvec/matvec-inl.h
/usr/include/hwy/contrib/random/random-inl.h
/usr/include/hwy/contrib/sort/order.h
/usr/include/hwy/contrib/sort/shared-inl.h
/usr/include/hwy/contrib/sort/sorting_networks-inl.h
/usr/include/hwy/contrib/sort/traits-inl.h
/usr/include/hwy/contrib/sort/traits128-inl.h
/usr/include/hwy/contrib/sort/vqsort-inl.h
/usr/include/hwy/contrib/sort/vqsort.h
/usr/include/hwy/contrib/thread_pool/futex.h
/usr/include/hwy/contrib/thread_pool/thread_pool.h
/usr/include/hwy/contrib/thread_pool/topology.h
/usr/include/hwy/contrib/unroller/unroller-inl.h
/usr/include/hwy/detect_compiler_arch.h
/usr/include/hwy/detect_targets.h
/usr/include/hwy/foreach_target.h
/usr/include/hwy/highway.h
/usr/include/hwy/highway_export.h
/usr/include/hwy/nanobenchmark.h
/usr/include/hwy/ops/arm_neon-inl.h
/usr/include/hwy/ops/arm_sve-inl.h
/usr/include/hwy/ops/emu128-inl.h
/usr/include/hwy/ops/generic_ops-inl.h
/usr/include/hwy/ops/inside-inl.h
/usr/include/hwy/ops/ppc_vsx-inl.h
/usr/include/hwy/ops/rvv-inl.h
/usr/include/hwy/ops/scalar-inl.h
/usr/include/hwy/ops/set_macros-inl.h
/usr/include/hwy/ops/shared-inl.h
/usr/include/hwy/ops/wasm_128-inl.h
/usr/include/hwy/ops/x86_128-inl.h
/usr/include/hwy/ops/x86_256-inl.h
/usr/include/hwy/ops/x86_512-inl.h
/usr/include/hwy/per_target.h
/usr/include/hwy/print-inl.h
/usr/include/hwy/print.h
/usr/include/hwy/profiler.h
/usr/include/hwy/robust_statistics.h
/usr/include/hwy/targets.h
/usr/include/hwy/tests/hwy_gtest.h
/usr/include/hwy/tests/test_util-inl.h
/usr/include/hwy/tests/test_util.h
/usr/include/hwy/timer-inl.h
/usr/include/hwy/timer.h
/usr/lib64/cmake/hwy/hwy-config-relwithdebinfo.cmake
/usr/lib64/cmake/hwy/hwy-config-version.cmake
/usr/lib64/cmake/hwy/hwy-config.cmake
/usr/lib64/libhwy.so
/usr/lib64/libhwy_contrib.so
/usr/lib64/libhwy_test.so
/usr/lib64/pkgconfig/libhwy-contrib.pc
/usr/lib64/pkgconfig/libhwy-test.pc
/usr/lib64/pkgconfig/libhwy.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhwy.so.1
/usr/lib64/libhwy.so.1.2.0
/usr/lib64/libhwy_contrib.so.1
/usr/lib64/libhwy_contrib.so.1.2.0
/usr/lib64/libhwy_test.so.1
/usr/lib64/libhwy_test.so.1.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/highway/58853eb8199b5afe72a73a25fd8cf8c94285174b
/usr/share/package-licenses/highway/7363889d9c7364f41a37d3efa2ec375bc836d916
/usr/share/package-licenses/highway/8ef530850989072e75f6f743a03e377de4392a68