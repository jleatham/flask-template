from marshmallow import Schema, fields, pprint, post_load

class Architecture(object):
    def __init__(self, date, arch, category, bullet, bLink, subBullet1, sb1Link, subBullet2, sb2Link, subBullet3, sb3Link, subBullet4, sb4Link, subBullet5, sb5Link, rowID):
        self.date       = date
        self.arch       = arch
        self.category   = category
        self.bullet     = bullet
        self.bLink      = bLink
        self.subBullet1 = subBullet1
        self.sb1Link    = sb1Link
        self.subBullet2 = subBullet2
        self.sb2Link    = sb2Link
        self.subBullet3 = subBullet3
        self.sb3Link    = sb3Link
        self.subBullet4 = subBullet4
        self.sb4Link    = sb4Link
        self.subBullet5 = subBullet5
        self.sb5Link    = sb5Link
        self.rowID      = rowID
    
    def __repr__(self):
        return "rowID: {} , date: {}  , bullet: {}".format(str(self.rowID), self.date, self.bullet)


class ArchitectureSchema(Schema):
    date        = fields.String()
    arch        = fields.String()
    category    = fields.String()
    bullet      = fields.String()
    bLink       = fields.String()
    subBullet1  = fields.String()
    sb1Link     = fields.String()
    subBullet2  = fields.String()
    sb2Link     = fields.String()
    subBullet3  = fields.String()
    sb3Link     = fields.String()
    subBullet4  = fields.String()
    sb4Link     = fields.String()
    subBullet5  = fields.String()
    sb5Link     = fields.String()
    rowID       = fields.Integer()

    @post_load
    def createArchitecture(self, data):
        return Architecture(**data) 

#ss_dict = {'date':date,'internal':internal,'category':category,etc}
#schema = ArchitectureSchema()
#archResult = schema.load(ss_dict)