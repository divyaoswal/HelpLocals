from project import app
# CsrfProtect(app)


if __name__ == "__main__":
	app.run(port=4002, debug=True)