"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from my_module.functions import idea, which_crime 
##
##

inp_crime = 'loitering'
def test_which_crime(monkeypatch):
    
    monkeypatch.setattr('sys.stdin', inp_crime)
    assert user_facts [3] == 'loitering'
    

inp_crime2 = 'possession of drugs'
def test_which_crime(monkeypatch):
    
    monkeypatch.setattr('sys.stdin', inp_crime)
    assert user_facts [3] == 'possession of drugs'
    

inp_crime3 = 'vehicular manslaughter'
def test_which_crime(monkeypatch):
    
    monkeypatch.setattr('sys.stdin', inp_crime)
    assert user_facts [3] == 'vehicular manslaughter'
    
    

inp_ans2 = "yes"
def test_idea (monkeypatch):
    
    monkeypatch.setattr('sys.stdin', inp_ans2)
    assert user_facts[5] == 'yes'
    
    
inp_ans2_3 = "no"   
def test_player_info (monkeypatch):
    
    monkeypatch.setattr('sys.stdin', inp_ans2_3)
    assert user_facts[1] == 'male'



                 
    