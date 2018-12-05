from flask import render_template, request, redirect, url_for

from app import app
from app.models import Movie, Comment, Review

type_keyword = None


@app.route('/', methods=['GET'])
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Movie.query.order_by(Movie.score.desc()).paginate(
        page, per_page=10,
        error_out=False
    )
    posts = pagination.items
    return render_template('index.html', posts=posts, pagination=pagination, )


@app.route('/search', methods=['GET'])
def search():
    global type_keyword
    type_keyword = request.args.get('type')
    if type_keyword is not None:
        return redirect(url_for('search_result', keyword=type_keyword))
    return render_template('search.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/search-result/<keyword>', methods=['GET'])
def search_result(keyword):
    page = request.args.get('page', 1, type=int)
    pagination = Movie.query.filter(Movie.type.contains(keyword)).order_by(Movie.score.desc()).paginate(
        page, per_page=10,
        error_out=False
    )
    posts = pagination.items
    return render_template('search-result.html', posts=posts, pagination=pagination, keyword=keyword)


@app.route('/movie-item/<mid>')
def movie_item(mid):
    item = Movie.query.filter(Movie.movie_id == mid).one()
    c_query = Comment.query.filter(Comment.movie_id == mid).order_by(Comment.comment_votes.desc()).all()
    r_query = Review.query.filter(Review.movie_id == mid).order_by(Review.review_useful_count.desc()).all()
    return render_template('movie-item.html', item=item, c_query=c_query, r_query=r_query)