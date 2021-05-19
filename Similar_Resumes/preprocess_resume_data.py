import pandas as pd
import operator
import random
import pickle
from sklearn.preprocessing import MultiLabelBinarizer


def classify_experience(final_val):
    grade = ''
    if(final_val < 2.5):
        grade = 1
    elif(final_val >= 2.5 and final_val < 4.5):
        grade = 2
    elif(final_val >= 4.5 and final_val < 7.5):
        grade = 3
    elif(final_val <= 7.5 and final_val < 10.5):
        grade = 4
    elif(final_val <= 10.5 and final_val < 15.5):
        grade = 5
    elif(final_val <= 15.5 and final_val < 20.5):
        grade = 6
    else:
        grade = 7
    return grade


def use_wanted_columns():
    df = pd.read_csv("Preprocessed_Resume.csv",
                     error_bad_lines=False, engine="python")

    df1 = df[['Name', 'Preferred Location', 'Total Experience', 'Highest Degree',
              'IT Skills', 'IT Skills Experience', 'Summary']]

    exp_list = df1["Total Experience"].tolist()
    experience = []
    for seq in exp_list:
        year_exp = seq.split(" ")
        if(len(year_exp) <= 2):
            if(year_exp[0] == 'None'):
                year = 0
                month = 0
            else:
                year = int(year_exp[0][:2])
                month = 2
        else:
            year = int(year_exp[0][:2])
            if('+' in year_exp[0]):
                month = 2
            else:
                month = int(year_exp[2])
        final_val = float(str(year) + '.' + str(month))
        grade = classify_experience(final_val)
        experience.append(grade)

    df1['experience'] = experience

    names = df1['Name'].tolist()
    changed_names = []
    for i in names:
        print(i)
        if(isinstance(i, float)):
            changed_names.append("Delete")
        else:
            num = random.randrange(100, 999)
            txt = i.replace(" ", "_")
            txt = txt + "_" + str(num)
            changed_names.append(txt)
    df1['Primary_Key'] = changed_names

    df1.to_csv(r'preprocessed.csv', index=False, header=True)


def use_preprocessed():
    df = pd.read_csv("preprocessed.csv")
    skills = df['IT Skills'].tolist()
    dict_unique = {}
    for i in range(len(skills)):
        if(skills[i] == skills[i]):
            split_array = skills[i].split(",")
            for j in split_array:
                if(j in dict_unique):
                    dict_unique[j] += 1
                else:
                    dict_unique[j] = 1
    sorted_x = sorted(dict_unique.items(),
                      key=operator.itemgetter(1), reverse=True)
    dict_important = dict(sorted_x[:500])
    return list(dict_important.keys())


