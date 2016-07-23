from settings import app, api
from util.Logger import InfoLogger
import resources.routes


# entry point
if __name__ == '__main__':
    info = InfoLogger(__name__)
    info.log("Started...")
    app.run(debug=False, host='0.0.0.0', port=8081)
