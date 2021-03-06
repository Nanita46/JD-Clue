image interrogatorio = "Interrogatorio.png"
image ciudad = "Ciudad.png"
image compu = "Compu.png"
image fin = "Fin.png"
image asesinoA = "AsesinoA.png"
image asesinoB = "AsesinoB.png"
image asesinoC = "AsesinoC.png"
image test1 = "Test1.png"
image test2 = "Test2.png"
image fotos = "Fotos.png"
image fotos2 = "Fotos2.png"

image detective = "Detective.png"
image detectivePruebas = "DetectivePruebas.png"
image detectiveConfron = "DetectiveConfron.png"
image detectivePensar = "DetectivePensar.png"
image detectiveAja = "DetectiveAja.png"

image art = "Art.png"
image art1 = "Art1.png"
image art2 = "Art2.png"

image burt = "Burt.png"
image burt1 = "Burt1.png"
image burt2 = "Burt2.png"

image carl = "Carl.png"
image carl1 = "Carl1.png"
image carl2 = "Carl2.png"

image marta = "Marta.png"

image prueba1 = "Prueba1.png"
image prueba2 = "Prueba2.png"
image prueba3 = "Prueba3.png"
image prueba4 = "Prueba4.png"

image detectivePensar = "DetectivePensar.png"

define d = Character('Detective', color="#c8ffc8")
define a = Character('Art', color ="#ff0000")
define b = Character('Burt', color ="#0000cd")
define c = Character('Carl', color ="#32cd32")
define n = Character('Niko', color ="#ffff00")
define u = Character('Usuario', color ="#33ff00")
define m = Character('Marta', color ="#ff69b4")

label start:
     scene ciudad
     "Se ha perpetrado un asesinato en la ciudad"
     "El cual por el momento no hemos podido resolver"

     scene interrogatorio
     show detective
     with dissolve
     d "Nos gustaria que nos ayudaras con este caso"
     d "Para tratar de resolver el asesinato de la Srta Victoria"
     d "Para comenzar te pondremos al tanto de los hechos"
     hide detective

     show detectivePruebas
     with dissolve
     d "Segun nuestros datos tenemos tres sospechosos hasta ahora"
     hide detectivePruebas
     
     scene ciudad
     show art
     with dissolve
     d "Art"
     hide art

     show burt
     with dissolve
     d "Burt"
     hide burt

     show carl
     with dissolve
     d "Y Carl"
     hide carl 

     scene interrogatorio
     show detectivePruebas
     d "Ademas tenemos dos testigos"

     scene ciudad
     show test1 at left
     show test2 at right
     with dissolve
     d "El Señor y la Señora Garcia los cuales aseguran haber visto a los sospechosos y a la victima juntos el dia del asesinato"
     
     scene interrogatorio
     show detective
     d "A ver Señor Art que nos puede decir"
     hide detective
     show art1 
     with dissolve
     a "Bern es amigo de Victoria"
     a "Pero Carl y Victoria se odiaban a muerte"
     hide art1

     show detective
     with dissolve
     d "Su turno Señor Burt"
     hide detective
     show burt1
     with dissolve
     b "Yo ni siquiera estaba en la ciudad ese dia..."
     b "Y por si fuera poco no conozco a la tal Victoria" 
     hide burt1

     show detective at left
     d "Y usted señor Carl lo veo muy tranquilo"
     hide detective
     show carl1
     with dissolve
     c "Yo soy inocente, no se que hago aqui"
     c "En lo unico que puedo ayudar es en decirles que vi a Art y a Burt conduciendo por la ciudad ese dia"
     hide carl1
     
     scene interrogatorio
     show detective
     with dissolve
     d "Me pregunto si tienes alguna prueba con la que puedas ayudarnos"
     hide detective

     menu:
          "Si.":
          
               jump si

          "No.":
  
               jump no

label si:
     python:
          new_code = open('/home/denis/Documentos/murder.pl','w')
          code=[]
     show detective 
     with dissolve
     d "Y de que se tratan estas pruebas exactamente?"
     hide detective
     
     menu:
          "Fotos.":
               python:
                    code.append('murderer(carl).')
                    write_code = list(set(code))
                    for x in write_code:
                         new_code.write(x)
                    new_code.close()               
               jump fotos

          "Testimonio.":
               python:
                    code.append('murderer(burt).')
                    write_code = list(set(code))
                    for x in write_code:
                         new_code.write(x)
                    new_code.close()  
               jump testimonio
               
          "Evidencia de Campo.":
               python:
                    code.append('murderer(art).')
                    write_code = list(set(code))
                    for x in write_code:
                         new_code.write(x)
                    new_code.close()  
               jump evidencia

label fotos:

     show fotos
     with dissolve
     u "Tengo estas fotos que incriminan a Carl"
     hide fotos
     show fotos2
     with dissolve
     u "Ademas estas que lo muestran saliendo del pueblo con la victima"
     hide fotos2
     scene interrogatorio
     show detectivePensar
     with dissolve
     d "Vaya esto cambia todo"
     d "Niko ya hiciste los cambios en los datos del computador?"
     hide detectivePensar
     scene compu
     n "Si detective ya casi tenemos un resultado"
     scene asesinoC
     python:
        from pyswip import Prolog
        prolog = Prolog()
        prolog.consult('/home/denis/Documentos/murder.pl')
        asesino = list(prolog.query('murderer(X)'))
        n("El asesino es %s " %asesino[0]['X'])

     scene interrogatorio
     show detectiveAja at right
     d "Detengan al Sr Carl"
     hide detectiveAja

     show carl2
     with dissolve
     c ".....rayos!"
     hide carl2

     show detective
     with dissolve
     d "No lo veremos por un buen tiempo"
     hide detective
    
     scene fin
     "FIN"

     menu:
          "Seguir Jugando":
               jump star2

          "Terminar":
               return

