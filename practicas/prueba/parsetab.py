
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NUMERO SUMA PRODUCTO IZQPARENTESIS DERPARENTESISexpression : expression SUMA termexpression : termterm : term PRODUCTO factorterm : factorfactor : NUMEROfactor : IZQPARENTESIS expression DERPARENTESIS'
    
_lr_action_items = {'NUMERO':([0,5,6,7,],[4,4,4,4,]),'IZQPARENTESIS':([0,5,6,7,],[5,5,5,5,]),'$end':([1,2,3,4,9,10,11,],[0,-2,-4,-5,-1,-3,-6,]),'SUMA':([1,2,3,4,8,9,10,11,],[6,-2,-4,-5,6,-1,-3,-6,]),'DERPARENTESIS':([2,3,4,8,9,10,11,],[-2,-4,-5,11,-1,-3,-6,]),'PRODUCTO':([2,3,4,9,10,11,],[7,-4,-5,7,-3,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,5,],[1,8,]),'term':([0,5,6,],[2,2,9,]),'factor':([0,5,6,7,],[3,3,3,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression SUMA term','expression',3,'p_expression_suma','parser_rules.py',6),
  ('expression -> term','expression',1,'p_expression_term','parser_rules.py',10),
  ('term -> term PRODUCTO factor','term',3,'p_term_producto','parser_rules.py',14),
  ('term -> factor','term',1,'p_term_factor','parser_rules.py',19),
  ('factor -> NUMERO','factor',1,'p_factor_numero','parser_rules.py',23),
  ('factor -> IZQPARENTESIS expression DERPARENTESIS','factor',3,'p_factor_expresion','parser_rules.py',27),
]