import pytest 
from calculate_metric import *

def test_load_confusion_matrices():
    assert load_confusion_matrices() == [[26, 23, 12, 37], [34, 15, 14, 35]]

def test_demographic_parity():
   assert demographic_parity() == [0.6122448979591837, 0.5102040816326531, 0.10204081632653061]

def test_predictive_parity():
   assert predictive_parity() == [0.7, 0.6166666666666667, 0.08333333333333326]

def test_equalized_odds():
   assert equalized_odds() == [0.04081632653061218, 0.16326530612244894]

def test_conditional_use_accuracy_equality():
   assert conditional_use_accuracy_equality() == [0.08333333333333326, 0.02412280701754388]

def test_equal_selection_parity():
   assert equal_selection_parity() == [50, 60, 10]

def test_equal_opportunity():
   assert equal_opportunity() == [0.7142857142857143, 0.7551020408163265, 0.04081632653061218]

def test_predictive_equality():
   assert predictive_equality() == [0.6938775510204082, 0.5306122448979592, 0.16326530612244894]


