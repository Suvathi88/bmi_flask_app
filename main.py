from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bmi():
    bmi_result = ""
    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            bmi = weight / (height ** 2)
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obese"
            bmi_result = f"Your BMI is {bmi:.2f} ({category})"
        except:
            bmi_result = "Invalid input. Please enter valid numbers."
    return render_template("index.html", result=bmi_result)

if __name__ == "__main__":
    app.run(debug=True)
