echo "java config..."
sudo mkdir /usr/local/java
sudo tar -xzvf jdk-8u391-linux-aarch64.tar.gz -C /usr/local/java
cat << EOF >> /etc/profile
JAVA_HOME=/usr/local/java/jdk1.8.0_391
PATH=$PATH:$JAVA_HOME/bin
JRE_HOME=/usr/local/java/jdk1.8.0_181/jre
CLASS_PATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib
PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin
EOF
source /etc/profile
echo "java config done."
