from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    ForeignKeyConstraint,
    Index,
    Integer,
    PrimaryKeyConstraint,
    SmallInteger,
    String,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class DatosCliente(Base):
    __tablename__ = "datos_cliente"
    tipo_id = Column(SmallInteger)
    identificacion = Column(Integer)
    nombre = Column(String(55))
    telefono = Column(String(30))
    correo = Column(String(55))
    macroportafolio = Column(String(20))
    probabilidad_pago = Column(Float)
    segmento_cliente = Column(String(10))
    tipo_cliente = Column(String(10))
    acciones_sobre_cliente = Column(String(55))
    dias_mora = Column(Integer)
    saldo_capital = Column(Float)
    rango_ingresos = Column(String(20))
    tendencia_ingresos = Column(String(20))
    endeudamiento_sector = Column(Float)
    suma_cuotas_sector = Column(Float)
    suma_cuotas_banco = Column(Float)
    nombre_entidad_1_deuda = Column(String(20))
    valor_entidad_1_deuda = Column(Float)
    nombre_entidad_2_deuda = Column(String(20))
    valor_entidad_2_deuda = Column(Float)
    nombre_entidad_3_deuda = Column(String(20))
    valor_entidad_3_deuda = Column(Float)
    abono_minimo_negociacion = Column(Float)
    cuota_minima_referencia = Column(Float)
    suma_capital = Column(Float)
    suma_intereses_corriente = Column(Float)
    suma_intereses_mora = Column(Float)
    suma_seguros = Column(Float)
    suma_otros_cargos = Column(Float)
    pago_minimo = Column(Float)
    codigos_listas_restrictivas = Column(Integer)
    etapa_procesos_juridicos = Column(String(20))
    cod_recuperador = Column(String(10))
    ingreso_certificado = Column(Float)
    numero_productos_mora = Column(Integer)
    __table_args__ = (
        PrimaryKeyConstraint("tipo_id", "identificacion"),
        UniqueConstraint("tipo_id", "identificacion", name="uq_tipo_id_identificacion"),
    )


class DatosProducto(Base):
    __tablename__ = "datos_producto"
    tipo_id = Column(SmallInteger)
    identificacion = Column(Integer)
    fecha_corte = Column(Date)
    id_producto = Column(String(18))
    familia_producto = Column(String(10))
    desembolso = Column(Float)
    plazo = Column(Integer)
    tasa = Column(Float)
    cuota = Column(Float)
    mora = Column(Boolean)
    dias_mora = Column(Integer)
    capital = Column(Float)
    interes_corriente = Column(Float)
    interes_mora = Column(Float)
    seguros = Column(Float)
    otros_cargos = Column(Float)
    pagos_acumulados = Column(Float)
    saldo_total = Column(Float)
    pago_minimo = Column(Float)
    flg_pagare = Column(Boolean)
    fecha_pago = Column(Date)
    codigo_preaprobacion = Column(String(5))
    compania = Column(Integer)
    circular_026 = Column(String(10))
    producto_en_dolares = Column(Boolean)
    __table_args__ = (
        PrimaryKeyConstraint("tipo_id", "identificacion", "id_producto", "fecha_corte"),
        UniqueConstraint("tipo_id", "identificacion", "fecha_corte", "id_producto", name="uq_datos_producto"),
    )


class ParametrosPoliticas(Base):
    __tablename__ = "parametros_politicas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    grupo = Column(String(20))
    subgrupo = Column(String(20))
    politica = Column(String(20))
    valor = Column(Float)


class OfertasClientes(Base):
    __tablename__ = "ofertas_clientes"
    tipo_id = Column(SmallInteger, primary_key=True)
    identificacion = Column(Integer, primary_key=True)
    oferta_1_abono = Column(String(300))
    oferta_2_abono = Column(String(300))
    oferta_3_abono = Column(String(300))
    oferta_1_cuota = Column(String(300))
    oferta_2_cuota = Column(String(300))
    oferta_3_cuota = Column(String(300))


class BaseResultadosDiaria(Base):
    __tablename__ = "base_resultados_diaria"
    codigo_gestion = Column(String(30), primary_key=True)
    usuario = Column(String(20))
    tipo_id = Column(SmallInteger)
    identificacion = Column(Integer)
    fecha = Column(DateTime)
    actualizacion_correo = Column(String(20))
    actualizacion_telefono = Column(String(20))
    abono_cliente = Column(Float)
    oferta_seleccionada_sobre_abono = Column(String(300))
    abono_cliente_con_oferta = Column(Float)
    cuota_cliente = Column(Float)
    oferta_seleccionada_sobre_cuota = Column(String(300))
    cuota_cliente_con_oferta = Column(Float)
    periodos_gracia = Column(String(20))
    abono_extraordinario_mes1 = Column(Integer)
    valor_mes1 = Column(Float)
    abono_extraordinario_mes2 = Column(Integer)
    valor_mes2 = Column(Float)
    flg_condonacion = Column(Boolean)
    item_condonacion = Column(String(50))
    porcentaje_condonacion = Column(Float)
    valor_condonacion = Column(Float)
    cod_estrategia = Column(String(20))
    fecha_pago_obligacion = Column(Date)
    codigo_estado_negociacion = Column(Integer)
    estado_oferta = Column(Integer)
    recuperador = Column(String(20))


