import numpy as np

def load_confusion_matrices():
    cm_priv = np.load('./Responsible_AI/confusion_matrix_priv_female.npy')
    tn_priv = cm_priv[0][0]
    fp_priv = cm_priv[0][1]
    fn_priv = cm_priv[1][0]
    tp_priv = cm_priv[1][1]
    cm_unpriv = np.load('./Responsible_AI/confusion_matrix_unpriv_male.npy')
    tn_unpriv = cm_unpriv[0][0]
    fp_unpriv = cm_unpriv[0][1]
    fn_unpriv = cm_unpriv[1][0]
    tp_unpriv = cm_unpriv[1][1]
    return [[tn_priv, fp_priv, fn_priv, tp_priv], [tn_unpriv, fp_unpriv, fn_unpriv, tp_unpriv]]

load_confusion_matrices()

def demographic_parity():
    return 

demographic_parity()

def predictive_parity():
    return 

predictive_parity()

def equalized_odds():
    return 

equalized_odds()

def conditional_use_accuracy_equality():
    return 

conditional_use_accuracy_equality()

def equal_selection_parity():
    return 

equal_selection_parity()

def equal_opportunity():
    return 

equal_opportunity()

def predictive_equality():
    return 

predictive_equality()
