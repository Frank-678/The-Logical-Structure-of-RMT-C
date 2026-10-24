#!/usr/bin/env python3
"""RULES-02 exact arithmetic examples; not a referee or robot simulator."""
from fractions import Fraction as F
import json

def update(previous, actual, bonus, deaths):
    return max(F(0), F(previous)+F(actual)+F(bonus)-60*deaths)

def score(d):
    return 15*min(F(d)/500,F(1))

def batch(hp, contributions, award=True):
    total=sum((F(n) for _,_,n in contributions),F(0))
    ratio=min(F(1),F(hp)/total) if total else F(0)
    ordinary={}; eligible=set()
    for team,kind,nominal in contributions:
        actual=F(nominal)*ratio
        if actual>0: eligible.add(team)
        if kind=='attack': ordinary[team]=ordinary.get(team,F(0))+actual
    bonus={t:F(60,len(eligible)) for t in eligible} if award and hp>0 and total>=hp and eligible else {}
    return ordinary,bonus

def completed(before,alive,d,threshold):
    return before or (alive and d>=threshold)

def main():
    rows=[]
    def check(name,actual,expected):
        assert actual==expected,(name,actual,expected)
        rows.append({'case':name,'result':str(actual),'passed':True})
    check('protocol_80_plus_20_plus_60',update(80,20,60,0),F(160))
    check('following_death',update(160,0,0,1),F(100))
    check('mutual_kill_add_before_floor',update(0,20,60,1),F(20))
    check('floor_after_tick_sum',update(30,20,0,1),F(0))
    check('world_split_no_bonus',update(30,0,0,1),F(0))
    check('above_500_preserved',update(600,0,0,1),F(540))
    check('full_score_can_fall',score(update(520,0,0,1)),F(69,5))
    check('ordinary_20_points',score(20),F(3,5))
    a,b=batch(10,[('A','attack',20),('B','attack',20)])
    check('overkill_actual_split',a,{'A':F(5),'B':F(5)})
    check('overkill_equal_bonus',b,{'A':F(30),'B':F(30)})
    a,b=batch(14,[('A','attack',20),('B','attack',50)])
    check('unequal_actual_proportional',a,{'A':F(4),'B':F(10)})
    check('unequal_damage_equal_bonus',b,{'A':F(30),'B':F(30)})
    a,b=batch(10,[('B','attack',20),('C','reflection',20)])
    check('reflection_not_ordinary',a,{'B':F(5)})
    check('reflection_shared_bonus',b,{'B':F(30),'C':F(30)})
    a,b=batch(30,[('A','pepper',50),('B','pepper',50)])
    check('pepper_not_ordinary',a,{})
    check('pepper_shared_bonus',b,{'A':F(30),'B':F(30)})
    a,b=batch(10,[('A','attack',20),('A','reflection',20),('B','attack',20),('Z','attack',0)])
    check('deduplicate_exclude_zero',b,{'A':F(30),'B':F(30)})
    check('exclude_previous_tick_C','C' in b,False)
    a,b=batch(10,[('A','attack',20),('B','attack',20),('C','attack',20)])
    check('fractional_attack_credit',a['A'],F(10,3))
    check('three_teams_equal_bonus',b,{'A':F(20),'B':F(20),'C':F(20)})
    a,b=batch(20,[('environment','explosion',80)],award=False)
    check('environment_no_bonus',b,{})
    check('dead_threshold_not_complete',completed(False,False,update(180,20,60,1),200),False)
    check('alive_threshold_complete',completed(False,True,200,200),True)
    check('completed_id_survives_drop',completed(True,False,0,200),True)
    print(json.dumps({'scope':'RULES-02 arithmetic only; no ROS/referee execution','cases':len(rows),'errors':[],'results':rows},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
