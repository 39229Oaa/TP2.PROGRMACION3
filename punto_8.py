transacciones_A={"TX01","TX02","TX03","TX04"}
transacciones_B={"TX03","TX04","TX05","TX06"}
anomalias=transacciones_A.symmetric_difference(transacciones_B)
print(anomalias)