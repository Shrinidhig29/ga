
import os
from flask import Flask, request
import json

app = Flask(__name__)

class Ingest:

    def find_all_class(self, path):
        """To find the class names.

        Input:
            path: A string for path of data
        Output:
            classArr: An array of strings(class names)"""
        class_arr = os.listdir(path)
        return class_arr

    def read_content_from_dir(self, basePath, className):

        class_dir = os.path.join(basePath, className)
        files = os.listdir(class_dir)
        contentList = []
        for file in files:
            with open(os.path.join(class_dir, file)) as fl:
                content = fl.read()
            contentList.append(content)
        return contentList

    def collect_data(self, basePath):
        class_names = self.find_all_class(basePath)
        final_Data = {}
        for class_name in class_names:
            content_list = self.read_content_from_dir(basePath, class_name)
            final_Data[class_name] = content_list
        return final_Data


@app.route('/fetch')
def get_Data():
    ingest_obj = Ingest()
    basePath = r'C:\Users\nidhi\Documents\GADEPLOY\DATA\20news-18828'
    final_Data = ingest_obj.collect_data(basePath)
    return final_Data

app.run('localhost: ')



