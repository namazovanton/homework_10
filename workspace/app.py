from flask import Flask

import utils

app = Flask(__name__)


@app.route("/")
def general_page():
    get_candidates = utils.get_all()
    return f"<pre>{get_candidates}</pre>"


@app.route("/candidates/<int:uid>/")
def search_by_pk(uid):
    url_of_photo, candidate_loaded = utils.get_by_pk(uid)
    return f"""<img src='({url_of_photo})'>\n
<pre>{candidate_loaded}</pre>"""


@app.route("/skills/<skill>/")
def search_by_skill(skill):
    candidates_loaded = utils.get_by_skill(skill)
    return f"<pre>{candidates_loaded}</pre>"


@app.errorhandler(404)
def page_not_found(e):
    return "Страница не найдена", 404


@app.errorhandler(500)
def page_server_error(e):
    return "Ошибка на сервере", 500


app.run()
