from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='profile_pics/')
    join_date = models.DateField()

    def __str__(self):
        return self.username
    
class Chat(models.Model):
    participants = models.ManyToManyField(User)
    timestamp = models.DateTimeField()

    def __str__(self):
        participant_names = ', '.join([str(user) for user in self.participants.all()])
        return f"Chat between {participant_names} at {self.timestamp}"

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField()
    attachments = models.ManyToManyField('PDFDocument', blank=True)

    def __str__(self):
        return f"Message from {self.sender} at {self.timestamp}"

class PDFDocument(models.Model):
    title = models.CharField(max_length=200)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField()
    embedding = models.TextField()

    def __str__(self):
        return self.title

class UserHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sent_messages = models.ManyToManyField(Message, related_name='sent_by')
    received_messages = models.ManyToManyField(Message, related_name='received_by')
    uploaded_pdfs = models.ManyToManyField(PDFDocument, blank=True)

    def __str__(self):
        return f"History of {self.user}"


