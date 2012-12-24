# Copyright 2012 (c) Kyan <kyan.ql.he@gmail.com>
{
  'targets': [
    {
      'target_name': 'ffmpeg',
      'type': 'none',

      'direct_dependent_settings': {
        'include_dirs': [
          'include',
        ],
      },

      'conditions': [
        ['OS == "win"', {
          'link_settings': {
            'libraries': [
              'prebuilt/win/<(target_arch)/lib/avcodec.lib',
              'prebuilt/win/<(target_arch)/lib/avdevice.lib',
              'prebuilt/win/<(target_arch)/lib/avfilter.lib',
              'prebuilt/win/<(target_arch)/lib/avformat.lib',
              'prebuilt/win/<(target_arch)/lib/avutil.lib',
              'prebuilt/win/<(target_arch)/lib/postproc.lib',
              'prebuilt/win/<(target_arch)/lib/swresample.lib',
              'prebuilt/win/<(target_arch)/lib/swscale.lib',
            ]
          }, # link_settings

          'copies': [
            {
              'destination': '<(PRODUCT_DIR)',
              'files': [
                'prebuilt/win/<(target_arch)/bin/avcodec-54.dll',
                'prebuilt/win/<(target_arch)/bin/avdevice-54.dll',
                'prebuilt/win/<(target_arch)/bin/avfilter-3.dll',
                'prebuilt/win/<(target_arch)/bin/avformat-54.dll',
                'prebuilt/win/<(target_arch)/bin/avutil-52.dll',
                'prebuilt/win/<(target_arch)/bin/postproc-52.dll',
                'prebuilt/win/<(target_arch)/bin/swresample-0.dll',
                'prebuilt/win/<(target_arch)/bin/swscale-2.dll',
              ],
            }
          ], # copies
        }], # ['OS == "win"']

      ],
    }
  ],
}
