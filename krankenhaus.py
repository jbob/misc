#!/usr/bin/env python
 
class Station:
  def __init__(self, name, anzahl_max):
    self.name = name
    self.anzahl_max = anzahl_max
    self.count = 0
    self.namen = []
 
  def aufnahme(self, patient):
    if self.count < self.anzahl_max:
      self.namen.append(patient)
      self.count += 1
      print patient, "in", self.name, "aufgenommmen."
      print self.count, "von", self.anzahl_max, "Betten belegt."
      return True
    else:
      print patient, "*nicht* in", self.name, "aufgenommmen."
      print self.name, "ist bereits voll."
      print self.count, "von", self.anzahl_max, "Betten belegt."
      return False
 
  def status(self):
    print "Patienten:"
    print ", ".join(self.namen)
    print self.count, "von", self.anzahl_max, "Betten belegt."
 
 
 
mystation = Station("Intensivstation", 3)
 
mystation.aufnahme("Alice")
mystation.aufnahme("Bob")
mystation.aufnahme("Eve")
mystation.aufnahme("John")
mystation.status()
