# Эта часть для трансляции странички с гороскопами через ботл (скрин соответствующий из модуля 4)

import os
from bottle import route, run, view
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies

@route("/")
@view("predictions")
def index():
  now = dt.now()

  x = random()

  return {
    "date": f"{now.year}-{now.month}-{now.day}",
    "predictions": [
        generate_prophecies()
    ],
    "special_date": x > 0.5,
    "x": x,
  }

@route("/api/test")
def api_test():
    return {"test_passed": True}



if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)


# run(
#   host="localhost",
#   port=8080,
#   autoreload=True
# )



# Это часть для трансляции предсказаний на узел с уадресом localhost8080/api/forecasts
# (см. скрин о модуле 4 блоке 5 задании с 2 серверами чать1)
# import bottle
# from horoscope import generate_prophecies

# @bottle.route("/api/forecasts")
# def api_test():
#    return {"prophecies": generate_prophecies()}
   
# bottle.run(host="localhost", port=8080, debug=True)


# Это часть для выполнения блока 5 модуля 4 (задание с 2 серверами, код решения которого нужны выложить на )

# from bottle import route, run, view

# @route("/")
# @view("predictions")
# def index():
#   now = dt.now()

#   return {
#     "date": f"{now.year}-{now.month}-{now.day}",
#     "predictions": [
#         generate_prophecies()
#     ],
#   }

# @route("/api/forecasts")
# def api_test():
#    return {"prophecies": generate_prophecies()}

# run(
#   host="localhost",
#   port=8080,
#   autoreload=True
# )