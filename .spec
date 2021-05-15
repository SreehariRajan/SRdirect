# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['.'],
             pathex=['C:/Program Files (x86)/Windows Kits/10/Redist/10.0.19041.0/ucrt/DLLs/x64', 'C:/Program Files (x86)/Windows Kits/10/Redist/10.0.19041.0/ucrt/DLLs/x86', 'C:\\Users\\Rajan\\Desktop\\studfinal'],
             binaries=[],
             datas=[],
             hiddenimports=['_posixsubprocess,multiprocessing.util,org,_frozen_importlib_external,importlib,importlib.abc,zipimport,_frozen_importlib,PyInstaller.loader.pyimod02_archive,urllib.pathname2url,PyInstaller.lib.modulegraph._compat,_posixshmem,multiprocessing.shared_memory,multiprocessing.set_start_method,multiprocessing.spawn,multiprocessing.get_start_method,multiprocessing.get_context,multiprocessing.TimeoutError,_scproxy,termios,java.lang,multiprocessing.BufferTooShort,multiprocessing.AuthenticationError,asyncio.DefaultEventLoopPolicy,vms_lib,java,_winreg,readline,org.python,grp,pwd,posix,resource,win32com.gen_py,pyimod03_importers,_uuid,__builtin__,ordereddict,com.sun,com,StringIO,pkg_resources.extern.pyparsing,pkg_resources.extern.packaging,pkg_resources.extern.appdirs,pkg_resources.extern.six.moves,pkg_resources.extern.six,regex.DEFAULT_VERSION,PyQt4,sip,shiboken,PySide,shiboken2,PySide2,QtSiteConfig,setuptools.extern.packaging,setuptools.extern.six,setuptools.extern.packaging.specifiers,setuptools.extern.packaging.version,setuptools.extern.six.moves.filterfalse,setuptools.extern.six.moves.filter,setuptools.extern.ordered_set,setuptools.extern.packaging.utils,setuptools.extern.packaging.tags,wincertstore,backports.ssl_match_hostname,backports,setuptools._vendor.six.moves,setuptools.extern.pyparsing,_manylinux,setuptools.extern.six.moves.map,setuptools.extern.six.moves,setuptools.extern.six,numpy_distutils.cpuinfo,numpy_distutils.fcompiler,numpy_distutils.command,numpy_distutils,__svn_version__,numarray,Numeric,_curses,_dummy_threading,hypothesis,nose.plugins,scipy,nose.util,nose,psutil,pytest,numpy.core.number,numpy.core.object_,numpy.core.signbit,numpy.core.isnan,numpy.core.float32,numpy.core.intp,numpy.lib.i0,numpy.linalg.matrix_power,numpy.core.integer,numpy.core.sqrt,numpy.core.conjugate,numpy.core.sign,numpy.core.divide,numpy.core.geterrobj,numpy.core.add,numpy.core.complexfloating,numpy.core.inexact,numpy.core.cdouble,numpy.core.csingle,numpy.core.double,numpy.core.single,numpy.linalg.inv,numpy.linalg.lstsq,numpy.linalg.eigvals,pickle5,numpy.recarray,numpy.dtype,numpy.expand_dims,numpy.array,numpy.bool_,numpy.iscomplexobj,numpy.amin,numpy.amax,numpy.ndarray,numpy.histogramdd,numpy.eye,olefile,PySide2.QtCore,cffi,httplib,urllib2,xmlrpclib,Queue,ConfigParser,_mysql_connector'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Users\\Rajan\\Desktop\\studfinal\\5.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='')
