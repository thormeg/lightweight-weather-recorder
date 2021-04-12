from flask import Blueprint, render_template, request

weather_charts = Blueprint('weather_charts', __name__)


@weather_charts.route('/weather_charts', methods=['GET', 'POST'])
def charts():
    # page = request.args.get('page', 1, type=int)
    # posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
   render_template('weather_chart.html', title='Weather Charts')
