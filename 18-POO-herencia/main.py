import clases

persona = clases.Persona()
persona.setNombre("Aldayr")
persona.setApellidos("Rdz")
persona.setAltura("175cm")
persona.setEdad("22 años")

print(f'La persona es: {persona.getNombre()} {persona.getApellidos()}')
print(persona.hablar())

print("----------------------------------")

informatico = clases.Informatico()
informatico.setNombre("Carlos")
informatico.setApellidos("Mtz")
print(f'El informatico es: {informatico.getNombre()} {informatico.getApellidos()}')
print(informatico.getLenguajes())
print(informatico.caminar())
print("----------------------------------")

tecnico= clases.TecnicoRedes()
tecnico.setNombre("Aldaya")
print(tecnico.getNombre(),tecnico.auditoria(), tecnico.getLenguajes())