import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])


def share price():

    
    revenue_current1 = float(request.form.get('revenue_current'))
    revenue_previous1 = float(request.form.get('revenue_previous'))
    Total_Equity1 = float(request.form.get('Total_Equity'))
    Total_Debt1 = float(request.form.get('Total_Debt'))
    Nifty50_Yearly_Returns1 = float(request.form.get('Nifty50_Yearly_Returns'))
    Beta1 = float(request.form.get('Beta'))
    Interest_Expenses1= float(request.form.get('Interest_Expenses'))
    EBIT1 = float(request.form.get('EBIT')))
    RF1 = float(request.form.get('RF'))
    LTGrowth1 = float(request.form.get('LTGrowth'))
    CapEx1 = float(request.form.get('CapEx'))
    NOPAT1 = float(request.form.get('NOPAT'))
    ETR1 = float(request.form.get('ETR'))
    numbre_of_shares1 = float(request.form.get('number_of_shares'))


    ###CREDIT SPREAD

    interest_coverage_ratio = EBIT1/Interest_Expenses1

    if interest_coverage_ratio > 8.5:
    #Rating is AAA
          credit_spread = 0.0063
    if (interest_coverage_ratio > 6.5) & (interest_coverage_ratio <= 8.5):
    #Rating is AA
         credit_spread = 0.0078
    if (interest_coverage_ratio > 5.5) & (interest_coverage_ratio <=  6.5): 
    #Rating is A+
         credit_spread = 0.0098
    if (interest_coverage_ratio > 4.25) & (interest_coverage_ratio <=  5.49):
    #Rating is A
         credit_spread = 0.0108
    if (interest_coverage_ratio > 3) & (interest_coverage_ratio <=  4.25):
    #Rating is A-
         credit_spread = 0.0122
    if (interest_coverage_ratio > 2.5) & (interest_coverage_ratio <=  3):
    #Rating is BBB
         credit_spread = 0.0156
    if (interest_coverage_ratio > 2.25) & (interest_coverage_ratio <=  2.5):
    #Rating is BB+
         credit_spread = 0.02
    if (interest_coverage_ratio > 2) & (interest_coverage_ratio <=  2.25):
    #Rating is BB
         credit_spread = 0.0240
    if (interest_coverage_ratio > 1.75) & (interest_coverage_ratio <=  2):
    #Rating is B+
         credit_spread = 0.0351
    if (interest_coverage_ratio > 1.5) & (interest_coverage_ratio <=  1.75):
    #Rating is B
         credit_spread = 0.0421
    if (interest_coverage_ratio > 1.25) & (interest_coverage_ratio <=  1.5):
    #Rating is B-
         credit_spread = 0.0515
    if (interest_coverage_ratio > 0.8) & (interest_coverage_ratio <=  1.25):
    #Rating is CCC
         credit_spread = 0.0820
    if (interest_coverage_ratio > 0.65) & (interest_coverage_ratio <=  0.8):
    #Rating is CC
         credit_spread = 0.0864
    if (interest_coverage_ratio > 0.2) & (interest_coverage_ratio <=  0.65):
    #Rating is C
         credit_spread = 0.1134
    if interest_coverage_ratio <=  0.2:
    #Rating is D
         credit_spread = 0.1512

    revenue_growth_rate = (revenue_current1-revenue_previous1)/revenue_previous1

    FCF = NOPAT1-CapEx1

    FCF1 = FCF

    FCF2 = FCF1*(1+revenue_growth_rate)

    FCF3 = FCF2*(1+revenue_growth_rate)

    FCF4 = FCF3*(1+revenue_growth_rate)

    FCF5 = FCF4*(1+revenue_growth_rate)

    FCF_list = [FCF1 , FCF2 , FCF3 , FCF4 , FCF5]

    ### kd = cost of debt

    kd = RF1+credit_spread

    ### ke = cost of equity

    ke = RF1+(Beta1*(Nifty50_Yearly_Returns1-RF1))

    #### DEBT & EQUITY PERCENTAGE WEIGHTAGE

    debt_weight = Total_Debt1/(Total_Debt1+Total_Equity1)
    equity_weight = Total_Equity1/(Total_Debt1+Total_Equity1)

    #### WACC = WEIGHTAGE AVERAGE OF COST OF CAPITAL

    wacc = (kd*(1-ETR1)*debt_weight)+(ke*equity_weight)

    #### TERMINAL VALUE
    terminal_value = (FCF_list[4]*(1+LTGrowth1))/(wacc-LTGrowth1)

    terminal_value_discounted = terminal_value/(1+wacc)**4
 

    
    npv = FCF_list[0]+(FCF_list[1]/(1+wacc))+(FCF_list[2]/(1+wacc)**2)+(FCF_list[3]/(1+wacc)**3)+(FCF_list[4]/(1+wacc)**4)

    ### kd = cost of debt

    kd = RF1+credit_spread

    ### ke = cost of equity

    ke = RF1+(Beta1*(Nifty50_Yearly_Returns1-RF1))

    #### DEBT & EQUITY PERCENTAGE WEIGHTAGE

    debt_weight = Total_Debt1/(Total_Debt1+Total_Equity1)
    equity_weight = Total_Equity1/(Total_Debt1+Total_Equity1)
 
     #### WACC = WEIGHTAGE AVERAGE OF COST OF CAPITAL

    wacc = (kd*(1-ETR1)*debt_weight)+(ke*equity_weight)

    #### TERMINAL VALUE
    terminal_value = (FCF_list[4]*(1+LTGrowth1))/(wacc-LTGrowth1)

    terminal_value_discounted = terminal_value/(1+wacc)**4
    target_equity_value = terminal_value_discounted + npv
    target_value = target_equity_value - Total_Debt1
    target_price_per_share = target_value/numbre_of_shares1
    




    ##### BETA CALCULATION

    #Beta= Covariance/Variance
 
    ##where: 
    
    #Covariance = Measure of a stock’s Return relative
    #to that of the market
    #Variance = Measure of how the market moves relative
    #to its mean


    
    #### RISK FREE RATE  
    #RF = current 10 year yield of treasury


    ## NIFTY50 YEARLY RETURNS 
    # avg of nifty50 annual return of last 10-15 year
    return render_template('index.html',share price=share price)


if __name__ == "__main__":
    app.run(debug=True)