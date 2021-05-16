import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import os
import pickle

driver = webdriver.Chrome()
skill_sets = ["python", "java", "javascript", "c++", "neural networks", "deep learning",
              "pytorch", "tensorflow", "machine learning", "data science", "analytics", "tableau", "power bi",
              "nlp", "artificial intelligence", "ai", "ml", "bi", "business intelligence", "model", "design",
              "testing", "deployment", "ci", "cd", "ci/cd", "natural language processing",
              "reinforcement learning", "mxnet", "cntk", "apache mahout", "sql", "docker", "kubernetes",
              "sisense", "git", "amazon cloud", "aws", "gcp", "google cloud", "azure", "ml studio",
              "postgresql", "cosmosdb", "mongodb", "sqlite", "classification", "clustering", "regression",
              "anomaly detection", "scikit learn", "scikit", "numpy", "pandas", "matplotlib", "pandas",
              "text analytics", "etl", "pipelines", "git", "object detection", "motion detection", "rest api",
              "keras", "opencv", "dl", "vision", "rekognition", "sagemaker", "matlab",
              "kafka", "hdfs", "hadoop", "spark", "hive", "pig", "nosql", "svm", "ml ops",
              "caffe", "theano", "torch", "dialogflow", "predictive modelling", "math", "stat",
              "gradient descent", "forecasting", "decision trees", "cluster analysis",
              "random forest", "excel", "presto", "druid", "computer vision", "transformer",
              "nltk", "selenium", "plotly", "scala", "nifi", "sqoop", "hbase", "airflow", "firebase",
              "sas", "d3", "ggplot2", "weka", "rapidminer", "qlickview", "pentaho", "splunk", "oracle",
              "sap", "hana", "kinesis", "storm", "julia", "jupyter", "spss", "h2o",  "bash", "ruby",
              "trifacta", "informatica", "s3", "bokeh", "datarobot", "mysql", "ms sql", "octave",
              "redis", "scikit-learn", "scipy", "cnn", "rnn", "lstm", "chatbot"]

ITSkills = ['html',  'jquery', 'ajax', 'flask', 'citrix', 'nosql', 'sql',  'android studio', 'glue', 'paradox', 'wds', 'perl',  'java', 'filenet', 'putty', 'hive', 'nexus', 'sap', 'ado.net', 'vsphere', 'unix', 'pytest', 'splunk', 'mokito', 'balsamiq', 'eclipse', 'hibernate', 'jdbc', 'tableau', 'tensorflow', 'siebel', 'solution architecture', 'VB.Net', 'apache', 'solarwinds', 'netbackup', 'redis', 'salesforce', 'windows', 'linux', 'xml', 'jdk', 'toad', 'gitlab',  'devops', 'verilog', 'Git',  'vmware', 'hybris', 'rest api', 'j2ee',  'php', 'dac', 'jenkins', 'mvc', 'qc', 'css', 'selenium', 'entity framework', 'json', 'log4j', 'django', 'go', 'libreoffice', 'active directory', 'docker', 'jsp', 'daq', 'ansible', 'netbeans', 'jira', 'ubuntu', 'postman', 'tally', 'sublime', 'action script', 'linq', 'api', 'swing', 'adobe analytics', 'adobe illustrator', 'aerospike', 'agilent', 'aginity', 'alexa', 'altiris', 'android studio', 'assembly', 'atmega', 'aurora', 'auto scaling', 'sas',  'rdbms', 'dbms', 'spark', 'devops', 'beautiful soup', 'map reduce', 'block chain', 'cypress', 'cassandra',
            'cloudwatch', 'cloud taleo', 'confluence', 'cosmos', 'couchdb', 'cron', 'crystal report', 'Cucumber', 'dell boomi', 'delphi', 'discoverer', 'docapp', 'dojo', 'ecmascript', 'ejb', 'etl',  'elastic load balancing', 'flutter', 'kotlin', 'force.com', 'fortify', 'gerrit', 'groovy', 'gentran', 'glacier', 'golden gate', 'google cloud', 'graylog', 'greenplum', 'guidewire', 'hana', 'hbase', 'highchart', 'hiplink', 'hortonworks', 'ibm bpm', 'ibm clear quest', 'ibm cognos', 'ibm db2', 'ibm mq', 'ibm spss modeler', 'ibm sterling integrator',  'image processing', 'intellij', 'ionic', 'ios', 'iot', 'impala', 'incident management', 'informatica', 'jasper', 'jee', 'jsf', 'junit', 'jwt', 'design patterns',  'load runner', 'magento', 'matlab', 'mern stack', 'mean stack', 'mqtt', 'ms visio',  'management studio', 'microsoft exchange', 'middleware', 'numpy', 'gunicorn', 'httpd', 'nifi', 'scipy', 'pandas', 'oauth', 'networking', 'oozie', 'opencv', 'pega', 'pig', 'powershell',  'pycharm', 'data science', 'cyclone', 'pytorch', 'qac', 'qt creator', 'rpa', 'redux', 'remedy', 'scala', 'servlet', 'soap',  'sqoop', 'swagger', 'sybase', 'teamcenter', 'terraform',  'toad', 'tortoise', 'vmware', 'websphere',"vue","angular","react"]


