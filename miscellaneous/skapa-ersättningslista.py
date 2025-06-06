#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default = "data.csv",
                    help = f"Raw data file, from web scraping studieinfo.liu.se, in CSV format", metavar = "file")

options = parser.parse_args()


import csv, hämta

courses = {}
with open(options.input) as in_file:

  csv_reader = csv.reader(in_file)

  first = True
  for row in csv_reader:
    if first:
      first = False
      continue

    web_scraper_order, web_scraper_start_url, course_link, course_link_href, oversikt_grunddata, Kursen_ges_för, Termin, Period, Block, Språk, Ort, VOF, EXA, Benämning, Omfattning, Betygsskala, Name, Introducera, Undervisa, Anvanda, Moduler, Kommentar, kursplan = row

    kurskod = course_link_href.split("/")[4]

    if kurskod not in courses and u"Kursen får ej ingå i examen tillsammans med" in kursplan:
      courses[kurskod] = { "Namn": course_link,
                           "Data": hämta.avsnitt(kursplan) }

mapping = {}
for kod, data in courses.items():
  for item, text in data["Data"].items():
    if u"i examen tillsammans med" in text:
      print(kod, text)
