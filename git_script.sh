#!/bin/bash
git add .  
if [ $# -eq 0]
  then
    read -p "Commit description: " desc 
    git commit -m "$desc"
  else
    git commit -m $0
fi 

git push
