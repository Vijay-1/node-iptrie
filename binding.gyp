{
  "targets": [
    {
      "include_dirs" : [ "<!(node -e \"require('nan')\")" ],
      "target_name": "iptrie",
      "sources": [ "src/iptrie.cc", "src/btrie.cc" ]
    }
  ]
}
