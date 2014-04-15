from __future__ import division
import sys, pdb

__author__ = 'phil'


# this should take a list of items with the format:
# <price> <share>
#
# price: the price of the item
# share: a regex matching the share of the item ^[P*B*]
#   if no share is listed, it's assumed to be split evenly
#
# ex: 1.99 P
# phil owes 100% of the price of that item

class ReceiptItem:
  def __init__(self, price, brian_share, phil_share):
    self.price = price
    self.brian_share = brian_share
    self.phil_share = phil_share

  def get_price(self):
    return self.price

  def get_brian_share(self):
    return self.brian_share

  def get_phil_share(self):
    return self.phil_share

  def __str__(self):
    return "Item(price:{0}, brian:{1}, phil:{2})".format(self.price, self.brian_share, self.phil_share)

  def __unicode__(self):
    return "Item(price:{0}, brian:{1}, phil:{2})".format(self.price, self.brian_share, self.phil_share)

def main():
  input_path = sys.argv[1]
  items = parse_input(input_path)
  # print map(str, items)
  for item in items:
    print str(item)

  # total = sum([lambda item: item.get_price() for item in items])
  total = sum(map(ReceiptItem.get_price, items))

  brian_total = sum(map(ReceiptItem.get_brian_share, items))
  phil_total = sum(map(ReceiptItem.get_phil_share, items))

  print "total: {0}".format(total)
  print "brian total: {0}".format(brian_total)
  print "phil total: {0}".format(phil_total)

# takes the path to the input file and parses it into ReceiptItems
def parse_input(input_path):
  with open(input_path) as input:
    lines = input.readlines()
    parsed_lines = map(parse_line, lines)
    return parsed_lines


def parse_line(line):
  # strip the newlines and tokenize the string on space
  line_tokens = line.strip('\n').split(' ')

  if len(line_tokens) == 1:
    price = float(line_tokens[0])
    share = "PB"
    return build_receipt_item(price, share)
    # return ReceiptItem
  elif len(line_tokens) == 2:
    price = float(line_tokens[0])
    share = line_tokens[1]
    return build_receipt_item(price, share)
  else:
    print "invalid line, skipping; [line={0}]".format(line)

def build_receipt_item(price, share):
  total_shares = len(share)
  brian_shares = share.count('B')
  phil_shares = share.count('P')
  brian_share = price * (brian_shares / total_shares)
  phil_share = price * (phil_shares / total_shares)
  # pdb.set_trace()
  return ReceiptItem(price, brian_share, phil_share)

if __name__=='__main__': main()
