from flask import render_template

def home():
  return render_template('pages/home.html')

def previous_chats():
  return render_template('pages/previous_charts.html')