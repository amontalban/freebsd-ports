--- ./native_client/src/trusted/debug_stub/debug_stub.gyp.orig	2014-04-24 22:36:36.000000000 +0200
+++ ./native_client/src/trusted/debug_stub/debug_stub.gyp	2014-04-24 23:23:46.000000000 +0200
@@ -27,7 +27,7 @@
       'test.cc',
     ],
     'conditions': [
-      ['OS=="linux" or OS=="mac"', {
+      ['OS=="linux" or OS=="freebsd" or OS=="mac"', {
         'platform_sources': [
           'posix/debug_stub_posix.cc',
           'posix/platform_impl.cc',
@@ -49,7 +49,7 @@
       'target_base': 'none',
     },
     'target_conditions': [
-      ['OS=="linux" or OS=="mac"', {
+      ['OS=="linux" or OS=="freebsd" or OS=="mac"', {
         'cflags': [
           '-fexceptions',
         ],
