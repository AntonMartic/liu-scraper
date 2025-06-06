#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default = "data.csv",
                    help = f"Raw data file, from web scraping studieinfo.liu.se, in CSV format", metavar = "file")
parser.add_argument("-o", "--output", default = "data_processed.csv",
                    help = f"Output file", metavar = "file")
parser.add_argument("-u", "--undervisa", action='store_true', default = False)
parser.add_argument("-a", "--anvanda", action='store_true', default = False)
parser.add_argument("-x", "--exa", action='store_true', default = False)

options = parser.parse_args()


import csv, hämta

courses = {}
koder = {}
with open(options.input) as in_file:

  csv_reader = csv.reader(in_file)

  first = True
  for row in csv_reader:
    if first:
      first = False
      continue

    web_scraper_order, web_scraper_start_url, course_link, course_link_href, oversikt_grunddata, Kursen_ges_för, Termin, Period, Block, Språk, Ort, VOF, EXA, Benämning, Omfattning, Betygsskala, Name, Introducera, Undervisa, Anvanda, Moduler, Kommentar, kursplan = row

    kurskod = course_link_href.split("/")[4]

    if kurskod not in courses:
      merdata = hämta.avsnitt(kursplan)
      courses[kurskod] = { "Namn": course_link,
                           "Nivå": merdata["Fördjupningsnivå"],
                           "Område": merdata["Huvudområde"],
                           "Matris": {} }

    if Name.strip() == "":
      continue

    matriskod = Name.split(" ")[0]
    beskrivning = Name[len(matriskod)+1:]
    koder[matriskod] = beskrivning

    text = ""
    if options.undervisa and "X" in Undervisa:
      text = text + "U"
    if options.anvanda and "X" in Anvanda:
      text = text + "A"
    if options.exa and "X" in Anvanda:
      text = text + " " + Moduler.replace("\n",",").replace(" ","")
    courses[kurskod]["Matris"][matriskod] = text

with open(options.output, 'w') as out_file:

  csv_writer = csv.writer(out_file, quoting = csv.QUOTE_ALL)
  row = ["Kurs", "Namn", "Nivå", "Område"]
  row.extend([x for x in koder])
  csv_writer.writerow(row)

  for kod, data in courses.items():
    row = [ kod, data["Namn"], data["Nivå"], data["Område"] ]

    for kod in koder:
      if kod in data["Matris"]:
        row.append(data["Matris"][kod])
      else:
        row.append("")

    csv_writer.writerow(row)

  csv_writer.writerow([])
  for kod in koder:
    csv_writer.writerow([kod, koder[kod]])
