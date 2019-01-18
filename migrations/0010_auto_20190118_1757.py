# Generated by Django 2.1 on 2019-01-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0009_auto_20190118_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtymodel',
            name='AppraisedMaxReduced_xx_AppMaxAmt',
            field=models.TextField(default='', verbose_name='AppraisedMaxReduced_xx_AppMaxAmt'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='AppraisedMaxReduced_xx_AppMaxYr',
            field=models.TextField(default='', verbose_name='AppraisedMaxReduced_xx_AppMaxYr'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='Appraised_xx_AppLastVal',
            field=models.TextField(default='', verbose_name='Appraised_xx_AppLastVal'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='Appraised_xx_AppMaxVal',
            field=models.TextField(default='', verbose_name='Appraised_xx_AppMaxVal'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='Appraised_xx_AppPctOfMax',
            field=models.TextField(default='', verbose_name='Appraised_xx_AppPctOfMax'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='AssessMaxReduced_xx_AssMaxAmt',
            field=models.TextField(default='', verbose_name='AssessMaxReduced_xx_AssMaxAmt'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='AssessMaxReduced_xx_AssMaxYr',
            field=models.TextField(default='', verbose_name='AssessMaxReduced_xx_AssMaxYr'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='Assess_xx_AssLastVal',
            field=models.TextField(default='', verbose_name='Assess_xx_AssLastVal'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='Assess_xx_AssMaxVal',
            field=models.TextField(default='', verbose_name='Assess_xx_AssMaxVal'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='Assess_xx_AssPctOfMax',
            field=models.TextField(default='', verbose_name='Assess_xx_AssPctOfMax'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='DatePulled',
            field=models.TextField(default='', verbose_name='DatePulled'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='DaysLate_xx_Curr',
            field=models.TextField(default='', verbose_name='DaysLate_xx_Curr'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='DaysLate_xx_Max',
            field=models.TextField(default='', verbose_name='DaysLate_xx_Max'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='Different_xx_Addr',
            field=models.TextField(default='', verbose_name='Different_xx_Addr'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='Different_xx_State',
            field=models.TextField(default='', verbose_name='Different_xx_State'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='Different_xx_Zip',
            field=models.TextField(default='', verbose_name='Different_xx_Zip'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='ImpHSMaxReduced_xx_ihsMaxAmt',
            field=models.TextField(default='', verbose_name='ImpHSMaxReduced_xx_ihsMaxAmt'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='ImpHSMaxReduced_xx_ihsMaxYr',
            field=models.TextField(default='', verbose_name='ImpHSMaxReduced_xx_ihsMaxYr'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='ImpHS_xx_ihsLastVal',
            field=models.TextField(default='', verbose_name='ImpHS_xx_ihsLastVal'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='ImpHS_xx_ihsMaxVal',
            field=models.TextField(default='', verbose_name='ImpHS_xx_ihsMaxVal'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='ImpHS_xx_ihsPctOfMax',
            field=models.TextField(default='', verbose_name='ImpHS_xx_ihsPctOfMax'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='ImpNHSMaxReduced_xx_MaxAmt',
            field=models.TextField(default='', verbose_name='ImpNHSMaxReduced_xx_MaxAmt'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='ImpNHSMaxReduced_xx_MaxYr',
            field=models.TextField(default='', verbose_name='ImpNHSMaxReduced_xx_MaxYr'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='ImpNHS_xx_LastPctOfMax',
            field=models.TextField(default='', verbose_name='ImpNHS_xx_LastPctOfMax'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='ImpNHS_xx_LastVal',
            field=models.TextField(default='', verbose_name='ImpNHS_xx_LastVal'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='ImpNHS_xx_MaxVal',
            field=models.TextField(default='', verbose_name='ImpNHS_xx_MaxVal'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='InstallYr',
            field=models.TextField(default='', verbose_name='InstallYr'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='LandHSMaxReduced_xx_lhsMaxAmt',
            field=models.TextField(default='', verbose_name='LandHSMaxReduced_xx_lhsMaxAmt'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='LandHSMaxReduced_xx_lhsMaxYr',
            field=models.TextField(default='', verbose_name='LandHSMaxReduced_xx_lhsMaxYr'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='LandHS_xx_lhsLastVal',
            field=models.TextField(default='', verbose_name='LandHS_xx_lhsLastVal'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='LandHS_xx_lhsMaxVal',
            field=models.TextField(default='', verbose_name='LandHS_xx_lhsMaxVal'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='LandHS_xx_lhsPctOfMax',
            field=models.TextField(default='', verbose_name='LandHS_xx_lhsPctOfMax'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='LandNHSMaxReduced_xx_lnhsMaxAmt',
            field=models.TextField(default='', verbose_name='LandNHSMaxReduced_xx_lnhsMaxAmt'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='LandNHSMaxReduced_xx_lnhsMaxYr',
            field=models.TextField(default='', verbose_name='LandNHSMaxReduced_xx_lnhsMaxYr'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='LandNHS_xx_lnhsLastVal',
            field=models.TextField(default='', verbose_name='LandNHS_xx_lnhsLastVal'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='LandNHS_xx_lnhsMaxVal',
            field=models.TextField(default='', verbose_name='LandNHS_xx_lnhsMaxVal'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='LandNHS_xx_lnhsPctOfMax',
            field=models.TextField(default='', verbose_name='LandNHS_xx_lnhsPctOfMax'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='LegalDesc',
            field=models.TextField(default='', verbose_name='LegalDesc'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='NHS_imp',
            field=models.TextField(default='', verbose_name='NHS_imp'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='OwnerAddr',
            field=models.TextField(default='', verbose_name='OwnerAddr'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='OwnerName',
            field=models.TextField(default='', verbose_name='OwnerName'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='PctDiffAddr',
            field=models.TextField(default='', verbose_name='PctDiffAddr'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='PropAddr',
            field=models.TextField(default='', verbose_name='PropAddr'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='Prop_Details_xx_AssessMinDue',
            field=models.TextField(default='', verbose_name='Prop_Details_xx_AssessMinDue'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='Prop_Details_xx_AssessVal',
            field=models.TextField(default='', verbose_name='Prop_Details_xx_AssessVal'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='TaxDates_xx_LastPaid',
            field=models.TextField(default='', verbose_name='TaxDates_xx_LastPaid'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='TaxDates_xx_LastYrPaid',
            field=models.TextField(default='', verbose_name='TaxDates_xx_LastYrPaid'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='TaxDates_xx_OldestDue',
            field=models.TextField(default='', verbose_name='TaxDates_xx_OldestDue'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='Tax_Due_xx_PctToAss',
            field=models.TextField(default='', verbose_name='Tax_Due_xx_PctToAss'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='Tax_Due_xx_TotAmtDue',
            field=models.TextField(default='', verbose_name='Tax_Due_xx_TotAmtDue'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='TimesSold_xx_Last',
            field=models.TextField(default='', verbose_name='TimesSold_xx_Last'),
        ),
        migrations.AddField(
            model_name='realtymodel',
            name='TimesSold_xx_Num',
            field=models.TextField(default='', verbose_name='TimesSold_xx_Num'),
        ),
    ]
