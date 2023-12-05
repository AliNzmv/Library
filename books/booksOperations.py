import booksModel as bc
import flask

#=========================================================main=====================================================
app=flask.Flask(__name__)
@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/about")
def about():
    return flask.render_template("about.html")


@app.route("/contactoperators")
def contactoperators():
    return flask.render_template("contactoperators.html")

@app.route("/bookslist")
def bookslist():
    return flask.render_template("bookslist.html",bookslist=bc.book.list_books())

@app.route("/deletebook",methods=["POST","GET"])
def deletebook():
    if flask.request.method=="POST":
        isbn=flask.request.form.get("isbn", type=str)
        result=bc.book.delete_book(isbn)
        if result==-1:
            return flask.render_template("error.html",errorcode="This isbn does not exists!")
        return flask.render_template("successfullynotif.html",successcode="Book has been deleted!")
    return flask.render_template("deletebook.html")


@app.route("/findbook",methods=["POST","GET"])
def findbook():
    if flask.request.method=="POST":
        isbn=flask.request.form.get("isbn", type=str)
        record=bc.book.find_book(isbn)
        if record==-1:
            return flask.render_template("error.html",errorcode="This isbn does not exists!!")
        return flask.render_template("showbook.html",book_data=record)
    return flask.render_template("findbook.html")



@app.route("/newbook",methods=["POST","GET"])
def newbook():
    if flask.request.method=="POST":
        isbn=flask.request.form.get("isbn", type=str)
        title=flask.request.form.get("title", type=str)
        author=flask.request.form.get("author", type=str)
        price=flask.request.form.get("price", type=int)
        pages=flask.request.form.get("pages", type=int)
        result=bc.book.add_book(isbn,title,author,price,pages)
        if result==1:
            return flask.render_template("error.html",errorcode="You must Enter 8 characters!")
        elif result==2:
            return flask.render_template("error.html",errorcode="This isbn already exists!")
        elif result==3:
            return flask.render_template("error.html",errorcode="Price must be at least 0!")
        else:
            return flask.render_template("successfullynotif.html",successcode="New book has been added!")
    else:
        return flask.render_template("newbook.html")




 






if __name__=="__main__":
    app.run()