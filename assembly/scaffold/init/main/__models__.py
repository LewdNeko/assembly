# -*- coding: utf-8 -*-
"""
Assembly: models.py

Contains applications models and other databases connections.

Do not `import`. This module is loaded implicitely by Assembly

To setup: `asm-admin sync-models`


## Example 

class MyModel(db.Model):
    name = db.Column(db.String(255), index=True)


## Usage

from assembly import models

Accessor: models.[ClassName]
ie: models.MyModel
-----
"""

from assembly import db, get_config

# ------------------------------------------------------------------------------

class Test(db.Model):
    name = db.Column(db.String(255), index=True)

