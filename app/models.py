from app import db

class Article(db.Model):
    """ each instance of this class represents an article in the database """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    text = db.Column(db.Text)
    desc = db.Column(db.String(200))
    datetime = db.Column(db.DateTime)
    author_id = db.Column(db.String, db.ForeignKey('user.id'))

    # returns the article title as its object representaion string
    def __repr__(self):
        return '<Article: {0}>'.format(self.title)

class User(db.Model):
    """ each instance of this class represents a user in the database """

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(80), index=True)
    email = db.Column(db.String)
    password = db.Column(db.String)  # this is not good but just to make simple
    articles = db.relationship('Article', backref='author', lazy='dynamic')

    # returns the users nickname as his object representaion string
    def __repr__(self):
        return '<User: {0}>'.format(self.nickname)
