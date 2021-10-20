update(){
  # bypass: Could not get lock
  pkill apt-get

}

install(){
  # install requirements
  for i in `cat requirements.txt`
  do
     apt-get install $i -y
  done

  # clean up
  apt autoremove -y
}

# run
update
install
