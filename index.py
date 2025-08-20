import random


# Classes

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise Exception("Author name must be a non-empty string")
        self._name = name.strip()

    @property
    def name(self):
        return self._name  # immutable

    def articles(self):
        return [article for article in Article._all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if mags:
            return list(set(m.category for m in mags))
        return None


class Magazine:
    _all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Magazine name must be a string")
        if not (2 <= len(value) <= 16):
            raise Exception("Magazine name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise Exception("Category must be a non-empty string")
        self._category = value.strip()

    def articles(self):
        return [article for article in Article._all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        arts = self.articles()
        if arts:
            return [a.title for a in arts]
        return None

    def contributing_authors(self):
        authors = [a.author for a in self.articles()]
        result = [author for author in set(authors) if authors.count(author) > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not Article._all:
            return None
        return max(cls._all, key=lambda mag: len(mag.articles()))


class Article:
    _all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        if not isinstance(title, str):
            raise Exception("title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("title must be between 5 and 50 characters")

        self.author = author
        self.magazine = magazine
        self._title = title
        Article._all.append(self)

    @property
    def title(self):
        return self._title  



if __name__ == "__main__":

    # Create Authors
    elvis = Author("Elvis Chumo")
    isabelle = Author("Isabelle Chumo")

    # Create Magazines
    tech_today = Magazine("TechToday", "Technology")
    health_mag = Magazine("HealthMag", "Health")

    # Create Articles using add_article
    elvis.add_article(tech_today, "The Future of AI")
    elvis.add_article(health_mag, "Healthy Living Tips")
    isabelle.add_article(tech_today, "Robotics Revolution")
    isabelle.add_article(tech_today, "AI in Healthcare")
    isabelle.add_article(tech_today, "Quantum Computing Simplified")

    # Test Author Methods
    print("Elvis Topic Areas:", elvis.topic_areas())
    print("Isabelle Topic Areas:", isabelle.topic_areas())

    # Test Magazine Methods
    print("TechToday Article Titles:", tech_today.article_titles())
    print("HealthMag Article Titles:", health_mag.article_titles())

    tech_authors = tech_today.contributing_authors()
    if tech_authors:
        print("TechToday Contributing Authors:", [a.name for a in tech_authors])
    else:
        print("TechToday Contributing Authors:", None)

    health_authors = health_mag.contributing_authors()
    if health_authors:
        print("HealthMag Contributing Authors:", [a.name for a in health_authors])
    else:
        print("HealthMag Contributing Authors:", None)
    # Test Magazine Class Method
    top_publisher = Magazine.top_publisher()
    if top_publisher:
        print("Top Publisher:", top_publisher.name)
    else:
        print("Top Publisher:", None)
 