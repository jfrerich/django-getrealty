from django.db import models


class TestModel(models.Model):
    r_num = models.TextField('r_num', max_length=100, default='')
    rpg = models.TextField('rpg', default='')
    Property_Interest = models.TextField('Property_Interest', max_length=100, default='')
    Files_xx_BillsF = models.TextField('Files_xx_BillsF', default='')
    # Files___HistF = models.TextField('Property_Interest', max_length=100, default='')
    # Files___DetF = models.TextField('Property_Interest', max_length=100, default='')
    # new Field('Files___DataF'),
    # new Field('Maps___GIS'),
    # new Field('Maps___Map'),
    # 'NOTES'
    Subd = models.TextField('Subd', default='')
    # 'Prop_Details___Acres'),
    # 'Prop_Details___AssessVal'),
    # 'Prop_Details___AssessMinDue'),
    # 'Tax_Due___PctToAss'),
    # 'Tax_Due___TotAmtDue'),
    # 'DatePulled'),
    # new Field('TaxDates___OldestDue'),
    # new Field('TaxDates___LastPaid'),
    # new Field('TaxDates___LastYrPaid'),
    # new Field('Different___Addr'),
    # new Field('Different___Zip'),
    # new Field('Different___State'),
    # new Field('NHS_imp'),
    # new Field('InstallYr'),
    # new Field('TimesSold___Num'),
    # new Field('TimesSold___Last'),
    # new Field('Appraised___AppPctOfMax'),
    # new Field('Appraised___AppLastVal'),
    # new Field('Appraised___AppMaxVal'),
    # new Field('AppraisedMaxReduced___AppMaxAmt'),
    # new Field('AppraisedMaxReduced___AppMaxYr'),
    # new Field('Assess___AssPctOfMax'),
    # new Field('Assess___AssLastVal'),
    # new Field('Assess___AssMaxVal'),
    # new Field('AssessMaxReduced___AssMaxAmt'),
    # new Field('AssessMaxReduced___AssMaxYr'),
    # new Field('ImpNHS___LastPctOfMax'),
    # new Field('ImpNHS___LastVal'),
    # new Field('ImpNHS___MaxVal'),
    # new Field('ImpNHSMaxReduced___MaxAmt'),
    # new Field('ImpNHSMaxReduced___MaxYr'),
    # new Field('ImpHS___ihsPctOfMax'),
    # new Field('ImpHS___ihsLastVal'),
    # new Field('ImpHS___ihsMaxVal'),
    # new Field('ImpHSMaxReduced___ihsMaxAmt'),
    # new Field('ImpHSMaxReduced___ihsMaxYr'),
    # new Field('LandHS___lhsPctOfMax'),
    # new Field('LandHS___lhsLastVal'),
    # new Field('LandHS___lhsMaxVal'),
    # new Field('LandHSMaxReduced___lhsMaxAmt'),
    # new Field('LandHSMaxReduced___lhsMaxYr'),
    # new Field('LandNHS___lnhsPctOfMax'),
    # new Field('LandNHS___lnhsLastVal'),
    # new Field('LandNHS___lnhsMaxVal'),
    # new Field('LandNHSMaxReduced___lnhsMaxAmt'),
    # new Field('LandNHSMaxReduced___lnhsMaxYr'),
    # new Field('DaysLate___Curr'),
    # new Field('DaysLate___Max'),
    # new Field('PctDiffAddr'),
    # new Field('PropAddr'),
    # new Field('OwnerAddr'),
    # new Field('OwnerName'),
    # new Field('LegalDesc'),

    class Meta:
        # managed = True
        db_table = 'RNUMBERS_Bastrop'

    @property
    def testproperty(self):
        return '{} testprop'.format(self.name)
# from django.conf.urls import url
# Create your models here.