def deal_years(initial):
    result = ''
    if(initial >= 0 and initial <= 2):
        result = "first_band"
    elif(initial > 2 and initial <= 5):
        result = "second_band"
    elif(initial > 5 and initial <= 8):
        result = "third_band"
    elif(initial > 8 and initial <= 11):
        result = "fourth_band"
    else:
        result = "fifth_band"
    return result


def transform_requirements(url):
    driver.get(url)
    time.sleep(3)
    a = driver.find_elements_by_class_name("top")
    if(len(a) != 0):
        skill = []
        result = 0
        for k in a[0].text.splitlines():
            if("years" in k):
                arr = k.split()
                initial = arr[0]
                if(initial.isdigit() == False):
                    result = 0
                    skill = []
                    return result, skill
                initial = int(arr[0])
                result = deal_years(initial)
                break
        b = driver.find_elements_by_class_name("job-desc")
        for ele in b[0].text.splitlines():
            ele = ele.lower()
            for o in skill_sets:
                if(o in ele):
                    skill.append(o)
                    continue
            for o in ITSkills:
                if(o in ele):
                    skill.append(o)
                    continue
            element = ele.split()
            if('r' in element):
                skill.append('r')
        return result, skill
    else:
        result = 0
        skill = []
        return result, skill


def mult_requirements():
    dff = pd.read_pickle(r'frontend_engineer.pickle')
    print("*********************************************************************")
    print(len(dff))
    print("*********************************************************************")

    # 5180
    df = list(dff.values())[4701:]
    count = 0
    first_dict = {}
    second_dict = {}
    third_dict = {}
    fourth_dict = {}
    fifth_dict = {}

    for i in df:
        if i == 'https://www.naukri.com/job-listings-ui-developer-experience-3-to-7-years-evolvus-evolvus-solutions-bangalore-bengaluru-3-to-7-years-020418501501?src=jobsearchDesk&sid=16201187062239386&xp=2&px=50':
            continue
        count += 1
        if(count % 100 == 0):
            print('\a')
        print(count)
        result, skill = transform_requirements(i)
        if(result != 0 and skill != []):
            skill = list(set(skill))
            if(result == "first_band"):
                for op in skill:
                    if(op in first_dict):
                        first_dict[op] += 1
                    else:
                        first_dict[op] = 1
            elif(result == "second_band"):
                for op in skill:
                    if(op in second_dict):
                        second_dict[op] += 1
                    else:
                        second_dict[op] = 1
            elif(result == "third_band"):
                for op in skill:
                    if(op in third_dict):
                        third_dict[op] += 1
                    else:
                        third_dict[op] = 1
            elif(result == "fourth_band"):
                for op in skill:
                    if(op in fourth_dict):
                        fourth_dict[op] += 1
                    else:
                        fourth_dict[op] = 1
            else:
                for op in skill:
                    if(op in fifth_dict):
                        fifth_dict[op] += 1
                    else:
                        fifth_dict[op] = 1

    with open("first_dict_fe6.pickle", "wb") as h1:
        pickle.dump(first_dict, h1)
    with open("second_dict_fe6.pickle", "wb") as h2:
        pickle.dump(second_dict, h2)
    with open("third_dict_fe6.pickle", "wb") as h3:
        pickle.dump(third_dict, h3)
    with open("fourth_dict_fe6.pickle", "wb") as h4:
        pickle.dump(fourth_dict, h4)
    with open("fifth_dict_fe6.pickle", "wb") as h5:
        pickle.dump(fifth_dict, h5)

    df1 = pd.read_pickle(r'first_dict_fe6.pickle')
    print(len(df1))
    df2 = pd.read_pickle(r'second_dict_fe6.pickle')
    print(len(df2))
    df3 = pd.read_pickle(r'third_dict_fe6.pickle')
    print(len(df3))
    df4 = pd.read_pickle(r'fourth_dict_fe6.pickle')
    print(len(df4))
    df5 = pd.read_pickle(r'fifth_dict_fe6.pickle')
    print(len(df5))

    print(df1)
    print("**********************************************************")
    print(df2)
    print("**********************************************************")
    print(df3)
    print("**********************************************************")
    print(df4)
    print("**********************************************************")
    print(df5)
    print("**********************************************************")

mult_requirements()



