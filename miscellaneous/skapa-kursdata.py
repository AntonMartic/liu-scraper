#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default = "data.csv",
                    help = f"Raw data file, from web scraping studieinfo.liu.se, in CSV format", metavar = "file")
parser.add_argument("-o", "--output", default = "data_processed.csv",
                    help = f"Output file", metavar = "file")

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

    if kurskod not in courses:
      courses[kurskod] = { "Namn": course_link }
      courses[kurskod].update(hämta.avsnitt(oversikt_grunddata))
      courses[kurskod].update(hämta.avsnitt(kursplan))


with open(options.output, 'w') as out_file:

  csv_writer = csv.writer(out_file, quoting = csv.QUOTE_ALL)
  row = ["Kurs", "Namn",
         "Huvudområde", "Utbildningsnivå", "Kurstyp",
         "Examinator", "Studierektor",
         "Undervisningstid",
         "Fördjupningsnivå",
         "Rekommenderade förkunskaper",
         "Lärandemål",
         "Kursinnehåll",
         "Undervisnings- och arbetsformer",
         "Examination",
         "Betygsskala",
         "Övrig information",
         "Påbyggnadskurser",
         "Institution",
         "Kurslitteratur"]
  csv_writer.writerow(row)


  
  for kod, data in courses.items():
    row = [ kod, data["Namn"],
            data["Huvudområde"] if "Huvudområde" in data else "",
            data["Utbildningsnivå"] if "Utbildningsnivå" in data else "",
            data["Kurstyp"] if "Kurstyp" in data else "",
            data["Examinator"] if "Examinator" in data else "",
            data["Studierektor eller motsvarande"] if "Studierektor eller motsvarande" in data else "",
            data["Undervisningstid"] if "Undervisningstid" in data else "",
            data["Fördjupningsnivå"] if "Fördjupningsnivå" in data else "",
            data["Rekommenderade förkunskaper"] if "Rekommenderade förkunskaper" in data else "",
            data["Lärandemål"] if "Lärandemål" in data else "",
            data["Kursinnehåll"] if "Kursinnehåll" in data else "",
            data["Undervisnings- och arbetsformer"] if "Undervisnings- och arbetsformer" in data else "",
            data["Examination"] if "Examination" in data else "",
            data["Betygsskala"] if "Betygsskala" in data else "",
            data["Övrig information"] if "Övrig information" in data else "",
            data["Påbyggnadskurser"] if "Påbyggnadskurser" in data else "",
            data["Institution"] if "Institution" in data else "",
            data["Kurslitteratur"] if "Kurslitteratur" in data else ""]
    
    csv_writer.writerow(row)
