from app.utils.database import get_db


class ClientModel:
    def __init__(
        self,
        tipo_id=None,
        identificacion=None,
        nombre=None,
        telefono=None,
        correo=None,
        macroportafolio=None,
        probabilidad_pago=None,
        segmento_cliente=None,
        tipo_cliente=None,
        acciones_sobre_cliente=None,
        dias_mora=None,
        saldo_capital=None,
        rango_ingresos=None,
        tendencia_ingresos=None,
        endeudamiento_sector=None,
        suma_cuotas_sector=None,
        suma_cuotas_banco=None,
        nombre_entidad_1_deuda=None,
        valor_entidad_1_deuda=None,
        nombre_entidad_2_deuda=None,
        valor_entidad_2_deuda=None,
        nombre_entidad_3_deuda=None,
        valor_entidad_3_deuda=None,
        abono_minimo_negociacion=None,
        cuota_minima_referencia=None,
        suma_capital=None,
        suma_intereses_corriente=None,
        suma_intereses_mora=None,
        suma_seguros=None,
        suma_otros_cargos=None,
        pago_minimo=None,
        codigos_listas_restrictivas=None,
        etapa_procesos_juridicos=None,
        cod_recuperador=None,
        ingreso_certificado=None,
        numero_productos_mora=None,
    ):
        self.tipo_id = tipo_id
        self.identificacion = identificacion
        self.tipo_id = tipo_id
        self.identificacion = identificacion
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.macroportafolio = macroportafolio
        self.probabilidad_pago = probabilidad_pago
        self.segmento_cliente = segmento_cliente
        self.tipo_cliente = tipo_cliente
        self.acciones_sobre_cliente = acciones_sobre_cliente
        self.dias_mora = dias_mora
        self.saldo_capital = saldo_capital
        self.rango_ingresos = rango_ingresos
        self.tendencia_ingresos = tendencia_ingresos
        self.endeudamiento_sector = endeudamiento_sector
        self.suma_cuotas_sector = suma_cuotas_sector
        self.suma_cuotas_banco = suma_cuotas_banco
        self.nombre_entidad_1_deuda = nombre_entidad_1_deuda
        self.valor_entidad_1_deuda = valor_entidad_1_deuda
        self.nombre_entidad_2_deuda = nombre_entidad_2_deuda
        self.valor_entidad_2_deuda = valor_entidad_2_deuda
        self.nombre_entidad_3_deuda = nombre_entidad_3_deuda
        self.valor_entidad_3_deuda = valor_entidad_3_deuda
        self.abono_minimo_negociacion = abono_minimo_negociacion
        self.cuota_minima_referencia = cuota_minima_referencia
        self.suma_capital = suma_capital
        self.suma_intereses_corriente = suma_intereses_corriente
        self.suma_intereses_mora = suma_intereses_mora
        self.suma_seguros = suma_seguros
        self.suma_otros_cargos = suma_otros_cargos
        self.pago_minimo = pago_minimo
        self.codigos_listas_restrictivas = codigos_listas_restrictivas
        self.etapa_procesos_juridicos = etapa_procesos_juridicos
        self.cod_recuperador = cod_recuperador
        self.ingreso_certificado = ingreso_certificado
        self.numero_productos_mora = numero_productos_mora

    def get_values(self, data):
        values = (
            data["tipo_id"],
            data["identificacion"],
            data["nombre"],
            data["telefono"],
            data["correo"],
            data["macroportafolio"],
            data["probabilidad_pago"],
            data["segmento_cliente"],
            data["tipo_cliente"],
            data["acciones_sobre_cliente"],
            data["dias_mora"],
            data["saldo_capital"],
            data["rango_ingresos"],
            data["tendencia_ingresos"],
            data["endeudamiento_sector"],
            data["suma_cuotas_sector"],
            data["suma_cuotas_banco"],
            data["nombre_entidad_1_deuda"],
            data["valor_entidad_1_deuda"],
            data["nombre_entidad_2_deuda"],
            data["valor_entidad_2_deuda"],
            data["nombre_entidad_3_deuda"],
            data["valor_entidad_3_deuda"],
            data["abono_minimo_negociacion"],
            data["cuota_minima_referencia"],
            data["suma_capital"],
            data["suma_intereses_corriente"],
            data["suma_intereses_mora"],
            data["suma_seguros"],
            data["suma_otros_cargos"],
            data["pago_minimo"],
            data["codigos_listas_restrictivas"],
            data["etapa_procesos_juridicos"],
            data["cod_recuperador"],
            data["ingreso_certificado"],
            data["numero_productos_mora"],
        )
        return values

    def validate_connect():

        db = get_db()
        if db is not None:
            return db.cursor()
        else:
            return None

    # def save(self, data):
    #     db = get_db()
    #     cursor = db.cursor()
    #     values = self.get_values(data)
    #     if self.get_by_id(data["tipo_id"]):
    #         values = list(values)
    #         first_val = values[:2]
    #         values = values[2:]
    #         values.extend(first_val)
    #         values = tuple(values)

    #         cursor.execute(
    #             "UPDATE datos_cliente SET nombre = %s,telefono = %s, correo = %s, macroportafolio = %s, probabilidad_pago = %s, segmento_cliente = %s, tipo_cliente = %s, acciones_sobre_cliente = %s, dias_mora = %s, saldo_capital = %s, rango_ingresos = %s, tendencia_ingresos = %s, endeudamiento_sector = %s, suma_cuotas_sector = %s, suma_cuotas_banco = %s, nombre_entidad_1_deuda = %s, valor_entidad_1_deuda = %s, nombre_entidad_2_deuda = %s, valor_entidad_2_deuda = %s, nombre_entidad_3_deuda = %s, valor_entidad_3_deuda = %s, abono_minimo_negociacion = %s, cuota_minima_referencia = %s, suma_capital = %s, suma_intereses_corriente = %s, suma_intereses_mora = %s, suma_seguros = %s, suma_otros_cargos = %s, pago_minimo = %s, codigos_listas_restrictivas = %s, etapa_procesos_juridicos = %s, cod_recuperador = %s, ingreso_certificado = %s, numero_productos_mora = %s             WHERE tipo_id = %s AND identificacion = %s",
    #             values,
    #         )
    #     else:
    #         cursor.execute("INSERT INTO datos_cliente VALUES" + str(values))
    #     db.commit()
    #     return data

    # @classmethod
    # def get_all(cls):
    #     db = get_db()
    #     cursor = db.cursor()
    #     cursor.execute("SELECT * FROM datos_cliente")
    #     rows = cursor.fetchall()
    #     return [cls(*row) for row in rows]

    @classmethod
    def get_by_id(cls, typeId, customId):
        cursor = get_db()
        if not cursor:
            return ("No Content", 204)

        cursor.execute(
            "SELECT * FROM datos_cliente WHERE tipo_id = %s and identificacion = %s ",
            (
                typeId,
                customId,
            ),
        )
        row = cursor.fetchone()
        if row:
            return cls(*row)
        else:
            return ("No Content", 204)

    # def delete(self, id):
    #     db = get_db()
    #     cursor = db.cursor()
    #     cursor.execute("DELETE FROM datos_cliente WHERE tipo_id = %s", (id,))
    #     if cursor.rowcount == 1:
    #         db.commit()
    #         return True
    #     return False


