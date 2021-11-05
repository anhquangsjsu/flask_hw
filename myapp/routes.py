from myapp import myapp_obj
from myapp.forms import TopCities
from flask import render_template, redirect, flash
from myapp import db
from myapp.models import Cities

def byRank(obj):
    return obj.rank

@myapp_obj.route("/", methods=['GET', 'POST'])
def home():
    title = "Top Cities"
    name = "Superman"
    form = TopCities()
    top_cities = Cities.query.all()
    top_cities.sort(key = byRank)
    if form.validate_on_submit():
        city = Cities(name = form.city_name.data, rank= form.city_rank.data, isVisited = form.is_visited.data)
        db.session.add(city)
        db.session.commit()
        flash(f'City name "{form.city_name.data}" of rank {form.city_rank.data} visited: {form.is_visited.data} was added')
        return redirect("/")
    return render_template("home.html",form = form, title = title, name = name, top_cities=top_cities)

