from flask import render_template, request, redirect, url_for
from app import App, db
from app.models import Article, User

from datetime import datetime

@App.route('/')
def Index():
    """ our Index page view """
    articles = Article.query.all()[:3]  # only the latest 3 atricles
    return render_template('index.html', articles=articles)


@App.route('/articles/<id>')
def ViewArticle(id):
    """ to view an article """
    article = Article.query.get(id)
    return render_template('article.html', article=article)


@App.route('/account/<id>')
def UserAccount(id):
    """ to view a user's full list of articles """
    user = User.query.get_or_404(int(id))
    if user:
        articles = user.articles.all()
    return render_template('account.html', user=user, articles=articles)


@App.route('/add', methods=['GET', 'POST'])
def AddArticle():
    """ add an article to our database
        it's a very long function as you can see
        so it's better to use WTForms
    """
    if request.method == "POST":
        # I'm not using WTForms so a little improvised validation
        # you should use WTForms
        title = request.form['title']
        if len(title) > 0:
            desc = request.form['desc']
            text = request.form['text']
            timestamp = datetime.now()

            # this is not good but we will use it for now
            user = User.query.get(1)

            article = Article(
                title=title, desc=desc, text=text,
                datetime=timestamp, author_id = user.id,
                author=user)
            db.session.add(article)
            db.session.commit()

            return redirect(url_for('UserAccount', id=user.id))
        else:
            error = "Article Title Required"
            return render_template('add_article.html', error=error)

    return render_template('add_article.html')
