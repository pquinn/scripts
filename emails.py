import sys, random, smtplib

subject = "Your Secret Santa assignment"

email_lines = ["Dearest {0},\n",
               "You're receiving this email because, even though you've done a lot wrong in your life, you've made a few good choices and you have some AMAZING friends.\n",
               "Since \"Secret Santa 2012\" was such a smashing success, we've decided to do it again.\n",
               "Rules:",
               " - Be sensible with the limit. There's no hard limit, but don't roll up with something ridiculous. Shoot for around $25.",
               " - Try to avoid alcohol as a gift. IT'S KIND OF A COP OUT, GUYS.",
               " - The exchange time is still TBD, so I guess we can figure that out later.\n\n"
               "Anyway, without further adieu, your assignee is: ",
               "<assignee>"]


signature = ["With love, \n",
             "-Philip Patrick Quinn\n\n",
             "NOTE: please don't reply to this email unless you want me to know who you have."]

class Person:
    def __init__(self, name, email):
      self.name = name
      self.email = email

    def __str__(self):
      return "({0}, {1})".format(self.name, self.email)

class Pair:
    def __init__(self, person, assignee):
      self.person = person
      self.assignee = assignee

    def get_email(self):
      return self.person.email

    def __str__(self):
      return "({0} -> {1})".format(self.person.name, self.assignee.name)

people = [Person("Phil Quinn", "phillmatic19@gmail.com"),
          Person("Kristina Portantino", "k.portantino@gmail.com"),
          Person("Matt Vitale", "matthewvitale23@gmail.com"),
          Person("Amanda Stallone", "stalloam01@mail.buffalostate.edu"),
          Person("Brian Jimenez", "jimenezbr7@gmail.com"),
          Person("Victoria Wong", "victoriawong6@gmail.com"),
          Person("Amy Komoroski", "akomoroski@hotmail.com"),
          Person("Mary Yacenda", "maryyacenda@aol.com"),
          Person("Chris Tinelli", "ctinelli213@gmail.com"),
          Person("Joseph Esposito", "jesposito424@yahoo.com")]

def make_pairs():
    pairs = []
    remaining_people = list(people)
    for person in people:
      assignment = random.choice(remaining_people)
      while assignment.name == person.name:
        assignment = random.choice(remaining_people)
      remaining_people.remove(assignment)
      pairs.append(Pair(person, assignment))

    return pairs
 
def make_message(pair):
    recipient = pair.get_email()
    assignee_name = pair.assignee.name
    assignee_email = pair.assignee.email
    recipient_first_name = pair.person.name.split(' ')[0]

    message = ""
    for line in email_lines:
      if line == "<assignee>":
        if assignee_name == "Phil Quinn":
          message += "ME (Philip Quinn) MOTHERFUCKER HAHAHA GOOD LUCK (don't worry I still don't know that you have me...)"
        else:
          message += "***{0}***".format(assignee_name)
      elif line == "Dearest {0},\n":
        message += line.format(recipient_first_name)
      else:
        message += line
      message += "\n"

    message += "\n"

    for line in signature:
      message += line

    return message

def make_and_send_email(pair, password):
  message = make_message(pair)
  to_addr = pair.get_email()
  from_addr = "phillmatic19@gmail.com"
  login = from_addr

  print sendemail(from_addr, to_addr, [], subject, message, login, password)

def sendemail(from_addr, to_addr, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % to_addr
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr, message)
    server.quit()
    return problems

def main():
    for participant in people:
      print participant

    print "%s participants" % len(people)

    pairs = make_pairs()

    if len(sys.argv) == 3:
      print "writing pairs to %s" % sys.argv[1]

      # serialize the pairs to disk
      with open(sys.argv[1], 'w') as f:
        for pair in pairs:
          f.write("{0} -> {1}".format(pair.person.name, pair.assignee))
          f.write('\n')

      # write the emails
      for pair in pairs:
        print make_and_send_email(pair, sys.argv[2])

    if len(sys.argv) == 4:
      from_addr = sys.argv[1]
      to_addr_list = [sys.argv[2]]
      my_pw = sys.argv[3]

      my_addr = "phillmatic19@gmail.com"

      print from_addr
      print to_addr_list

      #print sendemail(from_addr, to_addr_list, [], "test", "HEY! HAHA!", my_addr, my_pw)

if __name__ == '__main__': main()