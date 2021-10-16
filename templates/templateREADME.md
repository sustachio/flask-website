TO ADD: 
* explination for code
* example website (the basic blog w/ no styling)

# Template Notes

###### (When mentioning template engines I am talking about the engine that flask uses to load html templates)
---
### What are templates?

* Templates are html files that will be sent to the user's browser
* They can contain variables that you can change when the browser loads the file
* They can also contain code, such as a loop to generate lots of html

---

### Setting up templates

* All templates should be located in a "templates" folder (spelled exactly like that no capitol letters)
* All template files will be html files
* Here is how to load a template file from py code:
  * First you will want to import `render_template` from flask with `from flask import Flask, render_template`
  * To use these templates in your code you will need to call:
    ```py
    @app.route("/path")
    def page():
      return render_template('file.html')
    ```
---
### Variables with flask's template engine
* Variables will let you pass information from the py code to the html file while it is being generated
* Heres how to use them:
  * First, you will want to declare the cariable that you are going to pass (ex. `num=123`)
  * In your py file you will want to change the return render_template to `return render_template('home.html',  recive=pass)` there are no requirments on the names, so you can name them anything
  * In html you can use `{{ variable }}` to get a variable. (you can change out the variable name)
  * For example you could send a variable called 'content' and put it into paragraph tags
    * _`main.py`:_ 
        ```py
        nums = 12345
        
        @app.route("/contentpage")
        def contentpage():
            return render_template('content-page.html', content=nums)
        ```
    * _`templates/content-page.html`:_
        ```html
        <p>{{ content }}</p>
        ```
---
### Parent html and child html files
* For this website, I am using "layout.html" to store the layout
* The file will contain all of the code that would be the same throughout all of the html files to avoid repetition
  * The template file could look something like this looks like this (You can name the group anything):
    `layout.html`
    ```html
    <!DOCTYPE html>
    <html>
    <head>
      <title>This is the same</title>
    </head>
    <body>
      {% title of group %}{% endblock %}
    </body>
    </html>
    ```
* In the child files, it will tell the template engine what to replace from the parent file
  * It looks something like this:
    `home.html`
    ```html
    {% extends "layout.html" %}
    {% title of group %}
      <h1>{{ title }}</h1>
    {% endfor %}
    {% endblock optional text for readability %}
    ```
* This will basicly copy `layout.html`, but replace the `{% title of group %}{% endblock %}` with the h1 tags containing the title variable passed from the py file
---
* use this to make example website
    ```py
    @app.route("/")
    @app.route("/home")
        def contentpage():
            return render_template('content-page.html', title='Home asdf')
    ```
    Then html that the web browser will be loading will look like this:
    ```html
    <!DOCTYPE html>
    <html>
    <head>
      <title>This is the same</title>
    </head>
    <body>
      <h1>Home asdf<h1>
    </body>
    </html>
    ```