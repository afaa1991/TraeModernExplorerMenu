{
  'target_defaults': {
    'conditions': [
      [ 'OS=="win"', {
        'sources': [
          'src/explorer_command.cc',
          'src/explorer_command.def',
        ],
        'include_dirs': [
          'vcpkg_installed/<(target_arch)-windows/include/fmt',
          'vcpkg_installed/<(target_arch)-windows/include/wil',
        ],
        'defines': [
          '_WINDLL',
          'WIN32_LEAN_AND_MEAN',
          '_UNICODE',
          'UNICODE',
          '_CRT_SECURE_NO_DEPRECATE',
          '_CRT_NONSTDC_NO_DEPRECATE',
        ],
        'msvs_settings': {
          'WindowsTargetPlatformVersion': '10',
          'LanguageStandard': 'stdcpp20',
          'VCLinkerTool': {
            'AdditionalOptions': [
              '/guard:cf',
            ],
            'OptimizeReferences': 2,             # /OPT:REF
            'EnableCOMDATFolding': 2,            # /OPT:ICF
          },
          'VCCLCompilerTool': {
            'AdditionalOptions': [
              '/Zc:__cplusplus',
              '/std:c++20',
              '/Qspectre',
              '/guard:cf',
              '/utf-8'
            ],
            'BufferSecurityCheck': 'true',
            'ExceptionHandling': 1,               # /EHsc
            'EnableFunctionLevelLinking': 'true',
            'Optimization': 3,              # /Ox, full optimization
          },
        },
        'libraries': [
          '-ladvapi32.lib',
          '-lruntimeobject.lib',
          '-lshlwapi.lib',
          '-lonecore.lib',
        ]
      }],
    ],
  },
  'targets': [{
    'target_name': 'Trae Modern Explorer Menu',
    'type': 'shared_library',
    'defines': [
      'EXE_NAME="Trae CN.exe"',
      'DIR_NAME="Trae CN"',
    ],
    'conditions': [
      [ 'OS=="win"', {
        'conditions': [
          ['target_arch=="x64"', {
            'TargetMachine' : 17,             # /MACHINE:X64
            'defines': [ 
              'DLL_UUID="01607B4B-B639-44B5-86B9-3E134C67632D"',
            ],
          }],
          ['target_arch=="arm64"', {
            'TargetMachine' : 18,             # /MACHINE:ARM64 https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.vcprojectengine.machinetypeoption?view=visualstudiosdk-2022
            'defines': [ 
              'DLL_UUID="D905884C-EE96-4BC2-9771-9ABFFC4E214B"',
            ],
          }],
        ],
      }],
    ],
  }, {
    'target_name': 'Trae Insiders Modern Explorer Menu',
    'type': 'shared_library',
    'defines': [
      'EXE_NAME="Trae - Insiders.exe"',
      'DIR_NAME="Trae CN Insiders"',
      'INSIDER=1',
    ],
    'conditions': [
      [ 'OS=="win"', {
        'conditions': [
          ['target_arch=="x64"', {
            'TargetMachine' : 17,             # /MACHINE:X64
            'defines': [ 
              'DLL_UUID="7A2FA6D0-4E71-4211-8FA9-F4C7600936B3"',
            ],
          }],
          ['target_arch=="arm64"', {
            'TargetMachine' : 18,             # /MACHINE:ARM64
            'defines': [ 
              'DLL_UUID="0D8C9915-F368-4610-BBC7-B29A66DA13B1"',
            ],
          }],
        ],
      }],
    ],
  }],
}