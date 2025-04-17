from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
#from .forms import *
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView)
from . import models
from .forms import *
import joblib
import pickle
from django.core.files.storage import FileSystemStorage
#from topicApp.Topicfun import Topic
#from ckdApp.funckd import ckd
#from sklearn.tree import export_graphviz #plot tree
#from sklearn.metrics import roc_curve, auc #for model evaluation
#from sklearn.metrics import classification_report #for model evaluation
##from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(df2.drop('classification_yes', 1), df2['classification_yes'], test_size = .2, random_state=10)

import time
import pandas as pd
import numpy as np
#from sklearn.preprocessing import StandardScaler
#from sklearn.feature_selection import SelectKBest
#from sklearn.feature_selection import chi2
#from sklearn.model_selection import train_test_split
#from sklearn.decomposition import PCA
#from sklearn.feature_selection import RFE
#from sklearn.linear_model import LogisticRegression
import pickle
import matplotlib.pyplot as plt
#import eli5 #for purmutation importance
#from eli5.sklearn import PermutationImportance
#import shap #for SHAP values
#from pdpbox import pdp, info_plots #for partial plots
np.random.seed(123) #ensure reproduc
class dataUploadView(View):
    form_class = childInfoForm
    success_url = reverse_lazy('success')
    template_name = 'create.html'
    failure_url = reverse_lazy('fail')
    filenot_url = reverse_lazy('filenot')
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        #print('inside post')
        form = self.form_class(request.POST, request.FILES)
        #print('inside form')
        if form.is_valid():
            form.save()
            playHours = request.POST.get('Play_Hours')
            screenTime = request.POST.get('Screen_Time')
            studyHours = request.POST.get('Study_Hours')
            mealsPerDay = request.POST.get('Meals_Per_Day')
            sleepHours = request.POST.get('Sleep_Hours')

            model = joblib.load('childmodel.pkl')
            scaler = joblib.load('scaler1.pkl')
            label_encoders = joblib.load('label_encoders1.pkl')

            # # 3. Encode categorical value
            # valid_moods = label_encoders['Mood'].classes_
            # if data_bgr not in valid_moods:
            #     return render(request, "error.html", {
            #         "message": f"Invalid mood: '{data_bgr}'. Please choose from: {', '.join(valid_moods)}"
            #     })

            # mood_encoded = label_encoders['Mood'].transform([mood])[0]
            # mood_encoded = label_encoders['Mood'].transform([data_bgr])[0]

            # 4. Prepare input in correct order
            input_data = np.array([[playHours, screenTime, studyHours, mealsPerDay, sleepHours]])

            # 5. Scale input
            scaled_input = scaler.transform(input_data)

            # 6. Predict
            prediction = model.predict(scaled_input)[0]
            predicted_label = label_encoders['Behavior_Category'].inverse_transform([prediction])
            # #print (data)
            # #dataset1=pd.read_csv("prep.csv",index_col=None)
            # dicc={'yes':1,'no':0}
            # filename = 'finalized_model_ckd.sav'
            # classifier = pickle.load(open(filename, 'rb'))
            #
            # data = np.array([data_bgr,data_bu,data_sc,data_pcv,data_wc])
            # #sc = StandardScaler()
            # #data = sc.fit_transform(data.reshape(-1,1))
            # out=classifier.predict(data.reshape(1,-1))
# providing an index
            #ser = pd.DataFrame(data, index =['bgr','bu','sc','pcv','wbc'])

            #ss=ser.T.squeeze()
#data_for_prediction = X_test1.iloc[0,:].astype(float)

#data_for_prediction =obj.pca(np.array(data_for_prediction),y_test)
            #obj=ckd()
            ##plt.savefig("static/force_plot.png",dpi=150, bbox_inches='tight')
            return render(request, "succ_msg.html", {'playHours':playHours,'screenTime':screenTime,'studyHours':studyHours,'mealsPerDay':mealsPerDay,'sleepHours':sleepHours,
                                                        'out':predicted_label})


        else:
            return redirect(self.failure_url)
