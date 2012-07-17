# author :dylan_fan;
# write at 2012/07/07; 


import math
import string
import random


class SGD_LR:
    def __init__(self):
#        self.alpha = 0.0000012
#        self.lamb = 0.0000015  
        self.lamb = 0.000001
        self.weight = {}
        self.itera_times = 5000
             
    def logistic_train(self,Y, X):
        if len(Y) != len(X):
            print "Y and X length is matched"
            return 
        for i in range(self.itera_times):
            cost_f = 0.0
            self.alpha = math.sqrt(0.003/(0.003+i))
            
            for k in range(len(Y)):
                label = Y[k]
                feature = X[k]
                predict_value = self.predict(feature)
                error = label - predict_value
                cost_f += math.fabs(error)
#                error = label * math.log(predict_value) + (1-label) * math.log(1-predict_value)
#                cost_f += (-error)
                tmp1 = label * math.exp(-predict_value) /(1 + math.exp(-predict_value)) -(1-label) * math.exp(-(1-predict_value)) /(1 + math.exp(-(1 -predict_value)))
                
                weight_sum = 0.0
                
#                tmp = label/predict_value - (1-label)/(1-predict_value)
                
                for f , v in feature.items():                    
                    weight_sum += self.weight[f] * v
                if weight_sum < -8.0:
                    derivation = 0.0001
                else:
                    linear_sum = math.exp(-weight_sum)
                    derivation = linear_sum / (linear_sum * linear_sum + 2 * linear_sum +1)                
                
                for f in feature.keys():                    
                    self.weight[f] += self.alpha * (tmp1 * derivation * feature[f] - self.lamb * self.weight[f]) # update ruel by gradient Descent methods
            print 'iteration', i, cost_f/len(Y),'done'
                
        return
    
    def logistic_save_model(self, model_file):
        fw = open(model_file, "w")
        for f , w in self.weight.items():
            fw.write("%d : %f\n" %(f,w))
        fw.close()
        print "model save ok..."
         
    def logistic_load_model(self,model_file):
        fr = open(model_file,"r")
        for line in fr.readlines():
#            print line
            f, w = line.split(":")
            f = string.atoi(f)
            w = string.atof(w)
            self.weight[f] = w
        fr.close()                
        print "model load ok..."
    
    def predict(self, feature):
        weight_sum = 0        
        for f , v in feature.items():
            self.weight.setdefault(f,0)
            weight_sum += self.weight[f] * v
        if weight_sum < -8:
            return 0.01
        return 1.0 / (1.0 + math.exp(-weight_sum))
    
    def logistic_predict(self, Y, X):
        if len(Y) != len(X):
            print "Y and X length is matched"
        rmse = 0.0
        p_vals = []
        p_labels = []
        accuate = 0.0
        for i in range(len(Y)):
            feature = X[i]
            label = Y[i]
            predict_value = self.predict(feature)
            rmse += (label - predict_value) * (label - predict_value)
            p_vals.append([predict_value])
            if predict_value > 0.5:
                p_label = 1                
            else:
                p_label = 0                
            p_labels.append(p_label)
            if p_label == label:
                accuate += 1.0
                
        rmse /= len(Y)
        accuate /= len(Y)
        print "rmse : %f" %(rmse)
        print "Accuate : %g%%" %(accuate*100)
        return p_labels, p_vals
     
    
            
            
            
            
    
    
        
