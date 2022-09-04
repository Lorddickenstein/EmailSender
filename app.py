from web import create_app
import sys

app = create_app()

if __name__ == '__main__':
	port = int(sys.argv[1]) if sys.argv[1] else 5000
	app.run(debug=True, port=port)