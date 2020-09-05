#!/bin/bash
export PROJ_PATH=/root/.jenkins/workspace/
#tomcat path
#export tomcat_app_path=/usr/java/tomcat8/tomcat8.5.54

#killTomcat()
#{
# cd $tomcat_app_path/bin
# sh shutdown.sh
#}
cd $PROJ_PATH/interfaceTest/cmd
python3 report.py





 
