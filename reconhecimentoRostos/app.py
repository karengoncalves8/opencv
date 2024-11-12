import cv2
import mediapipe as mp

# Inicializar o opencv e a o mediapipe
webcam = cv2.VideoCapture(0) # Seleciona a webcam a ser utilizada, por padrão é 0
solucao_reconhecimento_rosto = mp.solutions.face_detection 
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection() #Objeto que irá buscar pelos rostos
desenho = mp.solutions.drawing_utils # Quadrados envolta do rostos

# Verificando os frames até que o programa seja parado
while True:
    # lendo as inforamções da webcam
    verificador, frame = webcam.read() # Retorna um boleano (se conseguiu ler a webcam) e o frame lido
    
    # caso não tenha conseguido ler a webcam
    if not verificador:
        break 
    
    # reconhecendo os rostos
    lista_rostos = reconhecedor_rostos.process(frame) # vai processar a imagem procurando por rostos 
    
    # se tiver achado rostos
    if lista_rostos.detections:
        # Para cada rosto encontrado
        for rosto in lista_rostos.detections:
            # desenhando os rostos na imagem
            desenho.draw_detection(frame, rosto) # draw_detection(ondeSeraDesenhado, o que será desenhado)
    
    cv2.imshow('Rostos na webcam', frame) # cv2.imshow(tituloJanela, oqSeraExibido)    
   
    # aperto ESC para sair
    # fazendo com que o loop tenha um delay para que a imagem seja retornada
    # se eu apertar ESC (tecla cod 27) durante esse período, sai do programa
    if cv2.waitKey(5) == 27: #cv2.waitKey(milisegundos) 
        break
    
# Fechando a webcam
webcam.release()