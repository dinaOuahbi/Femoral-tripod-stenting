# Femoral-tripod-stenting
Compare on several parameters two groups of patients having received two types of femoral tripod stenting



## INTRODUCTION
In epidemiology, there is frequent damage to the femoral tripod as a result of surgery, diabetes or obesity.
The stent ensures that the vessel does not shrink again over time.
There are two types of stents:
- Balloon (SB)
- Self-expanding (AE)

However, there are anatomical constraints with this type of treatment:
- Calcifications of the femoral artery
- Hip joint

## OBJECTIF
- Analysis of categorical and continuous variables
- Analysis of categorical and continuous variables in patients by group: stent-on-balloon (SB) and self-expanding stent (AE)
- PRIMARY PERFORMANCE OF STENTS ON THE BALLoon VS SELF-EXPANDING STENTS AT D1, M2 and M12
- Compare calcification versus patency variables

## METHODS
Continuous variables are characterized by their median and IQR, while categorical variables are characterized by the number of patients and percentages (%). 

The continuous variables are compared between the 2 groups of patients (SB vs AE) with Wilcoxon tests and the qualitative variables with Chi2 tests (if number/group > 5) or Fisher tests (if number/group <= 5). 

When a p-value is lower than the chosen level of significance (0.05), we admit that the difference between the two groups (for a given variable) is significant.

We will use the Benjamini-Hochberg method to adjust the p-values. This method allows us to control the false discovery rate (false positive), the expected proportion of false discoveries among the rejected hypotheses.

#### Some statistical concepts
The Wilcoxon test allows us to compare two means of two independent groups for a single variable. It is a non-parametric test because it makes no assumptions about the distribution of the samples.

The Chi2 (or Fisher) test allows us to test the independence of two qualitative variables.

The False Discovery Rate (FDR) is the proportion of false positives among all the tests declared positive. The estimate of the expected false discovery rate at a given p-value level is denoted by q-value

The interquartile range tells us the dispersion of the half of our sample from its median.

#### To visualize the difference between our two groups of patients on a continuous variable, we will use box plots

A boxplot summarizes several things
The trend: defined by the median

The dispersion: defined by the interquartile range (IQR) which is the difference between the 1st (25%) and the 3rd quantile (75%)

The Range: defined by the minimum and maximum of a variable

Notch at the median: useful to give an idea of the size of the difference between the medians; if the notches of two boxes do not overlap, it proves that there is a statistically significant difference between the medians.


























