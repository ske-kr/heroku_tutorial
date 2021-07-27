from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    
    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Increment the count
    count += 1

    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()

    # Render HTML with count variable
    return render_template("index.html", count=count)

@app.route("/index")
def home():
    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Increment the count
    count += 1

    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()
    return render_template("index.html", count=count)

@app.route("/resume")
def resume():
    
    return render_template("resume.html")    

@app.route("/info")
def info():
    
    return render_template("info.html")  

@app.route("/exprience")
def exprience():
    
    return render_template("exprience.html")  

@app.route("/project")
def project():
    
    return render_template("project.html")  



if __name__ == "__main__":
    app.run()