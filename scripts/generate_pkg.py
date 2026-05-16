#!/usr/bin/env python3
from __future__ import print_function
from shutil import copy
import os
import sys

code_clsid_map = {
  'x86': '8E31E1B4-F42E-4D30-AEAE-B34C70A4B0F1',
  'x64': '01607B4B-B639-44B5-86B9-3E134C67632D',
  'arm64': 'D905884C-EE96-4BC2-9771-9ABFFC4E214B'
}

code_insiders_clsid_map = {
  'x86': 'D905884C-EE96-4BC2-9771-9ABFFC4E214B',
  'x64': '7A2FA6D0-4E71-4211-8FA9-F4C7600936B3',
  'arm64': '0D8C9915-F368-4610-BBC7-B29A66DA13B1'
}

root = os.path.dirname(os.path.dirname(__file__))
out_dir = os.path.join(root, 'out')
pkg_type = sys.argv[1]
arch = sys.argv[2]
pkg_dir = os.path.join(out_dir, pkg_type + '_explorer_pkg_' + arch)

# Create output directory.
if not os.path.exists(pkg_dir):
    os.mkdir(pkg_dir)

# Update AppxManifest.
manifest = os.path.join(root, 'template', 'AppxManifest.xml')
with open(manifest, 'r') as f:
  content = f.read()
  content = content.replace('@@PublisherDisplayName@@', 'Trae Modern Explorer Menu')
  if pkg_type == 'stable':
    content = content.replace('@@Publisher@@', 'Trae.Modern.Explorer.Menu')
    content = content.replace('@@PackageDescription@@', 'Trae Modern Explorer Menu')
    content = content.replace('@@PackageName@@', 'Trae.Modern.Explorer.Menu')
    content = content.replace('@@PackageDisplayName@@', 'Trae Modern Explorer Menu')
    content = content.replace('@@Application@@', 'Trae.exe')
    content = content.replace('@@ApplicationIdShort@@', 'Trae')
    content = content.replace('@@MenuID@@', 'OpenWithTrae')
    content = content.replace('@@CLSID@@', code_clsid_map[arch])
    content = content.replace('@@PackageDLL@@', 'Trae Modern Explorer Menu.dll')
  if pkg_type == 'insiders':
    content = content.replace('@@Publisher@@', 'Trae.Insiders.Modern.Explorer.Menu')
    content = content.replace('@@PackageDescription@@', 'Trae Insiders Modern Explorer Menu')
    content = content.replace('@@PackageName@@', 'Trae.Insiders.Modern.Explorer.Menu')
    content = content.replace('@@PackageDisplayName@@', 'Trae Insiders Modern Explorer Menu')
    content = content.replace('@@Application@@', 'Trae - Insiders.exe')
    content = content.replace('@@ApplicationIdShort@@', 'TraeInsiders')
    content = content.replace('@@MenuID@@', 'OpenWithTraeInsiders')
    content = content.replace('@@CLSID@@', code_insiders_clsid_map[arch])
    content = content.replace('@@PackageDLL@@', 'Trae Insiders Modern Explorer Menu.dll')

# Copy AppxManifest file to the package directory.
manifest_output = os.path.join(pkg_dir, 'AppxManifest.xml')
with open(manifest_output, 'w+') as f:
  f.write(content)