label testimonio:
     
     scene interrogatorio
     u "Hay alguien a quien deberian conocer"
     u "La Señorita Marta"
     show marta
     with dissolve
     u "Ella tiene algo importante que decir en este caso"
     hide marta
     
     show detective
     with dissolve
     d "A ver Señorita Marta que tiene que decirnos....."
     hide detective

     show marta
     with dissolve
     m "Tengo un poco de miedo pero........"
     m "No me importa estoy dispuesta a enfrentar lo que sea!"
     hide marta 

     show detective 
     with dissolve
     d "Tranquila Señorita aqui esta a salvo diganos lo que sabe por favor"
     hide detective

     show marta 
     with dissolve
     m "Yo estaba ahi cuando ocurrio todo"
     m "Se quien es el asesino"
     hide marta
     show prueba1
     m "Fue aqui en la ciudad, yo estaba escondida y alcance a ver a un hombre alto con guantes cuando asesino a Victoria"
     hide prueba1     
     show  prueba2
     m "Vi cuando le clavo el cuchillo en la espalda"
     m "El asesino es el Señor Burt detective yo lo vi fue el esa noche en el hotel"
     hide prueba2     
     show detectivePensar
     with dissolve
     d "Vaya esto cambia todo"
     d "Niko ya hiciste los cambios en los datos del computador?"
     hide detectivePensar
     scene compu
     n "Si detective ya casi tenemos un resultado"
     scene asesinoB
     python:
        from pyswip import Prolog
        prolog = Prolog()
        prolog.consult('/home/denis/Documentos/murder.pl')
        asesino = list(prolog.query('murderer(X)'))
        n("El asesino es %s " %asesino[0]['X'])

     scene interrogatorio
     show detectiveAja at right
     d "Detengan al Sr Burt"
     hide detectiveAja

     show burt2
     with dissolve
     b "Por poco.....!"
     hide burt2

     show detective
     with dissolve
     d "No lo veremos por un buen tiempo"
     hide detective
    
     scene fin
     "FIN"

     menu:
          "Seguir Jugando":
               jump star2

          "Terminar":
               return

label evidencia:

     scene interrogatorio     
     u "Tengo en mi poder algo que podria ser importante"
     show detective
     with dissolve
     d "Y que podria ser ese algo al que se refiere"
     hide detective

     show prueba3 at truecenter
     with dissolve
     u "Estos negativos que muestran al Señor Art junto a la victima el dia del asesinato"
     hide prueba3

     show prueba4 at truecenter
     with dissolve
     u "Ademas de este cuchillo que fue ayado cerca del lugar de los echos y puedo apostar a qe las huellas borraran culquier duda" 
     hide prueba4
     show detectivePensar
     with dissolve
     d "Vaya esto cambia todo"
     d "Niko ya hiciste los cambios en los datos del computador?"
     hide detectivePensar
     scene compu
     n "Si detective ya casi tenemos un resultado"
     scene asesinoA
     python:
        from pyswip import Prolog
        prolog = Prolog()
        prolog.consult('/home/denis/Documentos/murder.pl')
        asesino = list(prolog.query('murderer(X)'))
        n("El asesino es %s " %asesino[0]['X'])

     scene interrogatorio
     show detectiveAja at right
     d "Detengan al Sr Art"
     hide detectiveAja

     show art2
     with dissolve
     a "Pero como?"
     hide art2

     show detective
     with dissolve
     d "No lo veremos por un buen tiempo"
     hide detective
    
     scene fin
     "FIN"
     menu:
          "Seguir Jugando":
               jump star2

          "Terminar":
               return

     
label no:
    show detectivePensar
    d "Vaya que interesante"
    d "Niko Alimentemos nuestra computadora con los datos a ver que nos dice"
    hide detectivePensar

    scene compu
    n "Si Detective ya me adelante, dentro de poco tendremos el nombre de nuestro asesino" 
    
    scene asesinoB

    python:
        from pyswip import Prolog
        prolog = Prolog()
        prolog.consult('/home/denis/Documentos/asesino.pl')
        asesinos = list(prolog.query('murderer(X)'))
        for asesino in asesinos:
          n("El asesino es %s " % str(asesino['X']))

    scene interrogatorio
    show detectiveAja at right
    d "Detengan al Sr Burt"
    hide detectiveAja

    show burt2 at left
    with dissolve
    b "Como fue que lo resolvieron.....rayos!"
    hide burt2

    show detective
    with dissolve
    d "No lo veremos por un buen tiempo"
    hide detective
    
    scene fin
    "FIN"
  
    menu:
          "Seguir Jugando":
               jump star2

          "Terminar":
               return
label star2:
     scene interrogatorio
     show detective
     with dissolve
     d "A ti tampoco te convencio cierto, intentemoslo otra vez"
     d "Aun hay algo extraño en todo esto"
     d "Tienes algo mas que nos pueda ayudar"
     jump si
        

