from django.db import models

class Client(models.Model):
  client_ip = models.GenericIPAddressField(unique=True)
  def __str__(self):
    return f"{self.client_ip}"
  def __repr__(self):
    return f"{self.client_ip}"
  # def __eq__(self,x) : 
  #     return self.client_ip == x.client_ip

class Page(models.Model):
  page_url = models.URLField(unique=True,max_length=1000)
  def __str__(self):
    return f"{self.page_url}"
  def __repr__(self):
    return f"{self.page_url}"

class Hit(models.Model):
  timestamp =  models.DateTimeField()
  referer =  models.URLField(max_length=1000)
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  page = models.ForeignKey(Page, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.timestamp} {self.referer} {self.client} {self.page}"
  def __repr__(self):
    return f"{self.timestamp} {self.referer} {self.client} {self.page}"

#models.CharField()