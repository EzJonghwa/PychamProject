# https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset?select=test_Y3wMUE5_7gLdaTN.csv
# Loan_ID: 대출 ID
# Gender: 성별
# Married: 결혼 여부
# Dependents: 부양가족 수
# Education: 학력 수준
# Self_Employed: 자영업 여부
# ApplicantIncome: 신청자의 소득
# CoapplicantIncome: 공동 신청자의 소득
# LoanAmount: 대출 금액
# Loan_Amount_Term: 대출 상환 기간
# Credit_History: 신용 이력
# Property_Area: 재산 위치
# Loan_Status: 대출 승인 여부 (Y: 승인, N: 불승인)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import pandas as pd
import joblib
