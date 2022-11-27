from flask import Flask, render_template

app = Flask(
    __name__,
    static_folder="../front/build",
    static_url_path="",
    template_folder="../front/build",
)


@app.route("/")
def home():
    return "Hello world !"


@app.route("/react")
def react():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5555)
