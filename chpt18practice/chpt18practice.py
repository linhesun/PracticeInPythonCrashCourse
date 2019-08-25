# Chapter 18 practice
# Linhe Sun

# practice 18-1

# practice 18-2
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        if len(self.text) <= 50:
            return self.text
        else:
            return self.text[:50] + '...'

# practice 18-3

