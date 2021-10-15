TO ADD: explination for code




#Template Notes

######(When mentioning template engines I am talking about the engine that flask uses to load html templates)

--

###What are templates?

*Templates are the html that you will send to the websites
*They can contain variables that the code will be passed over from the py file when loading teh website
*They can also contain code, such as a loop (ex. loading multiple blog posts with a loop)

--

###Setting up templates

*All templates should be located in a "templates" folder (spelled exactly like that no capitol letters)
*All template files will be html files
*Here is how to load a template file from py code:

  *First you will want to input `render_template` from flask with `from flask import Flask, render_template`
  *Next you will want to call
    ```@app.route("/path")
    def page():
      return render_template('file.html')```

--

###Variables with flask's template engine

*Variables will let you pass information from the py code to the html file while it is being generated
*Heres how to use them:

  *In your py file you will want to change the return render_template to `return render_template('home.html',  variableHL=variablePY)` where variableHL is what the html will recive and variablePY is the variable that you are sending

  *In html you can use `{{ variable }}` to get a variable. (you can change out the variable name)
  *You can put this variable in any tags, it is basicly just replaced with whatevery you said in the py file
    *_ex._ `<p>{{ content }}</p>`


--

###Parent html and child html files

*For this website, I am using "layout.html"
*It contains all of the code that would be the same throught all of the files to avoid repetition

  *It looks like this:
    ```<!DOCTYPE html>
    <html>
    <head>
      <title>This is the same</title>
    </head>
    <body>
      {% title of group %}{% endblock %}
    </body>
    </html>```

*In the child files, it will tell the template engine what to replace from the parent file

  *It looks something like this:
    ```{% extends "layout.html" %}
    {% title of group %}
      <h1>{{ title }}</h1>
    {% endfor %}
    {% endblock optional text for readability %}```