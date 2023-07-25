from django.db import models

class Account(models.Model):
    # Full name of the author
    name = models.CharField(max_length=100)
    # Alias/Nickname of the Author, will be seen below the title.
    alias = models.CharField(max_length=50)
    # Total number of article created/published
    num_article = models.IntegerField()

    def __str__(self) -> str:
        return f"Name: {self.name} / Alias: {self.alias}"

    # function to change alias
    def change_alias(self, newalias):
        old_alias = self.alias
        self.alias = newalias
        print(f"New Alias set to : {self.alias} / Old Alias : {old_alias}")
    
    # function to set/increment total articles created/published
    def add_new_article(self):
        self.num_article += 1
        print("A new article from you has been published")

class Article(models.Model):
    # Title of the Article
    title = models.CharField(max_length=100)
    # The owner/publisher of this article
    # author = models.ForeignKey(Account, on_delete=models.CASCADE)
    author = models.IntegerField()
    # The date this Article was created and published
    published_date = models.CharField(max_length=20)

    # def get_author(self):
    #     return f"Author: {self.author}"

    def getinfo(self):
        return [self.title, self.author]

class Comment(models.Model):
    # The article where this comment is placed
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # The account/person who wrote this comment
    alias = models.ForeignKey(Account, on_delete=models.CASCADE)

    def new_comment(self, article_id):
        article = Article.objects.get(pk=article_id)
        print(f"ARTICLE IS : {article}")