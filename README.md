# Extract dates scripts
These scripts extract timestamps from XML reports generating during born-digital processing.

## Requirements
Install Beautiful Soup and the lxml toolkit. If you're using Python 3 on Mac or Windows, run `pip3 install beautifulsoup4 lxml`. If you're on Linux, run `sudo apt-get install python3-bs4 python3-lxml`.

## DFXML date report
This script, dfxml_dates.py, creates a CSV with the filename, mtime, and ctime for each <fileobject> element in a [DFXML file](https://github.com/dfxml-working-group/dfxml_python).

1. Change to the directory containing your DFXML.
2. Run the script: `python3 dfxml_dates.py`
3. Open dfxml-dates.csv in Excel and sort the columns to find the earliest date.

## Mediainfo date report
This script, medainfo_dates.py, creates a CSV with the filename and various kinds of timestamps (Modified Date, Encoded Date, Tagged Date, Recorded Date, Mastered Date, and QuickTime Creation).

1. Change to the directory containing your mediainfo-report.xml.
2. Run the script: `python3 mediainfo_dates.py`
3. Open mediainfo-dates.csv in Excel and sort the columns to find the earliest date.

This script can also be run over multiple directories:
```
for dir in /path/*; do cd $dir/subdirectory && python3 mediainfo_extract_dates.py; done
```