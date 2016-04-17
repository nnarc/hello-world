#!/usr/bin/env python

import os, sys, argparse, logging
from datetime import datetime

# script info
DESCRIPTION = 'Hello World with Logging and Argparse'
VERSION = 0.1

def main():
    logging.debug('Hello World! -vv')
    logging.info('Hello World! -v')
    logging.warn('Hello World! -v')
    logging.error('Hello World! (default)')
    logging.critical('Hello World! (default)')

    try:
        logging.debug('Reading input file %s' % args.inputfile)

        with open(args.inputfile, 'r') as fp:
            logging.info('input file:\n-----------------\n' \
                          + fp.read() + '\n-----------------')

        logging.debug('Finished reading input file')

    except Exception, e:
        logging.error("Unable to read input file: %s" % str(e))

    return 0

# script entry point
if __name__ == "__main__":

    # initialize script argument parser
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    # specify an optional script argument for version
    parser.add_argument(
            '--version', # do not specify -v (reserved for verbosity)
            action='version',
            version='%(prog)s ' + str(VERSION)
        )

    # specify a REQUIRED script argument for an input file
    parser.add_argument(
            '-i', '--inputfile',
            type=str,
            required=True,
            help='path to input file'
        )

    # specify an optional script argument for an output directory
    parser.add_argument(
            '-o', '--output',
            type=str,
            default='./',
            help='path to the output directory'
        )

    # specify an optional script argument for log verbosity
    parser.add_argument(
            '-v', '--verbosity',
            action="count",
            default=0,
            help='verbosity of logs (default is ERROR, use -v for INFO or -vv for DEBUG)'
        )

    # specify an optional script argument for logfile output
    parser.add_argument(
            '-l', '--logfile',
            type=str,
            help='path to log file output'
        )

    # with script arguments specified, parse the actual arguments provided
    args = parser.parse_args()

    # create output directory if it does not exist
    if not os.path.isdir(args.output):
        os.makedirs(args.output)

    # set logging level based on verbosity
    if args.verbosity == 1:
        loglevel = "INFO"
    elif args.verbosity >= 2:
        loglevel = "DEBUG"
    else:
        loglevel = "ERROR"

    try:
        # initialize the logger
        if (args.logfile):
            # if a logfile was specified, output all logs to that file
            logging.basicConfig(
                filename=args.logfile, filemode='w',
                level=logging.getLevelName(loglevel),
                format='<%(asctime)s> %(levelname)s: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
        else:
            # no logfile specified, output logs to the screen
            logging.basicConfig(
                level=logging.getLevelName(loglevel),
                format='<%(asctime)s> %(levelname)s: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
    except Exception, e:
        parser.error("invalid logging configuration: %s" % str(e))

    sys.exit(main())
