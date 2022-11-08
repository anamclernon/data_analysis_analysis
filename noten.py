from PyPDF2 import PdfReader
from matplotlib import pyplot as plt
import numpy as np

def get_text_pdf(path: str)-> str:
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


def get_grades(text)->dict:
    dict = {}
    while len(text) > 10:
        dict[text[0:text.index(".")-1].replace("\n", "")] = text[text.index(".")-1:text.index(".")+3]
        text = text[text.index(".")+3:]
    return dict

def compare_grades(dict1, dict2):
    dict = {}
    for key, value in dict2.items():
        if key in dict1.keys():
            dict[key] = [dict1[key], dict2[key]]
    return dict


def make_size_xy(grades: dict)->list:
    occurence = []
    for value in grades.values():
        occurence.append((value, list(grades.values()).count(value)))
    return occurence


def plot(data: list): #list of form ([grade, grade], size)
    x = np.array([float(value[0][0]) for value in data])
    y = np.array([float(value[0][1]) for value in data])
    sizes = np.array([value[1]*80 for value in data])
    plt.scatter(x, y, s=sizes, color="magenta")
    plt.title("Students performance in Analysis 1 and 3")
    plt.xlabel("Analysis 1")
    plt.ylabel("Analysis 3")
    plt.xlim([0,6])
    plt.ylim([0,6])
    plt.show()

Ana1 = get_grades(get_text_pdf("Noten_A1.pdf"))
Ana3 = get_grades(get_text_pdf("Noten_A3.pdf"))

grades = compare_grades(Ana1, Ana3)

data = make_size_xy(grades)

plot(data)