"""Abuso de pilhas"""

importar  argparse
importar  aleatório


# -------------------------------------------------- -
def  get_args ():
    """Obter argumentos de linha de comando"""

    parser  =  argparse . ArgumentParser (
        descrição = 'Abuso de heap' ,
        formatador_class = argparse . ArgumentDefaultsHelpFormatter )

    analisador . add_argument ( '-a' ,
                        '--adjetivos' ,
                        help = 'Número de adjetivos' ,
                        metavar = 'adjetivos' ,
                        tipo = int ,
                        padrão = 2 )

    analisador . add_argument ( '-n' ,
                        '--número' ,
                        help = 'Número de insultos' ,
                        metavar = 'insultos' ,
                        tipo = int ,
                        padrão = 3 )

    analisador . add_argument ( '-s' ,
                        '--semente' ,
                        ajuda = 'Semente aleatória' ,
                        metavar = 'semente' ,
                        tipo = int ,
                        padrão = Nenhum )

    args  =  analisador . parse_args ()

    se  arg . adjetivos  <  1 :
        analisador . erro ( f'--adjetivos " { args . adjetivos } " deve ser > 0' )

    se  arg . número  <  1 :
        analisador . erro ( f'--number " { args . number } " deve ser > 0' )

     argumentos de retorno


# -------------------------------------------------- -
def  principal ():
    """Faça um barulho de jazz aqui"""

    args  =  get_args ()
    aleatório . semente ( args . semente )

    adjetivos  =  """
    falido base lamuriante corrupto cullily detestável desonesto falso
    imundo imundo tolo imundo grosseiro desatento indistinguível infectado
    insaciável cansativo lascivo lascivo repugnante engordurado velho rabugento
    malandro podre ruinoso escrupuloso escorbuto calunioso encharcado
    rosto fino manchas de sapo sem educação vil olhos pardos
    """ . strip (). split ()

    substantivos  =  """
    Judas Satã macaco bunda barbeiro mendigo quarteirão garoto fanfarrão bunda
    carbúnculo covarde coxcomb vira-lata dândi degenerado demônio peixeiro tolo
    gaivota gaivota cabeça-de-vento patife mentiroso lunático boca leiteira lacaio
    ratcatcher recreant ladino repreender escravo suíno traidor varlet vilão verme
    """ . strip (). split ()

    para  _  no  intervalo ( args . número ):
        adjs  =  ',' . join ( aleatório . sample ( adjetivos , k = args . adjetivos ))
        print ( f'Você { adjs }  { aleatório . escolha ( substantivos ) } !' )


# -------------------------------------------------- -
se  __name__  ==  '__main__' :
    principal ()
