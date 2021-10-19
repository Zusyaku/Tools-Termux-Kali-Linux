#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This file is part of youtube-video-image
    Copyright (C) 2017 @maldevel
    https://github.com/maldevel/youtube-video-image
    
    get-youtube-video-images.py - Download youtube video cover image.
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    For more see the file 'LICENSE' for copying permission.
"""

__author__ = "maldevel"
__copyright__ = "Copyright (c) 2017 @maldevel"
__credits__ = ["maldevel", "rkmylo"]
__license__ = "GPLv3"
__version__ = "0.2"
__maintainer__ = "maldevel"


#####################

import os
import re
import sys
import hashlib
import argparse
import requests
from bs4 import BeautifulSoup
from argparse import RawTextHelpFormatter


video_url = 'https://www.youtube.com/watch?v={}'
thumbnail_url = 'https://i.ytimg.com/vi/{}/maxresdefault.jpg'
empty_thumbnail_md5digest = 'e2ddfee11ae7edcae257da47f3a78a70'


def parse_args():
    parser = argparse.ArgumentParser(description="Download YouTube video cover image.",
                                     formatter_class=RawTextHelpFormatter)
    parser.add_argument("-i", '--id', action="store", metavar='YouTubeID', dest='ytid',
                        default=None, help="YouTube Video ID")
    parser.add_argument("-r", '--related', action="store_true", dest='related',
                        default=False, help="Download thumbnails from related videos as well")
    #parser.add_argument("-d", '--depth', action="store", metavar='Depth', dest='depth',
    #                    default=None, help="Crawl Depth")

    args = parser.parse_args()

    if len(sys.argv) is 1:
        parser.print_help()
        sys.exit()

    #if not args.ytid:
    #    print(red('[-] Please specify a YouTube URL'))
    #    sys.exit(2)

    return args


def download_thumbnail(ytid):
    resp = requests.get(thumbnail_url.format(ytid), stream=True)
    raw_resp = resp.raw.read()
    md5digest = hashlib.md5(raw_resp).hexdigest()

    if md5digest == empty_thumbnail_md5digest:
        print '[*] Empty thumbnail ({})'.format(ytid)
        return

    if md5digest in downloaded_thumbs:
        print '[*] Thumbnail already downloaded ({})'.format(ytid)
        return

    downloaded_thumbs.append(md5digest)
    print '[*] Downloading {}...'.format(ytid)
    with open('{}.png'.format(ytid), 'wb') as thumbnail:
        thumbnail.write(raw_resp)


def find_related(ytid):
    html = requests.get(video_url.format(ytid)).content
    soup = BeautifulSoup(html, 'lxml')
    related = list(set(re.findall('data\-thumb="https://i\.ytimg\.com/vi/([a-zA-Z0-9\-_]{5,20})/hqdefault\.jpg', html)))
    return related


def main():
    args = parse_args()
    global downloaded_thumbs
    downloaded_thumbs = []
    download_thumbnail(args.ytid)
    if args.related:
        related = find_related(args.ytid)
        for r in related:
            download_thumbnail(r)


if __name__ == '__main__':
    main()

