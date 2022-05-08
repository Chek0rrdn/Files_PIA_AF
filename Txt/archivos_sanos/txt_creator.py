import random


mensaje = """


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non volutpat sapien. Maecenas ut massa eu risus laoreet blandit vitae non leo. 
Sed eget egestas arcu. Cras sem tellus, fermentum ac mauris vitae, placerat aliquet leo. 
Sed in felis vitae ligula posuere elementum iaculis eget mi.
Donec quis nibh condimentum, pulvinar tellus et, tristique elit. Morbi scelerisque semper dolor eu scelerisque. 
Integer consectetur nibh quis nunc aliquet egestas. Nunc id elementum lorem. Nulla at porttitor odio. Aliquam a nisi sed purus efficitur finibus. 
Proin tincidunt, lorem ut pulvinar pharetra, lorem lorem ornare tellus, non mattis dolor leo id nisl. Nullam quis luctus augue.
Sed eget lacinia nibh.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum scelerisque dui est, eu pellentesque nunc interdum vel. 
Suspendisse nec tincidunt turpis. Proin quis magna non velit congue accumsan. Cras elit ligula, aliquam at augue ut, pharetra 
aliquam magna. Nunc pulvinar magna vel mauris ultricies, ut imperdiet arcu rutrum. Ut et dolor non nibh mollis tincidunt vel et erat. 
Nullam tincidunt efficitur malesuada. Praesent suscipit, augue eget pellentesque semper, eros arcu ultrices risus, ut viverra tortor 
justo sed enim. Nam eget vehicula tellus. Sed eget sem aliquam, consectetur turpis eleifend, vestibulum nisl.
Quisque in commodo metus. Sed a felis vehicula nulla iaculis viverra. Morbi vitae diam tristique, luctus massa et, tincidunt lacus. 
Proin tristique, massa dictum congue mattis, felis justo tincidunt lorem, in suscipit eros sem sit amet sem. Praesent in sem id massa 
volutpat hendrerit. Suspendisse a augue in orci consequat pellentesque nec at leo. Phasellus bibendum volutpat risus, id consectetur magna. 
Praesent a sapien nec dolor consectetur sagittis. Curabitur tincidunt tellus mauris, ullamcorper varius elit venenatis pulvinar. 
Proin non ligula scelerisque, vulputate magna et, pharetra lorem. Aenean imperdiet maximus ipsum, sed scelerisque quam scelerisque a.
Sed malesuada, nulla eu eleifend viverra, enim orci placerat diam, sit amet sodales lacus lorem ut nisi. Nunc at eros vitae enim 
scelerisque aliquet ac eget lectus. Nam aliquam est vitae luctus interdum. Nullam risus est, suscipit sit amet diam in, 
laoreet consequat risus. Praesent et finibus augue. Cras varius augue sed semper ornare. Quisque sed mi libero.
Nam egestas vitae neque at porttitor. Maecenas ultrices viverra orci, at laoreet ligula. Quisque ultricies non orci sed bibendum. 
Vestibulum volutpat justo nec tristique iaculis. Proin a dapibus elit. Quisque orci risus, sagittis tempus cursus ac, sagittis ut nulla. 
Quisque a sapien volutpat, aliquam velit a, rutrum erat. Nunc et leo sem.
In nec lectus cursus, sollicitudin sapien eu, dapibus lectus. Praesent arcu nisi, tincidunt a risus at, molestie egestas felis. 
Morbi consequat quis mi at facilisis. Aliquam erat volutpat. Morbi malesuada ligula in lectus luctus ultricies. Quisque placerat, 
eros at tincidunt venenatis, odio purus lacinia est, in lacinia enim sem quis urna. Maecenas pretium nunc quis turpis sollicitudin tincidunt.
Quisque rutrum bibendum lectus sed blandit. Nam sagittis tortor ante, egestas sollicitudin sapien malesuada vitae. 
Vestibulum pretium libero lorem.
Nunc lacinia nunc et lectus vulputate, placerat porta arcu eleifend. Nam aliquet enim vel ligula consectetur, ac venenatis dolor convallis. 
Nulla eros quam, pulvinar et sodales eu, ultricies eu ipsum.
Morbi nec dui sed ipsum venenatis lacinia. Cras laoreet bibendum felis. Aenean non pellentesque mi, et fringilla arcu. 
Vivamus gravida ut nisl a egestas. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; 
Integer tristique massa sed metus lobortis rhoncus. Phasellus rhoncus vitae orci ac fermentum. Vestibulum sit amet arcu tortor. 
Aliquam erat volutpat. Nulla consectetur turpis ut convallis tempus. Proin ac lorem et turpis lobortis eleifend eu in erat. 
Nulla facilisi. Quisque nec vehicula nunc. Aliquam ac tellus at urna porta tincidunt sit amet a neque.
Quisque pellentesque fringilla nisi, quis ornare est vestibulum a.
Nunc gravida magna ex, non porta augue volutpat sed. Nulla augue libero, mollis in faucibus vitae, euismod ullamcorper nibh.
Suspendisse nibh urna, tempor ut hendrerit at, condimentum quis eros. Aenean consequat lorem turpis, sed eleifend quam ornare ut. 
Vestibulum iaculis, leo nec auctor ultricies, ipsum enim fringilla mi, eu lobortis metus enim egestas leo. Vestibulum quis tincidunt ex. 
Maecenas a finibus nibh, non semper urna. Curabitur euismod dolor pretium nibh malesuada congue. Pellentesque placerat quis massa at bibendum.
Sed sit amet massa at metus gravida facilisis non vitae tortor. Nunc laoreet consectetur quam, ac scelerisque nibh volutpat sed. 
Nunc pellentesque volutpat lectus in elementum. Nam ac aliquam dui. Nulla imperdiet ipsum vel leo molestie, sed fermentum erat vehicula. 
Etiam porttitor, orci eget vulputate sodales, ante risus congue dui, non varius purus metus a erat. Nunc pretium ipsum est, 
at pellentesque est iaculis vitae. Aenean vel ligula ut metus fringilla mattis. Praesent sit amet dapibus purus. Curabitur ut nibh nisi. 
Morbi sit amet massa eu orci mattis dignissim. In luctus congue sapien at mollis. Nulla id orci faucibus, tempus arcu vitae, ornare tortor.
Mauris malesuada diam a nibh mollis convallis. Maecenas vehicula sit amet neque vitae pulvinar. In vulputate ante felis, vel tincidunt 
lorem blandit at. Duis eget efficitur odio, at laoreet metus. Aenean dictum ultrices porttitor. Suspendisse eu imperdiet massa. 
Donec sit amet libero hendrerit tellus porta ornare ac at mauris.
Integer lorem elit, fermentum rutrum dolor quis, volutpat molestie sem. Proin iaculis ligula sed sollicitudin accumsan. 
Praesent tempus placerat ultricies. Aliquam erat volutpat. Phasellus condimentum nibh eu leo lobortis sagittis. Nulla fringilla 
dignissim risus, ut volutpat lorem. Aenean rutrum tempor sodales. Sed libero ligula, interdum quis convallis ut, mattis in nunc. 
Praesent quam libero, gravida quis ullamcorper a, pretium ac eros. Ut sodales feugiat lacinia. Fusce tempor egestas viverra. 
Praesent pretium placerat nibh ac luctus. Praesent accumsan tortor vel felis ornare tempor. Duis quis erat ante. Vestibulum sit
 amet massa at nulla congue ullamcorper.
Mauris malesuada semper pulvinar. Cras hendrerit mattis odio, non lobortis est venenatis sit amet. Duis vel tristique erat. 
Nulla nec neque bibendum, feugiat felis sit amet, euismod lorem. Morbi in vestibulum urna, vitae malesuada metus. Pellentesque ut 
vehicula lacus, eget efficitur sem. Maecenas iaculis nulla nec dolor cursus venenatis. In hac habitasse platea dictumst. 
Cras a justo vitae nibh interdum volutpat. Duis eget lobortis tortor. Orci varius natoque penatibus et magnis dis parturient montes, 
nascetur ridiculus mus. Aliquam ultrices, ex nec posuere sodales, leo nunc dignissim lorem, nec commodo turpis sem varius turpis. 
Nulla tempor nibh sed venenatis bibendum. Quisque leo purus, suscipit sed suscipit nec, commodo in lorem.
Sed auctor dictum urna et porttitor. Sed viverra purus vitae nisl commodo lobortis. In diam elit, vestibulum eget nisl in, 
faucibus posuere turpis. Nullam eget gravida sem, et posuere erat. Etiam quis pretium nunc, eget semper ipsum. Aliquam iaculis justo varius 
vestibulum interdum. Fusce non ligula risus. Duis mattis erat in ante sagittis rutrum. Sed auctor leo in orci tempus congue vitae ut nibh.
Morbi convallis pretium ante ut porta. Pellentesque eget lorem ornare, pellentesque lacus a, semper dui. Mauris iaculis urna eget magna fermentum, 
ut imperdiet ipsum maximus. Donec auctor tortor ac augue condimentum lobortis. Morbi eget posuere ex. Vestibulum pharetra nulla arcu, 
vel tempus lorem ullamcorper non.
Praesent ac lorem vitae sem pellentesque efficitur. Morbi vel accumsan enim. Donec hendrerit risus id dolor facilisis auctor eu nec risus. 
A
enean sollicitudin blandit tempor. Nunc quis lorem mi. Duis tincidunt pellentesque sodales. Praesent nisl massa, congue ut facilisis non,
 pharetra ut mauris. Curabitur ornare massa ipsum, ut donec

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non volutpat sapien. Maecenas ut massa eu risus laoreet blandit vitae non leo. 
Sed eget egestas arcu. Cras sem tellus, fermentum ac mauris vitae, placerat aliquet leo. 
Sed in felis vitae ligula posuere elementum iaculis eget mi.
 Donec quis nibh condimentum, pulvinar tellus et, tristique elit. Morbi scelerisque semper dolor eu scelerisque. 
 Integer consectetur nibh quis nunc aliquet egestas. Nunc id elementum lorem. Nulla at porttitor odio. Aliquam a nisi sed purus efficitur finibus.
  Proin tincidunt, lorem ut pulvinar pharetra, lorem lorem ornare tellus, non mattis dolor leo id nisl. Nullam quis luctus augue.
   Sed eget lacinia nibh.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum scelerisque dui est, eu pellentesque nunc interdum vel. 
Suspendisse nec tincidunt turpis. Proin quis magna non velit congue accumsan. Cras elit ligula, aliquam at augue ut, pharetra aliquam magna.
 Nunc pulvinar magna vel mauris ultricies, ut imperdiet arcu rutrum. Ut et dolor non nibh mollis tincidunt vel et erat. 
 Nullam tincidunt efficitur malesuada. Praesent suscipit, augue eget pellentesque semper, eros arcu ultrices risus, 
 ut viverra tortor justo sed enim. Nam eget vehicula tellus. Sed eget sem aliquam, consectetur turpis eleifend, vestibulum nisl.
Quisque in commodo metus. Sed a felis vehicula nulla iaculis viverra. Morbi vitae diam tristique, luctus massa et, tincidunt lacus. 
Proin tristique, massa dictum congue mattis, felis justo tincidunt lorem, in suscipit eros sem sit amet sem. 
Praesent in sem id massa volutpat hendrerit. Suspendisse a augue in orci consequat pellentesque nec at leo. 
Phasellus bibendum volutpat risus, id consectetur magna. Praesent a sapien nec dolor consectetur sagittis. 
Curabitur tincidunt tellus mauris, ullamcorper varius elit venenatis pulvinar. Proin non ligula scelerisque, vulputate magna et, pharetra lorem.
Aenean imperdiet maximus ipsum, sed scelerisque quam scelerisque a.
Sed malesuada, nulla eu eleifend viverra, enim orci placerat diam, sit amet sodales lacus lorem ut nisi. 
Nunc at eros vitae enim scelerisque aliquet ac eget lectus. Nam aliquam est vitae luctus interdum. 
Nullam risus est, suscipit sit amet diam in, laoreet consequat risus. Praesent et finibus augue. 
Cras varius augue sed semper ornare. Quisque sed mi libero.
Nam egestas vitae neque at porttitor. Maecenas ultrices viverra orci, at laoreet ligula. Quisque ultricies non orci sed bibendum.
 Vestibulum volutpat justo nec tristique iaculis. Proin a dapibus elit. Quisque orci risus, sagittis tempus cursus ac, sagittis ut nulla. 
 Quisque a sapien volutpat, aliquam velit a, rutrum erat. Nunc et leo sem.
In nec lectus cursus, sollicitudin sapien eu, dapibus lectus. Praesent arcu nisi, tincidunt a risus at, molestie egestas felis.
 Morbi consequat quis mi at facilisis. Aliquam erat volutpat. Morbi malesuada ligula in lectus luctus ultricies. Quisque placerat, 
 eros at tincidunt venenatis, odio purus lacinia est, in lacinia enim sem quis urna. Maecenas pretium nunc quis turpis sollicitudin tincidunt. 
 Quisque rutrum bibendum lectus sed blandit. Nam sagittis tortor ante, egestas sollicitudin sapien malesuada vitae. 
 Vestibulum pretium libero lorem.
  Nunc lacinia nunc et lectus vulputate, placerat porta arcu eleifend. Nam aliquet enim vel ligula consectetur, ac venenatis dolor convallis. 
  Nulla eros quam, pulvinar et sodales eu, ultricies eu ipsum.
Morbi nec dui sed ipsum venenatis lacinia. Cras laoreet bibendum felis. Aenean non pellentesque mi, et fringilla arcu.
 Vivamus gravida ut nisl a egestas. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; 
 Integer tristique massa sed metus lobortis rhoncus. Phasellus rhoncus vitae orci ac fermentum. Vestibulum sit amet arcu tortor. 
 Aliquam erat volutpat. Nulla consectetur turpis ut convallis tempus. Proin ac lorem et turpis lobortis eleifend eu in erat. 
 Nulla facilisi. Quisque nec vehicula nunc. Aliquam ac tellus at urna porta tincidunt sit amet a neque. 
 Quisque pellentesque fringilla nisi, quis ornare est vestibulum a.
Nunc gravida magna ex, non porta augue volutpat sed. Nulla augue libero, mollis in faucibus vitae, euismod ullamcorper nibh. 
Suspendisse nibh urna,
 tempor ut hendrerit at, condimentum quis eros. Aenean consequat lorem turpis, sed eleifend quam ornare ut. Vestibulum iaculis, 
 leo nec auctor ultricies, ipsum enim fringilla mi, eu lobortis metus enim egestas leo. Vestibulum quis tincidunt ex. 
 Maecenas a finibus nibh, non semper urna. Curabitur euismod dolor pretium nibh malesuada congue. Pellentesque placerat quis massa at bibendum.
Sed sit amet massa at metus gravida facilisis non vitae tortor. Nunc laoreet consectetur quam, ac scelerisque nibh volutpat sed. 
Nunc pellentesque volutpat lectus in elementum. Nam ac aliquam dui. Nulla imperdiet ipsum vel leo molestie, sed fermentum erat vehicula. 
Etiam porttitor, orci eget vulputate sodales, ante risus congue dui, non varius purus metus a erat. 
Nunc pretium ipsum est, at pellentesque est iaculis vitae. Aenean vel ligula ut metus fringilla mattis.
 Praesent sit amet dapibus purus. Curabitur ut nibh nisi. Morbi sit amet massa eu orci mattis dignissim. 
 In luctus congue sapien at mollis. Nulla id orci faucibus, tempus arcu vitae, ornare tortor.
Mauris malesuada diam a nibh mollis convallis. Maecenas vehicula sit amet neque vitae pulvinar. In vulputate ante felis, vel tincidunt lorem blandit at. Duis eget efficitur odio, at laoreet metus. Aenean dictum ultrices porttitor. Suspendisse eu imperdiet massa. Donec sit amet libero hendrerit tellus porta ornare ac at mauris.
Integer lorem elit, fermentum rutrum dolor quis, volutpat molestie sem. Proin iaculis ligula sed sollicitudin accumsan. 
Praesent tempus placerat ultricies. Aliquam erat volutpat. Phasellus condimentum nibh eu leo lobortis sagittis. 
Nulla fringilla dignissim risus,
 ut volutpat lorem. Aenean rutrum tempor sodales. Sed libero ligula, interdum quis convallis ut, mattis in nunc. 
 Praesent quam libero, gravida quis ullamcorper a, pretium ac eros. Ut sodales feugiat lacinia. Fusce tempor egestas viverra. Praesent pretium placerat nibh ac luctus. Praesent accumsan tortor vel felis ornare tempor. Duis quis erat ante. Vestibulum sit amet massa at nulla congue ullamcorper.
Mauris malesuada semper pulvinar. Cras hendrerit mattis odio, non lobortis est venenatis sit amet. Duis vel tristique erat. 
Nulla nec neque bibendum, feugiat felis sit amet, euismod lorem. Morbi in vestibulum urna, vitae malesuada metus. 
Pellentesque ut vehicula lacus, eget efficitur sem. Maecenas iaculis nulla nec dolor cursus venenatis. 
In hac habitasse platea dictumst. Cras a justo vitae nibh interdum volutpat. Duis eget lobortis tortor. 
Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam ultrices, ex nec posuere sodales, 
leo nunc dignissim lorem, nec commodo turpis sem varius turpis. Nulla tempor nibh sed venenatis bibendum. Quisque leo purus, 
suscipit sed suscipit nec, commodo in lorem.
Sed auctor dictum urna et porttitor. Sed viverra purus vitae nisl commodo lobortis. In diam elit, vestibulum eget nisl in, faucibus posuere turpis.
 Nullam eget gravida sem, et posuere erat. Etiam quis pretium nunc, eget semper ipsum. Aliquam iaculis justo varius vestibulum interdum. 
 Fusce non ligula risus. Duis mattis erat in ante sagittis rutrum. Sed auctor leo in orci tempus congue vitae ut nibh. 
 Morbi convallis pretium ante ut porta. Pellentesque eget lorem ornare, pellentesque lacus a, semper dui. Mauris iaculis urna eget magna fermentum, ut imperdiet ipsum maximus. Donec auctor tortor ac augue condimentum lobortis. Morbi eget posuere ex. Vestibulum pharetra nulla arcu, vel tempus lorem ullamcorper non.
Praesent ac lorem vitae sem pellentesque efficitur. Morbi vel accumsan enim. Donec hendrerit risus id dolor facilisis auctor eu nec risus. 
Aenean sollicitudin blandit tempor. Nunc quis lorem mi. Duis tincidunt pellentesque sodales. 
Praesent nisl massa, congue ut facilisis non, pharetra ut mauris. Curabitur ornare massa ipsum, ut donec


"""

nombres = (
    "RecetaPaciente_","RecetaLab._","Nota_",
    "HistoriaClinica_","ResumenDeCaso_","Pedidos_",
    "ListaMedica_","Medicamentos_","Antibioticos_",
    "FormatoHist.Clinica_","ListaEstServicioSoc","Estudiantes_",
    "ListEnfermeras_","Nomina_","Presupuestos_",
    "ListadoHerramientas_","ListaInstrumentos_","PedidosMeds_",
    "PedidosMateriales_","Materiales_"
)

def elegir_materia():
    materia = random.choice(nombres)
    materia.encode()
    return materia

def main():
	for iterable in range(1, 51):
		
		titulo_txt = elegir_materia()
		titulo_txt = titulo_txt+str(iterable)+".txt"
		
		with open(titulo_txt, "w") as archivo:
			archivo.write(mensaje*30)	


if __name__ == '__main__':
	main()
print("Hecho!!!")