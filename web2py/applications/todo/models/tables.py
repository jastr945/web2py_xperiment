# -*- coding: utf-8 -*-
db.define_table('task',
    Field('title',unique=True,notnull=True),
    Field('description','text'),
    Field('priority','integer',default=3,
        requires=IS_IN_SET([1,2,3,4,5],
        labels=[
            T('Very low'), 
            T('Low'), 
            T('Medium'), 
            T('High'), 
            T('Very High')],
            zero=None)),
    Field('completed','boolean',default=False),
    Field('user_id','reference auth_user', default=auth.user_id))
