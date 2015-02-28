from app import login_manager
from app.models.user import User

@login_manager.user_loader
def load_user(used_id):
	return User.get(user_id)

@app.route("/login", methods=["GET","POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		login_user(user)
		flash("Logged In Successfully")
		return redirect(request.args.get("next") or url_for("index"))
	return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(somewhere)