def combine_skills(skills_1):
    skills_2 = ["python", "java", "javascript", "c++", "neural networks", "deep learning",
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

    skills_3 = ['html',  'jquery', 'ajax', 'flask', 'citrix', 'nosql', 'sql',  'android studio', 'glue', 'paradox', 'wds', 'perl',  'java', 'filenet', 'putty', 'hive', 'nexus', 'sap', 'ado.net', 'vsphere', 'unix', 'pytest', 'splunk', 'mokito', 'balsamiq', 'eclipse', 'hibernate', 'jdbc', 'tableau', 'tensorflow', 'siebel', 'solution architecture', 'VB.Net', 'apache', 'solarwinds', 'netbackup', 'redis', 'salesforce', 'windows', 'linux', 'xml', 'jdk', 'toad', 'gitlab',  'devops', 'verilog', 'Git',  'vmware', 'hybris', 'rest api', 'j2ee',  'php', 'dac', 'jenkins', 'mvc', 'qc', 'css', 'selenium', 'entity framework', 'json', 'log4j', 'django', 'go', 'libreoffice', 'active directory', 'docker', 'jsp', 'daq', 'ansible', 'netbeans', 'jira', 'ubuntu', 'postman', 'tally', 'sublime', 'action script', 'linq', 'api', 'swing', 'adobe analytics', 'adobe illustrator', 'aerospike', 'agilent', 'aginity', 'alexa', 'altiris', 'android studio', 'assembly', 'atmega', 'aurora', 'auto scaling', 'sas',  'rdbms', 'dbms', 'spark', 'devops', 'beautiful soup', 'map reduce', 'block chain', 'cypress', 'cassandra',
                'cloudwatch', 'cloud taleo', 'confluence', 'cosmos', 'couchdb', 'cron', 'crystal report', 'Cucumber', 'dell boomi', 'delphi', 'discoverer', 'docapp', 'dojo', 'ecmascript', 'ejb', 'etl',  'elastic load balancing', 'flutter', 'kotlin', 'force.com', 'fortify', 'gerrit', 'groovy', 'gentran', 'glacier', 'golden gate', 'google cloud', 'graylog', 'greenplum', 'guidewire', 'hana', 'hbase', 'highchart', 'hiplink', 'hortonworks', 'ibm bpm', 'ibm clear quest', 'ibm cognos', 'ibm db2', 'ibm mq', 'ibm spss modeler', 'ibm sterling integrator',  'image processing', 'intellij', 'ionic', 'ios', 'iot', 'impala', 'incident management', 'informatica', 'jasper', 'jee', 'jsf', 'junit', 'jwt', 'design patterns',  'load runner', 'magento', 'matlab', 'mern stack', 'mean stack', 'mqtt', 'ms visio',  'management studio', 'microsoft exchange', 'middleware', 'numpy', 'gunicorn', 'httpd', 'nifi', 'scipy', 'pandas', 'oauth', 'networking', 'oozie', 'opencv', 'pega', 'pig', 'powershell',  'pycharm', 'data science', 'cyclone', 'pytorch', 'qac', 'qt creator', 'rpa', 'redux', 'remedy', 'scala', 'servlet', 'soap',  'sqoop', 'swagger', 'sybase', 'teamcenter', 'terraform',  'toad', 'tortoise', 'vmware', 'websphere']

    final_skills = []
    skills_1 = [x.lower() for x in skills_1]
    final_skills.extend(skills_1)
    final_skills.extend(skills_2)
    final_skills.extend(skills_3)
    final_skills = list(set(final_skills))
    return final_skills


def create_dummies(final_skills):
    df = pd.read_csv("preprocessed.csv")
    summary_list = df['Summary'].tolist()
    skills_collect = []
    for summary in summary_list:
        skill = []
        if(isinstance(summary, float) == False):
            st = summary.lower()
            for j in final_skills:
                if(j in st):
                    skill.append(j)
                    continue
        skills_collect.append(skill)
    print(len(skills_collect))
    print("*************************************************")

    skills = df['IT Skills'].tolist()
    skills_collect2 = []
    for i in range(len(skills)):
        sk = []
        if(skills[i] == skills[i]):
            split_array = skills[i].split(",")
            for j in split_array:
                if(j.lower() in final_skills):
                    sk.append(j)
                    continue
        skills_collect2.append(sk)
    print(len(skills_collect2))
    print("*************************************************")

    final_skill_set = []
    for k in range(len(skills_collect)):
        sks = []
        sks.extend(skills_collect[k])
        sks.extend(skills_collect2[k])
        final_skill_set.append(sks)

    final_dict_skills = {}
    count = 1
    for i in final_skill_set:
        final_dict_skills[count] = i
        count += 1

    with open("final_dict_pickle.pickle", "wb") as h1:
        pickle.dump(final_dict_skills, h1)


def merge_skills():
    df = pd.read_csv("preprocessed.csv")
    # print(df.head())
    # print(df.columns)

    degree_list = df['Highest Degree'].tolist()
    degree_converted_list = convert_highest_degree(degree_list)

    df['degree_converted'] = degree_converted_list
    df_degree = df[['degree_converted', 'Primary_Key']]
    pm_key = df_degree['Primary_Key'].tolist()
    degree_conv = df_degree['degree_converted'].tolist()
    # print(df_degree.tail())

    s = df_degree['degree_converted']
    mlb = MultiLabelBinarizer()
    df2_degree = pd.DataFrame(mlb.fit_transform(
        s), columns=mlb.classes_, index=df.index)
    df2_degree['Primary_Key'] = pm_key
    # print(df2_degree.tail())

    df_experience = df[['experience', 'Primary_Key']]
    # print(df_experience.tail())

    e = df['experience'].tolist()
    first, second, third, fourth, fifth, sixth, seventh = create_experience(e)
    df2_experience = pd.DataFrame()
    df2_experience['First'] = first
    df2_experience['Second'] = second
    df2_experience['Third'] = third
    df2_experience['Fourth'] = fourth
    df2_experience['Fifth'] = fifth
    df2_experience['Sixth'] = sixth
    df2_experience['Seventh'] = seventh
    df2_experience['Primary_Key'] = pm_key

    # print(df2_experience.tail())

    df2_full = pd.merge(df2_degree, df2_experience, on='Primary_Key')
    # print(df2_full.tail())

    fd = pd.read_pickle(r'final_dict_pickle.pickle')
    final_skill_set = list(fd.values())

    df['Final_Skills'] = final_skill_set
    # print(df.tail())
    sp = df['Final_Skills']
    mlb = MultiLabelBinarizer()
    df3 = pd.DataFrame(mlb.fit_transform(
        sp), columns=mlb.classes_, index=df.index)
    df3['Primary_Key'] = pm_key

    df3_full = pd.merge(
        df2_full, df3, on='Primary_Key')

    # df3_full.to_csv('final_processed_resume.csv')
    return df3_full


def convert_highest_degree(degree_list):
    degree_converted = []
    for i in degree_list:
        if(i == "Bachelor's Degree"):
            degree_converted.append("B")
        elif(i == "Master's Degree"):
            degree_converted.append("M")
        elif(i == 'Doctorate Degree'):
            degree_converted.append("D")
        else:
            degree_converted.append("O")
    return degree_converted


def create_experience(e):
    first, second, third, fourth, fifth, sixth, seventh = [], [], [], [], [], [], []
    for i in e:
        if(i == "first"):
            first.append(1)
            second.append(0)
            third.append(0)
            fourth.append(0)
            fifth.append(0)
            sixth.append(0)
            seventh.append(0)
        elif(i == "second"):
            first.append(0)
            second.append(1)
            third.append(0)
            fourth.append(0)
            fifth.append(0)
            sixth.append(0)
            seventh.append(0)
        elif(i == "third"):
            first.append(0)
            second.append(0)
            third.append(1)
            fourth.append(0)
            fifth.append(0)
            sixth.append(0)
            seventh.append(0)
        elif(i == "fourth"):
            first.append(0)
            second.append(0)
            third.append(0)
            fourth.append(1)
            fifth.append(0)
            sixth.append(0)
            seventh.append(0)
        elif(i == "fifth"):
            first.append(0)
            second.append(0)
            third.append(0)
            fourth.append(0)
            fifth.append(1)
            sixth.append(0)
            seventh.append(0)
        elif(i == "sixth"):
            first.append(0)
            second.append(0)
            third.append(0)
            fourth.append(0)
            fifth.append(0)
            sixth.append(1)
            seventh.append(0)
        else:
            first.append(0)
            second.append(0)
            third.append(0)
            fourth.append(0)
            fifth.append(0)
            sixth.append(0)
            seventh.append(1)
    return first, second, third, fourth, fifth, sixth, seventh


def calculate_matrix(df):
    df = df[df['Primary_Key'] != 'Delete']
    df.reset_index(inplace=True)
    dict_name = {}
    for i in range(600, len(df)-1):
        if(i == 700):
            break
        name = df.loc[[i]]['Primary_Key'].tolist()[0]
        dict_2_name = {}
        for j in range(i+1, len(df)):
            score, p_key = calculate_distance(df.loc[[i]], df.loc[[j]])
            dict_2_name[p_key] = score
            print(i, score, p_key)
        if(len(dict_2_name) > 20):
            dict_name[name] = sorted(
                dict_2_name.items(), key=lambda x: x[1], reverse=True)[:20]
        else:
            dict_name[name] = sorted(
                dict_2_name.items(), key=lambda x: x[1], reverse=True)

    with open("dict_700.pickle", "wb") as h1:
        pickle.dump(dict_name, h1)

    df1 = pd.read_pickle(r'dict_700.pickle')
    print(len(df1))

    for j in df1:
        print(j, df1[j])


def calculate_distance(df1, df2):
    score = 0
    flag_degree = 0
    flag_experience = 0

    if(df1['B'].tolist()[0] == 1 and df2['B'].tolist()[0] == 1):
        score = score + 150
        flag_degree = 1
    elif(df1['D'].tolist()[0] == 1 and df2['D'].tolist()[0] == 1):
        score = score + 150
        flag_degree = 1
    elif(df1['M'].tolist()[0] == 1 and df2['M'].tolist()[0] == 1):
        score = score + 150
        flag_degree = 1
    elif(df1['O'].tolist()[0] == 1 and df2['O'].tolist()[0] == 1):
        score = score + 150
        flag_degree = 1

    if(df1['First'].tolist()[0] == 1 and df2['First'].tolist()[0] == 1):
        score = score + 500
        flag_experience = 1
    elif(df1['Second'].tolist()[0] == 1 and df2['Second'].tolist()[0] == 1):
        score = score + 500
        flag_experience = 1
    elif(df1['Third'].tolist()[0] == 1 and df2['Third'].tolist()[0] == 1):
        score = score + 500
        flag_experience = 1
    elif(df1['Fourth'].tolist()[0] == 1 and df2['Fourth'].tolist()[0] == 1):
        score = score + 500
        flag_experience = 1
    elif(df1['Fifth'].tolist()[0] == 1 and df2['Fifth'].tolist()[0] == 1):
        score = score + 500
        flag_experience = 1
    elif(df1['Sixth'].tolist()[0] == 1 and df2['Sixth'].tolist()[0] == 1):
        score = score + 500
        flag_experience = 1
    elif(df1['Seventh'].tolist()[0] == 1 and df2['Seventh'].tolist()[0] == 1):
        score = score + 500
        flag_experience = 1

    list_1 = df1.values.tolist()[0]
    list_2 = df2.values.tolist()[0]

    for k in range(len(list_1)):
        if(list_1[k] == list_2[k] and list_1[k] == 1):
            score = score + 1

    if(flag_experience == 1):
        score = score - 1
    if(flag_degree == 1):
        score = score - 1

    return score, df2['Primary_Key'].tolist()[0]


# use_wanted_columns()
# skills_1 = use_preprocessed()
# final_skills = combine_skills(skills_1)
# create_dummies(final_skills)
df = merge_skills()
calculate_matrix(df)
