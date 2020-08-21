#!/bin/bash

if [ -z ${oldPS1+x} ] 
then
	oldPS1=$PS1
fi	
PS1="(looper) $oldPS1"



export LOOPERPATH=$(pwd)/lib


t(){
	echo $LOOPERPATH
	if [ -t 0 ]
	then
		echo uwu $@
	else
		read line
		echo $line
	fi
}

play()
{
	if [ -t 0 ]
	then
		python3 "$LOOPERPATH/play.py" $@ 
		return $?
	else
		args=()
		while read line
		do
			args+=$line
		done
		python3 "$LOOPERPATH/play.py" $args $@
		return $?
	fi
}

slice()
{
	if [ -t 0 ]
	then
		python3 "$LOOPERPATH/slice.py" $@
		return $?
	else
		args=()
		while read line
		do
			args+=$line
		done
		python3 "$LOOPERPATH/slice.py" $args $@
		return $?
	fi
	
}

looper()
{
	if [ -t 0 ]
	then
		python3 "$LOOPERPATH/looper.py" $@
		return $?
	else
		read args
		python3 "$LOOPERPATH/looper.py" $args $@
		return $?
	fi
}

speed(){

}

release(){
	python3 "$LOOPERPATH/release.py" $@
	return $?

}
