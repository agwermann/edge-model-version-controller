from flask import Flask, request
from cloudevent import CloudEventService

app = Flask(__name__)

@app.route("/", methods=["POST"])
def home():
    cloud_event = CloudEventService()
    event = cloud_event.receive_message(request)

    print(
        f"Found {event['id']} from {event['source']} with type "
        f"{event['type']} and specversion {event['specversion']}"
    )

    # Return 204 - No-content
    return "", 204


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)