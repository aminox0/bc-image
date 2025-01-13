from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = "acc_2012c052d2d693c"
api_secret = "f2388a77e3a0ebd09a3e1f7fa43f82e6"

@app.route("/", methods=["GET", "POST"])
def home():
    image_url = None
    tags = []
    if request.method == "POST":
        image = request.files["image"]
        response = requests.post(
            "https://api.imagga.com/v2/tags",
            auth=(api_key, api_secret),
            files={"image": image}
        )

        if response.status_code == 200:
            tags = response.json().get("result", {}).get("tags", [])

        image_url = "path_to_image"  # أضف رابط الصورة هنا إذا كنت تحتاج إلى عرضه

    return render_template("index.html", image_url=image_url, tags=tags)

if __name__ == "__main__":
    app.run(debug=True)
