{
    "targets": [{
        "target_name": "native",
        "sources": [ "src/hashtable.cpp" ],
        "include_dirs" : [ "<!(node -e \"require('nan')\")" ],
        "cflags" : ["-O2"],
        "xcode_settings": {
                "OTHER_CFLAGS" : ["-O2"]
              },
        "conditions": [
            ['OS=="linux"', {
                "cflags": [ "-std=c++11", "-Wall" , "-O2"]
            }, {
                "cflags": [ "-std=c++11", "-stdlib=libc++", "-Wall" , "-O2"]
            }]
        ]
    }
  ]
}
