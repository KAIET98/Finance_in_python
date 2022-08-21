from modules.risk_ratios.risk_measurement import RiskMeasurement


#Vamos a hacer la estimacion sobre APPLE por ejemplo


firm = 'AAPL'

RM = RiskMeasurement()

HistoricVar = RM.HistoricVaR(column=firm)

VarOverHistoricData = RM.VaROverHistoricData()

CondVaR = RM.ConditionalValueAtRisk()

ParamVaR = RM.ParametricVaR()

MonteCarloSimulationQ99 = RM.MonteCarloSimulation( initial_price = 'd',

days = 255)

print(MonteCarloSimulationQ99)





