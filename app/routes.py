from app import myapp_obj
@myapp_obj.route("/")

def home():
        name = "Lisa"
        city_names = ["Paris", "London", "Rome", "Tahiti"]
        return render_template('home.html', name = name, city_names = city_names)
