import easyocr
import cv2
import matplotlib.pyplot as plt

def detectar_placa(imagem_path):
    reader = easyocr.Reader(['pt'])
    imagem = cv2.imread(imagem_path)
    resultado = reader.readtext(imagem)
    
    for (bbox, texto, conf) in resultado:
        (topo_esquerdo, topo_direito, rodape_direito, rodape_esquerdo) = bbox
        topo_esquerdo = tuple(map(int, topo_esquerdo))
        rodape_direito = tuple(map(int, rodape_direito))
        
        cv2.rectangle(imagem, topo_esquerdo, rodape_direito, (0, 255, 0), 2)
        cv2.putText(imagem, texto, (topo_esquerdo[0], topo_esquerdo[1] - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        print(f"Texto Detectado: {texto} (Confiança: {conf:.2f})")
    
    plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

detectar_placa("exemplo_carro.jpg")
