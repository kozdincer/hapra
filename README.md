hapra
=====

Haproxy Restful Api

app.route("/get")
app.route("/get/global")
app.route("/get/defaults")
app.route("/get/listen/str:<name>")
app.route("/get/listens")
app.route("/get/listensName")
app.route("/get/frontend/str:<name>")
app.route("/get/frontends")
app.route("/get/frontendsName")
app.route("/get/backend/str:<name>")
app.route("/get/backends")
app.route("/get/backendsName")

app.route("/add/global")
app.route("/add/defaults")
app.route("/add/listen")
app.route("/add/frontend")
app.route("/add/backend")

app.route("/del/global")
app.route("/del/defaults")
app.route("/del/listen/<number>")
app.route("/del/frontend/<number>")
app.route("/del/backend/<number>")

app.route("/addOption/global/<param_name>/<params>")
app.route("/addOption/defaults/<param_name>/<params>")
app.route("/addOption/listen/<number>/<param_name>/<params>")
app.route("/addOption/frontend/<number>/<param_name>/<params>")
app.route("/addOption/backend/<number>/<param_name>/<params>")

app.route("/delOption/global/<param_name>/<params>")
app.route("/delOption/defaults/<param_name>/<params>")
app.route("/delOption/listen/<number>/<param_name>/<params>")
app.route("/delOption/frontend/number/<param_name>/<params>")
app.route("/delOption/backend/<number>/<param_name><params>")
