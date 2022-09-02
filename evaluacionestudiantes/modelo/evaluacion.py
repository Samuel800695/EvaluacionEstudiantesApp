class EventoEvaluativo:

    def __init__(self, codigo: str, nombre: str, descripcion: str, porcentaje: float):
        # TODO: Definir atributos
        pass

    def __str__(self) -> str:
        return f"{self.codigo} - {self.nombre} ({self.porcentaje:.1f})%"


class Evaluacion:

    def __init__(self, evento: EventoEvaluativo, calificacion: float):
        # TODO: Definir atributos
        pass

    def __str__(self) -> str:
        return f"{str(self.evento)}: {self.calificacion: .1f}"


class Estudiante:

    def __init__(self, identificacion: str, nombre: str):
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        # TODO: Defina atributo evaluacion

    # TODO: Defina método de instancia calcular_promedio

    # TODO: Defina método de instancia agregar_evaluacion

    def __str__(self) -> str:
        return f"{self.identificacion} - {self.nombre}"


class Curso:

    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.eventos_evaluativos: dict[str, EventoEvaluativo] = {}
        self.estudiantes: dict[str, Estudiante] = {}

    def se_puede_agregar_evento_con_porcentaje(self, porcentaje: float):
        suma_porcentaje = sum([p.porcentaje for p in self.eventos_evaluativos.values()])
        return (suma_porcentaje + porcentaje) <= 100

    def agregar_evento_evaluativo(self, codigo: str, nombre: str, descripcion: str, porcentaje: float):
        if codigo not in self.eventos_evaluativos.keys():
            evento: EventoEvaluativo = EventoEvaluativo(codigo, nombre, descripcion, porcentaje)
            self.eventos_evaluativos[codigo] = evento
            return True
        else:
            return False

    def registrar_estudiante(self, identificacion: str, nombre: str):
        if identificacion not in self.estudiantes.keys():
            estudiante: Estudiante = Estudiante(identificacion, nombre)
            self.estudiantes[identificacion] = estudiante
            return True
        else:
            return False

    def agregar_calificacion_a_estudiante(self, identificacion: str, codigo_evento: str, calificacion: float):
        if identificacion in self.estudiantes.keys():
            estudiante = self.estudiantes[identificacion]
            evento = self.eventos_evaluativos[codigo_evento]
            estudiante.agregar_evaluacion(evento, calificacion)

    def estudiante_con_mejor_promedio(self) -> Estudiante:
        # TODO: Implemente el cuerpo del método
        pass

    def evaluaciones_faltantes_de_estudiante(self, identificacion: str) -> list[EventoEvaluativo]:
        evaluaciones_faltantes = []
        if identificacion in self.estudiantes.keys():
            estudiante = self.estudiantes[identificacion]
            eventos_evaluados = [e.evento for e in estudiante.evaluaciones]
            for codigo_evento in self.eventos_evaluativos.keys():
                if self.eventos_evaluativos[codigo_evento] not in eventos_evaluados:
                    evaluaciones_faltantes.append(self.eventos_evaluativos[codigo_evento])

            return evaluaciones_faltantes
        else:
            return None