class BaseResultadosHistorico(Base):
    __tablename__ = "base_resultados_historico"
    codigo_gestion = Column(String(30), primary_key=True)
    usuario = Column(String(20))
    tipo_id = Column(SmallInteger)
    identificacion = Column(Integer)
    fecha = Column(DateTime)
    actualizacion_correo = Column(String(20))
    actualizacion_telefono = Column(String(20))
    abono_cliente = Column(Float)
    oferta_seleccionada_sobre_abono = Column(String(300))
    abono_cliente_con_oferta = Column(Float)
    cuota_cliente = Column(Float)
    oferta_seleccionada_sobre_cuota = Column(String(300))
    cuota_cliente_con_oferta = Column(Float)
    periodos_gracia = Column(String(20))
    abono_extraordinario_mes1 = Column(Integer)
    valor_mes1 = Column(Float)
    abono_extraordinario_mes2 = Column(Integer)
    valor_mes2 = Column(Float)
    flg_condonacion = Column(Boolean)
    item_condonacion = Column(String(50))
    porcentaje_condonacion = Column(Float)
    valor_condonacion = Column(Float)
    cod_estrategia = Column(String(20))
    fecha_pago_obligacion = Column(Date)
    codigo_estado_negociacion = Column(Integer)
    estado_oferta = Column(Integer)
    recuperador = Column(String(20))


class BaseNegociacionDiariaProductos(Base):
    __tablename__ = "base_negociacion_diaria_productos"
    codigo_gestion = Column(String(30), primary_key=True)
    tipo_id = Column(SmallInteger, primary_key=True)
    identificacion = Column(Integer, primary_key=True)
    fecha_corte = Column(Date, primary_key=True)
    id_producto = Column(String(18))
    familia_producto = Column(String(18))
    desembolso = Column(Float)
    plazo = Column(Integer)
    tasa = Column(Float)
    cuota = Column(Float)
    mora = Column(Boolean)
    dias_mora = Column(Integer)
    capital = Column(Float)
    interes_corriente_mora = Column(Float)
    interes_mora = Column(Float)
    seguros_mora = Column(Float)
    otros_cargos = Column(Float)
    pagos_acumulados = Column(Float)
    saldo_total = Column(Float)
    pago_minimo = Column(Float)
    flg_pagare = Column(Boolean)
    fehca_pago = Column(Date)
    cod_estrategia = Column(String(20))
    compania = Column(Integer)
    estado_producto = Column(String(20))


class BaseNegociacionHistoricoProductos(Base):
    __tablename__ = "base_negociacion_historico_productos"
    codigo_gestion = Column(String(30), primary_key=True)
    tipo_id = Column(SmallInteger, primary_key=True)
    identificacion = Column(Integer, primary_key=True)
    fecha_corte = Column(Date, primary_key=True)
    id_producto = Column(String(18))
    familia_producto = Column(String(18))
    desembolso = Column(Float)
    plazo = Column(Integer)
    tasa = Column(Float)
    cuota = Column(Float)
    mora = Column(Boolean)
    dias_mora = Column(Integer)
    capital = Column(Float)
    interes_corriente_mora = Column(Float)
    interes_mora = Column(Float)
    seguros_mora = Column(Float)
    otros_cargos = Column(Float)
    pagos_acumulados = Column(Float)
    saldo_total = Column(Float)
    pago_minimo = Column(Float)
    flg_pagare = Column(Boolean)
    fehca_pago = Column(Date)
    cod_estrategia = Column(String(20))
    compania = Column(Integer)
    estado_producto = Column(String(20))


class Ftp(Base):
    __tablename__ = "ftp"
    id = Column(Integer, primary_key=True, autoincrement=True)
    plazo_meses = Column(Integer)
    plazo_dias = Column(Integer)
    ftp = Column(Float)
    tasa_mv = Column(Float)


class MonitoreoAsesor(Base):
    __tablename__ = "monitoreo_asesor"
    usuario = Column(String(20), primary_key=True)
    segmento = Column(String(20))
    accion = Column(String(20))
    valor = Column(String(100))
    fecha = Column(Date)


class AlertamientoClientes(Base):
    __tablename__ = "alertamiento_clientes"
    codigo_gestion = Column(String(30), primary_key=True)
    usuario = Column(String(20))
    tipo_id = Column(SmallInteger)
    identificacion = Column(Integer)
    fecha = Column(DateTime)
    categoria_pregunta = Column(String(50))
    pregunta_realizada = Column(String(300))
    respuesta_cliente = Column(String(200))
    validacion_respuesta = Column(bool)


class GestionAsesor(Base):
    __tablename__ = "gestion_asesor"
    codigo_gestion = Column(String(30), primary_key=True)
    usuario = Column(String(20))
    tipo_id = Column(SmallInteger)
    identificacion = Column(Integer)
    fecha = Column(DateTime)
    resultado_gestion = Column(String(20))
    tipo_comentario = Column(String(50))
    comentario = Column(String(300))
