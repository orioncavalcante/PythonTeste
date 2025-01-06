velocidade = 61
local_carro = 100

RADAR_1 = 60     #velocidade máxima do radar
LOCAL_1 = 100    #local onde o radar 1 está
RADAR_RANGE = 1  #a distância onde o radar pega

velocidade_carro_pass_radar1 = velocidade > RADAR_1
carro_multado_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
    
if velocidade_carro_pass_radar1:
    print("Velocidade do carro passou da velocidade máxima  do radar 1")

if carro_multado_radar1 and velocidade_carro_pass_radar1:
    print('Carro multado em radar 1')