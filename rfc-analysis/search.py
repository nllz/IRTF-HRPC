import urllib2
import urllib
import re
import os
from pprint import pprint as pp
import csv
from bs4 import BeautifulSoup
import json
from gather import * 
import logging

JSON_INPUT_FILENAME = 'rfc.json'
JSON_OUTPUT_FILENAME = 'rfc-search.json'

search_terms = ['interoperability','interoperable','distributed architecture','distributed','end to end','end-to-end','reliability','reliable','resiliency','resilience','permissionless innovation','transparency','transparent','data minimization','federation','graceful degradation','connectivity','innovation at the edges','content agnostic','application agnostic','graceful failure','partial healing','delay tolerance','data minimization','data compression','connectivity','stateless','statefull','scalable','debugging','robust','end user','end-user','decentralized','privacy','rights','surveillance','internationalization','openness', 'privacy','security']

def normalize_rfc_number(number):
  just_number = number.lower().split('rfc')[1]
  normalized = 'rfc' + just_number.lstrip('0')
  return normalized

with open(JSON_INPUT_FILENAME, 'r') as jsonfile:
  entries = json.load(jsonfile)
  
  for entry in entries:
    filename = archived_txt(normalize_rfc_number(entry['rfc_number']))
    
    if not filename:
      logging.warning(entry['rfc_number'] + ' has no available file.')
      #raise Exception(entry['rfc_number'] + ' has no available file.')
      continue
    
    with open(filename, 'r') as txt_file:
      # text = txt_file.read()
      #
      # for term in search_terms:
      #   matches = re.findall(term, text, flags=re.IGNORECASE)
      #   entry[term+'_search'] = len(matches)
    
      lines = txt_file.readlines()
      logging.info(filename)
      entry['lines'] = len(lines)
      
      # identifying the section titles
      potential_section_name = False
      current_section_name = ''
      section_name = ''
      empty_line = False
      previous_empty_line = False
      line_count = 0
      entry['sections'] = {}
      
      for line in lines:
        if re.match('\s+$', line):
          empty_line = True
        else:
          empty_line = False
        
        if potential_section_name and empty_line:
          logging.info(section_name)
          entry['sections'][current_section_name] = line_count
          current_section_name = section_name
          line_count = 1
          potential_section_name = False
          previous_empty_line = empty_line
          continue
        
        match = re.match('\d+\.?\s+([A-Z].+)$', line)
        non_numbered_match = re.match('([A-Z][\w\s\d-]+)$', line)
        if match:
          if not re.search('\.\.\.', line) and (not re.search('\s\s+\d+\s$', line)) and previous_empty_line:
            # multiple dots or multiple spaces before a number is a ToC entry, 
            # previous line should be blank
            potential_section_name = True
            section_name = match.group(1).strip()
          else:
            potential_section_name = False
        elif non_numbered_match:
          if not re.search('\s\s', line) and previous_empty_line: 
            # shouldn't have multiple consecutive spaces, previous line should be blank
            potential_section_name = True
            section_name = non_numbered_match.group(1).strip()
          else:
            potential_section_name = False
        else:
          potential_section_name = False  
        
        previous_empty_line = empty_line
        line_count += 1
      
    with open(filename, 'r') as txt_file:
      text = txt_file.read()

      for term in search_terms:
        matches = re.findall(term, text, flags=re.IGNORECASE)
        entry[term+'_search'] = len(matches)      
  
  with open(JSON_OUTPUT_FILENAME, 'wb') as outfile:
    outfile.write(json.dumps(entries))
