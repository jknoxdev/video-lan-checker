#!/bin/bash
  2>&1
  while read cline; do
      echo "processing $cline"
      sleep 0.01
      while read tline; do
          echo "processing $tline"
          sleep 0.01
          echo "processing: $cline : $tline"
          printf "Username:binary\nPassword:binary" | lpass add --non-interactive \\$cline/$tline
      done < topo-helper-one_list.txt
  done < clients_list
