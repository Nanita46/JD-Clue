image ciudad = "Ciudad.png"
image interrogatorio = "Interrogatorio.png"


image detective = "Detective.png"


define d = Character('Detective', color="#c8ffc8")

label start:
     scene ciudad
     "Se ha perpetrado un asesinato en la ciudad"
     "El cual por el momento no hemos podido resolver"

     scene interrogatorio
     show detective
     with dissolve
     d "Por eso los hemos citado a todos el dia de hoy"
     d "Para tratar de resolver el asecinato de la Srta Victoria"

return
