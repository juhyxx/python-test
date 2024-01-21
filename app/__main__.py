from flask import Flask
from flask import stream_with_context, request, Response
import zipfile
import os

from flask import Flask, render_template

import logging
from xmllib.parts import parts_list

from xmllib.product_list import product_list

from xmllib.count import product_count
import requests
import shutil


flask = Flask(__name__)

def download():
    logging.warning("downloading...")
    url = "https://www.retailys.cz/wp-content/uploads/astra_export_xml.zip"
    with requests.get(url, stream=True) as r:
        with open("./download/astra_export_xml.zip", 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    logging.warning("unzipping...")
    with zipfile.ZipFile("./download/astra_export_xml.zip", "r") as zipped_file:
        zipped_file.extractall("./download")

    logging.warning("reading...")
    dir_list = os.listdir("./download")
    file_name = "./download/" + dir_list[0]
    return file_name


file = download()


@flask.route("/")
def hello():
    return render_template("base.html")


@flask.route("/1")
def task1():
    global file
    return render_template("task1.html", count=product_count(file))


@flask.route("/2")
def task2():
    global file

    return render_template("task2.html", list=product_list(file))


@flask.route("/3")
def task3():
    global file

    return render_template("task3.html", list=parts_list(file))


if __name__ == "__main__":
    flask.run(host="0.0.0.0", port=8080, debug=True)
