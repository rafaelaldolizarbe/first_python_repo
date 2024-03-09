
class Catalogando:
    
    def __init__(self):
        import os
        import sys
        caminho_origem=input("Cole aqui o seu caminho de origem").replace("\\","/").replace("C:","")
        arquivos=os.listdir(caminho_origem)
        caminho_destino=input("Cole aqui o seu caminho de destino").replace("\\","/").replace("C:","")        
        self.caminho_origem = caminho_origem
        self.arquivos = arquivos
        self.caminho_destino = caminho_destino
        self.inicio= os.getcwd().replace("\\","/").replace("C:","")+str("/inicio")
        self.fim=os.getcwd().replace("\\","/").replace("C:","")+str("/fim")
        
    def renomear_arquivos_origem(self): #Seria interessante criar uma nova lista de nomes dos arquivos e não o renomeamento destes#
        import os
        import sys
        codigo_preco=input(str("Digite o código do produto seguindo a seguinte lógica lll000:"))# A lógica consiste nas três primeiras letras designarem a categoria e os tres últimos números, o valor da mercadoria sem a vírgula#
        numero_de_id=int(input("Digite o número sequencial N+1 do último produto listado:"))#Vale resaltar que o último registro possui uma numeração após os números correspondentes ao valor do produto, resgatar o número!#
        for index, file in enumerate(self.arquivos,numero_de_id):
            os.rename(os.path.join(self.caminho_origem, file), os.path.join(self.caminho_origem,codigo_preco+str(index)+'.jpg'))
            print(os.path.join(self.caminho_origem,codigo_preco+str(index)+'.jpg'))
        self.arquivos = os.listdir(self.caminho_origem)# Sem esta linha é impossível utilizar a função abaixo novamente
        
    def iniciar(self): # vamos fazer outra função universal para a conversão de diferentes tamanhos fazendo com que as imagens influenciem no tamanho das bordas, assim as bordas dependerão unicamente do tamanho da imagem
        import os
        import sys
        from PIL import Image, ImageDraw, ImageFont
        for arquivo in self.arquivos:
            with Image.open(os.path.join(self.caminho_origem,arquivo)) as im:
                fonte = ImageFont.truetype("encorpada-classic.otf", 14)
                titulo = ImageFont.truetype('encorpada-classic.otf', 30)
                preco= ImageFont.truetype('encorpada-classic.otf', 24)
                largura_card,comprimento_card=(768,1024)
                largura_foto,comprimento_foto=(667,837)
                razao_comp_larg=comprimento_foto/largura_foto
                novancora_larfoto,novancora_compfoto=(int((largura_card-largura_foto)/2),int((comprimento_card-comprimento_foto)/2))
                im0 = Image.new("RGB", (largura_card, comprimento_card), color=(246,247,249))

                if int(im.size[0]) > int(im.size[1]): # Condição para a qual podemos endireitar a imagem em caso de que ela não esteja em pé
                    im=im.transpose(Image.ROTATE_270)

                im=im.resize((largura_foto,comprimento_foto),Image.LANCZOS)                      
                im0.paste(im,(novancora_larfoto,novancora_compfoto))
                escreve = ImageDraw.Draw(im0)
                escreve.text((int(largura_card/2), 46), f'{arquivo[:-4]}', fill="black", anchor="mm", font=titulo)
                escreve.text((int(largura_card/2), int(comprimento_card/2)), '', fill="black", anchor="mm", font=fonte)
                escreve.text((int(largura_card/2), comprimento_card-46 ), f'Valor do Produto: R$ {arquivo[3]},{arquivo[4]}{arquivo[5]}', fill="black", anchor="mm", font=preco)
                #escreve.text((int(w/2), h-46 ), f'Valor do Produto: R$ {file[3]}{file[4]},{file[5]}{file[6]}', fill="black", anchor="mm", font=preco)
                im0.save(os.path.join(self.caminho_destino,arquivo))
