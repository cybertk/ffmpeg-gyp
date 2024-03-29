# Copyright 2012 (c) Kyan <kyan.ql.he@gmail.com>
{
  'variables': {
    'conditions': [
      ['OS == "linux"', {
        'use_system_ffmpeg%': 1,
      }, { # else, OS != "linux"
        'use_system_ffmpeg%': 0,
      }], # end, OS == "linux"
    ],
  }, # variables

  'targets': [
    {
      'target_name': 'ffmpeg',
      'type': '<(component)',

      'direct_dependent_settings': {
        'defines': [
          '__STDC_CONSTANT_MACROS', # for use UINT64_C().
        ],
      },

      'conditions': [
        ['use_system_ffmpeg == 1', {
          'link_settings': {
            'libraries': [
              # avdevice, avfilter, postproc are not used by our project.
              '-lavcodec',
              '-lavformat',
              '-lavutil',
              '-lswresample',
              '-lswscale',
            ],
          },
        }, { # else, use_system_ffmpeg != 1
      'direct_dependent_settings': {
        'include_dirs': [
          'include',
        ],
      },

      'conditions': [
        ['OS == "win"', {
          'type': 'none',
          'direct_dependent_settings': {
            'include_dirs': [
              'config/vc',
            ],
          },

          'link_settings': {
            'libraries': [
              'prebuilt/win/<(target_arch)/lib/avcodec.lib',
              'prebuilt/win/<(target_arch)/lib/avformat.lib',
              'prebuilt/win/<(target_arch)/lib/avutil.lib',
              'prebuilt/win/<(target_arch)/lib/swresample.lib',
              'prebuilt/win/<(target_arch)/lib/swscale.lib',
            ]
          }, # link_settings

          'include_dirs': [
            'config/vc',
          ],

          'copies': [
            {
              'destination': '<(PRODUCT_DIR)',
              'files': [
                'prebuilt/win/<(target_arch)/bin/avcodec-54.dll',
                'prebuilt/win/<(target_arch)/bin/avformat-54.dll',
                'prebuilt/win/<(target_arch)/bin/avutil-52.dll',
                'prebuilt/win/<(target_arch)/bin/swresample-0.dll',
                'prebuilt/win/<(target_arch)/bin/swscale-2.dll',
              ],
            }
          ], # copies
        }], # ['OS == "win"']
      ], # conditions

        }], # end, use_system_ffmpeg == 1
      ], # conditions
    },
  ],
}
