#!/usr/bin/env python3

from vzlogger2mqtt import config
from vzlogger2mqtt import daemon

def main():
	cfg = config.Config()
	cfg.read()
	d = daemon.Daemon(cfg)
	d.run()
	
main()

