
#import markdownify
import re

re_avsnitt_och_text = re.compile(r"<h[1-5][^>]*>([^<]*)</h[1-5]>(.*?(?=<h))",
                                 re.MULTILINE | re.DOTALL)

def avsnitt(html):

  data = {}
  while True:

    m = re_avsnitt_och_text.match(html)

    if m is None:
      break

    html = html[m.end():]
    data[m.group(1).strip()] = m.group(2).strip()

  return data
