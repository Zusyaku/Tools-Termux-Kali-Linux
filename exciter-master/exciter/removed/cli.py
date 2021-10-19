import argparse


def CLI():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-p', dest='password',
                        help='password list or file name', nargs='*', required=True)
    parser.add_argument('-r', dest='regex_pattern',
                        help='regex pattern to identify the user has been logged', default='(?i)(?:sign|log)\s*out')
    parser.add_argument('-u', dest='username', help='username or email target')
    parser.add_argument('-d', dest='delay', help='waiting time before starting the connection', default=3, type=int)
    parser.add_argument('-t', dest='url', help='valid url, http / https protocol is required', required=True)
    parser.add_argument('--proxy', help='proxy address')
    parser.add_argument('--timeout', help='time to wait before giving up', default=10)
    parser.add_argument('--hidden-inputs', action='store_true',
                        help='include all hidden inputs')

    return parser
