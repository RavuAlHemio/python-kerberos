##
# Copyright (c) 2006 Apple Computer, Inc. All rights reserved.
#
# This file contains Original Code and/or Modifications of Original Code
# as defined in and that are subject to the Apple Public Source License
# Version 2.0 (the 'License'). You may not use this file except in
# compliance with the License. Please obtain a copy of the License at
# http://www.opensource.apple.com/apsl/ and read it before using this
# file.
# 
# The Original Code and all software distributed under the License are
# distributed on an 'AS IS' basis, WITHOUT WARRANTY OF ANY KIND, EITHER
# EXPRESS OR IMPLIED, AND APPLE HEREBY DISCLAIMS ALL SUCH WARRANTIES,
# INCLUDING WITHOUT LIMITATION, ANY WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE, QUIET ENJOYMENT OR NON-INFRINGEMENT.
# Please see the License for the specific language governing rights and
# limitations under the License.
#
# DRI: Cyrus Daboo, cdaboo@apple.com
##

from distutils.core import setup, Extension

module1 = Extension(
    'kerberos',
    extra_link_args = ['-framework', 'Kerberos'],
    sources = [
        'src/kerberos.c',
        'src/kerberosbasic.c',
        'src/kerberosgss.c',
        'src/base64.c'
    ],
)

setup (
    name = 'kerberos',
    version = '1.0',
    description = 'This is a high-level interface to the Kerberos.framework',
    ext_modules = [module1]
)
