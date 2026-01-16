from bs4 import BeautifulSoup
import csv
from operator import attrgetter

try:
    with open("mediainfo-report.xml", encoding="utf8") as fp:
        soup = BeautifulSoup(fp, features="xml")
except FileNotFoundError:
    exit()

try:
    allfiles = soup.find_all(['media','File'])
except NameError:
    exit()
with open ('mediainfo-dates.csv', 'w', newline='', encoding="utf8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Filename", "Modified Date", "Encoded Date", "Tagged Date", "Recorded Date", "Mastered Date", "QuickTime Creation"])
    for file in allfiles:
        mediaRef = file.get("ref")
        if mediaRef is not None:
            fileNameText = mediaRef
        else:
            fileNameText = getattr(file.Complete_name, 'text', '')

        mdateText = getattr(file.File_Modified_Date, 'text', '')        
        edateText = getattr(file.Encoded_Date or file.Encoded_date, 'text', '')
        tdateText = getattr(file.Tagged_Date or file.Tagged_date, 'text', '')
        rdateText = getattr(file.Recorded_Date or file.Recorded_date, 'text', '')
        madateText = getattr(file.Mastered_Date, 'text', '')        
        qtCDateText = getattr(file.com_apple_quicktime_creationdate, 'text', '')
        
        writer.writerow([fileNameText, mdateText, edateText, tdateText, rdateText, madateText, qtCDateText])


# Run this script over multiple directories by using:
# for dir in $HOME/born_digital/to-qc/uuid-9/*/; do cd $dir/documentation && python3 $HOME/Desktop/mediainfo_extract_dates.py; done