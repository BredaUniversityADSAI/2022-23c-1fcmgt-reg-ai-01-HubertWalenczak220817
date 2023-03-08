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
    #DPPG - Demographic parity privileged group,
    #DPUG - Demographic parity unprivileged group,
    #AD_DPUP - Absolute difference of Demographic Parity between unprivileged and privileged group

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

    DPPG = (tp_priv+fp_priv)/(tp_priv+fp_priv+fn_priv+tn_priv)
    DPUG = (tp_unpriv+fp_unpriv)/(tp_unpriv+fp_unpriv+fn_unpriv+tn_unpriv)
    AD_DPUP = abs(DPPG - DPUG)
    return [DPPG,DPUG,AD_DPUP]

demographic_parity()

def predictive_parity():
    #PPUG - 
    #PPPG - 
    #AD_PUP - 
    
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

    PPUG = tp_unpriv/(tp_unpriv+fp_unpriv)
    PPPG = tp_priv/(tp_priv+fp_priv)
    AD_PPUP = abs(PPUG - PPPG)
    return [PPUG,PPPG,AD_PPUP]

predictive_parity()

def equalized_odds():
    #TPRP - TPR privilaged group
    #TPRU - TPR unprivilaged group
    #TNRP - TNR privilaged group
    #TNRU - TNR unprivilaged group
    #AD_TPR - Absolute difference TPR
    #AD_TNR - Absolute difference TNR

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
    
    TPRP = tp_priv/(fn_priv+tp_priv)
    TPRU = tp_unpriv/(fn_unpriv+tp_unpriv)
    TNRP = tn_priv/(tn_priv+fp_priv)
    TNRU = tn_unpriv/(tn_unpriv+fp_unpriv)

    AD_TPR = abs(TPRP - TPRU)
    AD_TNR = abs(TNRP - TNRU)
    return [AD_TPR, AD_TNR]

equalized_odds()

def conditional_use_accuracy_equality():
    #AD_PUP - Absolute difference in precision between unprivileged and privileged group
    #AD_NPVUP - Absolute difference in NPV between unprivileged and privileged group
    #PPVP - PPV privilaged group
    #PPVU - PPV unprivilaged group
    #NPVP - NPV privilaged group
    #NPVU - NPV unprivilaged group

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
    
    PPVP = tp_priv/(tp_priv+fp_priv)
    PPVU = tp_unpriv/(tp_unpriv+fp_unpriv)
    NPVP = tn_priv/(tn_priv+fn_priv)
    NPVU = tn_unpriv/(tn_unpriv+fn_unpriv)

    AD_PUP = abs(PPVP - PPVU)
    AD_NPVUP = abs(NPVP - NPVU)
    return [AD_PUP, AD_NPVUP]
    return 

conditional_use_accuracy_equality()

def equal_selection_parity():
    #ESPU - Equal Selection Parity unprivileged group,
    #ESPP - Equal Selection Parity privileged group,
    #AD_ESP - Absolute difference of Equal Selection Parity between unprivileged and privileged group

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
    
    ESPU = tp_unpriv + fp_unpriv
    ESPP = tp_priv + fp_priv
    AD_ESP = abs(ESPU - ESPP)
    return [ESPU, ESPP, AD_ESP]

equal_selection_parity()

def equal_opportunity():
    #TPRP - TPR privilaged group
    #TPRU - TPR unprivilaged group 
    #AD_TPR - Absolute difference TPR

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

    TPRP = tp_priv/(fn_priv+tp_priv)
    TPRU = tp_unpriv/(fn_unpriv+tp_unpriv)

    AD_TPR = abs(TPRP - TPRU)
    return [TPRU, TPRP, AD_TPR]

equal_opportunity()

def predictive_equality():
    #TNRP - TNR privilaged group
    #TNRU - TNR unprivilaged group
    #AD_TNR - Absolute difference TNR

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

    TNRP = tn_priv/(tn_priv+fp_priv)
    TNRU = tn_unpriv/(tn_unpriv+fp_unpriv)

    AD_TNR = abs(TNRP - TNRU)
    return [TNRU, TNRP, AD_TNR]

predictive_equality()

