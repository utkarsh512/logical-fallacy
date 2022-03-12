# Author: Utkarsh Patel

from Preprocess import Preprocess
import pandas as pd
import numpy as np 

import argparse
import os
from tqdm import tqdm

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--dirc", default=None, type=str, required=True, help="directory of json files containing threads (with context)")
  parser.add_argument("--dirnc", default=None, type=str, required=True, help="directory of json files containing comments (without context)")
  args = parser.parse_args()
  pr = Preprocess()

  json_files = os.listdir(args.dirc)
  for i in tqdm(range(len(json_files)), unit=" files", desc="JSON files processed"):
    raw_files = json_files[i]
    reader_addr = os.path.join(args.dirc, raw_files)
    reader = pd.read_json(reader_addr, lines=True, compression=None)
    reader = list(reader['body'])
    s = raw_files.split('_')
    label = s[1]
    s[-1] = s[-1].replace('.json', '')
    write_filename = s[0] + '_' + s[2] + '_' + s[-1] + '.txt'
    writer_addr = os.path.join('context', label, write_filename)
    writer = open(writer_addr, 'w')
    for idx in range(len(reader) - 1):
      cur = reader[idx]
      cur = pr.preprocess(cur)
      cur = ' '.join(cur)
      cur = cur + ' '
      writer.write(cur)
    writer.close()
  
  reader_addr = os.path.join(args.dirnc, 'comments.json')
  reader = pd.read_json(reader_addr, lines=True, compression=None)
  comments = list(reader['body'])
  violated_rule = list(reader['violated_rule'])
  cid = list(reader['id'])
  commentCount = len(comments)
  ahCommentCount = 0
  for i in tqdm(range(len(comments)), unit=" comments", desc="comments processed"):
    write_filename = cid[i] + '.txt'
    label = 'none'
    if violated_rule[i] == 2:
      label = 'ah'
      ahCommentCount += 1
    writer_addr = os.path.join('no-context', label, write_filename)
    writer = open(writer_addr, 'w')
    cur = pr.preprocess(comments[i])
    cur = ' '.join(cur)
    writer.write(cur)
    writer.close()
  print(commentCount, ahCommentCount)
  
if __name__ == '__main__':
  main()
