# coding: utf-8
from app import db


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    comment_username = db.Column(db.String(200))
    comment_time = db.Column(db.String(200))
    comment_content = db.Column(db.Text)
    comment_votes = db.Column(db.Integer)
    comment_id = db.Column(db.String(50), unique=True)
    movie_id = db.Column(db.String(50))


class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.String(50), unique=True)
    movie_title = db.Column(db.String(200))
    movie_img = db.Column(db.String(1000))
    synopsis = db.Column(db.Text)
    director = db.Column(db.String(200))
    screenwriter = db.Column(db.String(200))
    starring = db.Column(db.String(1000))
    type = db.Column(db.String(200))
    production_country = db.Column(db.String(200))
    language = db.Column(db.String(200))
    release_time = db.Column(db.String(200))
    length = db.Column(db.String(200))
    imdb_link = db.Column(db.String(1000))
    alias = db.Column(db.String(200))
    score = db.Column(db.String(20))
    score_count = db.Column(db.Integer)
    comment_count = db.Column(db.Integer)
    review_count = db.Column(db.Integer)


class Review(db.Model):
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    review_username = db.Column(db.String(200))
    review_time = db.Column(db.String(200))
    review_title = db.Column(db.String(200))
    review_s_content = db.Column(db.Text)
    review_useful_count = db.Column(db.Integer)
    review_useless_count = db.Column(db.Integer)
    review_comment_count = db.Column(db.Integer)
    review_id = db.Column(db.String(50), unique=True)
    review_url = db.Column(db.String(1000))
    movie_id = db.Column(db.String(50))
