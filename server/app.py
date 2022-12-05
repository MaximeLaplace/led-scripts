from flask import Flask, render_template

app = Flask(
    __name__,
    static_folder="../front/build",
    static_url_path="",
    template_folder="../front/build",
)


@app.route("/")
def home():
    return render_template("index.html")


class CustomManager(BaseManager):
    pass


CustomManager.register("Mode", Mode)


def work(shared_mode):
    while True:
        print(f"shared_modes is at list length : {shared_mode.get()}")
        time.sleep(1)


if __name__ == "__main__":

    app.run(port=5555)
