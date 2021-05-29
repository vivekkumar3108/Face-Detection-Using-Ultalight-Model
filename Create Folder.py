from flask import Flask, request, render_template 
import os
app = Flask(__name__, template_folder='template')   
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        print(request.form.get("name"))
        parent_dir = "C:/Users/Vivek Kumar/Desktop/Minor/Faces_DB/"
        path = os.path.join(parent_dir,request.form.get("name")  )
        os.mkdir(path)
    return render_template("1.html")
if __name__=='__main__':
   app.run()

