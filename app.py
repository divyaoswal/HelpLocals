from project import app
import os
# CsrfProtect(app)


if __name__ == "__main__":
	port = int(os.environ.get('PORT', 4002))
	app.run(port=port, debug=False)