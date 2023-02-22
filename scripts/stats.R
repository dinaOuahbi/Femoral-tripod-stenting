#R 4.2

# STAT DESC

library(tidyverse)
library(rstatix)
library(ggpubr)
library(gtsummary)


df<-read.csv('../data/processed_df.csv', na.strings=c("","NA"))



# VARIABLES CATEGORIELLES _ STAT DESC
df[,c(2:52)] %>% tbl_summary(missing_text = "NA",
                       type = list(c(names(df)[c(46:47)])~ 'continuous2')) %>% #longeur et diametre

  bold_labels()


# syndé les stat descriptive par groupe : VARIABLES CATEGORIELLE
df[,c(2:52)] %>%
  tbl_summary(by = stenting_method,
              missing_text = "NA") %>%
  add_p() %>%
  modify_header(label ~ "**Variable**") %>%
  bold_labels()

# syndé les stat descriptive par groupe : VARIABLES CONTINUES
df[,c(52:89)] %>%
  tbl_summary(by = stenting_method,
              type = all_continuous() ~ "continuous2",
              missing_text = "NA") %>%
  add_p() %>%
  modify_header(label ~ "**Variable**") %>%
  bold_labels()

# COMPARER LES GROUPES DE RUTHERFORD SUR LES VARIABLES DE CALCIFICATION 
calc_var <- cbind(df[,c(29, 78)], df[,c(54:71)]) # rut M2
calc_var %>%
  tbl_summary(by = Rutherford.pré.op,
              type = all_continuous() ~ "continuous2",
              statistic = all_continuous() ~ c("{median} ({p25}, {p75})"),
              missing = "no"
  ) %>%
  add_p(pvalue_fun = ~style_pvalue(.x, digits = 2))%>%
  add_n()%>%
  add_q(method="BH")%>%
  modify_header(label ~ "**Variable**") %>%
  bold_labels()

# COMPARER LES GROUPES de patient SB vs AE sur les classification DE RUTHERFORD 
RUTHERFORD <- df[c(52, 10,12,29)]

RUTHERFORD %>%
  tbl_summary(by=stenting_method,
              missing = 'no'
  ) %>%
  add_n() %>%
  add_p(pvalue_fun = ~style_pvalue(.x, digits = 2))%>%
  add_q(method="BH")%>%
  modify_header(label = "**Variable**") %>%
  bold_labels()

mytab <- table(RUTHERFORD$Rutherford.pré.op, RUTHERFORD$stenting_method)
barplot(t(mytab), legend.text = TRUE, beside = TRUE, ylim = c(0,70), main = 'Rutherford.pré.op')

# ----var calcif per groups----
calc_var <- cbind(df[,c(52, 78)], df[,c(54:71)])
calc_var %>%
  tbl_summary(by = stenting_method,
              type = all_continuous() ~ "continuous2",
              statistic = all_continuous() ~ c("{N_nonmiss}","{median} ({p25}, {p75})","{min}, {max}"),
              missing = "no"
  ) %>%
  add_p(pvalue_fun = ~style_pvalue(.x, digits = 2))%>%
  add_n()%>%
  add_q(method="BH")%>%
  modify_header(label ~ "**Variable**") %>%
  bold_labels()

# longeur et diamet


# ----var perm per groups----
perm <- df[c(52, 51,9,11)]

perm %>%
  tbl_summary(by=stenting_method,
              missing = 'no'
              ) %>%
  add_n() %>%
  add_p(pvalue_fun = ~style_pvalue(.x, digits = 2))%>%
  add_q(method="BH")%>%
  modify_header(label = "**Variable**") %>%
  bold_labels()


# Comparer les deux groupes (ECHEC vs PERMEABLE) sur les variables de CALCIFICATION durant les 3 temps (J1 / M2/ M12) 
calc_var <- cbind(df[,c(51, 9, 11, 78)], df[,c(54:71)])
calc_var %>%
  tbl_summary(by = X12ECHEC...PSVr...2.4,
              type = all_continuous() ~ "continuous2",
              statistic = all_continuous() ~ c("{N_nonmiss}","{median} ({p25}, {p75})","{min}, {max}"),
              missing = "no"
  ) %>%
  add_p(pvalue_fun = ~style_pvalue(.x, digits = 2))%>%
  add_n()%>%
  add_q(method="BH")%>%
  modify_header(label ~ "**Variable**") %>%
  bold_labels()


# bar plot
# Barplots empilés avec plusieurs groupes
# Save a table of the two-way interaction
mytab <- table(df$X12ECHEC...PSVr...2.4, df$stenting_method)
barplot(t(mytab), legend.text = TRUE, beside = TRUE, ylim = c(0,70), main = 'At 12 months ')



# boxplot
# Visualisation : Boxplots avec p-values
pwc <- wilcox.test(calc_var$Volume.zone.1~calc_var$X12ECHEC...PSVr...2.4)
pwc
#pwc <- pwc %>% add_xy_position(x = "X1ECHEC...PSVr...2.4")
ggboxplot(calc_var %>% filter(!is.na(X12ECHEC...PSVr...2.4)), x = "X12ECHEC...PSVr...2.4", y = "Densité.UH.moy3", fill = 'X12ECHEC...PSVr...2.4', notch = T) +
  geom_jitter(shape=16, position=position_jitter(0.2))+
  stat_summary(fun.y=mean, geom="point", shape=23, size=4)+
  scale_color_brewer(palette="Dark2")