# INSERT INTO datos_cliente (
#     tipo_id,
#     identificacion,
#     nombre,
#     telefono,
#     correo,
#     macroportafolio,
#     probabilidad_pago,
#     segmento_cliente,
#     tipo_cliente,
#     acciones_sobre_cliente,
#     dias_mora,
#     saldo_capital,
#     rango_ingresos,
#     tendencia_ingresos,
#     endeudamiento_sector,
#     suma_cuotas_sector,
#     suma_cuotas_banco,
#     nombre_entidad_1_deuda,
#     valor_entidad_1_deuda,
#     nombre_entidad_2_deuda,
#     valor_entidad_2_deuda,
#     nombre_entidad_3_deuda,
#     valor_entidad_3_deuda,
#     abono_minimo_negociacion,
#     cuota_minima_referencia,
#     suma_capital,
#     suma_intereses_corriente,
#     suma_intereses_mora,
#     suma_seguros,
#     suma_otros_cargos,
#     pago_minimo,
#     codigos_listas_restrictivas,
#     etapa_procesos_juridicos,
#     cod_recuperador,
#     ingreso_certificado,
#     numero_productos_mora
# )
# VALUES (
#     3,
#     123456789,
#     'Nom',
#     '123-456-7890',
#     'correo@example.com',
#     'Macroportafo',
#     0.85,
#     'Segme',
#     'T',
#     'Acciones Aleatorias',
#     30,
#     10000.50,
#     'Ra',
#     'Tendencia Aleatoria',
#     0.75,
#     500.25,
#     300.75,
#     'Entidad 1 Aleatoria',
#     150.50,
#     'Entidad 2 Aleatoria',
#     75.25,
#     'Entidad 3 Aleatoria',
#     30.50,
#     50.75,
#     25.25,
#     1000.75,
#     500.50,
#     300.25,
#     150.50,
#     75.25,
#     30,
#     5,
#     'Recupera',
#     5500.75,
#     5,
#     5
# );


# {
#     "tipo_id": 3,
#     "identificacion": 123456789,
#     "nombre": "Nom",
#     "telefono": "123-456-7890",
#     "correo": "correo@example.com",
#     "macroportafolio": "Macroportafo",
#     "probabilidad_pago": 0.85,
#     "segmento_cliente": "Segme",
#     "tipo_cliente": "T",
#     "acciones_sobre_cliente": "Acciones Aleatorias",
#     "dias_mora": 30,
#     "saldo_capital": 10000.50,
#     "rango_ingresos": "Ra",
#     "tendencia_ingresos": "Tendencia Aleatoria",
#     "endeudamiento_sector": 0.75,
#     "suma_cuotas_sector": 500.25,
#     "suma_cuotas_banco": 300.75,
#     "nombre_entidad_1_deuda": "Entidad 1 Aleatoria",
#     "valor_entidad_1_deuda": 150.50,
#     "nombre_entidad_2_deuda": "Entidad 2 Aleatoria",
#     "valor_entidad_2_deuda": 75.25,
#     "nombre_entidad_3_deuda": "Entidad 3 Aleatoria",
#     "valor_entidad_3_deuda": 30.50,
#     "abono_minimo_negociacion": 50.75,
#     "cuota_minima_referencia": 25.25,
#     "suma_capital": 1000.75,
#     "suma_intereses_corriente": 500.50,
#     "suma_intereses_mora": 300.25,
#     "suma_seguros": 150.50,
#     "suma_otros_cargos": 75.25,
#     "pago_minimo": 30,
#     "codigos_listas_restrictivas": 5,
#     "etapa_procesos_juridicos": "Recupera",
#     "cod_recuperador": 5500.75,
#     "ingreso_certificado": 5.0,
#     "numero_productos_mora": 5
# }
